"""Пример: типизированные категории — вместо словарей возвращаются модели.

Категории — это ``vk.users``, ``vk.messages``, ``vk.board`` и т.д. Аргументы
строго типизированы: лишний keyword даёт ``TypeError``.
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        me = (await vk.users.get(fields=["photo_100", "city"]))[0]
        print(type(me).__name__, me.first_name, me.last_name)

        countries = await vk.database.get_countries(count=3)
        print(f"стран: {countries.count}, пример: {[c.title for c in countries.items]}")

        # user_ids принимает и числовые id, и screen_name.
        users = await vk.users.get(user_ids=[1, "durov"])
        print([(u.id, u.first_name) for u in users])


if __name__ == "__main__":
    asyncio.run(main())
