"""Переопределение User-Agent при создании VKClient."""
import unittest

from vkx import VKClient


class FakeHttpClient:
    def __init__(self):
        self.headers = {"user-agent": "Original/1.0", "Accept": "application/json"}

    async def post(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP POST: {url}")

    async def get(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP GET: {url}")

    async def aclose(self):
        pass


class HttpUserAgentTests(unittest.TestCase):
    def test_user_agent_overrides_http_client_header(self):
        http = FakeHttpClient()

        VKClient(tokens="token", http_client=http, user_agent="VKX-Test/1.0")

        self.assertEqual(http.headers["User-Agent"], "VKX-Test/1.0")
        self.assertNotIn("user-agent", http.headers)
        self.assertEqual(http.headers["Accept"], "application/json")

    def test_user_agent_is_optional(self):
        http = FakeHttpClient()

        VKClient(tokens="token", http_client=http)

        self.assertEqual(http.headers["user-agent"], "Original/1.0")


if __name__ == "__main__":
    unittest.main()
