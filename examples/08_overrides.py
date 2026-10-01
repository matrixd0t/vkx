"""Пример: vk.overrides временно меняет батчинг и пагинацию для блока.

``None`` оставляет значение клиента; значения откатываются на выходе из блока.
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        async with vk.overrides(batching=False):
            # Типизированные методы внутри блока тоже идут прямыми вызовами.
            user = (await vk.users.get(user_ids=[1]))[0]
            print(f"без батчинга: {user.first_name}")

        async with vk.overrides(pagination=False):
            page = await vk.database.get_countries(count=1500)
            print(f"без пагинации: {len(page.items)}")

        async with vk.overrides(batching=False, pagination=False):
            user = (await vk.users.get(user_ids=[2]))[0]
            print(f"оба выключены: {user.first_name}")


if __name__ == "__main__":
    asyncio.run(main())
