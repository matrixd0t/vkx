from ..responses.downloaded_games import *  # type: ignore
from .base_category import BaseCategory


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
