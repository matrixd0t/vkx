
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.streaming import *  # type: ignore


class StreamingCategory(BaseCategory):
    async def get_server_url(
        self,
    ) -> GetServerUrlResponseModel:
        """Method `streaming.getServerUrl()`"""

        return await self._call("streaming.getServerUrl", locals(), GetServerUrlResponseModel)

    async def get_stats(
        self,
        end_time: int | None = None,
        interval: str | None = None,
        start_time: int | None = None,
        type: str | None = None,
    ) -> list[StreamingStats]:
        """Method `streaming.getStats()`

        :param end_time:
        :param interval:
        :param start_time:
        :param type:
        """

        return await self._call("streaming.getStats", locals(), list[StreamingStats])

    async def get_stem(
        self,
        word: str,
    ) -> GetStemResponseModel:
        """Method `streaming.getStem()`

        :param word:
        """

        return await self._call("streaming.getStem", locals(), GetStemResponseModel)


__all__ = ("StreamingCategory",)
