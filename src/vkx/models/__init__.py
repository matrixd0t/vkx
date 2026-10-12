"""Типы VK API и событий.

Слой самодостаточный и поддерживается вручную. Содержит:
``objects`` (API-объекты), ``responses`` (тела ответов),
``methods`` (типизированные методы), ``events`` (longpoll/callback-события).

Объекты событий (``group_event_objects``/``user_event_objects``) и классы
user Long Poll (``user_events``) тоже реэкспортируются здесь. При коллизии
имён (``MessageNewObject``/``MessageEditObject``, ``MessageNewEvent``/
``MessageEditEvent``) приоритет у group/bot-версий; user-версии доступны через
``vkx.models.events.objects.user_event_objects`` и ``vkx.models.events.user_events``.
"""

from . import objects as _objects  # noqa: I001
from .categories import APICategories
from .events import *
from .events import bot_events as _bot_events
from .events import callback_events as _callback_events
from .events import user_events as _user_events
from .events.enums import *
from .events.objects import group_event_objects as _group_event_objects
from .events.objects import user_event_objects as _user_event_objects

# Порядок звёздочных импортов важен: group/bot-версии идут последними,
# чтобы при коллизии имён (MessageNewObject/MessageEditObject,
# MessageNewEvent/MessageEditEvent) приоритет был у них.
from .events.objects.user_event_objects import *
from .events.objects.group_event_objects import *
from .events.user_events import *
from .events.bot_events import *
from .events.callback_events import *
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
    *_user_events.__all__,
    *_group_event_objects.__all__,
    *_user_event_objects.__all__,
]
