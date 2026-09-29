"""Типы VK API и событий.

Пакет самодостаточен и поддерживается вручную. Структура:
``objects`` (API-объекты), ``responses`` (модели ответов),
``methods`` (типизированные категории), ``events`` (longpoll/callback-события).
"""

from vkx.models import objects as _objects
from vkx.models.categories import APICategories
from vkx.models.events import *
from vkx.models.events import bot_events as _bot_events
from vkx.models.events import callback_events as _callback_events
from vkx.models.events.bot_events import *
from vkx.models.events.callback_events import *
from vkx.models.events.enums import *
from vkx.models.objects import *

API_URL: str = "https://api.vk.ru/method/"
API_VERSION: str = "5.199"

__all__ = [  # noqa: PLE0604
    "API_URL",
    "API_VERSION",
    "APICategories",
    "BaseCallbackEvent",
    "BaseGroupEvent",
    "BaseUserEvent",
    "CallbackEvent",
    "CallbackEventType",
    "Event",
    "GroupEventType",
    "GroupTypes",
    "UserEventType",
    "UserTypes",
    *_objects.__all__,
    *_bot_events.__all__,
    *_callback_events.__all__,
]
