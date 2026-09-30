from ..responses.auth import *  # type: ignore
from .base_category import BaseCategory


class AuthCategory(BaseCategory):
    async def restore(
        self,
        last_name: str,
        phone: str,
    ) -> RestoreResponseModel:
        """Method `auth.restore()`

        :param last_name: User last name.
        :param phone: User phone number.
        """

        return await self._call("auth.restore", locals(), RestoreResponseModel)


__all__ = ("AuthCategory",)
