from ..objects import *
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class StorageCategory(BaseCategory):
    async def get(
        self,
        key: str | None = None,
        keys: list[str] | None = None,
        user_id: int | None = None,
    ) -> list[Value]:
        """Method `storage.get()`

        :param key:
        :param keys:
        :param user_id:
        """

        return await self._call("storage.get", locals(), list[Value])

    async def get_keys(
        self,
        count: int | None = None,
        offset: int | None = None,
        user_id: int | None = None,
    ) -> list[str]:
        """Method `storage.getKeys()`

        :param count: amount of variable names the info needs to be collected from.
        :param offset:
        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        """

        return await self._call("storage.getKeys", locals(), list[str])

    async def set(
        self,
        key: str,
        user_id: int | None = None,
        value: str | None = None,
    ) -> OkResponseModel:
        """Method `storage.set()`

        :param key:
        :param user_id:
        :param value:
        """

        return await self._call("storage.set", locals(), OkResponseModel)


__all__ = ("StorageCategory",)
