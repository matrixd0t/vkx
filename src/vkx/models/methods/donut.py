from ..objects import *
from ..responses.donut import *  # type: ignore
from .base_category import BaseCategory


class DonutCategory(BaseCategory):
    async def get_friends(
        self,
        owner_id: int,
        count: int | None = None,
        fields: list[str] | None = None,
        offset: int | None = None,
    ) -> GetMembersFieldsResponseModel:
        """Method `donut.getFriends()`

        :param owner_id:
        :param count:
        :param fields:
        :param offset:
        """

        return await self._call("donut.getFriends", locals(), GetMembersFieldsResponseModel)

    async def get_subscription(
        self,
        owner_id: int,
    ) -> "DonatorSubscriptionInfo":
        """Method `donut.getSubscription()`

        :param owner_id:
        """

        return await self._call("donut.getSubscription", locals(), DonatorSubscriptionInfo)

    async def get_subscriptions(
        self,
        count: int | None = None,
        fields: list[UserGroupFields] | None = None,
        offset: int | None = None,
    ) -> DonutGetSubscriptionsResponseModel:
        """Method `donut.getSubscriptions()`

        :param count:
        :param fields:
        :param offset:
        """

        return await self._call("donut.getSubscriptions", locals(), DonutGetSubscriptionsResponseModel)

    async def is_don(
        self,
        owner_id: int,
    ) -> bool:
        """Method `donut.isDon()`

        :param owner_id:
        """

        return await self._call("donut.isDon", locals(), bool)


__all__ = ("DonutCategory",)
