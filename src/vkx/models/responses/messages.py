from ..base_model import BaseModel, Field
from ..objects import (
    Chat,
    ChatPreview,
    Conversation,
    ConversationWithMessage,
    GetInviteLinkByOwnerResponseItem,
    GroupFull,
    HistoryAttachment,
    LongpollMessages,
    LongpollParams,
    Message,
    MessagesArray,
    ReactionAssetItem,
    ReactionCounterResponseItem,
    ReactionCountersResponseItem,
    ReactionResponseItem,
    User,
    UserFull,
)


class AddChatUsersResponseModel(BaseModel):
    failed_peer_ids: list[int] = Field()
    failed_phone_numbers: list[str] = Field()
    invitees: list[int] = Field()


class CreateChatWithPeerIdsResponseModel(BaseModel):
    chat_id: int | None = Field(
        default=None,
    )
    peer_ids: list[int] | None = Field(
        default=None,
    )


class DeleteChatPhotoResponseModel(BaseModel):
    message_id: int | None = Field(
        default=None,
    )
    chat: "Chat | None" = Field(
        default=None,
    )


class DeleteConversationResponseModel(BaseModel):
    last_deleted_id: int = Field()


class GetByConversationMessageIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetByConversationMessageIdResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()


class MessagesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class MessagesGetByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()


class GetChatPreviewResponseModel(BaseModel):
    preview: "ChatPreview" = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetConversationsResponseModel(BaseModel):
    count: int = Field()
    items: list["ConversationWithMessage"] = Field()
    unread_count: int | None = Field(
        default=None,
    )
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetHistoryAttachmentsResponseModel(BaseModel):
    items: list["HistoryAttachment"] = Field()
    next_from: str | None = Field(
        default=None,
    )
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetHistoryExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    conversations: list["Conversation"] | None = Field(
        default=None,
    )


class GetHistoryResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()


class GetImportantMessagesExtendedResponseModel(BaseModel):
    messages: "MessagesArray" = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    conversations: list["Conversation"] | None = Field(
        default=None,
    )


class GetImportantMessagesResponseModel(BaseModel):
    messages: "MessagesArray" = Field()
    profiles: list["User"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    conversations: list["Conversation"] | None = Field(
        default=None,
    )


class GetIntentUsersResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )


class GetInviteLinkByOwnerResponseModel(BaseModel):
    items: list["GetInviteLinkByOwnerResponseItem"] = Field()


class GetInviteLinkResponseModel(BaseModel):
    link: str | None = Field(
        default=None,
    )


class GetLongPollHistoryResponseModel(BaseModel):
    history: list[list[str | int]] | None = Field(
        default=None,
    )
    messages: "LongpollMessages | None" = Field(
        default=None,
    )
    credentials: "LongpollParams | None" = Field(
        default=None,
    )
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    chats: list["Chat"] | None = Field(
        default=None,
    )
    new_pts: int | None = Field(
        default=None,
    )
    from_pts: int | None = Field(
        default=None,
    )
    more: bool | None = Field(
        default=None,
    )
    conversations: list["Conversation"] | None = Field(
        default=None,
    )


class GetMessagesReactionsResponseModel(BaseModel):
    items: list["ReactionCountersResponseItem"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetReactedPeersResponseModel(BaseModel):
    count: int = Field()
    reactions: list["ReactionResponseItem"] = Field()
    counters: list["ReactionCounterResponseItem"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class GetReactionsAssetsResponseModel(BaseModel):
    version: int = Field()
    assets: list["ReactionAssetItem"] = Field()
    reaction_ids: list[int] = Field()
    override_assets: list["ReactionAssetItem"] | None = Field(
        default=None,
    )


class IsMessagesFromGroupAllowedResponseModel(BaseModel):
    is_allowed: bool | None = Field(
        default=None,
    )


class JoinChatByInviteLinkResponseModel(BaseModel):
    chat_id: int | None = Field(
        default=None,
    )


class SearchConversationsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Conversation"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class SearchConversationsResponseModel(BaseModel):
    count: int = Field()
    items: list["Conversation"] = Field()


class MessagesSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    conversations: list["Conversation"] | None = Field(
        default=None,
    )


class MessagesSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["Message"] = Field()


class SetChatPhotoResponseModel(BaseModel):
    message_id: int | None = Field(
        default=None,
    )
    chat: "Chat | None" = Field(
        default=None,
    )


__all__ = (
    "AddChatUsersResponseModel",
    "CreateChatWithPeerIdsResponseModel",
    "DeleteChatPhotoResponseModel",
    "DeleteConversationResponseModel",
    "GetByConversationMessageIdExtendedResponseModel",
    "GetByConversationMessageIdResponseModel",
    "GetChatPreviewResponseModel",
    "GetConversationsResponseModel",
    "GetHistoryAttachmentsResponseModel",
    "GetHistoryExtendedResponseModel",
    "GetHistoryResponseModel",
    "GetImportantMessagesExtendedResponseModel",
    "GetImportantMessagesResponseModel",
    "GetIntentUsersResponseModel",
    "GetInviteLinkByOwnerResponseModel",
    "GetInviteLinkResponseModel",
    "GetLongPollHistoryResponseModel",
    "GetMessagesReactionsResponseModel",
    "GetReactedPeersResponseModel",
    "GetReactionsAssetsResponseModel",
    "IsMessagesFromGroupAllowedResponseModel",
    "JoinChatByInviteLinkResponseModel",
    "MessagesGetByIdExtendedResponseModel",
    "MessagesGetByIdResponseModel",
    "MessagesSearchExtendedResponseModel",
    "MessagesSearchResponseModel",
    "SearchConversationsExtendedResponseModel",
    "SearchConversationsResponseModel",
    "SetChatPhotoResponseModel",
)
