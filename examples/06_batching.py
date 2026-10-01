"""Пример: батчинг execute, немедленная отправка очереди, интервал."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        # Три запроса уедут одним execute-батчем — снаружи это невидимо.
        users = await asyncio.gather(
            vk.users.get(user_ids=[1]),
            vk.users.get(user_ids=[2]),
            vk.users.get(user_ids=[3]),
        )
        print([u[0].first_name for u in users])

        # Не ждать interval: отправить накопленную очередь прямо сейчас.
        task = asyncio.create_task(vk.users.get(user_ids=[4]))
        await vk.drain()
        print((await task)[0].first_name)

        # Точечно выключить батчинг у одного запроса...
        raw = await vk.call("users.get", user_ids=[5], batching=False)
        print(raw[0]["first_name"])

        # ...или на блок запросов (см. пример 08 про overrides).
        async with vk.overrides(batching=False):
            user = (await vk.users.get(user_ids=[6]))[0]
            print(user.first_name)


if __name__ == "__main__":
    asyncio.run(main())
