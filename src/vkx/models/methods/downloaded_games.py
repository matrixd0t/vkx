
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.downloaded_games import *  # type: ignore


class DownloadedGamesCategory(BaseCategory):
    async def get_paid_status(
        self,
        user_id: int | None = None,
    ) -> PaidStatusResponseModel:
        """Method `downloadedGames.getPaidStatus()`

        :param user_id:
        """

        return await self._call("downloadedGames.getPaidStatus", locals(), PaidStatusResponseModel)


__all__ = ("DownloadedGamesCategory",)
