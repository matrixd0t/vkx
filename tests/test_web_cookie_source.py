"""Проверки веб-cookie и входа по логину/паролю."""
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from vkx import VKClient
from vkx.client.storage import JSONStore, MemoryStore, SQLiteStore, State
from vkx.client.tokens import (
    WEB_TOKEN_URL,
    PasswordCookieSource,
    TokenSourceError,
    WebCookieSource,
)


class FakeResponse:
    status_code = 200
    text = "{}"

    def __init__(self, payload, cookies=None):
        self._payload = payload
        self.cookies = cookies or {}

    def json(self):
        return self._payload


class FakeHttpClient:
    def __init__(self, response):
        self.response = response
        self.calls = []

    async def post(self, url, **kwargs):
        call = dict(kwargs)
        call["cookies"] = dict(kwargs.get("cookies") or {})
        self.calls.append((url, call))
        return self.response

    async def get(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP GET: {url}")

    async def aclose(self):
        pass


class FakeAuthResponse:
    status_code = 200

    def __init__(self, payload=None, *, text="", cookies=None):
        self._payload = payload
        self.text = text
        self.cookies = cookies or {}

    def json(self):
        return self._payload


class FakePasswordHttpClient:
    def __init__(self, verification_method="password"):
        self.verification_method = verification_method
        self.calls = []

    async def get(self, url, **kwargs):
        self.calls.append(("GET", url, kwargs))
        config = {
            "auth": {
                "host_app_id": 7913379,
                "access_token": "anonymous-access",
                "anonymous_token": "anonymous-token",
            },
            "data": {"uuid": "test-uuid"},
        }
        return FakeAuthResponse(
            text=f"<script>window.init = {json.dumps(config)};</script>"
        )

    async def post(self, url, **kwargs):
        self.calls.append(("POST", url, kwargs))
        if url == WEB_TOKEN_URL:
            if kwargs.get("cookies", {}).get("p") == "old-p":
                return FakeAuthResponse({}, text="expired session")
            return FakeAuthResponse(
                {"data": {"access_token": "fresh-web-token", "expires": 4_000_000_000}}
            )
        if url.endswith("/method/auth.validateAccount"):
            return FakeAuthResponse(
                {
                    "response": {
                        "sid": "auth-sid",
                        "next_step": {"verification_method": self.verification_method},
                    }
                }
            )
        if url.endswith("/method/ecosystem.getVerificationMethods"):
            return FakeAuthResponse({"response": {"methods": [{"name": "sms"}]}})
        if "act=connect_authorize" in url:
            return FakeAuthResponse(
                {"type": "okay", "data": {"is_user_banned": False}},
                cookies={"p": "new-p", "remixsid": "new-sid"},
            )
        raise AssertionError(f"Unexpected URL: {url}")

    async def aclose(self):
        pass


class WebCookieSourceTests(unittest.IsolatedAsyncioTestCase):
    async def test_refresh_uses_and_persists_rotated_cookies(self):
        store = MemoryStore()
        http = FakeHttpClient(
            FakeResponse(
                {"data": {"access_token": "fresh-token", "expires": 4_000_000_000}},
                {"p": "new-p", "remixsid": "new-remixsid", "unrelated": "ignored"},
            )
        )
        source = WebCookieSource(
            {"p": "old-p", "remixsid": "old-remixsid"},
            http=http,
            store=store,
        )

        await source.refresh()

        self.assertEqual(
            source.cookies,
            {"p": "new-p", "remixsid": "new-remixsid"},
        )
        self.assertEqual(http.calls[0][1]["cookies"], {
            "p": "old-p",
            "remixsid": "old-remixsid",
        })
        state = await store.load(*source.identity)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.cookie_p, "new-p")
        self.assertEqual(state.cookie_remixsid, "new-remixsid")

    async def test_rotated_cookies_are_saved_if_token_response_is_invalid(self):
        store = MemoryStore()
        http = FakeHttpClient(FakeResponse({}, {"remixsid": "rotated-remixsid"}))
        source = WebCookieSource(
            {"p": "p-value", "remixsid": "old-remixsid"},
            http=http,
            store=store,
        )

        with self.assertRaises(TokenSourceError):
            await source.refresh()

        state = await store.load(*source.identity)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.cookie_remixsid, "rotated-remixsid")


class PasswordCookieSourceTests(unittest.IsolatedAsyncioTestCase):
    async def test_vkclient_accepts_login_and_password(self):
        client = VKClient(
            login="user@example.com",
            password="test-password",
            http_client=FakePasswordHttpClient(),
            store=MemoryStore(),
        )

        self.assertIsInstance(client._entries[-1].source, PasswordCookieSource)
        await client.aclose()

    async def test_reauthenticates_when_saved_cookies_cannot_get_web_token(self):
        store = MemoryStore()
        await store.save(
            State(
                app_id=6287487,
                client="default",
                source="password",
                user_id=42,
                cookie_p="old-p",
                cookie_remixsid="old-sid",
                login="user@example.com",
                password="test-password",
            )
        )
        http = FakePasswordHttpClient()
        source = PasswordCookieSource(
            "user@example.com", http=http, store=store, source="password"
        )

        token = await source.token()

        self.assertEqual(token, "fresh-web-token")
        self.assertEqual(
            [url for method, url, _ in http.calls if method == "POST"],
            [
                WEB_TOKEN_URL,
                "https://api.vk.ru/method/auth.validateAccount",
                "https://login.vk.ru/?act=connect_authorize",
                WEB_TOKEN_URL,
            ],
        )
        state = await store.load(*source.identity)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.cookie_p, "new-p")
        self.assertEqual(state.cookie_remixsid, "new-sid")
        self.assertEqual(state.login, "user@example.com")
        self.assertEqual(state.password, "test-password")

    async def test_fails_clearly_when_vk_requires_an_otp(self):
        source = PasswordCookieSource(
            "user@example.com",
            "test-password",
            http=FakePasswordHttpClient(verification_method="sms"),
            store=MemoryStore(),
        )

        with self.assertRaises(TokenSourceError) as context:
            await source.token()

        self.assertEqual(context.exception.code, "password_auth_failed")
        self.assertIn("невозможно авторизоваться только по логину/паролю", str(context.exception))
        self.assertIn("дополнительный код", str(context.exception))
        self.assertNotIn("test-password", str(context.exception))

    async def test_requires_password_when_cookies_are_invalid(self):
        store = MemoryStore()
        await store.save(
            State(
                app_id=6287487,
                client="default",
                source="password",
                cookie_p="old-p",
                cookie_remixsid="old-sid",
            )
        )
        source = PasswordCookieSource(
            "user@example.com",
            http=FakePasswordHttpClient(),
            store=store,
            source="password",
        )

        with self.assertRaises(TokenSourceError) as context:
            await source.token()

        self.assertEqual(context.exception.code, "password_auth_failed")
        self.assertIn("пароль не передан", str(context.exception))


class PasswordCredentialStoreTests(unittest.IsolatedAsyncioTestCase):
    async def test_json_store_persists_credentials_with_cookie_record(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "auth.json"
            store = JSONStore(path)
            state = State(
                app_id=6287487,
                client="default",
                source="password",
                user_id=42,
                cookie_p="p-value",
                cookie_remixsid="sid-value",
                login="user@example.com",
                password="test-password",
            )

            await store.save(state)

            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["cookies"][0]["_vkx"]["login"], "user@example.com")
            self.assertEqual(saved["cookies"][0]["_vkx"]["password"], "test-password")
            self.assertEqual(await store.load(6287487, "default", "password"), state)

    async def test_sqlite_persists_credentials_and_migrates_old_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "auth.sqlite"
            connection = sqlite3.connect(path)
            connection.execute(
                """
                CREATE TABLE states (
                    app_id INTEGER NOT NULL,
                    client TEXT NOT NULL,
                    source TEXT NOT NULL,
                    user_id INTEGER,
                    group_id INTEGER,
                    token TEXT,
                    token_expires REAL,
                    cookie_p TEXT,
                    cookie_remixsid TEXT,
                    updated_at REAL NOT NULL DEFAULT 0,
                    PRIMARY KEY (app_id, client, source)
                )
                """
            )
            connection.execute(
                "INSERT INTO states (app_id, client, source) VALUES (?, ?, ?)",
                (6287487, "default", "password"),
            )
            connection.commit()
            connection.close()

            store = SQLiteStore(path)
            state = State(
                app_id=6287487,
                client="default",
                source="password",
                login="user@example.com",
                password="test-password",
            )
            await store.save(state)

            self.assertEqual(await store.load(6287487, "default", "password"), state)
            await store.aclose()


if __name__ == "__main__":
    unittest.main()
