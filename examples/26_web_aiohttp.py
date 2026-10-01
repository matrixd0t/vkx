"""Пример: приём Callback API в aiohttp через vkx.adapters.aiohttp."""

from __future__ import annotations

import os

from aiohttp import web

from vkx import CallbackListener, CallbackServer
from vkx.adapters import CallbackDispatch
from vkx.adapters.aiohttp import create_callback_router
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
app = web.Application()
app.add_routes(create_callback_router(dispatch))


async def on_cleanup(app: web.Application) -> None:
    await dispatch.aclose(timeout=5.0)


app.on_cleanup.append(on_cleanup)


def main() -> None:
    web.run_app(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
