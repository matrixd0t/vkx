"""Пример: свой источник токена по протоколу TokenSource."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient


class RotatingTokenSource:
    """Отдаёт токены по кругу и умеет duck-refresh.

    Достаточно метода ``token(method)``. Если у источника есть ``refresh``,
    клиент вызовет его при авторизационной ошибке (5/27/28) и повторит запрос
    тем же источником.
    """

    def __init__(self, tokens: list[str]) -> None:
        self._tokens = tokens
        self._index = 0

    async def token(self, method: str | None = None) -> str | None:
        if not self._tokens:
            return None
        return self._tokens[self._index % len(self._tokens)]

    async def refresh(self) -> None:
        self._index += 1


async def main() -> None:
    token = os.environ.get("VK_TOKEN")
    if not token:
        raise SystemExit("Задайте VK_TOKEN")
    source = RotatingTokenSource([token])
    vk = VKClient(sources=[source])
    async with vk:
        await vk.probe()
        print(f"владелец: id{vk.user_id} ({vk.kind})")


if __name__ == "__main__":
    asyncio.run(main())
