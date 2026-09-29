
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.base import (
    OkResponseModel,
)
from vkx.models.responses.calls import *  # type: ignore


class CallsCategory(BaseCategory):
    async def force_finish(
        self,
        call_id: str,
    ) -> OkResponseModel:
        """Method `calls.forceFinish()`

        :param call_id:
        """

        return await self._call("calls.forceFinish", locals(), OkResponseModel)

    async def start(
        self,
        group_id: int | None = None,
    ) -> StartResponseModel:
        """Method `calls.start()`

        :param group_id:
        """

        return await self._call("calls.start", locals(), StartResponseModel)


__all__ = ("CallsCategory",)
