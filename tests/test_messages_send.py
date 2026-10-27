import unittest

from vkx.models.methods.messages import MessagesCategory
from vkx.models.responses.messages import MessagesSendResponseModel


class FakeApi:
    def __init__(self):
        self.calls = []

    async def request(self, method, params):
        self.calls.append((method, params.copy()))
        call_id = len(self.calls)
        if "peer_ids" in params:
            return {
                "response": [
                    {"peer_id": peer_id, "message_id": call_id}
                    for peer_id in params["peer_ids"]
                ]
            }
        return {"response": {"message_id": call_id, "cmid": call_id + 100}}


class MessagesSendTests(unittest.IsolatedAsyncioTestCase):
    async def test_splits_long_message_and_groups_single_peer_ids(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        result = await messages.send(peer_id=42, message="a" * 4001, random_id=7)

        self.assertEqual([item.message_id for item in result[0]], [1, 2])
        self.assertEqual([item.cmid for item in result[0]], [101, 102])
        self.assertEqual([len(params["message"]) for _, params in api.calls], [4000, 1])
        self.assertEqual([params["random_id"] for _, params in api.calls], [7, 8])
        self.assertEqual("".join(params["message"] for _, params in api.calls), "a" * 4001)

        short = await messages.send(peer_id=42, message="short")
        self.assertEqual(short[0][0].message_id, 3)
        self.assertEqual(short[0][0].cmid, 103)

    async def test_groups_bulk_results_by_peer_across_chunks(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        result = await messages.send(peer_ids=[42, 43], message="b" * 8001)

        self.assertEqual([[item.peer_id for item in peer] for peer in result], [[42] * 3, [43] * 3])
        self.assertEqual(
            [[item.message_id for item in peer] for peer in result],
            [[1, 2, 3], [1, 2, 3]],
        )
        self.assertEqual(
            [len(params["message"]) for _, params in api.calls],
            [4000, 4000, 1],
        )

    async def test_from_and_group_parameters_are_sent_to_vk(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        result = await messages.send(
            peer_id=42,
            message="test",
            group_id=62391174,
            _from="reforged",
        )

        self.assertEqual(result[0][0].message_id, 1)
        self.assertEqual(result[0][0].cmid, 101)
        self.assertEqual(
            api.calls,
            [
                (
                    "messages.send",
                    {
                        "peer_id": 42,
                        "message": "test",
                        "group_id": 62391174,
                        "from": "reforged",
                        "random_id": 0,
                    },
                )
            ],
        )

    async def test_random_id_defaults_to_zero(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="test")

        self.assertEqual(api.calls[0][1]["random_id"], 0)

    async def test_message_defaults_to_empty_string(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42)

        self.assertEqual(api.calls[0][1]["message"], "")

    async def test_random_id_zero_keeps_every_chunk_at_zero(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="a" * 8001, random_id=0)

        self.assertEqual(
            [params["random_id"] for _, params in api.calls],
            [0, 0, 0],
        )

    async def test_explicit_random_id_is_incremented_per_chunk(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="a" * 8001, random_id=7)

        self.assertEqual(
            [params["random_id"] for _, params in api.calls],
            [7, 8, 9],
        )

    def test_legacy_integer_response_keeps_message_id(self):
        result = MessagesSendResponseModel.model_validate(42)

        self.assertEqual(result.message_id, 42)
        self.assertIsNone(result.cmid)


if __name__ == "__main__":
    unittest.main()
