"""Starlette-адаптер Callback API.

Starlette в зависимости vkx не тянется: модуль импортируют только те, у кого
он уже есть (сам Starlette, FastAPI и т.п.).

Пример:

    from vkx.adapters.starlette import create_callback_router

    dispatch = CallbackDispatch(listener, handler=handle_vk_event)
    app = Starlette(routes=[*create_callback_router(dispatch).routes])
"""

from __future__ import annotations

from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Router

from ._common import CallbackDispatch

__all__ = ("create_callback_router",)


def create_callback_router(
    dispatch: CallbackDispatch,
    *,
    path: str = "/vk/callback",
    name: str = "vk_callback",
) -> Router:
    """Собрать ``Router`` с POST-роутом для уведомлений Callback API.

    Роут сам отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает
    обработчик из ``dispatch`` в фоне.
    """

    async def vk_callback(request: Request) -> PlainTextResponse:
        body, status = dispatch.dispatch(await request.body())
        return PlainTextResponse(body, status_code=status)

    return Router(routes=[Route(path, vk_callback, methods=["POST"], name=name)])
