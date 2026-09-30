from typing import Any, Self

from ..base_model import BaseModel
from .enums import UserEventType
from .objects import user_event_objects


class BaseUserEvent(BaseModel):
    object: Any | None
    unprepared_ctx_api: Any | None = None

    @classmethod
    def from_raw(cls, data: str | bytes, **kwargs) -> Self:
        return cls.model_validate_json(data)

    @classmethod
    def parse(cls, obj: list[Any]) -> Self:
        return cls.model_validate({"object": obj})

    def to_dict(self, **kwargs) -> dict[str, Any]:
        return self.model_dump()

    @property
    def ctx_api(self) -> "Any":
        if self.unprepared_ctx_api is None:
            raise AssertionError
        return self.unprepared_ctx_api


class RawUserEvent(BaseUserEvent):
    object: list[Any]


class MessageFlagsReplaceEvent(BaseUserEvent):
    object: user_event_objects.MessageFlagsReplaceObject


class MessageSetFlagsEvent(BaseUserEvent):
    object: user_event_objects.MessageSetFlagsObject


class MessageResetFlagsEvent(BaseUserEvent):
    object: user_event_objects.MessageResetFlagsObject


class MessageNewEvent(BaseUserEvent):
    object: user_event_objects.MessageNewObject


class MessagesDeleteEvent(BaseUserEvent):
    object: user_event_objects.DeleteObject


class MessagesRestoreEvent(BaseUserEvent):
    object: user_event_objects.RestoreObject


class MessageEditEvent(BaseUserEvent):
    object: user_event_objects.MessageEditObject


class ChatVoiceMessageStatesEvent(BaseUserEvent):
    object: user_event_objects.ChatVoiceMessageStatesObject


class ChatEditEvent(BaseUserEvent):
    object: user_event_objects.ChatEditObject


class ChatInfoEditEvent(BaseUserEvent):
    object: user_event_objects.ChatInfoEditObject


class ChatTypingStateEvent(BaseUserEvent):
    object: user_event_objects.ConversationTypingStateObject


class DialogTypingStateEvent(BaseUserEvent):
    object: user_event_objects.DialogTypingStateObject


class UsersTypingStateEvent(BaseUserEvent):
    object: user_event_objects.TypingStateObject


class DialogResetFlagsEvent(BaseUserEvent):
    object: user_event_objects.DialogResetFlagsObject


class DialogFlagsReplaceEvent(BaseUserEvent):
    object: user_event_objects.DialogFlagsReplaceObject


class DialogSetFlagsEvent(BaseUserEvent):
    object: user_event_objects.DialogSetFlagsObject


class FriendOnlineEvent(BaseUserEvent):
    object: user_event_objects.FriendOnlineObject


class FriendOfflineEvent(BaseUserEvent):
    object: user_event_objects.FriendOfflineObject


class FriendActionEvent(BaseUserEvent):
    object: user_event_objects.FriendActionObject


class CounterEvent(BaseUserEvent):
    object: user_event_objects.CounterObject


class CallEvent(BaseUserEvent):
    object: user_event_objects.CallObject


class NotificationsSettingsChangedEvent(BaseUserEvent):
    object: user_event_objects.SettingsChangedObject


class InReadEvent(BaseUserEvent):
    object: user_event_objects.InReadObject


class OutReadEvent(BaseUserEvent):
    object: user_event_objects.OutReadObject


class CreateFolderEvent(BaseUserEvent):
    object: user_event_objects.CreateFolderObject


class DeleteFolderEvent(BaseUserEvent):
    object: user_event_objects.DeleteFolderObject


class RenameFolderEvent(BaseUserEvent):
    object: user_event_objects.RenameFolderObject


class AddConversationsToFolderEvent(BaseUserEvent):
    object: user_event_objects.AddConversationsToFolderObject


class RemoveConversationsFromFolderEvent(BaseUserEvent):
    object: user_event_objects.RemoveConversationsFromFolderObject


class ChangeFolderOrderEvent(BaseUserEvent):
    object: user_event_objects.ChangeFolderOrderObject


class CounterUnreadDialogsInFoldersEvent(BaseUserEvent):
    object: list[user_event_objects.CounterUnreadDialogsInFoldersObject]


USER_EVENTS: dict[UserEventType, type[BaseUserEvent]] = {
    UserEventType.MESSAGE_FLAGS_REPLACE: MessageFlagsReplaceEvent,
    UserEventType.MESSAGE_FLAGS_SET: MessageSetFlagsEvent,
    UserEventType.MESSAGE_FLAGS_RESET: MessageResetFlagsEvent,
    UserEventType.MESSAGE_NEW: MessageNewEvent,
    UserEventType.MESSAGE_EDIT: MessageEditEvent,
    UserEventType.IN_READ: InReadEvent,
    UserEventType.OUT_READ: OutReadEvent,
    UserEventType.FRIEND_ONLINE: FriendOnlineEvent,
    UserEventType.FRIEND_OFFLINE: FriendOfflineEvent,
    UserEventType.DIALOG_FLAGS_RESET: DialogResetFlagsEvent,
    UserEventType.DIALOG_FLAGS_REPLACE: DialogFlagsReplaceEvent,
    UserEventType.DIALOG_FLAGS_SET: DialogSetFlagsEvent,
    UserEventType.MESSAGES_DELETE: MessagesDeleteEvent,
    UserEventType.MESSAGES_RESTORE: MessagesRestoreEvent,
    UserEventType.CHAT_EDIT: ChatEditEvent,
    UserEventType.CHAT_INFO_EDIT: ChatInfoEditEvent,
    UserEventType.DIALOG_TYPING_STATE: DialogTypingStateEvent,
    UserEventType.CHAT_TYPING_STATE: ChatTypingStateEvent,
    UserEventType.USERS_TYPING_STATE: UsersTypingStateEvent,
    UserEventType.CHAT_VOICE_MESSAGE_STATES: ChatVoiceMessageStatesEvent,
    UserEventType.CALL: CallEvent,
    UserEventType.COUNTER: CounterEvent,
    UserEventType.FRIEND_ACTION: FriendActionEvent,
    UserEventType.NOTIFICATIONS_SETTINGS_CHANGED: NotificationsSettingsChangedEvent,
    UserEventType.CREATE_FOLDER: CreateFolderEvent,
    UserEventType.DELETE_FOLDER: DeleteFolderEvent,
    UserEventType.RENAME_FOLDER: RenameFolderEvent,
    UserEventType.ADD_CONVERSATIONS_TO_FOLDER: AddConversationsToFolderEvent,
    UserEventType.REMOVE_CONVERSATIONS_FROM_FOLDER: RemoveConversationsFromFolderEvent,
    UserEventType.CHANGE_FOLDER_ORDER: ChangeFolderOrderEvent,
    UserEventType.COUNTER_UNREAD_DIALOGS_IN_FOLDERS: CounterUnreadDialogsInFoldersEvent,
}


def parse_user_event(raw: list[Any], /) -> BaseUserEvent:
    """Разобрать один update User Long Poll (``[code, *values]``) в типизированное событие.

    Неизвестный код или несовпадение позиций отдают ``RawUserEvent`` без ошибки.
    """
    if not raw:
        return RawUserEvent.parse(raw)
    event_type = UserEventType(raw[0])
    event_cls = USER_EVENTS.get(event_type, RawUserEvent)
    try:
        return event_cls.parse(raw[1:])
    except Exception:  # noqa: BLE001 — событие без модели не должно ронять поллинг
        return RawUserEvent.parse(raw[1:])


__all__ = (
    "USER_EVENTS",
    "AddConversationsToFolderEvent",
    "BaseUserEvent",
    "CallEvent",
    "ChangeFolderOrderEvent",
    "ChatEditEvent",
    "ChatInfoEditEvent",
    "ChatTypingStateEvent",
    "ChatVoiceMessageStatesEvent",
    "CounterEvent",
    "CounterUnreadDialogsInFoldersEvent",
    "CreateFolderEvent",
    "DeleteFolderEvent",
    "DialogFlagsReplaceEvent",
    "DialogResetFlagsEvent",
    "DialogSetFlagsEvent",
    "DialogTypingStateEvent",
    "FriendOfflineEvent",
    "FriendOnlineEvent",
    "InReadEvent",
    "MessageEditEvent",
    "MessageFlagsReplaceEvent",
    "MessageNewEvent",
    "MessageResetFlagsEvent",
    "MessageSetFlagsEvent",
    "MessagesDeleteEvent",
    "MessagesRestoreEvent",
    "NotificationsSettingsChangedEvent",
    "OutReadEvent",
    "RawUserEvent",
    "RemoveConversationsFromFolderEvent",
    "RenameFolderEvent",
    "UsersTypingStateEvent",
    "parse_user_event",
)
