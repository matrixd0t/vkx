import typing

from ..objects import *
from ..objects import SetCounterItem
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class SecureCategory(BaseCategory):
    async def add_app_event(
        self,
        activity_id: int,
        user_id: int | None = None,
        value: int | None = None,
    ) -> OkResponseModel:
        """Method `secure.addAppEvent()`

        :param activity_id: there are 2 default activities: , * 1 - level. Works similar to ,, * 2 - points, saves points amount, Any other value is for saving completed missions
        :param user_id: ID of a user to save the data
        :param value: depends on activity_id: * 1 - number, current level number,, * 2 - number, current user's points amount, , Any other value is ignored
        """

        return await self._call("secure.addAppEvent", locals(), OkResponseModel)

    async def check_token(
        self,
        ip: str | None = None,
        token: str | None = None,
    ) -> "TokenChecked":
        """Method `secure.checkToken()`

        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        :param token: client 'access_token'
        """

        return await self._call("secure.checkToken", locals(), TokenChecked)

    async def get_app_balance(
        self,
    ) -> int:
        """Method `secure.getAppBalance()`"""

        return await self._call("secure.getAppBalance", locals(), int)

    async def get_smshistory(
        self,
        date_from: int | None = None,
        date_to: int | None = None,
        limit: int | None = None,
        user_id: int | None = None,
    ) -> list[SmsNotification]:
        """Method `secure.getSMSHistory()`

        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default - 1000.
        :param user_id:
        """

        return await self._call("secure.getSMSHistory", locals(), list[SmsNotification])

    async def get_transactions_history(
        self,
        date_from: int | None = None,
        date_to: int | None = None,
        limit: int | None = None,
        type: int | None = None,
        uid_from: int | None = None,
        uid_to: int | None = None,
    ) -> list[Transaction]:
        """Method `secure.getTransactionsHistory()`

        :param date_from:
        :param date_to:
        :param limit:
        :param type:
        :param uid_from:
        :param uid_to:
        """

        return await self._call("secure.getTransactionsHistory", locals(), list[Transaction])

    async def get_user_level(
        self,
        user_ids: list[int],
    ) -> list[Level]:
        """Method `secure.getUserLevel()`

        :param user_ids:
        """

        return await self._call("secure.getUserLevel", locals(), list[Level])

    async def give_event_sticker(
        self,
        achievement_id: int,
        user_ids: list[int],
    ) -> list[GiveEventStickerItem]:
        """Method `secure.giveEventSticker()`

        :param achievement_id:
        :param user_ids:
        """

        return await self._call("secure.giveEventSticker", locals(), list[GiveEventStickerItem])

    async def send_notification(
        self,
        message: str,
        notification_id: int | None = None,
        promo_id: int | None = None,
        user_id: int | None = None,
        user_ids: list[int] | None = None,
    ) -> list[int]:
        """Method `secure.sendNotification()`

        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param notification_id:
        :param promo_id:
        :param user_id:
        :param user_ids:
        """

        return await self._call("secure.sendNotification", locals(), list[int])

    async def send_smsnotification(
        self,
        message: str,
        user_id: int,
    ) -> OkResponseModel:
        """Method `secure.sendSMSNotification()`

        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        """

        return await self._call("secure.sendSMSNotification", locals(), OkResponseModel)

    def __init__(self, api: "typing.Any") -> None:
        super().__init__(api)

    async def set_counter(  # type: ignore
        self,
        counters: list[str] | None = None,
        user_id: int | None = None,
        counter: int | None = None,
        increment: bool | None = None,
    ) -> int | list["SetCounterItem"]:
        """Sets a counter which is shown to the user in bold in the left menu.

        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """

        return await self._call("secure.setCounter", locals(), list[SetCounterItem] if counters and counters.count(",") > 0 else int)


__all__ = ("SecureCategory",)


__all__ = ("SecureCategory",)
