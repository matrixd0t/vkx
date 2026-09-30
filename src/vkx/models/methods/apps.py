from ..objects import *
from ..responses.apps import *  # type: ignore
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class AppsCategory(BaseCategory):
    async def add_snippet(
        self,
        button: str | None = None,
        description: str | None = None,
        group_id: list[int] | None = None,
        hash: list[str] | None = None,
        image_url: str | None = None,
        small_image_url: str | None = None,
        snippet_id: int | None = None,
        title: str | None = None,
        vk_ref: list[typing.Literal["snippet_im", "snippet_post"]] | None = None,
    ) -> AddSnippetResponseModel:
        """Method `apps.addSnippet()`

        :param button:
        :param description:
        :param group_id:
        :param hash:
        :param image_url:
        :param small_image_url:
        :param snippet_id:
        :param title:
        :param vk_ref:
        """

        return await self._call("apps.addSnippet", locals(), AddSnippetResponseModel)

    async def add_users_to_testing_group(
        self,
        group_id: int,
        user_ids: list[int],
    ) -> bool:
        """Method `apps.addUsersToTestingGroup()`

        :param group_id:
        :param user_ids:
        """

        return await self._call("apps.addUsersToTestingGroup", locals(), bool)

    async def delete_app_requests(
        self,
    ) -> OkResponseModel:
        """Method `apps.deleteAppRequests()`"""

        return await self._call("apps.deleteAppRequests", locals(), OkResponseModel)

    async def delete_snippet(
        self,
        id: int | None = None,
    ) -> OkResponseModel:
        """Method `apps.deleteSnippet()`

        :param id:
        """

        return await self._call("apps.deleteSnippet", locals(), OkResponseModel)

    async def get(
        self,
        app_fields: list[AppFields] | None = None,
        app_id: int | None = None,
        app_ids: list[int] | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        name_case: str | None = None,
        platform: str | None = None,
        return_friends: bool | None = None,
    ) -> AppsGetResponseModel:
        """Method `apps.get()`

        :param app_fields: List of app fields to return. Fields 'id', 'type' and 'title' will always be in response. Leave this field empty to get all fields
        :param app_id: Application ID
        :param app_ids: List of application ID
        :param extended:
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default),, 'gen' - genitive,, 'dat' - dative,, 'acc' - accusative,, 'ins' - instrumental,, 'abl' - prepositional. (only if 'return_friends' = '1')
        :param platform: platform. Possible values: *'ios' - iOS,, *'android' - Android,, *'winphone' - Windows Phone,, *'web' - приложения на vk.com. By default: 'web'.
        :param return_friends:
        """

        return await self._call("apps.get", locals(), AppsGetResponseModel)

    async def get_catalog(
        self,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        filter: str | None = None,
        genre_id: int | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        platform: str | None = None,
        q: str | None = None,
        return_friends: bool | None = None,
        sort: str | None = None,
    ) -> "CatalogList":
        """Method `apps.getCatalog()`

        :param count: Number of apps to return.
        :param extended: '1' - to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' - not to return additional fields (default).
        :param fields:
        :param filter: 'installed' - to return list of installed apps (only for mobile platform).
        :param genre_id:
        :param name_case:
        :param offset: Offset required to return a specific subset of apps.
        :param platform:
        :param q: Search query string.
        :param return_friends:
        :param sort: Sort order: 'popular_today' - popular for one day (default), 'visitors' - by visitors number , 'create_date' - by creation date, 'growth_rate' - by growth rate, 'popular_week' - popular for one week
        """

        return await self._call("apps.getCatalog", locals(), CatalogList)

    @typing.overload
    async def get_friends_list(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        query: str | None = None,
        type: str | None = None,
    ) -> GetFriendsListExtendedResponseModel: ...

    @typing.overload
    async def get_friends_list(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        query: str | None = None,
        type: str | None = None,
    ) -> GetFriendsListResponseModel: ...

    async def get_friends_list(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        query: str | None = None,
        type: str | None = None,
    ) -> GetFriendsListResponseModel | GetFriendsListExtendedResponseModel:
        """Method `apps.getFriendsList()`

        :param extended:
        :param count: List size.
        :param fields: Additional profile fields, see [vk.com/dev/fields|description].
        :param offset:
        :param query: Search query string (e.g., 'Vasya Babich').
        :param type: List type. Possible values: * 'invite' - available for invites (don't play the game),, * 'request' - available for request (play the game). By default: 'invite'.
        """

        return await self._call(
            "apps.getFriendsList",
            locals(),
            dependent=((("extended",), GetFriendsListExtendedResponseModel),),
            default=GetFriendsListResponseModel,
        )

    @typing.overload
    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Literal[True],
        global_: bool | None = None,
    ) -> GetLeaderboardExtendedResponseModel: ...

    @typing.overload
    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Literal[False] | None = None,
        global_: bool | None = None,
    ) -> GetLeaderboardResponseModel: ...

    async def get_leaderboard(
        self,
        type: str,
        extended: bool | None = None,
        global_: bool | None = None,
    ) -> GetLeaderboardResponseModel | GetLeaderboardExtendedResponseModel:
        """Method `apps.getLeaderboard()`

        :param type: Leaderboard type. Possible values: *'level' - by level,, *'points' - by mission points,, *'score' - by score ().
        :param extended: 1 - to return additional info about users
        :param global: Rating type. Possible values: *'1' - global rating among all players,, *'0' - rating among user friends.
        """

        return await self._call(
            "apps.getLeaderboard",
            locals(),
            dependent=((("extended",), GetLeaderboardExtendedResponseModel),),
            default=GetLeaderboardResponseModel,
        )

    async def get_mini_app_policies(
        self,
        app_id: int,
    ) -> GetMiniAppPoliciesResponseModel:
        """Method `apps.getMiniAppPolicies()`

        :param app_id: Mini App ID
        """

        return await self._call("apps.getMiniAppPolicies", locals(), GetMiniAppPoliciesResponseModel)

    async def get_scopes(
        self,
        type: str | None = None,
    ) -> GetScopesResponseModel:
        """Method `apps.getScopes()`

        :param type:
        """

        return await self._call("apps.getScopes", locals(), GetScopesResponseModel)

    async def get_score(
        self,
        user_id: int | None = None,
    ) -> int:
        """Method `apps.getScore()`

        :param user_id:
        """

        return await self._call("apps.getScore", locals(), int)

    async def get_snippets(
        self,
    ) -> GetSnippetsResponseModel:
        """Method `apps.getSnippets()`"""

        return await self._call("apps.getSnippets", locals(), GetSnippetsResponseModel)

    async def get_testing_groups(
        self,
        group_id: int | None = None,
    ) -> list[TestingGroup]:
        """Method `apps.getTestingGroups()`

        :param group_id:
        """

        return await self._call("apps.getTestingGroups", locals(), list[TestingGroup])

    async def is_notifications_allowed(
        self,
        user_id: int | None = None,
    ) -> IsNotificationsAllowedResponseModel:
        """Method `apps.isNotificationsAllowed()`

        :param user_id:
        """

        return await self._call("apps.isNotificationsAllowed", locals(), IsNotificationsAllowedResponseModel)

    async def promo_has_active_gift(
        self,
        promo_id: int,
        user_id: int | None = None,
    ) -> bool:
        """Method `apps.promoHasActiveGift()`

        :param promo_id: Id of game promo action
        :param user_id:
        """

        return await self._call("apps.promoHasActiveGift", locals(), bool)

    async def promo_use_gift(
        self,
        promo_id: int,
        user_id: int | None = None,
    ) -> bool:
        """Method `apps.promoUseGift()`

        :param promo_id: Id of game promo action
        :param user_id:
        """

        return await self._call("apps.promoUseGift", locals(), bool)

    async def remove_testing_group(
        self,
        group_id: int,
    ) -> bool:
        """Method `apps.removeTestingGroup()`

        :param group_id:
        """

        return await self._call("apps.removeTestingGroup", locals(), bool)

    async def remove_users_from_testing_groups(
        self,
        user_ids: list[int],
    ) -> bool:
        """Method `apps.removeUsersFromTestingGroups()`

        :param user_ids:
        """

        return await self._call("apps.removeUsersFromTestingGroups", locals(), bool)

    async def send_request(
        self,
        user_id: int,
        key: str | None = None,
        name: str | None = None,
        separate: bool | None = None,
        text: str | None = None,
        type: str | None = None,
    ) -> int:
        """Method `apps.sendRequest()`

        :param user_id: id of the user to send a request
        :param key: special string key to be sent with the request
        :param name:
        :param separate:
        :param text: request text
        :param type: request type. Values: 'invite' - if the request is sent to a user who does not have the app installed,, 'request' - if a user has already installed the app
        """

        return await self._call("apps.sendRequest", locals(), int)

    async def update_meta_for_testing_group(
        self,
        name: str,
        platforms: list[typing.Literal["mobile", "web", "mvk"]],
        webview: str,
        group_id: int | None = None,
        user_ids: list[int] | None = None,
    ) -> CreatedGroupResponseModel:
        """Method `apps.updateMetaForTestingGroup()`

        :param name:
        :param platforms:
        :param webview:
        :param group_id:
        :param user_ids:
        """

        return await self._call("apps.updateMetaForTestingGroup", locals(), CreatedGroupResponseModel)


__all__ = ("AppsCategory",)
