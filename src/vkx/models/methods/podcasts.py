from ..responses.podcasts import *  # type: ignore
from .base_category import BaseCategory


class PodcastsCategory(BaseCategory):
    async def search_podcast(
        self,
        search_string: str,
        count: int | None = None,
        offset: int | None = None,
    ) -> SearchPodcastResponseModel:
        """Method `podcasts.searchPodcast()`

        :param search_string:
        :param count:
        :param offset:
        """

        return await self._call("podcasts.searchPodcast", locals(), SearchPodcastResponseModel)


__all__ = ("PodcastsCategory",)
