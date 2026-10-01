"""Пример: свой HTTP-клиент по протоколу HttpClient."""

from __future__ import annotations

import asyncio
import os
from typing import Any

import httpx

from vkx import VKClient


class LoggingHttpClient:
    """Обёртка над httpx.AsyncClient, логирующая запросы.

    Протоколу HttpClient достаточно асинхронных ``get``/``post`` и ``aclose``.
    """

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0), follow_redirects=True
        )

    async def get(self, url: str, **kwargs: Any) -> httpx.Response:
        print("GET", url)
        return await self._client.get(url, **kwargs)

    async def post(self, url: str, **kwargs: Any) -> httpx.Response:
        print("POST", url)
        return await self._client.post(url, **kwargs)

    async def aclose(self) -> None:
        await self._client.aclose()


async def main() -> None:
    http = LoggingHttpClient()
    # Чужой HTTP-клиент vk.aclose() не закрывает — закрываем сами.
    vk = VKClient(tokens=os.environ["VK_TOKEN"], http_client=http)
    async with vk:
        await vk.call("users.get", user_ids=[1])
    await http.aclose()


if __name__ == "__main__":
    asyncio.run(main())
