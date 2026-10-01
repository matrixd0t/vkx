"""Django-адаптер Callback API.

Django в зависимости vkx не тянется: модуль импортируют только те, у кого он
уже есть.

Django WSGI синхронный, поэтому используйте ``SyncCallbackDispatch`` с обычным
(не async) хендлером — он выполнится в том же потоке, что и обработка колбека:

    from vkx.adapters import SyncCallbackDispatch
    from vkx.adapters.django import create_callback_view

    dispatch = SyncCallbackDispatch(listener, handler=handle_vk_event)

    urlpatterns = [path("vk/callback", create_callback_view(dispatch))]
"""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt as csrf_exempt_decorator

from ._common import CallbackDispatch

__all__ = ("create_callback_view",)


def create_callback_view(
    dispatch: CallbackDispatch,
    *,
    csrf_exempt: bool = True,
) -> Callable[[HttpRequest], HttpResponse]:
    """Вернуть Django-view для уведомлений Callback API.

    View отвечает VK ``ok`` (или ``confirmation``-кодом) и запускает обработчик
    из ``dispatch`` в фоне. Подключите в ``urls.py`` через ``path``. По умолчанию
    view освобождён от CSRF-проверки — VK не присылает CSRF-токен.
    """

    def view(request: HttpRequest) -> HttpResponse:
        body, status = dispatch.dispatch(request.body)
        return HttpResponse(body.encode("utf-8"), status=status, content_type="text/plain")

    if csrf_exempt:
        return cast(Callable[[HttpRequest], HttpResponse], csrf_exempt_decorator(view))
    return view
