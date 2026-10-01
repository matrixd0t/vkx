"""Пример: CallbackServer/CallbackListener — secret, confirmation, дедупликация.

Парсер ``parse_callback`` ничего не проверяет; проверки живут здесь.
"""

from __future__ import annotations

from vkx import CallbackListener, CallbackServer
from vkx.models import CallbackEventType

BODY = {
    "type": "message_new",
    "group_id": 1,
    "event_id": "e1",
    "secret": "s3cret",
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


def main() -> None:
    server = CallbackServer(group_id=1, secret="s3cret", confirmation_code="abc123")
    listener = CallbackListener([server])  # необязательно

    event = listener.handle(BODY)
    # или event = server.handle(BODY), если вам не нужна группировка нескольких серверов
    print("первое уведомление:", event)

    # Повтор с тем же event_id — дубликат, возвращается None.
    print("повтор:", listener.handle(BODY))

    # Событие с чужим secret отбрасывается.
    forged = {**BODY, "event_id": "e2", "secret": "wrong"}
    print("чужой secret:", listener.handle(forged))

    # confirmation нужно вернуть синхронно.
    confirmation = listener.handle({"type": "confirmation", "group_id": 1})
    if confirmation and confirmation.type is CallbackEventType.CONFIRMATION:
        print("confirmation:", server.confirmation_code)

    # Несколько сообществ на одном URL — маршрутизация по group_id.
    server_b = CallbackServer(group_id=2, confirmation_code="def456")
    both = CallbackListener([server, server_b])
    # или listener.add(server_b)
    print("серверов:", len(both), "| от группы id=2:", 2 in both)

    # Ручная проверка секрета/дедупликации без парсинга
    print("accepts:", server.accepts(event) if event else None)
    print("is_duplicate:", server.is_duplicate("e1"))


if __name__ == "__main__":
    main()
