
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.pretty_cards import *  # type: ignore


class PrettyCardsCategory(BaseCategory):
    async def create(
        self,
        link: str,
        owner_id: int,
        photo: str,
        title: str,
        button: str | None = None,
        price: str | None = None,
        price_old: str | None = None,
    ) -> PrettyCardsCreateResponseModel:
        """Method `prettyCards.create()`

        :param link:
        :param owner_id:
        :param photo:
        :param title:
        :param button:
        :param price:
        :param price_old:
        """

        return await self._call("prettyCards.create", locals(), PrettyCardsCreateResponseModel)

    async def delete(
        self,
        card_id: int,
        owner_id: int,
    ) -> PrettyCardsDeleteResponseModel:
        """Method `prettyCards.delete()`

        :param card_id:
        :param owner_id:
        """

        return await self._call("prettyCards.delete", locals(), PrettyCardsDeleteResponseModel)

    async def edit(
        self,
        card_id: int,
        owner_id: int,
        button: str | None = None,
        link: str | None = None,
        photo: str | None = None,
        price: str | None = None,
        price_old: str | None = None,
        title: str | None = None,
    ) -> PrettyCardsEditResponseModel:
        """Method `prettyCards.edit()`

        :param card_id:
        :param owner_id:
        :param button:
        :param link:
        :param photo:
        :param price:
        :param price_old:
        :param title:
        """

        return await self._call("prettyCards.edit", locals(), PrettyCardsEditResponseModel)

    async def get(
        self,
        owner_id: int,
        count: int | None = None,
        offset: int | None = None,
    ) -> PrettyCardsGetResponseModel:
        """Method `prettyCards.get()`

        :param owner_id:
        :param count:
        :param offset:
        """

        return await self._call("prettyCards.get", locals(), PrettyCardsGetResponseModel)

    async def get_by_id(
        self,
        card_ids: list[int],
        owner_id: int,
    ) -> list[PrettyCardOrError]:
        """Method `prettyCards.getById()`

        :param card_ids:
        :param owner_id:
        """

        return await self._call("prettyCards.getById", locals(), list[PrettyCardOrError])

    async def get_upload_url(
        self,
    ) -> str:
        """Method `prettyCards.getUploadURL()`"""

        return await self._call("prettyCards.getUploadURL", locals(), str)


__all__ = ("PrettyCardsCategory",)
