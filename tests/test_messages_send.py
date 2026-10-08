import unittest

from vkx.models.methods.messages import MessagesCategory


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
        return {"response": call_id}


class MessagesSendTests(unittest.IsolatedAsyncioTestCase):
    async def test_splits_long_message_and_groups_single_peer_ids(self):
        api = FakeApi()
        messages = MessagesCategory(api)

        result = await messages.send(peer_id=42, message="a" * 4001, random_id=7)

        self.assertEqual(result, [[1, 2]])
        self.assertEqual([len(params["message"]) for _, params in api.calls], [4000, 1])
        self.assertEqual([params["random_id"] for _, params in api.calls], [7, 8])
        self.assertEqual("".join(params["message"] for _, params in api.calls), "a" * 4001)
        self.assertEqual(await messages.send(peer_id=42, message="short"), [[3]])

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


if __name__ == "__main__":
    unittest.main()
