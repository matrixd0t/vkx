"""Пример: произвольный VKScript через vk.execute."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        code = "return [API.users.get({'user_ids': '1'}), API.users.get({'user_ids': '2'})];"
        users = await vk.execute(code)
        print([u[0]["first_name"] for u in users])


if __name__ == "__main__":
    asyncio.run(main())
