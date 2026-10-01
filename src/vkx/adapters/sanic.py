"""Sanic-адаптер Callback API.

Sanic в зависимости vkx не тянется: модуль импортируют только те, у кого он
уже есть.

Пример:

    from vkx.adapters.sanic import create_callback_router

    dispatch = CallbackDispatch(listener, handler=handle_vk_event)
    app.blueprint(create_callback_router(dispatch))
"""

from __future__ import annotations

from sanic import Blueprint, Request
from sanic.response import HTTPResponse, text

from ._common import CallbackDispatch

__all__ = ("create_callback_router",)


def create_callback_router(
    dispatch: CallbackDispatch,
    *,
    path: str = "/vk/callback",
    name: str = "vk_callback",
) -> Blueprint:
    """Собрать ``Blueprint`` с POST-роутом для уведомлений Callback API.

    Роут сам отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает
    обработчик из ``dispatch`` в фоне. Подключите через ``app.blueprint``.
    """
    bp = Blueprint(name)

    @bp.post(path, name=name)
    async def vk_callback(request: Request) -> HTTPResponse:
        body, status = dispatch.dispatch(request.body)
        return text(body, status=status)

    return bp
