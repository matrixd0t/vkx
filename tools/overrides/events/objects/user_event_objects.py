import enum
from datetime import UTC, datetime
from typing import Any

from vkx.callback.generated.base_model import BaseModel

JsonObject = dict[str, Any] | list[Any]
Attachments = JsonObject
ExtraValues = JsonObject


class EventObject(BaseModel):
    pass


class MessageObject(EventObject):
    message_id: int | None = None
    flags: int | None = None
    peer_id: int | None = None
    timestamp: int | None = None
    text: str | None = None
    extra_values: ExtraValues | None = None
    attachments: Attachments | None = None
    random_id: int | None = None

    @property
    def date(self) -> datetime | None:
        if self.timestamp is None:
            return None
        return datetime.fromtimestamp(timestamp=self.timestamp, tz=UTC)

    @property
    def message(self) -> str | None:
        if self.text is None:
            return None
        return self.text.replace("<br>", "\n").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&")


class MessageFlagsReplaceObject(MessageObject):
    pass


class MessageSetFlagsObject(MessageObject):
    pass


class MessageResetFlagsObject(MessageObject):
    pass


class MessageNewObject(MessageObject):
    pass


class MessageEditObject(MessageObject):
    pass


class InReadObject(EventObject):
    peer_id: int | None = None
    local_id: int | None = None


class OutReadObject(InReadObject):
    pass


class FriendOnlineObject(EventObject):
    user_id: int | None = None
    extra: int = 0
    timestamp: int | None = None


class FriendOfflineObject(EventObject):
    user_id: int | None = None
    flags: int = 0
    timestamp: int | None = None


class DialogResetFlagsObject(EventObject):
    peer_id: int | None = None
    mask: int | None = None


class DialogFlagsReplaceObject(EventObject):
    peer_id: int | None = None
    flags: int | None = None


class DialogSetFlagsObject(DialogResetFlagsObject):
    pass


class DeleteObject(InReadObject):
    pass


class RestoreObject(InReadObject):
    pass


class ChangeConversationParamsObject(EventObject):
    chat_id: int | None = None
    self: int | None = None


class DialogTypingStateObject(EventObject):
    user_id: int | None = None
    flags: int | None = None


class ConversationTypingStateObject(EventObject):
    user_id: int | None = None
    chat_id: int | None = None


class TypingStateObject(EventObject):
    user_ids: list[int] | None = None
    peer_id: int | None = None
    total_count: int | None = None
    ts: int | None = None


class CallObject(EventObject):
    user_id: int | None = None
    call_id: int | None = None


class CounterObject(EventObject):
    count: int | None = None


class SettingsChangedObject(EventObject):
    peer_id: int | None = None
    sound: int | None = None
    disabled_until: int | None = None


class ChatInfoEditObject(EventObject):
    type_id: int | None = None
    peer_id: int | None = None
    info: str | int | None = None


class ChatVoiceMessageStatesObject(EventObject):
    user_ids: list[int] | None = None
    peer_id: int | None = None
    total_count: int | None = None
    ts: int | None = None


class ChatEditObject(EventObject):
    chat_id: int | None = None
    self: int | None = None


class ActionType(enum.IntEnum):
    ACCEPT = 2
    REMOVE_OR_CANCEL = 3


class FriendActionObject(EventObject):
    action_type: ActionType | None = None
    user_id: int | None = None


class CreateFolderObject(EventObject):
    folder_id: int | None = None
    folder_name: str | None = None
    random_id: int | None = None


class DeleteFolderObject(EventObject):
    folder_id: int | None = None


class RenameFolderObject(EventObject):
    folder_id: int | None = None
    new_folder_name: str | None = None


class AddConversationsToFolderObject(EventObject):
    folder_id: int | None = None
    peer_ids: list[int] | None = None


class RemoveConversationsFromFolderObject(EventObject):
    folder_id: int | None = None
    peer_ids: list[int] | None = None


class ChangeFolderOrderObject(EventObject):
    folder_ids: list[int] | None = None


class CounterUnreadDialogsInFoldersObject(EventObject):
    folder_id: int | None = None
    unread_count: int | None = None
    unread_unmuted_count: int | None = None


__all__ = (
    "AddConversationsToFolderObject",
    "CallObject",
    "ChangeConversationParamsObject",
    "ChangeFolderOrderObject",
    "ChatEditObject",
    "ChatInfoEditObject",
    "ChatVoiceMessageStatesObject",
    "ConversationTypingStateObject",
    "CounterObject",
    "CounterUnreadDialogsInFoldersObject",
    "CreateFolderObject",
    "DeleteFolderObject",
    "DeleteObject",
    "DialogFlagsReplaceObject",
    "DialogResetFlagsObject",
    "DialogSetFlagsObject",
    "DialogTypingStateObject",
    "FriendActionObject",
    "FriendOfflineObject",
    "FriendOnlineObject",
    "InReadObject",
    "MessageEditObject",
    "MessageFlagsReplaceObject",
    "MessageNewObject",
    "MessageObject",
    "MessageResetFlagsObject",
    "MessageSetFlagsObject",
    "OutReadObject",
    "RemoveConversationsFromFolderObject",
    "RenameFolderObject",
    "RestoreObject",
    "SettingsChangedObject",
    "TypingStateObject",
)
