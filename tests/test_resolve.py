"""Резолв упоминаний (resolve): разбор текста и запросы к VK API."""
import json
import unittest

from vkx import VKClient
from vkx.client.resolve import (
    DEFAULT_RESOLVE_CACHE_SIZE,
    DEFAULT_RESOLVE_CACHE_TTL,
    parse_mentions,
    RESOLVE_CACHE,
    resolve_texts,
)


class FakeResponse:
    status_code = 200

    def __init__(self, payload):
        self.text = json.dumps(payload, separators=(",", ":"))
        self._payload = payload

    def json(self):
        return self._payload


class FakeHttpClient:
    def __init__(self, execute_payloads):
        self.calls = []
        self.execute_payloads = list(execute_payloads)

    async def post(self, url, **kwargs):
        method = url.rsplit("/", 1)[-1]
        self.calls.append((method, dict(kwargs.get("data") or {})))
        if method == "users.get":
            # probe: текущий пользователь
            return FakeResponse({"response": [{"id": 1, "first_name": "Тест", "last_name": "Юзер"}]})
        if method == "account.getAppPermissions":
            return FakeResponse({"response": 4096})
        if method == "execute":
            payload = self.execute_payloads.pop(0) if self.execute_payloads else {"response": [], "execute_errors": []}
            return FakeResponse(payload)
        raise AssertionError(f"Unexpected VK method: {method}")

    async def get(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP GET: {url}")

    async def aclose(self):
        pass


class ResolveParsingTests(unittest.TestCase):
    def test_parse_mentions_ids(self):
        text = "Привет [id123|@Иван] и https://vk.com/club456"
        items = parse_mentions(text)
        self.assertEqual([(m.kind, m.value) for m in items], [("user", "123"), ("group", "456")])

    def test_parse_mentions_invite(self):
        items = parse_mentions("https://vk.ru/invite/abc123")
        self.assertEqual([(m.kind, m.value) for m in items], [("invite", "abc123")])

    def test_parse_mentions_at(self):
        items = parse_mentions("@durov написал")
        self.assertEqual([(m.kind, m.value) for m in items], [("screen", "durov")])

    def test_parse_mentions_resource_owner(self):
        items = parse_mentions("https://vk.com/wall-123_456")
        self.assertEqual([(m.kind, m.value) for m in items], [("group", "123")])

    def test_parse_mentions_dedup(self):
        items = parse_mentions("@durov @durov")
        self.assertEqual(len(items), 1)

    def test_parse_mentions_sorted_by_position(self):
        items = parse_mentions("https://vk.com/club456 @durov")
        self.assertEqual([(m.kind, m.value) for m in items], [("group", "456"), ("screen", "durov")])

    def test_parse_mentions_bracket_raw_full(self):
        items = parse_mentions("[id1|@Иван]")
        self.assertEqual(items[0].raw, "[id1|@Иван]")


class ResolveClientTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        RESOLVE_CACHE.clear()
        self.execute_payloads = [
            {
                "response": [
                    [{"id": 1, "first_name": "Павел", "last_name": "Дуров", "screen_name": "durov"}],
                    {"groups": [{"id": 238753609, "name": "Тест-группа", "screen_name": "night_superior"}], "profiles": []},
                ],
                "execute_errors": [],
            },
        ]
        self.http = FakeHttpClient(self.execute_payloads)
        self.vk = VKClient(tokens="fake", http_client=self.http, interval=0, resolve_cache_ttl=100, resolve_cache_size=10)
        await self.vk.probe()

    async def asyncTearDown(self):
        await self.vk.aclose()

    async def test_resolve_str(self):
        result = await self.vk.resolve("Привет [id1|@Дуров] и https://vk.ru/night_superior")
        self.assertEqual(len(result.users), 1)
        self.assertEqual(result.users[0].id, 1)
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(result.groups[0].id, 238753609)
        # один execute (плюс probe-запросы)
        methods = [m for m, _ in self.http.calls]
        self.assertEqual(methods.count("execute"), 1)

    async def test_resolve_cache_hits(self):
        await self.vk.resolve("@durov")
        before = len(self.http.calls)
        await self.vk.resolve("@durov")
        after = len(self.http.calls)
        self.assertEqual(before, after)  # нет новых execute

    async def test_resolve_dict(self):
        out = await self.vk.resolve({"a": "@durov", "b": "https://vk.ru/night_superior"})
        self.assertEqual(set(out.keys()), {"a", "b"})
        self.assertEqual(len(out["a"].users), 1)
        self.assertEqual(len(out["b"].groups), 1)

    async def test_resolve_list(self):
        out = await self.vk.resolve(["@durov", "https://vk.ru/night_superior", "пусто"])
        self.assertEqual(len(out), 3)
        self.assertEqual((len(out[0].users), len(out[1].groups), len(out[2].users)), (1, 1, 0))

    async def test_resolve_ttl_zero_disables_cache(self):
        self.vk.resolve_cache_ttl = 0
        await self.vk.resolve("@durov")
        before = len(self.http.calls)
        await self.vk.resolve("@durov")
        after = len(self.http.calls)
        self.assertEqual(after - before, 1)  # новый execute


class ResolveInviteTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        RESOLVE_CACHE.clear()
        self.execute_payloads = [
            {
                "response": [
                    {"invite_link": {"group_id": 238753609, "url": "https://vk.ru/invite/keqmlqX", "id": 86287}, "hidden_preview_reason": "invalid_link"},
                ],
                "execute_errors": [],
            },
            {
                "response": [
                    {"groups": [{"id": 238753609, "name": "Приглашённая", "screen_name": "night_superior"}], "profiles": []},
                ],
                "execute_errors": [],
            },
        ]
        self.http = FakeHttpClient(self.execute_payloads)
        self.vk = VKClient(tokens="fake", http_client=self.http, interval=0, resolve_cache_ttl=100, resolve_cache_size=10)
        await self.vk.probe()

    async def asyncTearDown(self):
        await self.vk.aclose()

    async def test_resolve_invite(self):
        result = await self.vk.resolve("https://vk.ru/invite/keqmlqX")
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(result.groups[0].id, 238753609)
        self.assertEqual(result.groups[0].name, "Приглашённая")


if __name__ == "__main__":
    unittest.main()
