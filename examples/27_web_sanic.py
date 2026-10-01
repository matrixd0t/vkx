"""Пример: приём Callback API в Sanic через vkx.adapters.sanic."""

from __future__ import annotations

import os

from sanic import Sanic

from vkx import CallbackListener, CallbackServer
from vkx.adapters import CallbackDispatch
from vkx.adapters.sanic import create_callback_router
from vkx.models import CallbackEvent


def make_listener() -> CallbackListener:
    server = CallbackServer(
        group_id=int(os.environ["VK_GROUP_ID"]),
        secret=os.environ.get("VK_CALLBACK_SECRET"),
        confirmation_code=os.environ.get("VK_CONFIRMATION_CODE"),
    )
    return CallbackListener([server])


async def handle_vk_event(event: CallbackEvent) -> None:
    print("событие:", event.type)


dispatch = CallbackDispatch(make_listener(), handler=handle_vk_event)
app = Sanic("vkx_callback")
app.blueprint(create_callback_router(dispatch))


@app.before_server_stop
async def stop(app: Sanic, loop: object) -> None:
    await dispatch.aclose(timeout=5.0)


def main() -> None:
    app.run(host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
