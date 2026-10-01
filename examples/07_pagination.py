"""Пример: автопагинация — count больше лимита метода и count=None."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        # VK отдаёт максимум 1000 стран за запрос — клиент доберёт остаток сам.
        countries = await vk.database.get_countries(count=1500)
        print(f"получено: {len(countries.items)} из {countries.count}")

        # count=None — забрать всё, что отдаёт VK (по лимитам метода).
        all_countries = await vk.database.get_countries(count=None)
        print(f"все страны: {len(all_countries.items)} из {all_countries.count}")

        # Автопагинация есть только у типизированных методов; vk.call — как есть.
        async with vk.overrides(pagination=False):
            page = await vk.database.get_countries(count=1500)
            print(f"без пагинации: {len(page.items)}")


if __name__ == "__main__":
    asyncio.run(main())
