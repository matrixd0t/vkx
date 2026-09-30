from ..responses.base import OkResponseModel
from ..responses.calls import *  # type: ignore
from .base_category import BaseCategory


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
