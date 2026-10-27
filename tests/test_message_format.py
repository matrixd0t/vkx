"""Разбор разметки сообщений (HTML/markdown) -> format_data VK."""

import json
import unittest

from vkx import VKClient
from vkx.models.formatting import (
    FormatData,
    format_data_json,
    format_data_to_json,
    parse_format,
    u16_len,
)
from vkx.models.methods.messages import MessagesCategory
from vkx.models.objects import Message


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
            payload = {"response": [{"message_id": 1, "cmid": 101}], "execute_errors": []}
        elif method == "messages.send":
            payload = {"response": {"message_id": len(self.calls), "cmid": len(self.calls) + 100}}
        elif method == "messages.edit":
            payload = {"response": 1}
        else:
            raise AssertionError(f"Unexpected VK method: {method}")
        return FakeResponse(payload)

    async def get(self, url, **kwargs):
        raise AssertionError(f"Unexpected HTTP GET: {url}")

    async def aclose(self):
        pass


class FormattingApi:
    """Мост категории: разбор разметки (как у клиента)."""

    def __init__(self, parse=True):
        self.calls = []
        self.parse = parse

    def format_message(self, message):
        if not self.parse:
            return message, []
        return parse_format(message)

    async def request(self, method, params):
        self.calls.append((method, params.copy()))
        if method == "messages.edit":
            return {"response": 1}
        return {"response": {"message_id": len(self.calls), "cmid": len(self.calls) + 100}}


class ParseFormatTests(unittest.TestCase):
    def test_plain_text_is_untouched(self):
        text, items = parse_format("простой текст")

        self.assertEqual(text, "простой текст")
        self.assertEqual(items, [])

    def test_html_tags_become_items(self):
        text, items = parse_format("привет <b>мир</b> и <i>тест</i>")

        self.assertEqual(text, "привет мир и тест")
        self.assertEqual(
            [(item.type, item.offset, item.length) for item in items],
            [("bold", 7, 3), ("italic", 13, 4)],
        )

    def test_markdown_becomes_items(self):
        text, items = parse_format("**жирный** и *курсив* и _подчёркнутый_")

        self.assertEqual(text, "жирный и курсив и подчёркнутый")
        self.assertEqual(
            [(item.type, item.offset, item.length) for item in items],
            [("bold", 0, 6), ("italic", 9, 6), ("italic", 18, 12)],
        )

    def test_double_underscore_is_underline(self):
        text, items = parse_format("__подчёркнутый__")

        self.assertEqual(text, "подчёркнутый")
        self.assertEqual([(item.type, item.length) for item in items], [("underline", 12)])

    def test_links_become_url_items(self):
        text, items = parse_format("ссылка [тут](https://google.com)")

        self.assertEqual(text, "ссылка тут")
        self.assertEqual(items[0].type, "url")
        self.assertEqual(items[0].url, "https://google.com")
        self.assertEqual((items[0].offset, items[0].length), (7, 3))

    def test_html_link_becomes_url_item(self):
        text, items = parse_format('<a href="https://google.com">гугл</a>')

        self.assertEqual(text, "гугл")
        self.assertEqual(items[0].type, "url")
        self.assertEqual(items[0].url, "https://google.com")

    def test_nested_tags_produce_overlapping_items(self):
        text, items = parse_format("<b>bold <i>both</i></b>")

        self.assertEqual(text, "bold both")
        self.assertEqual(
            [(item.type, item.offset, item.length) for item in items],
            [("bold", 0, 9), ("italic", 5, 4)],
        )

    def test_unsupported_strike_is_stripped_without_item(self):
        text, items = parse_format("<s>зачёркнутый</s> и ~~ещё~~")

        self.assertEqual(text, "зачёркнутый и ещё")
        self.assertEqual(items, [])

    def test_offsets_count_utf16_units(self):
        text, items = parse_format("😀😀<b>тест</b>")

        self.assertEqual(text, "😀😀тест")
        self.assertEqual(u16_len(text), 8)
        self.assertEqual((items[0].offset, items[0].length), (4, 4))

    def test_plain_stars_and_underscores_stay_text(self):
        self.assertEqual(parse_format("2 * 3 * 4")[1], [])
        self.assertEqual(parse_format("snake_case_name")[1], [])
        self.assertEqual(parse_format("текст с < неизвестным > тегом")[1], [])

    def test_br_becomes_newline(self):
        text, items = parse_format("первая<br>вторая")

        self.assertEqual(text, "первая\nвторая")
        self.assertEqual(items, [])

    def test_format_data_json_is_compact(self):
        payload = format_data_json(parse_format("**жир**")[1])

        self.assertEqual(
            payload,
            '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
        )

    def test_format_data_to_json_accepts_dict_and_model(self):
        self.assertEqual(
            format_data_to_json({"version": "1", "items": []}),
            '{"version":"1","items":[]}',
        )
        model = FormatData(items=parse_format("**жир**")[1])
        self.assertEqual(
            format_data_to_json(model),
            '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
        )
        self.assertIsNone(format_data_to_json(None))


class MessagesFormatDataTests(unittest.IsolatedAsyncioTestCase):
    async def test_send_parses_markup(self):
        api = FormattingApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="привет <b>мир</b>")

        method, params = api.calls[0]
        self.assertEqual(method, "messages.send")
        self.assertEqual(params["message"], "привет мир")
        self.assertEqual(
            params["format_data"],
            '{"version":"1","items":[{"type":"bold","offset":7,"length":3}]}',
        )

    async def test_send_keeps_own_format_data_and_skips_parsing(self):
        api = FormattingApi()
        messages = MessagesCategory(api)
        own = '{"version":"1","items":[{"type":"italic","offset":0,"length":3}]}'

        await messages.send(peer_id=42, message="<b>мир</b>", format_data=own)

        _, params = api.calls[0]
        self.assertEqual(params["message"], "<b>мир</b>")
        self.assertEqual(params["format_data"], own)

    async def test_send_accepts_format_data_as_dict(self):
        api = FormattingApi()
        messages = MessagesCategory(api)

        await messages.send(
            peer_id=42,
            message="мир",
            format_data={"version": "1", "items": [{"type": "bold", "offset": 0, "length": 3}]},
        )

        _, params = api.calls[0]
        self.assertEqual(
            params["format_data"],
            '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
        )

    async def test_send_without_parsing_keeps_text_as_is(self):
        api = FormattingApi(parse=False)
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="привет <b>мир</b>")

        _, params = api.calls[0]
        self.assertEqual(params["message"], "привет <b>мир</b>")
        self.assertNotIn("format_data", params)

    async def test_long_message_is_split_with_shifted_offsets(self):
        api = FormattingApi()
        messages = MessagesCategory(api)

        await messages.send(peer_id=42, message="a" * 4000 + "**жир**")

        self.assertEqual(len(api.calls), 2)
        first, second = api.calls[0][1], api.calls[1][1]
        self.assertEqual(len(first["message"]), 4000)
        self.assertNotIn("format_data", first)
        self.assertEqual(second["message"], "жир")
        self.assertEqual(
            second["format_data"],
            '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
        )

    async def test_edit_parses_markup(self):
        api = FormattingApi()
        messages = MessagesCategory(api)

        await messages.edit(peer_id=42, message_id=1, message="привет <i>мир</i>")

        method, params = api.calls[0]
        self.assertEqual(method, "messages.edit")
        self.assertEqual(params["message"], "привет мир")
        self.assertEqual(
            params["format_data"],
            '{"version":"1","items":[{"type":"italic","offset":7,"length":3}]}',
        )


class SyntaxSwitchTests(unittest.TestCase):
    def test_markdown_only(self):
        text, items = parse_format("**жир** и <b>тоже жир</b>", markdown=True, html=False)

        self.assertEqual(text, "жир и <b>тоже жир</b>")
        self.assertEqual([(item.type, item.offset, item.length) for item in items], [("bold", 0, 3)])

    def test_html_only(self):
        text, items = parse_format("**жир** и <b>тоже жир</b>", markdown=False, html=True)

        self.assertEqual(text, "**жир** и тоже жир")
        self.assertEqual([(item.type, item.offset, item.length) for item in items], [("bold", 10, 8)])

    def test_both_disabled(self):
        text, items = parse_format("**жир** и <b>тоже жир</b>", markdown=False, html=False)

        self.assertEqual(text, "**жир** и <b>тоже жир</b>")
        self.assertEqual(items, [])

    def test_markdown_link_is_markdown(self):
        text, items = parse_format("[тут](https://google.com)", markdown=True, html=False)

        self.assertEqual(text, "тут")
        self.assertEqual([(item.type, item.url) for item in items], [("url", "https://google.com")])

    def test_html_link_is_html(self):
        text, items = parse_format(
            '<a href="https://google.com">тут</a>', markdown=False, html=True
        )

        self.assertEqual(text, "тут")
        self.assertEqual([(item.type, item.url) for item in items], [("url", "https://google.com")])


class ClientParseFormatTests(unittest.IsolatedAsyncioTestCase):
    async def test_raw_send_without_message_uses_empty_string(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            await client.call("messages.send", peer_id=42, attachment="photo1_2")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "")
        finally:
            await client.aclose()

    async def test_raw_call_gets_random_id_zero_by_default(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            await client.call("messages.send", peer_id=42, message="**жир**")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["random_id"], "0")
        finally:
            await client.aclose()

    async def test_typed_send_parses_markup(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            await client.messages.send(peer_id=42, message="привет <b>мир</b>")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "привет мир")
            self.assertEqual(
                sends[0]["format_data"],
                '{"version":"1","items":[{"type":"bold","offset":7,"length":3}]}',
            )
        finally:
            await client.aclose()

    async def test_raw_call_parses_markup(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            await client.call("messages.send", peer_id=42, message="**жир**")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "жир")
            self.assertEqual(
                sends[0]["format_data"],
                '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
            )
        finally:
            await client.aclose()

    async def test_raw_call_with_own_format_data_is_not_parsed(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        own = '{"version":"1","items":[{"type":"italic","offset":0,"length":3}]}'
        try:
            await client.call(
                "messages.send",
                peer_id=42,
                message="<b>мир</b>",
                format_data=own,
            )

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "<b>мир</b>")
            self.assertEqual(sends[0]["format_data"], own)
        finally:
            await client.aclose()

    async def test_parse_format_disabled_on_client(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
            parse_format=False,
        )
        try:
            await client.messages.send(peer_id=42, message="привет <b>мир</b>")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "привет <b>мир</b>")
            self.assertNotIn("format_data", sends[0])
        finally:
            await client.aclose()

    async def test_parse_format_disabled_by_overrides(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            async with client.overrides(parse_format=False):
                await client.messages.send(peer_id=42, message="**жир**")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "**жир**")
            self.assertNotIn("format_data", sends[0])

            await client.messages.send(peer_id=42, message="**жир**")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[1]["message"], "жир")
            self.assertIn("format_data", sends[1])
        finally:
            await client.aclose()

    async def test_batched_call_embeds_format_data(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=True,
            pagination=False,
        )
        try:
            await client.messages.send(peer_id=42, message="**жир**")

            executes = [data for method, data in http.calls if method == "execute"]
            code = executes[0]["code"]
            self.assertIn('"message":"жир"', code)
            self.assertIn("format_data", code)
        finally:
            await client.aclose()

    async def test_parse_markdown_disabled_keeps_markdown_as_text(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
            parse_markdown=False,
        )
        try:
            await client.messages.send(peer_id=42, message="**жир** и <b>тег</b>")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "**жир** и тег")
            self.assertEqual(
                sends[0]["format_data"],
                '{"version":"1","items":[{"type":"bold","offset":10,"length":3}]}',
            )
        finally:
            await client.aclose()

    async def test_parse_html_disabled_keeps_html_as_text(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
            parse_html=False,
        )
        try:
            await client.messages.send(peer_id=42, message="**жир** и <b>тег</b>")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "жир и <b>тег</b>")
            self.assertEqual(
                sends[0]["format_data"],
                '{"version":"1","items":[{"type":"bold","offset":0,"length":3}]}',
            )
        finally:
            await client.aclose()

    async def test_syntax_switches_by_overrides(self):
        http = FakeHttpClient()
        client = VKClient(
            tokens="test-token",
            http_client=http,
            interval=0,
            batching=False,
            pagination=False,
        )
        try:
            async with client.overrides(parse_html=False):
                await client.messages.send(peer_id=42, message="**жир** и <b>тег</b>")

            sends = [data for method, data in http.calls if method == "messages.send"]
            self.assertEqual(sends[0]["message"], "жир и <b>тег</b>")
        finally:
            await client.aclose()

    async def test_format_message_helper(self):
        client = VKClient(tokens="test-token", http_client=FakeHttpClient(), interval=0)
        try:
            text, items = client.format_message("**жир**")

            self.assertEqual(text, "жир")
            self.assertEqual([item.type for item in items], ["bold"])

            client.parse_format = False
            text, items = client.format_message("**жир**")

            self.assertEqual(text, "**жир**")
            self.assertEqual(items, [])
        finally:
            await client.aclose()


class MessageModelTests(unittest.TestCase):
    def test_message_exposes_format_data(self):
        message = Message.model_validate(
            {
                "conversation_message_id": 1,
                "date": 1700000000,
                "from_id": 123,
                "id": 5,
                "text": "привет мир",
                "version": 1,
                "out": 0,
                "peer_id": 123,
                "format_data": {
                    "version": "1",
                    "items": [
                        {"type": "bold", "offset": 7, "length": 3},
                        {"type": "url", "offset": 0, "length": 7, "url": "https://vk.com"},
                    ],
                },
            }
        )

        self.assertIsNotNone(message.format_data)
        self.assertEqual(message.format_data.version, "1")
        self.assertEqual(message.format_data.items[0].type, "bold")
        self.assertEqual(message.format_data.items[1].url, "https://vk.com")

    def test_message_without_format_data(self):
        message = Message.model_validate(
            {
                "conversation_message_id": 1,
                "date": 1700000000,
                "from_id": 123,
                "id": 5,
                "text": "привет",
                "version": 1,
                "out": 0,
                "peer_id": 123,
            }
        )

        self.assertIsNone(message.format_data)


if __name__ == "__main__":
    unittest.main()
