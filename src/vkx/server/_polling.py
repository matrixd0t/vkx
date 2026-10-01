"""Общая основа Long Poll-серверов: цикл опроса и async-контекст.

Модуль framework-agnostic: он не знает, какой именно Long Poll (пользователя
или сообщества) обслуживает — наследники задают ``get_server`` (какой метод VK
вызвать) и ``parse_updates`` (как разобрать сырые объекты в события).

Сервер — асинхронный контекстный менеджер и асинхронный итератор:

    async with LongPoll(vk) as longpoll:
        async for event in longpoll:
            ...

``__aenter__`` запускает фоновый поллинг в очередь, ``__aexit__`` останавливает
его. События забираются из очереди через ``async for`` или ``await get_event()``.
"""

from __future__ import annotations

import asyncio
import contextlib
import enum
import logging
from collections.abc import AsyncIterator, Iterable
from typing import TYPE_CHECKING, Any, Self

if TYPE_CHECKING:
    from ..client.client import VKClient
    from ..client.http import HttpClient

DEFAULT_WAIT = 25
MAX_WAIT = 90
DEFAULT_LP_VERSION = 3

_ERROR = object()


class LongPollFailure(enum.IntEnum):
    """Коды ``failed`` в ответе Long Poll."""

    HISTORY_OUTDATED = 1
    KEY_EXPIRED = 2
    INFORMATION_LOST = 3
    INVALID_VERSION = 4


def _server_url(server: str) -> str:
    """Пользовательский Long Poll отдаёт хост без схемы, ботовый — полный URL."""
    if server.startswith(("http://", "https://")):
        return server
    return f"https://{server}"


class BaseLongPoll:
    """Фоновый опрос Long Poll с выдачей событий через очередь.

    Наследник обязан реализовать ``get_server`` (params сервера: server/key/ts)
    и ``parse_updates`` (сырые объекты -> события). Опционально переопределяется
    ``_fetch_params`` (доп. параметры a_check) и ``_on_invalid_version``.
    """

    def __init__(
        self,
        client: VKClient,
        *,
        http_client: HttpClient | None = None,
        logger: logging.Logger | None = None,
        wait: int = DEFAULT_WAIT,
    ) -> None:
        if wait <= 0:
            raise ValueError("wait: пауза Long Poll должна быть положительной")
        self._client = client
        self._http = http_client or client.http_client
        self._logger = logger or logging.getLogger("vkx.server.longpoll")
        self._wait = min(wait, MAX_WAIT)
        self._queue: asyncio.Queue[Any] = asyncio.Queue()
        self._task: asyncio.Task[None] | None = None
        self._stop = asyncio.Event()
        self._failure: BaseException | None = None

    @property
    def client(self) -> VKClient:
        return self._client

    @property
    def wait(self) -> int:
        return self._wait

    # ---------- контекстный менеджер ----------

    async def __aenter__(self) -> Self:
        self._start()
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    def _start(self) -> None:
        if self._task is not None and not self._task.done():
            return
        self._stop = asyncio.Event()
        self._failure = None
        self._task = asyncio.get_running_loop().create_task(self._pump())

    def stop(self) -> None:
        """Просит цикл опроса завершиться после текущего запроса."""
        self._stop.set()

    async def aclose(self) -> None:
        self.stop()
        task = self._task
        self._task = None
        if task is not None:
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task

    # ---------- получение событий ----------

    def __aiter__(self) -> AsyncIterator[Any]:
        return self.iter_events()

    async def iter_events(self) -> AsyncIterator[Any]:
        """Асинхронный генератор событий из очереди (лениво стартует поллинг)."""
        if self._task is None:
            self._start()
        while True:
            event = await self._queue.get()
            if event is _ERROR:
                if self._failure is not None:
                    raise self._failure
                return
            yield event

    async def get_event(self) -> Any:
        """Одно следующее событие (лениво стартует поллинг)."""
        if self._task is None:
            self._start()
        while True:
            event = await self._queue.get()
            if event is _ERROR:
                if self._failure is not None:
                    raise self._failure
                raise RuntimeError("LongPoll остановлен")
            return event

    async def _pump(self) -> None:
        try:
            async for event in self.listen():
                self._queue.put_nowait(event)
        except asyncio.CancelledError:
            raise
        except BaseException as exc:  # ошибку отдаём потребителю
            self._failure = exc
            self._logger.exception("LongPoll остановлен из-за ошибки")
            self._queue.put_nowait(_ERROR)

    # ---------- цикл опроса ----------

    async def listen(self) -> AsyncIterator[Any]:
        """Бесконечный цикл: получить сервер, опросить, разобрать updates."""
        self._stop = asyncio.Event()
        server = await self.get_server()
        retry = 0
        while not self._stop.is_set():
            try:
                payload = await self.fetch(server)
                if "failed" in payload:
                    recovered = await self._handle_failed(server, payload)
                    if recovered is None:
                        retry = min(retry + 1, 60)
                        await asyncio.sleep(0.1 * retry)
                    else:
                        server = recovered
                    continue
                ts = payload.get("ts")
                if ts is None:
                    server = await self.get_server()
                    continue
                server["ts"] = ts
                retry = 0
                for event in self.parse_updates(payload.get("updates") or []):
                    yield event
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # noqa: BLE001 — цикл обязан выжить
                self._logger.warning("LongPoll: ошибка опроса (%r), повтор", exc)
                retry = min(retry + 1, 60)
                await asyncio.sleep(0.1 * retry)

    async def fetch(self, server: dict[str, Any]) -> dict[str, Any]:
        """Один a_check-запрос к серверу Long Poll."""
        params: dict[str, Any] = {
            "act": "a_check",
            "key": server["key"],
            "ts": server["ts"],
            "wait": self._wait,
            **self._fetch_params(),
        }
        self._logger.debug("LongPoll: a_check %s", server.get("server"))
        response = await self._http.get(
            _server_url(str(server["server"])),
            params=params,
            timeout=self._wait + 10,
        )
        try:
            payload = response.json()
        except ValueError as exc:
            raise RuntimeError(
                f"LongPoll: некорректный ответ (HTTP {response.status_code})"
            ) from exc
        if not isinstance(payload, dict):
            raise TypeError(f"LongPoll: неожиданный ответ {payload!r}")
        return payload

    async def _handle_failed(
        self, server: dict[str, Any], payload: dict[str, Any]
    ) -> dict[str, Any] | None:
        """Реакция на ``failed``: остаться на сервере, обновить его или отказаться."""
        code = int(payload.get("failed") or 0)
        if code == LongPollFailure.HISTORY_OUTDATED:
            server["ts"] = payload.get("ts", server["ts"])
            return server
        if code == LongPollFailure.KEY_EXPIRED:
            fresh = await self.get_server()
            fresh["ts"] = server["ts"]
            return fresh
        if code == LongPollFailure.INFORMATION_LOST:
            return await self.get_server()
        if code == LongPollFailure.INVALID_VERSION:
            self._on_invalid_version()
            return await self.get_server()
        self._logger.warning("LongPoll: неизвестный failed=%s", code)
        return None

    def _fetch_params(self) -> dict[str, Any]:
        return {}

    def _on_invalid_version(self) -> None:
        pass

    # ---------- точки расширения ----------

    async def get_server(self) -> dict[str, Any]:
        raise NotImplementedError

    def parse_updates(self, updates: Iterable[Any]) -> Iterable[Any]:
        raise NotImplementedError


__all__ = ("BaseLongPoll", "LongPollFailure")
