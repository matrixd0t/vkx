"""Пример: типы vkx.models — объекты и события без сетевого клиента."""

from __future__ import annotations

from vkx import parse_callback
from vkx.models import (
    Button,
    CallbackEventType,
    Keyboard,
    KeyboardButton,
    KeyboardButtonColor,
    Photo,
    parse_user_event,
)
from vkx.models.events.user_events import MessageNewEvent


def main() -> None:
    # --- Клавиатуры ---
    keyboard = Keyboard.from_rows(
        [
            [
                Button("Да", payload={"cmd": "yes"}, color=KeyboardButtonColor.POSITIVE),
                Button("Нет", payload={"cmd": "no"}),
            ],
            [Button("Сайт", type="open_link", link="https://vk.com")],
        ]
    )
    print("keyboard:", keyboard.to_json())

    # Низкоуровневые фабрики (когда нужна именно KeyboardButton).
    print(KeyboardButton.callback("Ок", payload={"a": 1}))
    print(KeyboardButton.link("Сайт", "https://vk.com"))

    # --- Строка-вложение ---
    photo = Photo(album_id=1, date=1700000000, id=5, owner_id=-1, access_key="abc")
    print("attachment:", photo.as_att)  # photo-1_5_abc

    # --- Callback API ---
    event = parse_callback(
        {
            "type": "message_new",
            "group_id": 1,
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
    )
    print("callback:", event.type, "| enum:", event.type is CallbackEventType.MESSAGE_NEW)

    # --- User Long Poll ---
    # Позиционный формат: [код события, message_id, flags, peer_id, timestamp, text, ...]
    user_event = parse_user_event([4, 123, 0, 1, 1700000000, "привет"])
    if isinstance(user_event, MessageNewEvent):
        print("longpoll:", user_event.object.text, user_event.object.peer_id)


if __name__ == "__main__":
    main()
