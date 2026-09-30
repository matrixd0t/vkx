"""Типы VK API и событий.

Пакет самодостаточен и поддерживается вручную. Структура:
``objects`` (API-объекты), ``responses`` (модели ответов),
``methods`` (типизированные категории), ``events`` (longpoll/callback-события).
"""

from . import objects as _objects
from .categories import APICategories
from .events import *
from .events import bot_events as _bot_events
from .events import callback_events as _callback_events
from .events.bot_events import *
from .events.callback_events import *
from .events.enums import *
from .objects import *

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
    "UserEventType",
    *_objects.__all__,
    *_bot_events.__all__,
    *_callback_events.__all__,
]
