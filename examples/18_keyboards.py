"""Пример: сборка клавиатуры и отправка сообщения с ней."""

from __future__ import annotations

import asyncio
import os
import random

from vkx import VKClient
from vkx.models import Button, Keyboard
from vkx.models import KeyboardButtonColor as c


async def main() -> None:
    peer_id = int(os.environ.get("VK_PEER_ID", "1"))

    keyboard = Keyboard.from_rows(
        [
            [
                Button("Да", payload={"cmd": "yes"}, color=c.POSITIVE),
                Button("Нет", payload={"cmd": "no"}, color='negative'),
            ],
            [Button("Сайт", type="open_link", link="https://vk.com")],
        ],
        inline=True,
    )
    print("inline:", keyboard.to_json())

    # Чатовая клавиатура: inline=False, лимит рядов — 10 (вместо 6).
    chat_keyboard = Keyboard.from_rows(
        [[Button("Помощь", type="text")]], inline=False, one_time=True
    )
    print("chat:", chat_keyboard.to_json())

    token = os.environ.get("VK_TOKEN")
    if not token:
        print("(сеть пропущена: задайте VK_TOKEN и VK_PEER_ID для отправки)")
        return

    vk = VKClient(tokens=token)
    async with vk:
        await vk.messages.send(
            peer_id=peer_id,
            random_id=random.getrandbits(31),
            message="Выбирай",
            keyboard=keyboard.to_json(),
        )


if __name__ == "__main__":
    asyncio.run(main())
