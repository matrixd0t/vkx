"""Пример: несколько источников одного владельца и хранилище состояния.

Смешивать можно строки, cookies и готовые TokenSource. Источники с чужим
владельцем отбрасываются, нерабочие — пропускаются с логированием.
"""

from __future__ import annotations

import asyncio
import os

from vkx import StaticTokenSource, VKClient, open_store


def token() -> str:
    value = os.environ.get("VK_TOKEN")
    if not value:
        raise SystemExit("Задайте VK_TOKEN")
    return value


async def main() -> None:
    store = open_store("examples-state.sqlite")  # *.json -> JSONStore, иначе SQLite
    vk = VKClient(
        tokens=[token()],                       # строки -> StaticTokenSource
        sources=[StaticTokenSource(token(), label="резерв", store=store)],
        store=store,                            # владелец и токен запомнятся при probe
    )
    async with vk:
        await vk.probe()
        print(f"клиент: {vk!r}")
        print(f"владелец: id{vk.user_id} ({vk.kind}), права: {vk.permissions}")
    await store.aclose()


if __name__ == "__main__":
    asyncio.run(main())
