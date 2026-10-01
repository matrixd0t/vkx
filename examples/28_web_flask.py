"""Пример: приём Callback API во Flask через vkx.adapters.flask.

Flask синхронный (WSGI), поэтому используется SyncCallbackDispatch, а обработчик
обязан быть обычной функцией — async-функция вызовет TypeError.
"""

from __future__ import annotations

import os

from flask import Flask

from vkx import CallbackListener, CallbackServer
from vkx.adapters import SyncCallbackDispatch
from vkx.adapters.flask import create_callback_router
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
app = Flask(__name__)
app.register_blueprint(create_callback_router(dispatch))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
