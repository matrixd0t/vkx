
from ..objects import *
from ..responses.gifts import *  # type: ignore
from .base_category import BaseCategory


class GiftsCategory(BaseCategory):
    async def get(
        self,
        count: int | None = None,
        offset: int | None = None,
        user_id: int | None = None,
    ) -> GiftsGetResponseModel:
        """Method `gifts.get()`

        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        :param user_id: User ID.
        """

        return await self._call("gifts.get", locals(), GiftsGetResponseModel)


__all__ = ("GiftsCategory",)
