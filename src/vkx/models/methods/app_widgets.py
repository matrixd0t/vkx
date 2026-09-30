from ..objects import *
from ..responses.app_widgets import *  # type: ignore
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class AppWidgetsCategory(BaseCategory):
    async def get_app_image_upload_server(
        self,
        image_type: str,
    ) -> GetAppImageUploadServerResponseModel:
        """Method `appWidgets.getAppImageUploadServer()`

        :param image_type:
        """

        return await self._call("appWidgets.getAppImageUploadServer", locals(), GetAppImageUploadServerResponseModel)

    async def get_app_images(
        self,
        count: int | None = None,
        image_type: str | None = None,
        offset: int | None = None,
    ) -> "Photos":
        """Method `appWidgets.getAppImages()`

        :param count: Maximum count of results.
        :param image_type:
        :param offset: Offset needed to return a specific subset of images.
        """

        return await self._call("appWidgets.getAppImages", locals(), Photos)

    async def get_group_image_upload_server(
        self,
        image_type: str,
    ) -> GetGroupImageUploadServerResponseModel:
        """Method `appWidgets.getGroupImageUploadServer()`

        :param image_type:
        """

        return await self._call("appWidgets.getGroupImageUploadServer", locals(), GetGroupImageUploadServerResponseModel)

    async def get_group_images(
        self,
        count: int | None = None,
        image_type: str | None = None,
        offset: int | None = None,
    ) -> "Photos":
        """Method `appWidgets.getGroupImages()`

        :param count: Maximum count of results.
        :param image_type:
        :param offset: Offset needed to return a specific subset of images.
        """

        return await self._call("appWidgets.getGroupImages", locals(), Photos)

    async def get_images_by_id(
        self,
        images: list[str],
    ) -> list[AppWidgetsPhoto]:
        """Method `appWidgets.getImagesById()`

        :param images: List of images IDs
        """

        return await self._call("appWidgets.getImagesById", locals(), list[AppWidgetsPhoto])

    async def save_app_image(
        self,
        hash: str,
        image: str,
    ) -> "AppWidgetsPhoto":
        """Method `appWidgets.saveAppImage()`

        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        return await self._call("appWidgets.saveAppImage", locals(), AppWidgetsPhoto)

    async def save_group_image(
        self,
        hash: str,
        image: str,
    ) -> "AppWidgetsPhoto":
        """Method `appWidgets.saveGroupImage()`

        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        return await self._call("appWidgets.saveGroupImage", locals(), AppWidgetsPhoto)

    async def update(
        self,
        code: str,
        type: str,
    ) -> OkResponseModel:
        """Method `appWidgets.update()`

        :param code:
        :param type:
        """

        return await self._call("appWidgets.update", locals(), OkResponseModel)


__all__ = ("AppWidgetsCategory",)
