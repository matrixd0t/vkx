from typing import Any, Self

from vkx.callback.generated.base_model import BaseModel

from .objects import user_event_objects


class BaseUserEvent(BaseModel):
    object: Any | None
    unprepared_ctx_api: Any | None = None

    @classmethod
    def from_raw(cls, data: bytes) -> Self:
        return cls.model_validate_json(data)

    @classmethod
    def parse(cls, obj: list[Any]) -> Self:
        return cls.model_validate({"object": obj})

    def to_dict(self) -> dict[str, Any]:
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


__all__ = (
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
)
