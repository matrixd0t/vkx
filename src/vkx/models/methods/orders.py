from ..objects import *
from ..responses.orders import *  # type: ignore
from .base_category import BaseCategory


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        subscription_id: int,
        user_id: int,
        pending_cancel: bool | None = None,
    ) -> bool:
        """Method `orders.cancelSubscription()`

        :param subscription_id:
        :param user_id:
        :param pending_cancel:
        """

        return await self._call("orders.cancelSubscription", locals(), bool)

    async def change_state(
        self,
        action: str,
        order_id: int,
        app_order_id: int | None = None,
        test_mode: bool | None = None,
    ) -> str:
        """Method `orders.changeState()`

        :param action: action to be done with the order. Available actions: *cancel - to cancel unconfirmed order. *charge - to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund - to cancel confirmed order.
        :param order_id: order ID.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        return await self._call("orders.changeState", locals(), str)

    async def get(
        self,
        count: int | None = None,
        offset: int | None = None,
        test_mode: bool | None = None,
    ) -> list[OrdersOrder]:
        """Method `orders.get()`

        :param count: number of returned orders.
        :param offset:
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        return await self._call("orders.get", locals(), list[OrdersOrder])

    async def get_amount(
        self,
        user_id: int,
        votes: list[str],
    ) -> list[Amount]:
        """Method `orders.getAmount()`

        :param user_id:
        :param votes:
        """

        return await self._call("orders.getAmount", locals(), list[Amount])

    async def get_by_id(
        self,
        order_id: int | None = None,
        order_ids: list[int] | None = None,
        test_mode: bool | None = None,
    ) -> list[OrdersOrder]:
        """Method `orders.getById()`

        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        return await self._call("orders.getById", locals(), list[OrdersOrder])

    async def get_user_subscription_by_id(
        self,
        subscription_id: int,
        user_id: int,
    ) -> "Subscription":
        """Method `orders.getUserSubscriptionById()`

        :param subscription_id:
        :param user_id:
        """

        return await self._call("orders.getUserSubscriptionById", locals(), Subscription)

    async def get_user_subscriptions(
        self,
        user_id: int,
    ) -> GetUserSubscriptionsResponseModel:
        """Method `orders.getUserSubscriptions()`

        :param user_id:
        """

        return await self._call("orders.getUserSubscriptions", locals(), GetUserSubscriptionsResponseModel)


__all__ = ("OrdersCategory",)
