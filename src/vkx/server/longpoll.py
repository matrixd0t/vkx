"""Long Poll пользователя (``messages.getLongPollServer``).

Асинхронный контекстный менеджер и асинхронный итератор событий:

    async with LongPoll(vk) as longpoll:
        async for event in longpoll:
            ...

``__aenter__`` запускает фоновый поллинг, ``__aexit__`` останавливает его.
Поллинг пользуется токеном ``VKClient`` (через ``messages.getLongPollServer``),
а событие — типизированный ``BaseUserEvent`` из ``vkx.models.events``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from vkx.models.events.user_events import BaseUserEvent, parse_user_event

from ._polling import DEFAULT_LP_VERSION, DEFAULT_WAIT, BaseLongPoll

if TYPE_CHECKING:
    import logging
    from collections.abc import Iterable

    from vkx.client.client import VKClient
    from vkx.client.http import HttpClient

DEFAULT_MODE = 234


class LongPoll(BaseLongPoll):
    """Long Poll для токена пользователя или сообщества (user Long Poll)."""

    def __init__(
        self,
        client: VKClient,
        *,
        group_id: int | None = None,
        need_pts: bool | None = None,
        mode: int = DEFAULT_MODE,
        lp_version: int | None = None,
        http_client: HttpClient | None = None,
        logger: logging.Logger | None = None,
        wait: int = DEFAULT_WAIT,
    ) -> None:
        super().__init__(client, http_client=http_client, logger=logger, wait=wait)
        self._group_id = group_id
        self._need_pts = need_pts
        self._mode = mode
        self._version = lp_version or DEFAULT_LP_VERSION

    async def get_server(self) -> dict[str, Any]:
        params = await self._client.messages.get_long_poll_server(
            group_id=self._group_id,
            lp_version=self._version,
            need_pts=self._need_pts,
        )
        return {"server": params.server, "key": params.key, "ts": params.ts}

    def _fetch_params(self) -> dict[str, Any]:
        return {"mode": self._mode, "version": self._version}

    def _on_invalid_version(self) -> None:
        self._version = DEFAULT_LP_VERSION

    def parse_updates(self, updates: Iterable[Any]) -> list[BaseUserEvent]:
        return [parse_user_event(list(update)) for update in updates]


__all__ = ("LongPoll",)
