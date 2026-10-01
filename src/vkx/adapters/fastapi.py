"""FastAPI-адаптер Callback API.

FastAPI в зависимости vkx не тянется: модуль импортируют только те, у кого он
уже есть.

Пример:

    from vkx.adapters.fastapi import create_callback_router
    from vkx.server import CallbackListener

    listener = CallbackListener([server])
    dispatch = CallbackDispatch(listener, handler=handle_vk_event)
    app.include_router(create_callback_router(dispatch))

``handle_vk_event`` получит событие уже после того, как VK прочитает ``ok``.
"""

from __future__ import annotations

from fastapi import APIRouter, Request, Response

from ._common import CallbackDispatch

__all__ = ("create_callback_router",)


def create_callback_router(
    dispatch: CallbackDispatch,
    *,
    path: str = "/vk/callback",
    name: str = "vk_callback",
) -> APIRouter:
    """Собрать ``APIRouter`` с POST-роутом для уведомлений Callback API.

    Роут сам отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает
    обработчик из ``dispatch`` в фоне. Подключите через ``app.include_router``.
    """
    router = APIRouter()

    @router.post(path, name=name, include_in_schema=False)
    async def vk_callback(request: Request) -> Response:
        body, status = dispatch.dispatch(await request.body())
        return Response(content=body, status_code=status, media_type="text/plain")

    return router
