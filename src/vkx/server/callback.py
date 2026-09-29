"""Разбор уведомлений Callback API.

Модуль не зависит от веб-фреймворка: принимает сырое тело запроса и
возвращает типизированное событие. Проверку ``secret``, подтверждение
адреса, дедупликацию ``event_id`` и ответ ``ok`` берёт на себя вызывающая
сторона (Django, Starlette, aiohttp, ...).
"""

from __future__ import annotations

import json
from typing import Any

from vkx.models.events.callback_events import (
    CALLBACK_EVENTS,
    BaseCallbackEvent,
    CallbackEvent,
)
from vkx.models.events.enums import CallbackEventType

type RawCallback = bytes | bytearray | str | dict


def _as_dict(raw: RawCallback) -> dict[str, Any]:
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, (bytes, bytearray)):
        raw = bytes(raw).decode("utf-8")
    if isinstance(raw, str):
        data = json.loads(raw)
    else:
        raise TypeError(f"Ожидались bytes, str или dict, получено {type(raw).__name__}")
    if not isinstance(data, dict):
        raise ValueError("Уведомление Callback API должно быть JSON-объектом")  # noqa: TRY004
    return data


def parse_callback(raw: RawCallback, /) -> CallbackEvent:
    """Разобрать уведомление Callback API в типизированное событие.

    :param raw: сырое тело запроса (``bytes``/``str``) или уже разобранный dict.
    :return: конкретный ``*CallbackEvent`` по полю ``type``.

    Неизвестный ``type`` не считается ошибкой: вернётся ``BaseCallbackEvent``
    с ``type = CallbackEventType.NOT_SUPPORTED_MEMBER`` и сырым ``object``.
    """
    data = _as_dict(raw)
    event_cls = CALLBACK_EVENTS.get(CallbackEventType(data.get("type")))
    if event_cls is None:
        return BaseCallbackEvent.model_validate(data)
    return event_cls.model_validate(data)


__all__ = ("RawCallback", "parse_callback")
