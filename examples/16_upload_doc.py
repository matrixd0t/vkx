"""Пример: загрузка документа в сообщения."""

from __future__ import annotations

import asyncio
import os
import random
from pathlib import Path

from vkx import VKClient
from vkx.client.upload import upload_doc_to_messages

FILE = Path("report.pdf")


async def main() -> None:
    data = FILE.read_bytes()
    peer_id = int(os.environ["VK_PEER_ID"])
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        # namespace клиента
        doc = await vk.upload.doc_to_messages(
            data, peer_id=peer_id, filename="report.pdf", title="Отчёт"
        )
        print(f"документ: {doc.as_att}")

        # та же операция свободной функцией (клиент первым аргументом)
        doc2 = await upload_doc_to_messages(
            vk, data, peer_id=peer_id, filename="report.pdf", title="Отчёт"
        )

        await vk.messages.send(
            peer_id=peer_id,
            random_id=random.getrandbits(31),
            message="Документ",
            attachment=(doc2 or doc).as_att or "",
        )


if __name__ == "__main__":
    asyncio.run(main())
