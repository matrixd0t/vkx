
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.auth import *  # type: ignore


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
