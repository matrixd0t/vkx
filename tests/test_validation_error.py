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
    def __init__(self):
        self.calls = []

    async def post(self, url, **kwargs):
        method = url.rsplit("/", 1)[-1]
        self.calls.append((method, kwargs["data"].copy()))
        if method == "users.get":
            payload = {"response": [{"id": 123, "first_name": "Test", "last_name": "User"}]}
        elif method == "account.getAppPermissions":
            payload = {"response": 4096}
        elif method == "execute":
            payload = {"response": [{"personal": []}], "execute_errors": []}
        elif method == "account.getProfileInfo":
            payload = {"response": {"personal": []}}
        elif method == "messages.send":
            payload = {
                "response": {
                    "message_id": len(self.calls),
                    "cmid": len(self.calls) + 100,
                }
            }
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


class MethodVersionTests(unittest.IsolatedAsyncioTestCase):
    async def test_method_versions_apply_to_user_group_and_per_call_override(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
            method_versions={"users.get": "5.131"},
        )
        try:
            user_result = await client.messages.send(peer_id=123, message="user")
            group_result = await client.messages.send(
                peer_id=123,
                message="group",
                group_id=62391174,
            )
            await client.call(
                "messages.send",
                v="5.150",
                peer_id=123,
                message="explicit version",
            )

            self.assertEqual(user_result[0][0].cmid, 103)
            self.assertEqual(group_result[0][0].cmid, 104)
            versions = {method: data["v"] for method, data in http.calls}
            self.assertEqual(versions["users.get"], "5.131")
            self.assertEqual(versions["account.getAppPermissions"], "5.199")
            self.assertEqual(
                [data["v"] for method, data in http.calls if method == "messages.send"],
                ["5.281", "5.281", "5.150"],
            )
            self.assertEqual(
                [data.get("group_id") for method, data in http.calls if method == "messages.send"],
                [None, "62391174", None],
            )
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
