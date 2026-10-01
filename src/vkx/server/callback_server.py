"""Callback-сервер: персистентное состояние для уведомлений Callback API.

``parse_callback`` — чистый парсер без состояния. Всё, что требует памяти между
запросами (ожидаемый ``secret``, ``confirmation``-код, дедупликация ``event_id``),
живёт здесь. Модуль по-прежнему framework-agnostic: он не знает про HTTP, но
хранит состояние и решает, какое уведомление «своё».

- ``CallbackServer`` — один колбек-сервер сообщества: пропускает только события
  своего ``group_id`` с корректным ``secret`` и каждое ``event_id`` — один раз.
- ``CallbackListener`` — набор ``CallbackServer``: маршрутизирует уведомление по
  ``group_id``. Одному URL можно отдать несколько сообществ.
- ``create_callback_server`` — регистрирует сервер в сообществе
  (``groups.addCallbackServer``), забирает ``confirmation``-код и возвращает
  готовый ``CallbackServer``.

Типовой вебхук (любой фреймворк):

    listener = CallbackListener([server])
    event = listener.handle(request.body)
    if event is None:            # чужой group_id / плохой secret / дубликат
        return Response("ok", status=200)
    if event.type is CallbackEventType.CONFIRMATION:
        return Response(server.confirmation_code or "", media_type="text/plain")
    return Response("ok", status=200)
"""

from __future__ import annotations

from collections import OrderedDict
from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING

from ..models.events.callback_events import CallbackEvent
from ..models.events.enums import CallbackEventType
from .callback import RawCallback, parse_callback

if TYPE_CHECKING:
    from ..client.client import VKClient

MAX_TITLE_LENGTH = 14
MAX_SECRET_LENGTH = 50
DEFAULT_DEDUP_SIZE = 200


class CallbackServer:
    """Состояние одного колбек-сервера сообщества.

    Хранит ``group_id``, ожидаемый ``secret``, ``confirmation``-код и кольцевой
    буфер недавних ``event_id``. ``handle``/``handle_event`` возвращают событие,
    если оно принадлежит этому серверу, прошло проверку ``secret`` и не является
    дубликатом; иначе ``None``.
    """

    def __init__(
        self,
        group_id: int,
        *,
        secret: str | None = None,
        confirmation_code: str | None = None,
        server_id: int | None = None,
        dedup_size: int = DEFAULT_DEDUP_SIZE,
    ) -> None:
        if secret is not None and len(secret) > MAX_SECRET_LENGTH:
            raise ValueError(
                f"secret: длина не больше {MAX_SECRET_LENGTH} символов (получено {len(secret)})"
            )
        if dedup_size <= 0:
            raise ValueError("dedup_size: размер буфера дедупликации должен быть положительным")
        self.group_id = group_id
        self.secret = secret
        self.confirmation_code = confirmation_code
        self.server_id = server_id
        self.dedup_size = dedup_size
        self._seen: OrderedDict[str, None] = OrderedDict()

    def __repr__(self) -> str:
        return f"CallbackServer(group_id={self.group_id}, server_id={self.server_id})"

    def accepts(self, event: CallbackEvent) -> bool:
        """Своё ли событие: совпадает ``group_id`` и (если задан) ``secret``."""
        if event.group_id is not None and event.group_id != self.group_id:
            return False
        return self.secret is None or event.secret == self.secret

    def is_duplicate(self, event_id: str | int | None) -> bool:
        """True, если ``event_id`` уже встречался; новый id запоминает."""
        if event_id is None:
            return False
        key = str(event_id)
        if key in self._seen:
            self._seen.move_to_end(key)
            return True
        self._seen[key] = None
        if len(self._seen) > self.dedup_size:
            self._seen.popitem(last=False)
        return False

    def handle(self, raw: RawCallback, /) -> CallbackEvent | None:
        """Разобрать и отфильтровать уведомление (чужое/поддельное/дубль -> None)."""
        return self.handle_event(parse_callback(raw))

    def handle_event(self, event: CallbackEvent) -> CallbackEvent | None:
        """Отфильтровать уже разобранное событие."""
        if not self.accepts(event):
            return None
        if event.type is CallbackEventType.CONFIRMATION:
            return event
        if self.is_duplicate(event.event_id):
            return None
        return event

    def clear_dedup(self) -> None:
        """Забыть историю ``event_id`` (например, при перезапуске обработки)."""
        self._seen.clear()


class CallbackListener:
    """Набор ``CallbackServer``: маршрутизация уведомлений по ``group_id``."""

    def __init__(self, servers: Iterable[CallbackServer] | None = None) -> None:
        self._servers: dict[int, CallbackServer] = {}
        for server in servers or ():
            self.add(server)

    def __iter__(self) -> Iterator[CallbackServer]:
        return iter(self._servers.values())

    def __len__(self) -> int:
        return len(self._servers)

    def __contains__(self, group_id: object) -> bool:
        return group_id in self._servers

    @property
    def servers(self) -> tuple[CallbackServer, ...]:
        return tuple(self._servers.values())

    def add(self, server: CallbackServer) -> CallbackServer:
        """Добавить сервер (или заменить существующий с тем же ``group_id``)."""
        self._servers[server.group_id] = server
        return server

    def remove(self, group_id: int) -> CallbackServer | None:
        return self._servers.pop(group_id, None)

    def get(self, group_id: int) -> CallbackServer | None:
        return self._servers.get(group_id)

    def handle(self, raw: RawCallback, /) -> CallbackEvent | None:
        """Разобрать уведомление и отдать серверу его ``group_id``."""
        event = parse_callback(raw)
        if event.group_id is None:
            return None
        server = self._servers.get(event.group_id)
        if server is None:
            return None
        return server.handle_event(event)


async def create_callback_server(
    client: VKClient,
    group_id: int,
    url: str,
    *,
    title: str = "vkx",
    secret: str | None = None,
    confirmation_code: str | None = None,
    dedup_size: int = DEFAULT_DEDUP_SIZE,
) -> CallbackServer:
    """Зарегистрировать колбек-сервер в сообществе и вернуть ``CallbackServer``.

    :param client: клиент сообщества (нужны права на управление).
    :param group_id: id сообщества.
    :param url: адрес вебхука, который принимает уведомления.
    :param title: название сервера (не длиннее ``MAX_TITLE_LENGTH``).
    :param secret: секрет; если задан, передаётся в VK как ``secret_key`` (не длиннее ``MAX_SECRET_LENGTH``). Если не задан — секрет не ставится.
    :param confirmation_code: готовый код; если не задан — берётся через ``groups.getCallbackConfirmationCode``.
    """
    if not title or len(title) > MAX_TITLE_LENGTH:
        raise ValueError(
            f"title: длина от 1 до {MAX_TITLE_LENGTH} символов (получено {len(title)})"
        )
    if secret is not None and len(secret) > MAX_SECRET_LENGTH:
        raise ValueError(
            f"secret: длина не больше {MAX_SECRET_LENGTH} символов (получено {len(secret)})"
        )
    created = await client.groups.add_callback_server(
        group_id=group_id,
        title=title,
        url=url,
        secret_key=secret,
    )
    if confirmation_code is None:
        response = await client.groups.get_callback_confirmation_code(group_id=group_id)
        confirmation_code = response.code
    return CallbackServer(
        group_id,
        secret=secret,
        confirmation_code=confirmation_code,
        server_id=created.server_id,
        dedup_size=dedup_size,
    )


__all__ = (
    "DEFAULT_DEDUP_SIZE",
    "MAX_SECRET_LENGTH",
    "MAX_TITLE_LENGTH",
    "CallbackListener",
    "CallbackServer",
    "create_callback_server",
)
