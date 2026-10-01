"""aiohttp-адаптер Callback API.

aiohttp в зависимости vkx не тянется: модуль импортируют только те, у кого он
уже есть.

Пример:

    from vkx.adapters.aiohttp import create_callback_router

    dispatch = CallbackDispatch(listener, handler=handle_vk_event)
    app = web.Application()
    app.add_routes(create_callback_router(dispatch))
"""

from __future__ import annotations

from aiohttp import web

from ._common import CallbackDispatch

__all__ = ("create_callback_router",)


def create_callback_router(
    dispatch: CallbackDispatch,
    *,
    path: str = "/vk/callback",
    name: str = "vk_callback",
) -> web.RouteTableDef:
    """Собрать ``RouteTableDef`` с POST-роутом для уведомлений Callback API.

    Роут сам отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает
    обработчик из ``dispatch`` в фоне. Подключите через ``app.add_routes``.
    """
    routes = web.RouteTableDef()

    @routes.post(path, name=name)
    async def vk_callback(request: web.Request) -> web.Response:
        body, status = dispatch.dispatch(await request.read())
        return web.Response(text=body, status=status)

    return routes
