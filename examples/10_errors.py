"""Пример: типизированные ошибки VK API и их свойства."""

from __future__ import annotations

import asyncio
import os

from vkx import (
    VKAuthError,
    VKCaptchaError,
    VKClient,
    VKError,
    VKFloodError,
    VKPermissionError,
    VKRateLimitError,
    VKRequestError,
)


async def main() -> None:
    vk = VKClient(tokens=os.environ["VK_TOKEN"])
    async with vk:
        try:
            await vk.call("users.get", user_ids=[1])
        except VKError as exc:
            # except VKError ловит всё; подкласс выбирается по коду.
            print(type(exc).__name__, exc.code)
            print("auth:", exc.is_auth, "rate:", exc.is_rate_limit, "captcha:", exc.is_captcha)
            print("retryable:", exc.is_retryable, "retry_after:", exc.retry_after)
            print("метод:", exc.call.method if exc.call else None)

            if isinstance(exc, VKRateLimitError):
                await asyncio.sleep(exc.retry_after or 1.0)
            elif isinstance(exc, VKCaptchaError):
                print("капча:", exc.captcha_img, exc.captcha_sid)
            elif isinstance(exc, VKPermissionError):
                print("действие запрещено для токена")
            elif isinstance(exc, VKRequestError):
                print("некорректные параметры")
            elif isinstance(exc, (VKFloodError, VKAuthError)):
                print("нужно сбавить темп или обновить токен")


if __name__ == "__main__":
    asyncio.run(main())
