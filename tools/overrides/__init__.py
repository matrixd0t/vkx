"""Сгенерированные из ``vkbottle-types`` типы VK API.

Пакет самодостаточен: не импортирует ``vkbottle_types`` в рантайме.
Имена классов приведены к vkx-стилю (снятие категорийного префикса,
суффикс ``Event`` у событий). Модули повторяют структуру источника:
``objects``, ``responses``, ``methods``, ``codegen``, ``events``.
"""

from vkx.callback.generated import objects as _objects
from vkx.callback.generated.categories import APICategories
from vkx.callback.generated.events import *
from vkx.callback.generated.events import bot_events as _bot_events
from vkx.callback.generated.events.bot_events import *
from vkx.callback.generated.events.enums import *
from vkx.callback.generated.objects import *

API_URL: str = "https://api.vk.ru/method/"
API_VERSION: str = "5.199"

__all__ = [  # noqa: PLE0604
    "API_URL",
    "API_VERSION",
    "APICategories",
    "BaseGroupEvent",
    "BaseUserEvent",
    "Event",
    "GroupEventType",
    "UserEventType",
    *_objects.__all__,
    *_bot_events.__all__,
]
