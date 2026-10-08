import typing
from typing import Literal

from ..objects import *
from ..objects import Chat, ChatFull, SendPeerIdsResponseItem, UsersFields
from ..responses.base import OkResponseModel
from ..responses.messages import *  # type: ignore
from .base_category import BaseCategory

_MESSAGE_MAX_LENGTH = 4000


class MessagesCategory(BaseCategory):
    async def add_chat_user(
            self,
            chat_id: int,
            user_id: int | None = None,
            visible_messages_count: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.addChatUser()`

        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count:
        """

        return await self._call("messages.addChatUser", locals(), OkResponseModel)

    async def add_chat_users(
            self,
            chat_id: int | None = None,
            visible_messages_count: int | None = None,
    ) -> AddChatUsersResponseModel:
        """Method `messages.addChatUsers()`

        :param chat_id:
        :param visible_messages_count:
        """

        return await self._call("messages.addChatUsers", locals(), AddChatUsersResponseModel)

    async def allow_messages_from_group(
            self,
            group_id: int,
            key: str | None = None,
    ) -> OkResponseModel:
        """Method `messages.allowMessagesFromGroup()`

        :param group_id: Group ID.
        :param key:
        """

        return await self._call("messages.allowMessagesFromGroup", locals(), OkResponseModel)

    async def create_chat(
            self,
            group_id: int | None = None,
            title: str | None = None,
            user_ids: list[int] | None = None,
    ) -> CreateChatWithPeerIdsResponseModel:
        """Method `messages.createChat()`

        :param group_id:
        :param title: Chat title.
        :param user_ids: IDs of the users to be added to the chat.
        """

        return await self._call("messages.createChat", locals(), CreateChatWithPeerIdsResponseModel)

    async def delete(
            self,
            cmids: list[int] | None = None,
            delete_for_all: bool | None = None,
            group_id: int | None = None,
            message_ids: list[int] | None = None,
            peer_id: int | None = None,
            reason: int | None = None,
            spam: bool | None = None,
    ) -> list[DeleteFullResponseItem]:
        """Method `messages.delete()`

        :param cmids: Conversation message IDs.
        :param delete_for_all: '1' - delete message for for all.
        :param group_id: Group ID (for group messages with user access token)
        :param message_ids: Message IDs.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param reason: Reason for spam
        :param spam: '1' - to mark message as spam.
        """

        return await self._call("messages.delete", locals(), list[DeleteFullResponseItem])

    async def delete_chat_photo(
            self,
            chat_id: int,
            group_id: int | None = None,
    ) -> DeleteChatPhotoResponseModel:
        """Method `messages.deleteChatPhoto()`

        :param chat_id: Chat ID.
        :param group_id:
        """

        return await self._call("messages.deleteChatPhoto", locals(), DeleteChatPhotoResponseModel)

    async def delete_conversation(
            self,
            group_id: int | None = None,
            peer_id: int | None = None,
            user_id: int | None = None,
    ) -> DeleteConversationResponseModel:
        """Method `messages.deleteConversation()`

        :param group_id: Group ID (for group messages with user access token)
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param user_id: User ID. To clear a chat history use 'chat_id'
        """

        return await self._call("messages.deleteConversation", locals(), DeleteConversationResponseModel)

    async def delete_reaction(
            self,
            cmid: int,
            peer_id: int,
    ) -> bool:
        """Method `messages.deleteReaction()`

        :param cmid:
        :param peer_id:
        """

        return await self._call("messages.deleteReaction", locals(), bool)

    async def deny_messages_from_group(
            self,
            group_id: int,
    ) -> OkResponseModel:
        """Method `messages.denyMessagesFromGroup()`

        :param group_id: Group ID.
        """

        return await self._call("messages.denyMessagesFromGroup", locals(), OkResponseModel)

    async def edit(
            self,
            peer_id: int,
            attachment: AttachmentsInput | None = None,
            cmid: int | None = None,
            disable_mentions: bool | None = None,
            dont_parse_links: bool | None = None,
            group_id: int | None = None,
            keep_forward_messages: bool | None = None,
            keep_snippets: bool | None = None,
            keyboard: str | None = None,
            lat: float | None = None,
            long: float | None = None,
            message: str | None = None,
            message_id: int | None = None,
            template: str | None = None,
    ) -> bool:
        """Method `messages.edit()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'wall' - wall post, '<owner_id>' - ID of the media attachment owner. '<media_id>' - media attachment ID. Example: "photo100172_166443618"
        :param cmid:
        :param disable_mentions:
        :param dont_parse_links:
        :param group_id: Group ID (for group messages with user access token)
        :param keep_forward_messages: '1' - to keep forwarded, messages.
        :param keep_snippets: '1' - to keep attached snippets.
        :param keyboard:
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param message_id:
        :param template:
        """

        return await self._call("messages.edit", locals(), bool)

    async def edit_chat(
            self,
            chat_id: int,
            title: str | None = None,
    ) -> OkResponseModel:
        """Method `messages.editChat()`

        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """

        return await self._call("messages.editChat", locals(), OkResponseModel)

    @typing.overload
    async def get_by_conversation_message_id(
            self,
            conversation_message_ids: list[int],
            peer_id: int,
            extended: typing.Literal[True],
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
    ) -> GetByConversationMessageIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_conversation_message_id(
            self,
            conversation_message_ids: list[int],
            peer_id: int,
            extended: typing.Literal[False] | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
    ) -> GetByConversationMessageIdResponseModel: ...

    async def get_by_conversation_message_id(
            self,
            conversation_message_ids: list[int],
            peer_id: int,
            extended: bool | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
    ) -> GetByConversationMessageIdExtendedResponseModel | GetByConversationMessageIdResponseModel:
        """Method `messages.getByConversationMessageId()`

        :param conversation_message_ids: Conversation message IDs.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        return await self._call(
            "messages.getByConversationMessageId",
            locals(),
            dependent=((("extended",), GetByConversationMessageIdExtendedResponseModel),),
            default=GetByConversationMessageIdResponseModel,
        )

    @typing.overload
    async def get_by_id(
            self,
            extended: typing.Literal[True],
            cmids: list[int] | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            message_ids: list[int] | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
    ) -> MessagesGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
            self,
            extended: typing.Literal[False] | None = None,
            cmids: list[int] | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            message_ids: list[int] | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
    ) -> MessagesGetByIdResponseModel: ...

    async def get_by_id(
            self,
            extended: bool | None = None,
            cmids: list[int] | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            message_ids: list[int] | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
    ) -> MessagesGetByIdResponseModel | MessagesGetByIdExtendedResponseModel:
        """Method `messages.getById()`

        :param extended: Information whether the response should be extended
        :param cmids:
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param message_ids: Message IDs.
        :param peer_id:
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        """

        return await self._call(
            "messages.getById",
            locals(),
            dependent=((("extended",), MessagesGetByIdExtendedResponseModel),),
            default=MessagesGetByIdResponseModel,
        )

    async def get_chat_preview(
            self,
            fields: list[UsersFields] | None = None,
            link: str | None = None,
            peer_id: int | None = None,
    ) -> GetChatPreviewResponseModel:
        """Method `messages.getChatPreview()`

        :param fields: Profile fields to return.
        :param link: Invitation link.
        :param peer_id:
        """

        return await self._call("messages.getChatPreview", locals(), GetChatPreviewResponseModel)

    async def get_conversation_members(
            self,
            peer_id: int,
            count: int | None = None,
            extended: bool | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            member_ids: list[int] | None = None,
            offset: int | None = None,
    ) -> "GetConversationMembers":
        """Method `messages.getConversationMembers()`

        :param peer_id: Peer ID.
        :param count:
        :param extended: Extended flag
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param member_ids:
        :param offset:
        """

        return await self._call("messages.getConversationMembers", locals(), GetConversationMembers)

    async def get_conversations(
            self,
            count: int | None = None,
            extended: bool | None = None,
            fields: list[UserGroupFields] | None = None,
            filter: str | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            start_message_id: int | None = None,
    ) -> GetConversationsResponseModel:
        """Method `messages.getConversations()`

        :param count: Number of conversations to return.
        :param extended: '1' - return extra information about users and communities
        :param fields: Profile and communities fields to return.
        :param filter: Filter to apply: 'all' - all conversations, 'unread' - conversations with unread messages, 'important' - conversations, marked as important (only for community messages), 'unanswered' - conversations, marked as unanswered (only for community messages)
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of conversations.
        :param start_message_id: ID of the message from what to return dialogs.
        """

        return await self._call("messages.getConversations", locals(), GetConversationsResponseModel)

    @typing.overload
    async def get_conversations_by_id(
            self,
            peer_ids: list[int],
            extended: typing.Literal[True],
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
    ) -> "GetConversationByIdExtended": ...

    @typing.overload
    async def get_conversations_by_id(
            self,
            peer_ids: list[int],
            extended: typing.Literal[False] | None = None,
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
    ) -> "GetConversationById": ...

    async def get_conversations_by_id(
            self,
            peer_ids: list[int],
            extended: bool | None = None,
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
    ) -> "GetConversationByIdExtended | GetConversationById":
        """Method `messages.getConversationsById()`

        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        return await self._call(
            "messages.getConversationsById",
            locals(),
            dependent=((("extended",), GetConversationByIdExtended),),
            default=GetConversationById,
        )

    @typing.overload
    async def get_history(
            self,
            extended: typing.Literal[True],
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            rev: int | None = None,
            start_message_id: int | None = None,
            user_id: int | None = None,
    ) -> GetHistoryExtendedResponseModel: ...

    @typing.overload
    async def get_history(
            self,
            extended: typing.Literal[False] | None = None,
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            rev: int | None = None,
            start_message_id: int | None = None,
            user_id: int | None = None,
    ) -> GetHistoryResponseModel: ...

    async def get_history(
            self,
            extended: bool | None = None,
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            rev: int | None = None,
            start_message_id: int | None = None,
            user_id: int | None = None,
    ) -> GetHistoryResponseModel | GetHistoryExtendedResponseModel:
        """Method `messages.getHistory()`

        :param extended: Information whether the response should be extended
        :param count: Number of messages to return.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of messages.
        :param peer_id:
        :param rev: Sort order: '1' - return messages in chronological order. '0' - return messages in reverse chronological order.
        :param start_message_id: Starting message ID from which to return history.
        :param user_id: ID of the user whose message history you want to return.
        """

        return await self._call(
            "messages.getHistory",
            locals(),
            dependent=((("extended",), GetHistoryExtendedResponseModel),),
            default=GetHistoryResponseModel,
        )

    async def get_history_attachments(
            self,
            attachment_position: int | None = None,
            attachment_types: list[
                                  typing.Literal[
                                      "app_action_games",
                                      "app_action_mini_apps",
                                      "audio",
                                      "audio_message",
                                      "clip",
                                      "doc",
                                      "graffiti",
                                      "link",
                                      "market",
                                      "photo",
                                      "share",
                                      "video",
                                      "wall",
                                  ]
                              ]
                              | None = None,
            cmid: int | None = None,
            count: int | None = None,
            extended: bool | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            max_forwards_level: int | None = None,
            media_type: str | None = None,
            message_video: bool | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            photo_sizes: bool | None = None,
            preserve_order: bool | None = None,
            start_from: str | None = None,
    ) -> GetHistoryAttachmentsResponseModel:
        """Method `messages.getHistoryAttachments()`

        :param attachment_position:
        :param attachment_types:
        :param cmid:
        :param count: Number of objects to return.
        :param extended:
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with group access token)
        :param max_forwards_level:
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param message_video:
        :param offset:
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param photo_sizes: '1' - to return photo sizes in a
        :param preserve_order:
        :param start_from: Message ID to start return results from.
        """

        return await self._call("messages.getHistoryAttachments", locals(), GetHistoryAttachmentsResponseModel)

    @typing.overload
    async def get_important_messages(
            self,
            extended: typing.Literal[True],
            count: int | None = None,
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            preview_length: int | None = None,
            start_message_id: int | None = None,
    ) -> GetImportantMessagesExtendedResponseModel: ...

    @typing.overload
    async def get_important_messages(
            self,
            extended: typing.Literal[False] | None = None,
            count: int | None = None,
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            preview_length: int | None = None,
            start_message_id: int | None = None,
    ) -> GetImportantMessagesResponseModel: ...

    async def get_important_messages(
            self,
            extended: bool | None = None,
            count: int | None = None,
            fields: list[UserGroupFields] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            preview_length: int | None = None,
            start_message_id: int | None = None,
    ) -> GetImportantMessagesExtendedResponseModel | GetImportantMessagesResponseModel:
        """Method `messages.getImportantMessages()`

        :param extended: Return extended properties
        :param count: Amount of needed important messages.
        :param fields: Actors fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param offset:
        :param preview_length: Maximum length of messages body.
        :param start_message_id:
        """

        return await self._call(
            "messages.getImportantMessages",
            locals(),
            dependent=((("extended",), GetImportantMessagesExtendedResponseModel),),
            default=GetImportantMessagesResponseModel,
        )

    async def get_intent_users(
            self,
            intent: str,
            count: int | None = None,
            extended: bool | None = None,
            fields: list[str] | None = None,
            name_case: str | None = None,
            offset: int | None = None,
            subscribe_id: int | None = None,
    ) -> GetIntentUsersResponseModel:
        """Method `messages.getIntentUsers()`

        :param intent:
        :param count:
        :param extended:
        :param fields:
        :param name_case:
        :param offset:
        :param subscribe_id:
        """

        return await self._call("messages.getIntentUsers", locals(), GetIntentUsersResponseModel)

    async def get_invite_link(
            self,
            peer_id: int,
            group_id: int | None = None,
            reset: bool | None = None,
    ) -> GetInviteLinkResponseModel:
        """Method `messages.getInviteLink()`

        :param peer_id: Destination ID.
        :param group_id: Group ID
        :param reset: 1 - to generate new link (revoke previous), 0 - to return previous link.
        """

        return await self._call("messages.getInviteLink", locals(), GetInviteLinkResponseModel)

    async def get_last_activity(
            self,
            user_id: int,
    ) -> "LastActivity":
        """Method `messages.getLastActivity()`

        :param user_id: User ID.
        """

        return await self._call("messages.getLastActivity", locals(), LastActivity)

    async def get_long_poll_history(
            self,
            credentials: bool | None = None,
            events_limit: int | None = None,
            extended: bool | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            last_n: int | None = None,
            lp_version: int | None = None,
            max_msg_id: int | None = None,
            msgs_limit: int | None = None,
            onlines: bool | None = None,
            preview_length: int | None = None,
            pts: int | None = None,
            ts: int | None = None,
    ) -> GetLongPollHistoryResponseModel:
        """Method `messages.getLongPollHistory()`

        :param credentials:
        :param events_limit: Maximum number of events to return.
        :param extended:
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with user access token)
        :param last_n:
        :param lp_version:
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param msgs_limit: Maximum number of messages to return.
        :param onlines: '1' - to return history with online users only.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param pts: Last value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        return await self._call("messages.getLongPollHistory", locals(), GetLongPollHistoryResponseModel)

    async def get_long_poll_server(
            self,
            group_id: int | None = None,
            lp_version: int | None = None,
            need_pts: bool | None = None,
    ) -> "LongpollParams":
        """Method `messages.getLongPollServer()`

        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        :param need_pts: '1' - to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        return await self._call("messages.getLongPollServer", locals(), LongpollParams)

    async def get_messages_reactions(
            self,
            cmids: list[int],
            peer_id: int,
    ) -> GetMessagesReactionsResponseModel:
        """Method `messages.getMessagesReactions()`

        :param cmids:
        :param peer_id:
        """

        return await self._call("messages.getMessagesReactions", locals(), GetMessagesReactionsResponseModel)

    async def get_reacted_peers(
            self,
            cmid: int,
            peer_id: int,
            reaction_id: int | None = None,
    ) -> GetReactedPeersResponseModel:
        """Method `messages.getReactedPeers()`

        :param cmid:
        :param peer_id:
        :param reaction_id:
        """

        return await self._call("messages.getReactedPeers", locals(), GetReactedPeersResponseModel)

    async def get_reactions_assets(
            self,
            client_version: int | None = None,
    ) -> GetReactionsAssetsResponseModel:
        """Method `messages.getReactionsAssets()`

        :param client_version:
        """

        return await self._call("messages.getReactionsAssets", locals(), GetReactionsAssetsResponseModel)

    async def is_messages_from_group_allowed(
            self,
            group_id: int,
            user_id: int,
    ) -> IsMessagesFromGroupAllowedResponseModel:
        """Method `messages.isMessagesFromGroupAllowed()`

        :param group_id: Group ID.
        :param user_id: User ID.
        """

        return await self._call("messages.isMessagesFromGroupAllowed", locals(), IsMessagesFromGroupAllowedResponseModel)

    async def join_chat_by_invite_link(
            self,
            link: str,
    ) -> JoinChatByInviteLinkResponseModel:
        """Method `messages.joinChatByInviteLink()`

        :param link: Invitation link.
        """

        return await self._call("messages.joinChatByInviteLink", locals(), JoinChatByInviteLinkResponseModel)

    async def mark_as_answered_conversation(
            self,
            peer_id: int,
            answered: bool | None = None,
            group_id: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.markAsAnsweredConversation()`

        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' - to mark as answered, '0' - to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """

        return await self._call("messages.markAsAnsweredConversation", locals(), OkResponseModel)

    async def mark_as_important(
            self,
            important: int | None = None,
            message_ids: list[int] | None = None,
    ) -> list[int]:
        """Method `messages.markAsImportant()`

        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        :param message_ids: IDs of messages to mark as important.
        """

        return await self._call("messages.markAsImportant", locals(), list[int])

    async def mark_as_important_conversation(
            self,
            peer_id: int,
            group_id: int | None = None,
            important: bool | None = None,
    ) -> OkResponseModel:
        """Method `messages.markAsImportantConversation()`

        :param peer_id: ID of conversation to mark as important.
        :param group_id: Group ID (for group messages with group access token)
        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        """

        return await self._call("messages.markAsImportantConversation", locals(), OkResponseModel)

    async def mark_as_read(
            self,
            group_id: int | None = None,
            mark_conversation_as_read: bool | None = None,
            message_ids: list[int] | None = None,
            peer_id: int | None = None,
            start_message_id: int | None = None,
            up_to_cmid: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.markAsRead()`

        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read:
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param up_to_cmid:
        """

        return await self._call("messages.markAsRead", locals(), OkResponseModel)

    async def mark_reactions_as_read(
            self,
            peer_id: int,
            cmids: list[int] | None = None,
    ) -> bool:
        """Method `messages.markReactionsAsRead()`

        :param peer_id:
        :param cmids:
        """

        return await self._call("messages.markReactionsAsRead", locals(), bool)

    async def mute_chat_mentions(
            self,
            mention_status: str,
            peer_id: int,
    ) -> OkResponseModel:
        """Method `messages.muteChatMentions()`

        :param mention_status:
        :param peer_id: Chat id
        """

        return await self._call("messages.muteChatMentions", locals(), OkResponseModel)

    async def pin(
            self,
            peer_id: int,
            cmid: int | None = None,
            message_id: int | None = None,
    ) -> "PinnedMessage":
        """Method `messages.pin()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param cmid: Conversation message ID
        :param message_id: Message ID
        """

        return await self._call("messages.pin", locals(), PinnedMessage)

    async def remove_chat_user(
            self,
            chat_id: int,
            member_id: int | None = None,
            user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.removeChatUser()`

        :param chat_id: Chat ID.
        :param member_id:
        :param user_id: ID of the user to be removed from the chat.
        """

        return await self._call("messages.removeChatUser", locals(), OkResponseModel)

    async def restore(
            self,
            cmid: int | None = None,
            group_id: int | None = None,
            message_id: int | None = None,
            peer_id: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.restore()`

        :param cmid:
        :param group_id: Group ID (for group messages with user access token)
        :param message_id: ID of a previously-deleted message to restore.
        :param peer_id: Destination ID.
        """

        return await self._call("messages.restore", locals(), OkResponseModel)

    @typing.overload
    async def search(
            self,
            extended: typing.Literal[True],
            count: int | None = None,
            date: int | None = None,
            fields: list[str] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
            q: str | None = None,
    ) -> MessagesSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
            self,
            extended: typing.Literal[False] | None = None,
            count: int | None = None,
            date: int | None = None,
            fields: list[str] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
            q: str | None = None,
    ) -> MessagesSearchResponseModel: ...

    async def search(
            self,
            extended: bool | None = None,
            count: int | None = None,
            date: int | None = None,
            fields: list[str] | None = None,
            group_id: int | None = None,
            offset: int | None = None,
            peer_id: int | None = None,
            preview_length: int | None = None,
            q: str | None = None,
    ) -> MessagesSearchExtendedResponseModel | MessagesSearchResponseModel:
        """Method `messages.search()`

        :param extended:
        :param count: Number of messages to return.
        :param date: Date to search message before in Unixtime.
        :param fields:
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of messages.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param q: Search query string.
        """

        return await self._call(
            "messages.search",
            locals(),
            dependent=((("extended",), MessagesSearchExtendedResponseModel),),
            default=MessagesSearchResponseModel,
        )

    @typing.overload
    async def search_conversations(
            self,
            extended: typing.Literal[True],
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            q: str | None = None,
    ) -> SearchConversationsExtendedResponseModel: ...

    @typing.overload
    async def search_conversations(
            self,
            extended: typing.Literal[False] | None = None,
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            q: str | None = None,
    ) -> SearchConversationsResponseModel: ...

    async def search_conversations(
            self,
            extended: bool | None = None,
            count: int | None = None,
            fields: list[UsersFields] | None = None,
            group_id: int | None = None,
            q: str | None = None,
    ) -> SearchConversationsExtendedResponseModel | SearchConversationsResponseModel:
        """Method `messages.searchConversations()`

        :param extended: '1' - return extra information about users and communities
        :param count: Maximum number of results.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        :param q: Search query string.
        """

        return await self._call(
            "messages.searchConversations",
            locals(),
            dependent=((("extended",), SearchConversationsExtendedResponseModel),),
            default=SearchConversationsResponseModel,
        )

    async def send_message_event_answer(
            self,
            event_id: str,
            peer_id: int,
            user_id: int,
            event_data: str | None = None,
    ) -> OkResponseModel:
        """Method `messages.sendMessageEventAnswer()`

        :param event_id:
        :param peer_id:
        :param user_id:
        :param event_data:
        """

        return await self._call("messages.sendMessageEventAnswer", locals(), OkResponseModel)

    async def send_reaction(
            self,
            cmid: int,
            peer_id: int,
            reaction_id: int,
    ) -> bool:
        """Method `messages.sendReaction()`

        :param cmid:
        :param peer_id:
        :param reaction_id:
        """

        return await self._call("messages.sendReaction", locals(), bool)

    async def set_activity(
            self,
            group_id: int | None = None,
            peer_id: int | None = None,
            type: str | None = None,
            user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.setActivity()`

        :param group_id: Group ID (for group messages with group access token)
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param type: 'typing' - user has started to type.
        :param user_id: User ID.
        """

        return await self._call("messages.setActivity", locals(), OkResponseModel)

    async def set_chat_photo(
            self,
            file: str,
    ) -> SetChatPhotoResponseModel:
        """Method `messages.setChatPhoto()`

        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """

        return await self._call("messages.setChatPhoto", locals(), SetChatPhotoResponseModel)

    async def unpin(
            self,
            peer_id: int,
            group_id: int | None = None,
    ) -> OkResponseModel:
        """Method `messages.unpin()`

        :param peer_id:
        :param group_id:
        """

        return await self._call("messages.unpin", locals(), OkResponseModel)

    @typing.overload  # type: ignore
    async def send(  # type: ignore
            self,
            user_id: int | None = None,
            random_id: int | None = None,
            peer_id: int | None = None,
            peer_ids: None = None,
            domain: str | None = None,
            chat_id: int | None = None,
            user_ids: None = ...,
            message: str | None = None,
            lat: float | None = None,
            long: float | None = None,
            attachment: AttachmentsInput | None = None,
            reply_to: int | None = None,
            forward_messages: list[int] | None = None,
            forward: str | None = None,
            sticker_id: int | None = None,
            group_id: int | None = None,
            keyboard: str | None = None,
            template: str | None = None,
            payload: str | None = None,
            content_source: str | None = None,
            dont_parse_links: bool | None = None,
            disable_mentions: bool | None = None,
            intent: (
                    Literal[
                        "account_update",
                        "bot_ad_invite",
                        "bot_ad_promo",
                        "confirmed_notification",
                        "customer_support",
                        "default",
                        "game_notification",
                        "moderated_newsletter",
                        "non_promo_newsletter",
                        "promo_newsletter",
                        "purchase_update",
                    ]
                    | None
            ) = None,
            subscribe_id: int | None = None,
    ) -> list[list[int]]: ...

    @typing.overload
    async def send(
            self,
            user_id: int | None = None,
            random_id: int | None = None,
            peer_id: int | None = None,
            peer_ids: list[int] | None = None,
            domain: str | None = None,
            chat_id: int | None = None,
            user_ids: list[int] = ...,
            message: str | None = None,
            lat: float | None = None,
            long: float | None = None,
            attachment: AttachmentsInput | None = None,
            reply_to: int | None = None,
            forward_messages: list[int] | None = None,
            forward: str | None = None,
            sticker_id: int | None = None,
            group_id: int | None = None,
            keyboard: str | None = None,
            template: str | None = None,
            payload: str | None = None,
            content_source: str | None = None,
            dont_parse_links: bool | None = None,
            disable_mentions: bool | None = None,
            intent: (
                    Literal[
                        "account_update",
                        "bot_ad_invite",
                        "bot_ad_promo",
                        "confirmed_notification",
                        "customer_support",
                        "default",
                        "game_notification",
                        "moderated_newsletter",
                        "non_promo_newsletter",
                        "promo_newsletter",
                        "purchase_update",
                    ]
                    | None
            ) = None,
            subscribe_id: int | None = None,
    ) -> list[list[SendPeerIdsResponseItem]]: ...

    @typing.overload
    async def send(
            self,
            user_id: int | None = None,
            random_id: int | None = None,
            peer_id: int | None = None,
            peer_ids: list[int] = ...,
            domain: str | None = None,
            chat_id: int | None = None,
            user_ids: list[int] | None = None,
            message: str | None = None,
            lat: float | None = None,
            long: float | None = None,
            attachment: AttachmentsInput | None = None,
            reply_to: int | None = None,
            forward_messages: list[int] | None = None,
            forward: str | None = None,
            sticker_id: int | None = None,
            group_id: int | None = None,
            keyboard: str | None = None,
            template: str | None = None,
            payload: str | None = None,
            content_source: str | None = None,
            dont_parse_links: bool | None = None,
            disable_mentions: bool | None = None,
            intent: (
                    Literal[
                        "account_update",
                        "bot_ad_invite",
                        "bot_ad_promo",
                        "confirmed_notification",
                        "customer_support",
                        "default",
                        "game_notification",
                        "moderated_newsletter",
                        "non_promo_newsletter",
                        "promo_newsletter",
                        "purchase_update",
                    ]
                    | None
            ) = None,
            subscribe_id: int | None = None,
    ) -> list[list[SendPeerIdsResponseItem]]: ...

    async def send(
            self,
            user_id: int | None = None,
            random_id: int | None = None,
            peer_id: int | None = None,
            peer_ids: list[int] | None = None,
            domain: str | None = None,
            chat_id: int | None = None,
            user_ids: list[int] | None = None,
            message: str | None = None,
            lat: float | None = None,
            long: float | None = None,
            attachment: AttachmentsInput | None = None,
            reply_to: int | None = None,
            forward_messages: list[int] | None = None,
            forward: str | None = None,
            sticker_id: int | None = None,
            group_id: int | None = None,
            keyboard: str | None = None,
            template: str | None = None,
            payload: str | None = None,
            content_source: str | None = None,
            dont_parse_links: bool | None = None,
            disable_mentions: bool | None = None,
            intent: (
                    Literal[
                        "account_update",
                        "bot_ad_invite",
                        "bot_ad_promo",
                        "confirmed_notification",
                        "customer_support",
                        "default",
                        "game_notification",
                        "moderated_newsletter",
                        "non_promo_newsletter",
                        "promo_newsletter",
                        "purchase_update",
                    ]
                    | None
            ) = None,
            subscribe_id: int | None = None,
    ) -> list[list[SendPeerIdsResponseItem | int]]:
        """Sends a message.

        :param user_id: User ID (by default — current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param peer_ids: IDs of message recipients. (See peer_id)
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param user_ids: IDs of message recipients (if new conversation shall be started).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param forward: JSON describing the forwarded message or reply
        :param sticker_id: Sticker id.
        :param group_id: Group ID (for group messages with group access token)
        :param keyboard:
        :param template:
        :param payload:
        :param content_source: JSON describing the content source in the message
        :param dont_parse_links:
        :param disable_mentions:
        :param intent:
        :param subscribe_id:
        """

        params = locals().copy()
        chunks = (
            [
                message[index:index + _MESSAGE_MAX_LENGTH]
                for index in range(0, len(message), _MESSAGE_MAX_LENGTH)
            ]
            if message
            else [message]
        )
        responses: list[SendPeerIdsResponseItem | int] = []
        for index, chunk in enumerate(chunks):
            chunk_params = params.copy()
            chunk_params["message"] = chunk
            if random_id is not None and index:
                chunk_params["random_id"] = random_id + index
            response = await self._call(
                "messages.send",
                chunk_params,
                dependent=(
                    (("user_ids",), list[SendPeerIdsResponseItem]),
                    (("peer_ids",), list[SendPeerIdsResponseItem]),
                ),
                default=int,
            )
            responses.extend(response if isinstance(response, list) else [response])

        if user_ids is not None or peer_ids is not None:
            peers: dict[int, list[SendPeerIdsResponseItem]] = {}
            for response in responses:
                if isinstance(response, SendPeerIdsResponseItem):
                    peers.setdefault(response.peer_id, []).append(response)
            return list(peers.values())

        return [[typing.cast(int, response) for response in responses]]

    @typing.overload  # type: ignore
    async def get_chat(
            self,
            *,
            chat_id: int,
            name_case: str | None = None,
    ) -> Chat: ...

    @typing.overload
    async def get_chat(
            self,
            *,
            chat_id: int,
            fields: list[UsersFields],
            name_case: str | None = None,
    ) -> ChatFull: ...

    @typing.overload
    async def get_chat(
            self,
            *,
            chat_ids: list[int],
            name_case: str | None = None,
    ) -> list[Chat]: ...

    @typing.overload
    async def get_chat(
            self,
            *,
            chat_ids: list[int],
            fields: list[UsersFields],
            name_case: str | None = None,
    ) -> list[ChatFull]: ...

    async def get_chat(
            self,
            fields: list[UsersFields] | None = None,
            chat_ids: list[int] | None = None,
            chat_id: int | None = None,
            name_case: str | None = None,
    ) -> Chat | ChatFull | list[Chat] | list[ChatFull]:
        """Method `messages.getChat()`

        :param fields: Profile fields to return.
        :param chat_ids: Chat IDs.
        :param chat_id: Chat ID.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """

        return await self._call(
            "messages.getChat",
            locals(),
            dependent=((("fields", "chat_id"), ChatFull), (("fields", "chat_ids"), list[ChatFull]), (("chat_id",), Chat), (("chat_ids",), list[Chat]),),
            default=Chat,
        )


__all__ = ("MessagesCategory",)

__all__ = ("MessagesCategory",)
