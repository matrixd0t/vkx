"""Пример: загрузка голосового сообщения (audio_message)."""

from __future__ import annotations

import asyncio
import os
import random
from pathlib import Path

from vkx import VKClient

VOICE = Path("voice.ogg")


async def main() -> None:
    data = VOICE.read_bytes()
    peer_id = int(os.environ["VK_PEER_ID"])
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        voice = await vk.upload.audio_message(data, peer_id=peer_id)
        print(f"голосовое: {voice.as_att}")
        await vk.messages.send(
            peer_id=peer_id,
            random_id=random.getrandbits(31),
            attachment=voice.as_att or "",
        )


if __name__ == "__main__":
    asyncio.run(main())
