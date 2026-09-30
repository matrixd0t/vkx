from ..responses.search import *  # type: ignore
from .base_category import BaseCategory


class SearchCategory(BaseCategory):
    async def get_hints(
        self,
        fields: list[str] | None = None,
        filters: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        q: str | None = None,
        search_global: bool | None = None,
    ) -> GetHintsResponseModel:
        """Method `search.getHints()`

        :param fields:
        :param filters:
        :param limit: Maximum number of results to return.
        :param offset: Offset for querying specific result subset
        :param q: Search query string.
        :param search_global:
        """

        return await self._call("search.getHints", locals(), GetHintsResponseModel)


__all__ = ("SearchCategory",)
