import typing

from ..objects import *
from ..responses.account import *  # type: ignore
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class AccountCategory(BaseCategory):
    async def ban(
        self,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `account.ban()`

        :param owner_id:
        """

        return await self._call("account.ban", locals(), OkResponseModel)

    async def change_password(
        self,
        new_password: str,
        change_password_hash: str | None = None,
        old_password: str | None = None,
        restore_sid: str | None = None,
    ) -> ChangePasswordResponseModel:
        """Method `account.changePassword()`

        :param new_password: New password that will be set as a current
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        :param restore_sid: Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        """

        return await self._call("account.changePassword", locals(), ChangePasswordResponseModel)

    async def get_active_offers(
        self,
        count: int | None = None,
        offset: int | None = None,
    ) -> GetActiveOffersResponseModel:
        """Method `account.getActiveOffers()`

        :param count: Number of results to return.
        :param offset:
        """

        return await self._call("account.getActiveOffers", locals(), GetActiveOffersResponseModel)

    async def get_app_permissions(
        self,
        user_id: int | None = None,
    ) -> int:
        """Method `account.getAppPermissions()`

        :param user_id: User ID whose settings information shall be got. By default: current user.
        """

        return await self._call("account.getAppPermissions", locals(), int)

    async def get_banned(
        self,
        count: int | None = None,
        fields: list[UserGroupFields] | None = None,
        offset: int | None = None,
    ) -> AccountGetBannedResponseModel:
        """Method `account.getBanned()`

        :param count: Number of results to return.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        return await self._call("account.getBanned", locals(), AccountGetBannedResponseModel)

    async def get_counters(
        self,
        filter: list[str] | None = None,
    ) -> "AccountCounters":
        """Method `account.getCounters()`

        :param filter: Counters to be returned.
        """

        return await self._call("account.getCounters", locals(), AccountCounters)

    async def get_info(
        self,
        fields: list[typing.Literal["country", "https_required", "own_posts_default", "no_wall_replies", "intro", "lang", "audio_autoplay"]]
        | None = None,
    ) -> "AccountInfo":
        """Method `account.getInfo()`

        :param fields: Fields to return. Possible values: *'country' - user country,, *'https_required' - is "HTTPS only" option enabled,, *'own_posts_default' - is "Show my posts only" option is enabled,, *'no_wall_replies' - are wall replies disabled or not,, *'intro' - is intro passed by user or not,, *'lang' - user language. By default: all.
        """

        return await self._call("account.getInfo", locals(), AccountInfo)

    async def get_profile_info(
        self,
    ) -> "UserSettings":
        """Method `account.getProfileInfo()`"""

        return await self._call("account.getProfileInfo", locals(), UserSettings)

    async def get_push_settings(
        self,
        device_id: str | None = None,
    ) -> "AccountPushSettings":
        """Method `account.getPushSettings()`

        :param device_id: Unique device ID.
        """

        return await self._call("account.getPushSettings", locals(), AccountPushSettings)

    async def register_device(
        self,
        device_id: str,
        token: str,
        device_model: str | None = None,
        device_year: int | None = None,
        pushes_granted: bool | None = None,
        sandbox: bool | None = None,
        settings: str | None = None,
        system_version: str | None = None,
    ) -> OkResponseModel:
        """Method `account.registerDevice()`

        :param device_id: Unique device ID.
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param pushes_granted:
        :param sandbox:
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param system_version: String version of device operating system.
        """

        return await self._call("account.registerDevice", locals(), OkResponseModel)

    async def save_profile_info(
        self,
        bdate: str | None = None,
        bdate_visibility: int | None = None,
        cancel_request_id: int | None = None,
        city_id: int | None = None,
        country_id: int | None = None,
        first_name: str | None = None,
        home_town: str | None = None,
        last_name: str | None = None,
        maiden_name: str | None = None,
        relation: int | None = None,
        relation_partner_id: int | None = None,
        screen_name: str | None = None,
        sex: int | None = None,
        status: str | None = None,
    ) -> SaveProfileInfoResponseModel:
        """Method `account.saveProfileInfo()`

        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' - show birth date,, * '2' - show only month and day,, * '0' - hide birth date.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param city_id: User city.
        :param country_id: User country.
        :param first_name: User first name.
        :param home_town: User home town.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param relation: User relationship status. Possible values: , * '1' - single,, * '2' - in a relationship,, * '3' - engaged,, * '4' - married,, * '5' - it's complicated,, * '6' - actively searching,, * '7' - in love,, * '0' - not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param screen_name: User screen name.
        :param sex: User sex. Possible values: , * '1' - female,, * '2' - male.
        :param status: Status text.
        """

        return await self._call("account.saveProfileInfo", locals(), SaveProfileInfoResponseModel)

    async def set_info(
        self,
        name: str | None = None,
        value: str | None = None,
    ) -> OkResponseModel:
        """Method `account.setInfo()`

        :param name: Setting name.
        :param value: Setting value.
        """

        return await self._call("account.setInfo", locals(), OkResponseModel)

    async def set_offline(
        self,
    ) -> OkResponseModel:
        """Method `account.setOffline()`"""

        return await self._call("account.setOffline", locals(), OkResponseModel)

    async def set_online(
        self,
        voip: bool | None = None,
    ) -> OkResponseModel:
        """Method `account.setOnline()`

        :param voip: '1' if videocalls are available for current device.
        """

        return await self._call("account.setOnline", locals(), OkResponseModel)

    async def set_push_settings(
        self,
        device_id: str,
        key: str | None = None,
        settings: str | None = None,
        value: list[str] | None = None,
    ) -> OkResponseModel:
        """Method `account.setPushSettings()`

        :param device_id: Unique device ID.
        :param key: Notification key.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param value: New value for the key in a [vk.com/dev/push_settings|special format].
        """

        return await self._call("account.setPushSettings", locals(), OkResponseModel)

    async def set_silence_mode(
        self,
        device_id: str | None = None,
        peer_id: int | None = None,
        sound: int | None = None,
        time: int | None = None,
    ) -> OkResponseModel:
        """Method `account.setSilenceMode()`

        :param device_id: Unique device ID.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' - to enable sound in this dialog, '0' - to disable sound. Only if 'peer_id' contains user or community ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        """

        return await self._call("account.setSilenceMode", locals(), OkResponseModel)

    async def unban(
        self,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `account.unban()`

        :param owner_id:
        """

        return await self._call("account.unban", locals(), OkResponseModel)

    async def unregister_device(
        self,
        device_id: str | None = None,
        sandbox: bool | None = None,
    ) -> OkResponseModel:
        """Method `account.unregisterDevice()`

        :param device_id: Unique device ID.
        :param sandbox:
        """

        return await self._call("account.unregisterDevice", locals(), OkResponseModel)


__all__ = ("AccountCategory",)
