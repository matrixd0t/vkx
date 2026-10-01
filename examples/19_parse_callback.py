"""Пример: разбор уведомления Callback API (без сети и состояния)."""

from __future__ import annotations

from vkx import parse_callback
from vkx.models import (
    CallbackEventType,
    MessageEventCallbackEvent,
    MessageNewCallbackEvent,
)

NEW_MESSAGE = {
    "type": "message_new",
    "group_id": 1,
    "event_id": "abc",
    "object": {
        "message": {
            "id": 1,
            "date": 1700000000,
            "from_id": 42,
            "peer_id": 42,
            "text": "привет",
            "conversation_message_id": 10,
            "out": 0,
            "version": 1,
        }
    },
}

BUTTON_PRESS = {
    "type": "message_event",
    "group_id": 1,
    "object": {
        "user_id": 42,
        "peer_id": 42,
        "event_id": "e1",
        "payload": {"cmd": "yes"},
    },
}


def main() -> None:
    event = parse_callback(NEW_MESSAGE)  # bytes / str / dict
    print(event.type, event.group_id)
    if isinstance(event, MessageNewCallbackEvent) and event.object.message:
        print(event.object.message.text, event.object.message.peer_id)

    press = parse_callback(BUTTON_PRESS)
    if isinstance(press, MessageEventCallbackEvent):
        print(press.object.payload, press.object.user_id)

    # Неизвестный тип не роняет парсер: BaseCallbackEvent с сырым object.
    unknown = parse_callback({"type": "future_event", "object": {"x": 1}})
    print(unknown.type is CallbackEventType.NOT_SUPPORTED_MEMBER, unknown.object)


if __name__ == "__main__":
    main()
