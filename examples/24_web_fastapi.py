"""Пример: приём Callback API во FastAPI через vkx.adapters.fastapi.

Запуск: VK_GROUP_ID=1 python examples/24_web_fastapi.py
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from vkx import CallbackListener, CallbackServer
from vkx.adapters import CallbackDispatch
from vkx.adapters.fastapi import create_callback_router
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


listener = make_listener()
dispatch = CallbackDispatch(listener, handler=handle_vk_event)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    # Дождаться фоновых задач обработчика перед остановкой.
    await dispatch.aclose(timeout=5.0)


app = FastAPI(lifespan=lifespan)
app.include_router(create_callback_router(dispatch))


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
