"""Общая логика веб-адаптеров Callback API.

VK ждёт от вебхука ответ: если он задерживается, событие приходит повторно, а
при регулярных задержках сообщество может отключить сервер. Поэтому для
async-фреймворков уведомление разбирается, ответ ``ok`` отдаётся сразу, а
обработчик запускается фоновой задачей. Исключение — ``confirmation``: код
подтверждения адреса нужно вернуть немедленно, откладывать его нельзя.

Диспетчеры:

- ``CallbackDispatch`` — для async-фреймворков (FastAPI, Starlette, aiohttp,
  Sanic, Django ASGI): задача ставится в текущий loop.
- ``SyncCallbackDispatch`` — для синхронных (Flask, Django WSGI): синхронный
  обработчик вызывается прямо в текущем потоке, без пула потоков и loop.

Адаптеры конкретных фреймворков (``vkx.adapters.fastapi``,
``vkx.adapters.starlette``, ``vkx.adapters.aiohttp``, ``vkx.adapters.sanic``,
``vkx.adapters.django``, ``vkx.adapters.flask``) — тонкие обёртки над ними.
"""

from __future__ import annotations

import asyncio
import inspect
import logging
from collections.abc import Awaitable, Callable
from typing import Any

from ..models.events.callback_events import CallbackEvent
from ..models.events.enums import CallbackEventType
from ..server.callback import RawCallback
from ..server.callback_server import CallbackListener

EventHandler = Callable[[CallbackEvent], Any | Awaitable[Any]]


class _DispatchBase:
    """Общее для диспетчеров: разбор уведомления и ответ VK."""

    def __init__(
        self,
        listener: CallbackListener,
        *,
        handler: EventHandler | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._listener = listener
        self._handler = handler
        self._logger = logger or logging.getLogger("vkx.adapters")

    @property
    def listener(self) -> CallbackListener:
        return self._listener

    @property
    def handler(self) -> EventHandler | None:
        return self._handler

    def dispatch(self, raw: RawCallback) -> tuple[str, int]:
        """Разобрать уведомление и решить, что ответить VK.

        :return: пара ``(тело, статус)`` для HTTP-ответа.
        """
        event = self._listener.handle(raw)
        if event is None:  # чужой group_id / плохой secret / дубликат
            return "ok", 200
        if event.type is CallbackEventType.CONFIRMATION:
            return self._confirmation(event), 200
        self.schedule(event)
        return "ok", 200

    def schedule(self, event: CallbackEvent) -> None:
        """Выполнить обработчик события."""
        raise NotImplementedError

    def _confirmation(self, event: CallbackEvent) -> str:
        server = self._listener.get(event.group_id) if event.group_id else None
        code = server.confirmation_code if server else None
        return code or ""


class CallbackDispatch(_DispatchBase):
    """Ответ ``ok`` сразу + обработка в фоне задачей текущего loop.

    Для async-фреймворков (FastAPI, Starlette, aiohttp, Sanic, Django ASGI).
    ``handler`` может быть как async, так и обычной функцией: синхронная уходит
    в отдельный поток (``asyncio.to_thread``), чтобы не блокировать loop.

    Задачи удерживаются внутри, чтобы их не собрал GC, и логируются при падении;
    на остановке приложения дождитесь их через ``aclose``.
    """

    def __init__(
        self,
        listener: CallbackListener,
        *,
        handler: EventHandler | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        super().__init__(listener, handler=handler, logger=logger)
        self._tasks: set[asyncio.Task[None]] = set()

    def schedule(self, event: CallbackEvent) -> None:
        if self._handler is None:
            self._logger.debug("Событие %s отброшено: обработчик не задан", event.type)
            return
        task = asyncio.create_task(self._run(event))
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

    async def aclose(self, *, timeout: float | None = None) -> None:
        """Дождаться завершения фоновых задач."""
        tasks = set(self._tasks)
        if tasks:
            await asyncio.wait(tasks, timeout=timeout)

    async def __aenter__(self) -> CallbackDispatch:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    async def _run(self, event: CallbackEvent) -> None:
        handler = self._handler
        if handler is None:
            return
        try:
            if inspect.iscoroutinefunction(handler):
                await handler(event)
            else:
                result = await asyncio.to_thread(handler, event)
                if inspect.isawaitable(result):
                    await result
        except Exception:  # noqa: BLE001
            self._logger.exception("Ошибка обработки события %s", event.type)


class SyncCallbackDispatch(_DispatchBase):
    """Синхронный диспетчер для Flask и Django WSGI.

    Синхронный ``handler`` вызывается прямо в том же потоке, что и первичная
    обработка колбека (WSGI-сервер обычно выделяет отдельный поток на запрос),
    поэтому ни пул потоков, ни event loop не нужны. ``handler`` обязан быть
    синхронным: async-функция вызовет ``TypeError`` — для неё нужен
    ``CallbackDispatch``.
    """

    def __init__(
        self,
        listener: CallbackListener,
        *,
        handler: EventHandler | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        super().__init__(listener, handler=handler, logger=logger)
        if handler is not None and inspect.iscoroutinefunction(handler):
            raise TypeError(
                "SyncCallbackDispatch требует синхронный handler; "
                "для async-функции используйте CallbackDispatch"
            )

    def schedule(self, event: CallbackEvent) -> None:
        handler = self._handler
        if handler is None:
            self._logger.debug("Событие %s отброшено: обработчик не задан", event.type)
            return
        try:
            handler(event)
        except Exception:  # noqa: BLE001
            self._logger.exception("Ошибка обработки события %s", event.type)


__all__ = ("CallbackDispatch", "EventHandler", "SyncCallbackDispatch")
