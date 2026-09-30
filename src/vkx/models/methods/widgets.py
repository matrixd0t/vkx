from ..objects import *
from ..responses.widgets import *  # type: ignore
from .base_category import BaseCategory


class WidgetsCategory(BaseCategory):
    async def get_comments(
        self,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        order: str | None = None,
        page_id: str | None = None,
        url: str | None = None,
        widget_api_id: int | None = None,
    ) -> WidgetsGetCommentsResponseModel:
        """Method `widgets.getComments()`

        :param count:
        :param fields:
        :param offset:
        :param order:
        :param page_id:
        :param url:
        :param widget_api_id:
        """

        return await self._call("widgets.getComments", locals(), WidgetsGetCommentsResponseModel)

    async def get_pages(
        self,
        count: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        period: str | None = None,
        widget_api_id: int | None = None,
    ) -> WidgetsGetPagesResponseModel:
        """Method `widgets.getPages()`

        :param count:
        :param offset:
        :param order:
        :param period:
        :param widget_api_id:
        """

        return await self._call("widgets.getPages", locals(), WidgetsGetPagesResponseModel)


__all__ = ("WidgetsCategory",)
