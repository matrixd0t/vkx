"""Пример: User Long Poll — события пользователя."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient
from vkx.server import LongPoll


async def main() -> None:
    # Сервер — async-контекст и async-итератор
    async with VKClient(tokens=os.environ["VK_TOKEN"]) as vk, LongPoll(vk, mode=234, lp_version=3, wait=25) as longpoll:
        for _ in range(5):
            event = await longpoll.get_event()
            print(type(event).__name__, event)
        # либо:  async for event in longpoll: ...


if __name__ == "__main__":
    asyncio.run(main())
