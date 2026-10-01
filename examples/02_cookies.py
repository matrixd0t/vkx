"""Пример: веб-вход по cookies — токен получается и обновляется автоматически.

Нужны только cookies веб-сессии ``p`` и ``remixsid``.
"""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


def cookies() -> dict[str, str]:
    p = os.environ.get("VK_P")
    remixsid = os.environ.get("VK_REMIXSID")
    if not p or not remixsid:
        raise SystemExit("Задайте VK_P и VK_REMIXSID")
    return {"p": p, "remixsid": remixsid}


async def main() -> None:
    # Обязательные cookies проверяются сразу; WebCookieSource импортировать не нужно.
    vk = VKClient(cookies=cookies())
    async with vk:
        await vk.probe()
        print(f"владелец: id{vk.user_id} ({vk.kind})")
        me = (await vk.users.get(fields=["photo_100"]))[0]
        print(f"я: {me.first_name} {me.last_name}")


if __name__ == "__main__":
    asyncio.run(main())
