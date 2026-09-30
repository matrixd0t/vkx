import typing

from ..objects import *
from ..objects import (
    MutualFriend,
    OnlineUsers,
    OnlineUsersWithMobile,
    UsersFields,
)
from ..responses.base import OkResponseModel
from ..responses.friends import *  # type: ignore
from ..responses.friends import (
    FriendsGetRequestsResponseModel,
    GetOnlineOnlineMobileResponseModel,
    GetRequestsExtendedResponseModel,
    GetRequestsNeedMutualResponseModel,
)
from .base_category import BaseCategory


class FriendsCategory(BaseCategory):
    async def add(
        self,
        follow: bool | None = None,
        text: str | None = None,
        user_id: int | None = None,
    ) -> FriendsAddResponseModel:
        """Method `friends.add()`

        :param follow: '1' to pass an incoming request to followers list.
        :param text: Text of the message (up to 500 characters) for the friend request, if any.
        :param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
        """

        return await self._call("friends.add", locals(), FriendsAddResponseModel)

    async def add_list(
        self,
        name: str,
        user_ids: list[int] | None = None,
    ) -> AddListResponseModel:
        """Method `friends.addList()`

        :param name: Name of the friend list.
        :param user_ids: IDs of users to be added to the friend list.
        """

        return await self._call("friends.addList", locals(), AddListResponseModel)

    @typing.overload
    async def are_friends(
        self,
        user_ids: list[int],
        extended: typing.Literal[True],
        need_sign: bool | None = None,
    ) -> list[FriendExtendedStatus]: ...

    @typing.overload
    async def are_friends(
        self,
        user_ids: list[int],
        extended: typing.Literal[False] | None = None,
        need_sign: bool | None = None,
    ) -> list[FriendStatus]: ...

    async def are_friends(
        self,
        user_ids: list[int],
        extended: bool | None = None,
        need_sign: bool | None = None,
    ) -> list[FriendStatus] | list[FriendExtendedStatus]:
        """Method `friends.areFriends()`

        :param user_ids: IDs of the users whose friendship status to check.
        :param extended: Return friend request read_state field
        :param need_sign: '1' - to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        """

        return await self._call(
            "friends.areFriends",
            locals(),
            dependent=((("extended",), list[FriendExtendedStatus]),),
            default=list[FriendStatus],
        )

    async def delete(
        self,
        user_id: int | None = None,
    ) -> FriendsDeleteResponseModel:
        """Method `friends.delete()`

        :param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        """

        return await self._call("friends.delete", locals(), FriendsDeleteResponseModel)

    async def delete_all_requests(
        self,
    ) -> OkResponseModel:
        """Method `friends.deleteAllRequests()`"""

        return await self._call("friends.deleteAllRequests", locals(), OkResponseModel)

    async def delete_list(
        self,
        list_id: int,
    ) -> OkResponseModel:
        """Method `friends.deleteList()`

        :param list_id: ID of the friend list to delete.
        """

        return await self._call("friends.deleteList", locals(), OkResponseModel)

    async def edit(
        self,
        user_id: int,
        list_ids: list[int] | None = None,
    ) -> OkResponseModel:
        """Method `friends.edit()`

        :param user_id: ID of the user whose friend list is to be edited.
        :param list_ids: IDs of the friend lists to which to add the user.
        """

        return await self._call("friends.edit", locals(), OkResponseModel)

    async def edit_list(
        self,
        list_id: int,
        add_user_ids: list[int] | None = None,
        delete_user_ids: list[int] | None = None,
        name: str | None = None,
        user_ids: list[int] | None = None,
    ) -> OkResponseModel:
        """Method `friends.editList()`

        :param list_id: Friend list ID.
        :param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        :param name: Name of the friend list.
        :param user_ids: IDs of users in the friend list.
        """

        return await self._call("friends.editList", locals(), OkResponseModel)

    @typing.overload
    async def get(
        self,
        fields: list[UsersFields],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        ref: str | None = None,
        user_id: int | None = None,
    ) -> GetFieldsResponseModel: ...

    @typing.overload
    async def get(
        self,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        ref: str | None = None,
        user_id: int | None = None,
    ) -> FriendsGetResponseModel: ...

    async def get(
        self,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        ref: str | None = None,
        user_id: int | None = None,
    ) -> GetFieldsResponseModel | FriendsGetResponseModel:
        """Method `friends.get()`

        :param fields: Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param count: Number of friends to return.
        :param list_id: ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param offset: Offset needed to return a specific subset of friends.
        :param order: Sort order: , 'name' - by name (enabled only if the 'fields' parameter is used), 'hints' - by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param ref:
        :param user_id: User ID. By default, the current user ID.
        """

        return await self._call(
            "friends.get",
            locals(),
            dependent=((("fields",), GetFieldsResponseModel),),
            default=FriendsGetResponseModel,
        )

    async def get_app_users(
        self,
    ) -> list[int]:
        """Method `friends.getAppUsers()`"""

        return await self._call("friends.getAppUsers", locals(), list[int])

    async def get_lists(
        self,
        return_system: bool | None = None,
        user_id: int | None = None,
    ) -> FriendsGetListsResponseModel:
        """Method `friends.getLists()`

        :param return_system: '1' - to return system friend lists. By default: '0'.
        :param user_id: User ID.
        """

        return await self._call("friends.getLists", locals(), FriendsGetListsResponseModel)










    async def get_recent(
        self,
        count: int | None = None,
    ) -> list[int]:
        """Method `friends.getRecent()`

        :param count: Number of recently added friends to return.
        """

        return await self._call("friends.getRecent", locals(), list[int])





    async def get_suggestions(
        self,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        filter: list[typing.Literal["contacts", "mutual", "mutual_contacts"]] | None = None,
        name_case: str | None = None,
        offset: int | None = None,
    ) -> GetSuggestionsResponseModel:
        """Method `friends.getSuggestions()`

        :param count: Number of suggestions to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param filter: Types of potential friends to return: 'mutual' - users with many mutual friends , 'contacts' - users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' - users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param name_case: Case for declension of user name and surname: , 'nom' - nominative (default) , 'gen' - genitive , 'dat' - dative , 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of suggestions.
        """

        return await self._call("friends.getSuggestions", locals(), GetSuggestionsResponseModel)

    async def search(
        self,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        q: str | None = None,
        user_id: int | None = None,
    ) -> FriendsSearchResponseModel:
        """Method `friends.search()`

        :param count: Number of friends to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of friends.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param user_id: User ID.
        """

        return await self._call("friends.search", locals(), FriendsSearchResponseModel)
    def __init__(self, api: "typing.Any") -> None:
        super().__init__(api)

    @typing.overload
    async def get_mutual(
        self,
        *,
        total_count: int,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> "MutualFriend": ...

    @typing.overload
    async def get_mutual(
        self,
        *,
        target_uids: list[int],
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> list[MutualFriend]: ...

    @typing.overload
    async def get_mutual(
        self,
        *,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> list[int]: ...

    async def get_mutual(
        self,
        *,
        target_uids: list[int] | None = None,
        total_count: int | None = None,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> MutualFriend | list[int] | list[MutualFriend]:
        """Method `friends.getMutual()`

        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param count: Number of mutual friends to return.
        :param need_common_count: Return mutual friends total count
        :param offset: Offset needed to return a specific subset of mutual friends.
        :param order: Sort order: 'random' - random order
        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        """

        return await self._call(
            "friends.getMutual",
            locals(),
            dependent=( (("target_uids",), list[MutualFriend]), (("total_count",), MutualFriend), ),
            default=list[int],
        )

    @typing.overload
    async def get_online(
        self,
        *,
        online_mobile: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> GetOnlineOnlineMobileResponseModel: ...

    @typing.overload
    async def get_online(
        self,
        *,
        extended: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> "OnlineUsers": ...

    @typing.overload
    async def get_online(
        self,
        *,
        online_mobile_extended: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        online_mobile: bool | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> "OnlineUsersWithMobile": ...

    @typing.overload
    async def get_online(
        self,
        *,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> list[int]: ...

    async def get_online(
        self,
        *,
        online_mobile: bool | None = None,
        extended: bool | None = None,
        online_mobile_extended: bool | None = None,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> OnlineUsersWithMobile | list[int] | GetOnlineOnlineMobileResponseModel | OnlineUsers:
        """Method `friends.getOnline()`

        :param online_mobile: '1' - to return an additional 'online_mobile' field, '0' - (default),
        :param count: Number of friends to return.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param offset: Offset needed to return a specific subset of friends.
        :param order: Sort order: 'random' - random order
        :param user_id: User ID.
        """

        return await self._call(
            "friends.getOnline",
            locals(),
            dependent=( (("online_mobile",), GetOnlineOnlineMobileResponseModel), (("extended",), OnlineUsers), (("online_mobile_extended",), OnlineUsersWithMobile), ),
            default=list[int],
        )

    @typing.overload
    async def get_requests(
        self,
        *,
        need_mutual: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> GetRequestsNeedMutualResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        *,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> GetRequestsExtendedResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        *,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> FriendsGetRequestsResponseModel: ...

    async def get_requests(
        self,
        *,
        need_mutual: bool | None = None,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> GetRequestsNeedMutualResponseModel | FriendsGetRequestsResponseModel | GetRequestsExtendedResponseModel:
        """Method `friends.getRequests()`

        :param need_mutual: '1' - to return a list of mutual friends (up to 20), if any
        :param extended: '1' - to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param fields:
        :param need_viewed:
        :param offset: Offset needed to return a specific subset of friend requests.
        :param out: '1' - to return outgoing requests, '0' - to return incoming requests (default)
        :param ref:
        :param sort: Sort order: '1' - by number of mutual friends, '0' - by date
        :param suggested: '1' - to return a list of suggested friends, '0' - to return friend requests (default)
        """

        return await self._call(
            "friends.getRequests",
            locals(),
            dependent=( (("need_mutual",), GetRequestsNeedMutualResponseModel), (("extended",), GetRequestsExtendedResponseModel), ),
            default=FriendsGetRequestsResponseModel,
        )


__all__ = ("FriendsCategory",)
