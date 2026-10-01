import typing

from ..objects import *
from ..objects import DomainResolved
from ..responses.base import OkResponseModel
from ..responses.utils import *  # type: ignore
from .base_category import BaseCategory


class UtilsCategory(BaseCategory):
    async def check_link(
        self,
        url: str,
    ) -> "LinkChecked":
        """Method `utils.checkLink()`

        :param url: Link to check (e.g., 'http://google.com').
        """

        return await self._call("utils.checkLink", locals(), LinkChecked)

    async def delete_from_last_shortened(
        self,
        key: str,
    ) -> OkResponseModel:
        """Method `utils.deleteFromLastShortened()`

        :param key: Link key (characters after vk.cc/).
        """

        return await self._call("utils.deleteFromLastShortened", locals(), OkResponseModel)

    async def get_last_shortened_links(
        self,
        count: int | None = None,
        offset: int | None = None,
    ) -> GetLastShortenedLinksResponseModel:
        """Method `utils.getLastShortenedLinks()`

        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """

        return await self._call("utils.getLastShortenedLinks", locals(), GetLastShortenedLinksResponseModel)

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        extended: typing.Literal[True],
        access_key: str | None = None,
        interval: str | None = None,
        intervals_count: int | None = None,
        source: str | None = None,
    ) -> "LinkStatsExtended": ...

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        extended: typing.Literal[False] | None = None,
        access_key: str | None = None,
        interval: str | None = None,
        intervals_count: int | None = None,
        source: str | None = None,
    ) -> "LinkStats": ...

    async def get_link_stats(
        self,
        key: str,
        extended: bool | None = None,
        access_key: str | None = None,
        interval: str | None = None,
        intervals_count: int | None = None,
        source: str | None = None,
    ) -> "LinkStatsExtended | LinkStats":
        """Method `utils.getLinkStats()`

        :param key: Link key (characters after vk.cc/).
        :param extended: 1 - to return extended stats data (sex, age, geo). 0 - to return views number only.
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param source: Source of scope
        """

        return await self._call(
            "utils.getLinkStats",
            locals(),
            dependent=((("extended",), LinkStatsExtended),),
            default=LinkStats,
        )

    async def get_server_time(
        self,
    ) -> int:
        """Method `utils.getServerTime()`"""

        return await self._call("utils.getServerTime", locals(), int)

    async def get_short_link(
        self,
        url: str,
        private: bool | None = None,
    ) -> "ShortLink":
        """Method `utils.getShortLink()`

        :param url: URL to be shortened.
        :param private: 1 - private stats, 0 - public stats.
        """

        return await self._call("utils.getShortLink", locals(), ShortLink)

    async def resolve_screen_name(  # type: ignore
        self,
        screen_name: str,
    ) -> DomainResolved | list[typing.Any]:
        """Method `utils.resolveScreenName()`

        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """

        return await self._call("utils.resolveScreenName", locals(), DomainResolved | list[typing.Any])


__all__ = ("UtilsCategory",)


__all__ = ("UtilsCategory",)
