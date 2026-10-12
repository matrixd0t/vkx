import unittest
from unittest import mock

from vkx.server.callback import parse_callback
from vkx.server.callback_server import CallbackServer

GROUP_ID = 242194568

PHOTO_COMMENT_NEW = {
    "group_id": GROUP_ID,
    "type": "photo_comment_new",
    "event_id": "f964f2e5b48800bc2d12ea719f20928f5a861883",
    "v": "5.199",
    "object": {
        "photo_owner_id": -GROUP_ID,
        "id": 1,
        "from_id": -GROUP_ID,
        "date": 1791786715,
        "text": "комментарий",
        "can_delete": 1,
        "photo_id": 457239018,
    },
}

WALL_REPLY_NEW = {
    "group_id": GROUP_ID,
    "type": "wall_reply_new",
    "event_id": "bf1c44f5a7e90ee19a46327048bd53caef6bca22",
    "v": "5.199",
    "object": {
        "id": 6,
        "from_id": -GROUP_ID,
        "date": 1791786715,
        "text": "комментарий",
        "can_delete": 1,
        "post_id": 5,
        "owner_id": -GROUP_ID,
        "parents_stack": [],
        "thread": {"count": 0},
        "is_from_post_author": True,
        "post_owner_id": -GROUP_ID,
    },
}


def _with(fields):
    raw = {**WALL_REPLY_NEW, "object": {**WALL_REPLY_NEW["object"], **fields}}
    return parse_callback(raw)


class ContentDedupTests(unittest.TestCase):
    def test_cross_type_duplicate_is_filtered(self):
        server = CallbackServer(GROUP_ID)
        first = parse_callback(PHOTO_COMMENT_NEW)
        second = parse_callback(WALL_REPLY_NEW)

        self.assertIsNotNone(server.handle_event(first))
        self.assertIsNone(server.handle_event(second))

    def test_can_be_disabled(self):
        server = CallbackServer(GROUP_ID, content_dedup=False)
        first = parse_callback(PHOTO_COMMENT_NEW)
        second = parse_callback(WALL_REPLY_NEW)

        self.assertIsNotNone(server.handle_event(first))
        self.assertIsNotNone(server.handle_event(second))

    def test_different_text_is_not_duplicate(self):
        server = CallbackServer(GROUP_ID)
        self.assertIsNotNone(server.handle_event(parse_callback(PHOTO_COMMENT_NEW)))
        self.assertIsNotNone(server.handle_event(_with({"text": "другой"})))

    def test_different_author_is_not_duplicate(self):
        server = CallbackServer(GROUP_ID)
        self.assertIsNotNone(server.handle_event(parse_callback(PHOTO_COMMENT_NEW)))
        self.assertIsNotNone(server.handle_event(_with({"from_id": 777})))

    def test_allows_again_after_ttl(self):
        server = CallbackServer(GROUP_ID, content_dedup_ttl=10.0)
        first = parse_callback(PHOTO_COMMENT_NEW)
        second = parse_callback(WALL_REPLY_NEW)
        third = parse_callback({**WALL_REPLY_NEW, "event_id": "another-event-id"})

        with mock.patch("vkx.server.callback_server.time.monotonic", side_effect=[100.0, 105.0]):
            self.assertIsNotNone(server.handle_event(first))
            self.assertIsNone(server.handle_event(second))

        with mock.patch("vkx.server.callback_server.time.monotonic", return_value=111.0):
            self.assertIsNotNone(server.handle_event(third))

    def test_clear_dedup_forgets_content(self):
        server = CallbackServer(GROUP_ID)
        first = parse_callback(PHOTO_COMMENT_NEW)
        second = parse_callback(WALL_REPLY_NEW)

        self.assertIsNotNone(server.handle_event(first))
        self.assertIsNone(server.handle_event(second))
        server.clear_dedup()
        self.assertIsNotNone(server.handle_event(second))

    def test_invalid_ttl_rejected(self):
        with self.assertRaises(ValueError):
            CallbackServer(GROUP_ID, content_dedup_ttl=0)


if __name__ == "__main__":
    unittest.main()
