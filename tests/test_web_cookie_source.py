"""Проверки обновления веб-токена и ротации cookie-сессии."""
import unittest

from vkx.client.storage import MemoryStore
from vkx.client.tokens import TokenSourceError, WebCookieSource


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


if __name__ == "__main__":
    unittest.main()
