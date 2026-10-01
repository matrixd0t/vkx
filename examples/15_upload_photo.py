"""Пример: загрузка фото в сообщения и на стену.

Хелпер сам получает сервер загрузки через очередь, отправляет байты напрямую
HTTP-клиентом и сохраняет фото через save-метод.
"""

from __future__ import annotations

import asyncio
import os
import random
from pathlib import Path

from vkx import VKClient

PHOTO = Path("photo.jpg")


def peer_id() -> int:
    value = os.environ.get("VK_PEER_ID")
    if not value:
        raise SystemExit("Задайте VK_PEER_ID")
    return int(value)


async def main() -> None:
    data = PHOTO.read_bytes()
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        # namespace vk.upload.* привязан к клиенту.
        photos = await vk.upload.photo_to_messages(data, peer_id=peer_id())
        photo = photos[0]
        print(f"загружено: {photo.as_att}")

        await vk.messages.send(
            peer_id=peer_id(),
            random_id=random.getrandbits(31),
            message="Кот",
            attachment=photo.as_att,
        )

        # Фото на стену сообщества (для группового токена).
        if vk.is_group and vk.group_id:
            uploaded = await vk.upload.photo_to_wall(
                data, group_id=vk.group_id, caption="Кот"
            )
            print(f"на стену: {uploaded[0].as_att}")

        # Свободная функция делает то же самое, но клиент передаётся явно:
        # from vkx.client.upload import upload_photo_to_wall
        # photo = (await upload_photo_to_wall(vk, data, group_id=vk.group_id))[0]


if __name__ == "__main__":
    asyncio.run(main())
