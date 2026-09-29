"""Bots Long Poll сообщества (``groups.getLongPollServer``).

Асинхронный контекстный менеджер и асинхронный итератор событий:

    async with BotsLongPoll(vk) as longpoll:
        async for event in longpoll:
            ...

``__aenter__`` запускает фоновый поллинг, ``__aexit__`` останавливает его.
Формат событий совпадает с Callback API, поэтому updates разбираются тем же
``parse_callback`` и отдаются как типизированные ``CallbackEvent``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from vkx.client.client import VKError
from vkx.models.events.callback_events import CallbackEvent
from vkx.server.callback import parse_callback

from ._polling import DEFAULT_WAIT, BaseLongPoll

if TYPE_CHECKING:
    import logging
    from collections.abc import Iterable

    from vkx.client.client import VKClient
    from vkx.client.http import HttpClient


class BotsLongPoll(BaseLongPoll):
    """Bots Long Poll для токена сообщества (group Long Poll)."""

    def __init__(
        self,
        client: VKClient,
        *,
        group_id: int | None = None,
        http_client: HttpClient | None = None,
        logger: logging.Logger | None = None,
        wait: int = DEFAULT_WAIT,
    ) -> None:
        super().__init__(client, http_client=http_client, logger=logger, wait=wait)
        self._group_id = group_id

    @property
    def group_id(self) -> int | None:
        return self._group_id if self._group_id is not None else self._client.group_id

    async def get_server(self) -> dict[str, Any]:
        group_id = self.group_id
        if group_id is None:
            raise VKError(
                "BotsLongPoll: нужен group_id — клиент не привязан к сообществу",
                client=self._client,
            )
        params = await self._client.groups.get_long_poll_server(group_id=group_id)
        return {"server": params.server, "key": params.key, "ts": params.ts}

    def parse_updates(self, updates: Iterable[Any]) -> list[CallbackEvent]:
        return [parse_callback(update) for update in updates]


__all__ = ("BotsLongPoll",)
