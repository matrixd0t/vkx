"""Пример: таймаут ожидания ответа (клиентский, не сетевой)."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient, VKTimeoutError


async def main() -> None:
    # Таймаут клиента применяется ко всем запросам.
    vk = VKClient(tokens=os.environ["VK_TOKEN"], timeout=5.0)
    async with vk:
        try:
            # Можно переопределить на один запрос.
            await vk.call("users.get", user_ids=[1], timeout=1.0)
        except VKTimeoutError as exc:
            print("не дождались ответа:", exc)
            print("запрос помечен отменённым:", exc.call is not None)


if __name__ == "__main__":
    asyncio.run(main())
