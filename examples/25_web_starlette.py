"""Пример: приём Callback API в Starlette через vkx.adapters.starlette."""

from __future__ import annotations

import os

from starlette.applications import Starlette

from vkx import CallbackListener, CallbackServer
from vkx.adapters import CallbackDispatch
from vkx.adapters.starlette import create_callback_router
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
router = create_callback_router(dispatch)
app = Starlette(routes=[*router.routes])


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
