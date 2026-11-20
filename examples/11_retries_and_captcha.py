"""Пример: повторы транзиентных сбоев, backoff и обработчик капчи."""

from __future__ import annotations

import asyncio
import os

from vkx import VKClient, VKError, VKFloodError, VKHttpError, VKTransportError


def error_handler(history: tuple[VKError, ...]) -> float | None:
    """Разные политики для HTTP и flood-control.

    ``history`` — ошибки текущей последовательности (от старой к новой).
    Возвращает паузу до повтора или ``None`` (не повторять).
    """
    last = history[-1]
    if isinstance(last, VKFloodError):
        return 1.0 if len(history) <= 3 else None
    if isinstance(last, (VKHttpError, VKTransportError)):
        return (last.retry_after or 0.5) if len(history) <= 5 else None
    return None


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
        error_handler=error_handler,
        captcha_handler=captcha_handler,
    )
    async with vk:
        result = await vk.call("users.get", user_ids=[1])
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
