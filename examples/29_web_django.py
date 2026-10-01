"""Пример: приём Callback API во Django (WSGI).

Этот файл — фрагмент ``urls.py`` проекта. Django WSGI синхронный, поэтому
обработчик обязан быть обычной функцией, а диспетчер — SyncCallbackDispatch.
"""

from __future__ import annotations

import os

from django.urls import path

from vkx import CallbackListener, CallbackServer
from vkx.adapters import SyncCallbackDispatch
from vkx.adapters.django import create_callback_view
from vkx.models import CallbackEvent


def make_listener() -> CallbackListener:
    server = CallbackServer(
        group_id=int(os.environ["VK_GROUP_ID"]),
        secret=os.environ.get("VK_CALLBACK_SECRET"),
        confirmation_code=os.environ.get("VK_CONFIRMATION_CODE"),
    )
    return CallbackListener([server])


def handle_vk_event(event: CallbackEvent) -> None:
    print("событие:", event.type)


dispatch = SyncCallbackDispatch(make_listener(), handler=handle_vk_event)

# По умолчанию view освобождён от CSRF-проверки (csrf_exempt=True).
urlpatterns = [path("vk/callback", create_callback_view(dispatch))]

# Для Django ASGI (async view) используйте CallbackDispatch + create_callback_view.
