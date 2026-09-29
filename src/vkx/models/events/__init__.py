from .bot_events import BaseGroupEvent
from .bot_typings import GroupTypes
from .callback_events import BaseCallbackEvent, CallbackEvent
from .enums import CallbackEventType, GroupEventType, UserEventType
from .user_events import USER_EVENTS, BaseUserEvent, RawUserEvent, parse_user_event
from .user_typings import UserTypes

type Event = UserEventType | GroupEventType


__all__ = (
    "USER_EVENTS",
    "BaseCallbackEvent",
    "BaseGroupEvent",
    "BaseUserEvent",
    "CallbackEvent",
    "CallbackEventType",
    "Event",
    "GroupEventType",
    "GroupTypes",
    "RawUserEvent",
    "UserEventType",
    "UserTypes",
    "parse_user_event",
)
