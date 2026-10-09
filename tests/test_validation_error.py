import json
import unittest

from pydantic import ValidationError

from vkx import VKClient, VKError, VKValidationError
from vkx.models.objects import Personal, UserSettings


class FakeResponse:
    status_code = 200

    def __init__(self, payload):
        self.text = json.dumps(payload, separators=(",", ":"))
        self._payload = payload

    def json(self):
        return self._payload


class FakeHttpClient:
    async def post(self, url, **kwargs):
        method = url.rsplit("/", 1)[-1]
        if method == "users.get":
            payload = {"response": [{"id": 123, "first_name": "Test", "last_name": "User"}]}
        elif method == "account.getAppPermissions":
            payload = {"response": 0}
        elif method == "execute":
            payload = {"response": [{"personal": []}], "execute_errors": []}
        elif method == "account.getProfileInfo":
            payload = {"response": {"personal": []}}
        else:
            raise AssertionError(f"Unexpected VK method: {method}")
        return FakeResponse(payload)

    async def get(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP GET: {url}")

    async def aclose(self):
        pass


class ValidationErrorTests(unittest.IsolatedAsyncioTestCase):
    async def test_validation_error_keeps_raw_http_body_for_direct_and_batched_calls(self):
        for batching in (False, True):
            with self.subTest(batching=batching):
                client = VKClient(
                    tokens="test-token",
                    http_client=FakeHttpClient(),
                    interval=0,
                    batching=batching,
                    pagination=False,
                )
                try:
                    with self.assertRaises(VKValidationError) as caught:
                        await client.account.get_profile_info()

                    error = caught.exception
                    self.assertIsInstance(error, VKError)
                    self.assertEqual(error.call.method, "account.getProfileInfo")
                    self.assertEqual(error.raw, {"personal": []})
                    self.assertEqual(
                        error.raw_response,
                        '{"response":{"personal":[]}}'
                        if not batching
                        else '{"response":[{"personal":[]}],"execute_errors":[]}',
                    )
                    self.assertTrue(error.validation_error.errors())
                finally:
                    await client.aclose()


class PersonalModelTests(unittest.TestCase):
    def test_empty_personal_array_is_parsed_as_an_empty_model(self):
        settings = UserSettings.model_validate(
            {
                "id": 123,
                "home_town": "",
                "status": "",
                "personal": [],
            }
        )

        self.assertIsInstance(settings.personal, Personal)
        self.assertIsNone(settings.personal.alcohol)

    def test_non_empty_personal_array_is_not_silently_accepted(self):
        with self.assertRaises(ValidationError):
            Personal.model_validate([1])


if __name__ == "__main__":
    unittest.main()
