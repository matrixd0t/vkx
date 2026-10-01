"""Flask-адаптер Callback API.

Flask в зависимости vkx не тянется: модуль импортируют только те, у кого он
уже есть.

Flask WSGI синхронный, поэтому используйте ``SyncCallbackDispatch`` с обычным
(не async) хендлером — он выполнится в том же потоке, что и обработка колбека:

    from vkx.adapters import SyncCallbackDispatch
    from vkx.adapters.flask import create_callback_router

    dispatch = SyncCallbackDispatch(listener, handler=handle_vk_event)
    app.register_blueprint(create_callback_router(dispatch))
"""

from __future__ import annotations

from flask import Blueprint, Response, request

from ._common import SyncCallbackDispatch

__all__ = ("create_callback_router",)


def create_callback_router(
    dispatch: SyncCallbackDispatch,
    *,
    path: str = "/vk/callback",
    name: str = "vk_callback",
) -> Blueprint:
    """Собрать ``Blueprint`` с POST-роутом для уведомлений Callback API.

    Роут сам отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает
    обработчик из ``dispatch`` в фоне. Подключите через ``app.register_blueprint``.
    """
    bp = Blueprint(name, __name__)

    @bp.post(path)
    def vk_callback() -> Response:
        body, status = dispatch.dispatch(request.get_data())
        return Response(body, status=status, mimetype="text/plain")

    return bp
