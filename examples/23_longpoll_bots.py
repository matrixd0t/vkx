"""Пример: Bots Long Poll — события сообщества.

События разбираются тем же ``parse_callback``, что и Callback API.
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient
from vkx.models import MessageNewCallbackEvent
from vkx.server import BotsLongPoll


async def main() -> None:
    # group_id берётся из клиента (групповой токен); можно передать явно.
    async with VKClient(tokens=os.environ["VK_TOKEN"]) as vk, BotsLongPoll(vk, wait=25) as longpoll:
        for _ in range(5):
            event = await longpoll.get_event()
            print(type(event).__name__)
            if isinstance(event, MessageNewCallbackEvent) and event.object.message:
                print("  <-", event.object.message.text)


if __name__ == "__main__":
    asyncio.run(main())
