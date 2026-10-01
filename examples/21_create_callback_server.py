"""Пример: регистрация Callback-сервера в сообществе.

``create_callback_server`` вызывает ``groups.addCallbackServer`` и забирает
confirmation-код; ``title`` — не длиннее 14 символов, ``secret`` — не длиннее 50.
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient, create_callback_server


async def main() -> None:
    group_id = int(os.environ["VK_GROUP_ID"])
    url = os.environ["VK_CALLBACK_URL"]
    async with VKClient(tokens=os.environ["VK_TOKEN"]) as vk:
        server = await create_callback_server(
            vk, group_id=group_id, url=url, title="vkx", secret="s3cret"
        )
        print("server_id:", server.server_id, "confirmation:", server.confirmation_code)

        # Включить нужные события для зарегистрированного сервера.
        await vk.groups.set_callback_settings(
            group_id=group_id,
            server_id=server.server_id,
            message_new=True,
            message_event=True,
        )


if __name__ == "__main__":
    asyncio.run(main())
