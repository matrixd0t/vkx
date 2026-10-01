"""Пример: сырой вызов метода через vk.call — без моделей и автопагинации."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        response = await vk.call("users.get", user_ids=[1], fields="photo_100")
        print(response)  # тело response как есть

        # HTTP-настройки можно переопределить на один запрос.
        response = await vk.call(
            "users.get",
            user_ids=[1],
            v="5.131",
            base_api_url="https://api.vk.com",
        )
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
