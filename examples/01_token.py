"""Пример: статичный токен, определение владельца и прав.

Запуск: VK_TOKEN=... python examples/01_token.py
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


def token() -> str:
    value = os.environ.get("VK_TOKEN")
    if not value:
        raise SystemExit("Задайте токен: VK_TOKEN=... python examples/01_token.py")
    return value


async def main() -> None:
    vk = VKClient(tokens=token())
    # Конструктор не ходит в сеть: probe случится здесь или при первом запросе.
    async with vk:
        await vk.probe()
        print(f"клиент: {vk!r}")
        print(f"владелец: id={vk.user_id} ({vk.kind})")
        if vk.is_group:
            print(f"сообщество: id{vk.group_id}")
        print(f"права: {vk.permissions}")
        print(f"пауза между батчами: {vk.interval} с")


if __name__ == "__main__":
    asyncio.run(main())
