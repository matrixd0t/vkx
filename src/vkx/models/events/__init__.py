from .bot_events import BaseGroupEvent
from .callback_events import BaseCallbackEvent, CallbackEvent
from .enums import CallbackEventType, GroupEventType, UserEventType
from .user_events import USER_EVENTS, BaseUserEvent, RawUserEvent, parse_user_event

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
    "RawUserEvent",
    "UserEventType",
    "parse_user_event",
)
