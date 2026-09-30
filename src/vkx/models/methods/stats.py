
from ..objects import *
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class StatsCategory(BaseCategory):
    async def get(
        self,
        app_id: int | None = None,
        extended: bool | None = None,
        filters: list[str] | None = None,
        group_id: int | None = None,
        interval: str | None = None,
        intervals_count: int | None = None,
        stats_groups: list[str] | None = None,
        timestamp_from: float | None = None,
        timestamp_to: float | None = None,
    ) -> list[Period]:
        """Method `stats.get()`

        :param app_id: Application ID.
        :param extended:
        :param filters:
        :param group_id: Community ID.
        :param interval:
        :param intervals_count:
        :param stats_groups:
        :param timestamp_from:
        :param timestamp_to:
        """

        return await self._call("stats.get", locals(), list[Period])

    async def get_post_reach(
        self,
        owner_id: int,
        post_ids: list[int],
    ) -> list[WallpostStat]:
        """Method `stats.getPostReach()`

        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """

        return await self._call("stats.getPostReach", locals(), list[WallpostStat])

    async def track_visitor(
        self,
        type: str | None = None,
    ) -> OkResponseModel:
        """Method `stats.trackVisitor()`

        :param type:
        """

        return await self._call("stats.trackVisitor", locals(), OkResponseModel)


__all__ = ("StatsCategory",)
