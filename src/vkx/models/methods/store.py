from ..responses.base import OkResponseModel
from ..responses.store import *  # type: ignore
from .base_category import BaseCategory


class StoreCategory(BaseCategory):
    async def add_stickers_to_favorite(
        self,
        sticker_ids: list[int],
    ) -> OkResponseModel:
        """Method `store.addStickersToFavorite()`

        :param sticker_ids: Sticker IDs to be added
        """

        return await self._call("store.addStickersToFavorite", locals(), OkResponseModel)

    async def get_favorite_stickers(
        self,
    ) -> GetFavoriteStickersResponseModel:
        """Method `store.getFavoriteStickers()`"""

        return await self._call("store.getFavoriteStickers", locals(), GetFavoriteStickersResponseModel)

    async def get_products(
        self,
        extended: bool | None = None,
        filters: list[str] | None = None,
        merchant: str | None = None,
        product_ids: list[int] | None = None,
        section: str | None = None,
        type: str | None = None,
    ) -> GetProductsResponseModel:
        """Method `store.getProducts()`

        :param extended:
        :param filters:
        :param merchant:
        :param product_ids:
        :param section:
        :param type:
        """

        return await self._call("store.getProducts", locals(), GetProductsResponseModel)

    async def get_stickers_keywords(
        self,
        aliases: bool | None = None,
        all_products: bool | None = None,
        need_stickers: bool | None = None,
        products_ids: list[int] | None = None,
        stickers_ids: list[int] | None = None,
        vmoji_promo: bool | None = None,
    ) -> GetStickersKeywordsResponseModel:
        """Method `store.getStickersKeywords()`

        :param aliases:
        :param all_products:
        :param need_stickers:
        :param products_ids:
        :param stickers_ids:
        :param vmoji_promo:
        """

        return await self._call("store.getStickersKeywords", locals(), GetStickersKeywordsResponseModel)

    async def remove_stickers_from_favorite(
        self,
        sticker_ids: list[int],
    ) -> OkResponseModel:
        """Method `store.removeStickersFromFavorite()`

        :param sticker_ids: Sticker IDs to be removed
        """

        return await self._call("store.removeStickersFromFavorite", locals(), OkResponseModel)


__all__ = ("StoreCategory",)
