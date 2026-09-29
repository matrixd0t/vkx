
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.base import (
    OkResponseModel,
)


class StatusCategory(BaseCategory):
    async def get(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
    ) -> "Status":
        """Method `status.get()`

        :param group_id:
        :param user_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        return await self._call("status.get", locals(), Status)

    async def set(
        self,
        group_id: int | None = None,
        text: str | None = None,
    ) -> OkResponseModel:
        """Method `status.set()`

        :param group_id: Identifier of a community to set a status in. If left blank the status is set to current user.
        :param text: Text of the new status.
        """

        return await self._call("status.set", locals(), OkResponseModel)


__all__ = ("StatusCategory",)
