"""Пример: повторы транзиентных сбоев, backoff и обработчик капчи."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient, VKError


async def captcha_handler(error: VKError) -> dict[str, str] | None:
    """Получает VKCaptchaError; верните лишние параметры для повтора запроса.

    Обработчик может быть и обычной функцией, и корутиной.
    """
    print(f"требуется капча: {error.captcha_img}")
    key = input("код с картинки: ").strip()
    if not key:
        return None
    return {"captcha_sid": error.captcha_sid or "", "captcha_key": key}


async def main() -> None:
    vk = VKClient(
        tokens=os.environ["VK_TOKEN"],
        max_retries=3,        # сеть, HTTP 5xx/429 и коды 1/6/9/10/29
        retry_backoff=0.5,    # базовая пауза; растёт экспоненциально
        captcha_handler=captcha_handler,
    )
    async with vk:
        result = await vk.call("users.get", user_ids=[1])
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
