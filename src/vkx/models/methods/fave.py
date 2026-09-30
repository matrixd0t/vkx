from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.fave import *  # type: ignore
from .base_category import BaseCategory


class FaveCategory(BaseCategory):
    async def add_article(
        self,
        url: str,
    ) -> OkResponseModel:
        """Method `fave.addArticle()`

        :param url:
        """

        return await self._call("fave.addArticle", locals(), OkResponseModel)

    async def add_link(
        self,
        link: str,
    ) -> OkResponseModel:
        """Method `fave.addLink()`

        :param link: Link URL.
        """

        return await self._call("fave.addLink", locals(), OkResponseModel)

    async def add_page(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `fave.addPage()`

        :param group_id:
        :param user_id:
        """

        return await self._call("fave.addPage", locals(), OkResponseModel)

    async def add_post(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
    ) -> OkResponseModel:
        """Method `fave.addPost()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        return await self._call("fave.addPost", locals(), OkResponseModel)

    async def add_product(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
    ) -> OkResponseModel:
        """Method `fave.addProduct()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        return await self._call("fave.addProduct", locals(), OkResponseModel)

    async def add_tag(
        self,
        name: str | None = None,
        position: str | None = None,
    ) -> "Tag":
        """Method `fave.addTag()`

        :param name:
        :param position:
        """

        return await self._call("fave.addTag", locals(), Tag)

    async def add_video(
        self,
        id: int,
        owner_id: int,
        access_key: str | None = None,
    ) -> OkResponseModel:
        """Method `fave.addVideo()`

        :param id:
        :param owner_id:
        :param access_key:
        """

        return await self._call("fave.addVideo", locals(), OkResponseModel)

    async def edit_tag(
        self,
        id: int,
        name: str,
    ) -> OkResponseModel:
        """Method `fave.editTag()`

        :param id:
        :param name:
        """

        return await self._call("fave.editTag", locals(), OkResponseModel)

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
    ) -> FaveGetExtendedResponseModel: ...

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
    ) -> FaveGetResponseModel: ...

    async def get(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: str | None = None,
        is_from_snackbar: bool | None = None,
        item_type: str | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
    ) -> FaveGetExtendedResponseModel | FaveGetResponseModel:
        """Method `fave.get()`

        :param extended: '1' - to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param count: Number of users to return.
        :param fields:
        :param is_from_snackbar:
        :param item_type:
        :param offset: Offset needed to return a specific subset of users.
        :param tag_id: Tag ID.
        """

        return await self._call(
            "fave.get",
            locals(),
            dependent=((("extended",), FaveGetExtendedResponseModel),),
            default=FaveGetResponseModel,
        )

    async def get_pages(
        self,
        count: int | None = None,
        fields: list[UserGroupFields] | None = None,
        offset: int | None = None,
        tag_id: int | None = None,
        type: str | None = None,
    ) -> FaveGetPagesResponseModel:
        """Method `fave.getPages()`

        :param count:
        :param fields:
        :param offset:
        :param tag_id:
        :param type:
        """

        return await self._call("fave.getPages", locals(), FaveGetPagesResponseModel)

    async def get_tags(
        self,
    ) -> GetTagsResponseModel:
        """Method `fave.getTags()`"""

        return await self._call("fave.getTags", locals(), GetTagsResponseModel)

    async def mark_seen(
        self,
    ) -> bool:
        """Method `fave.markSeen()`"""

        return await self._call("fave.markSeen", locals(), bool)

    async def remove_article(
        self,
        article_id: int,
        owner_id: int,
    ) -> bool:
        """Method `fave.removeArticle()`

        :param article_id:
        :param owner_id:
        """

        return await self._call("fave.removeArticle", locals(), bool)

    async def remove_link(
        self,
        link: str | None = None,
        link_id: str | None = None,
    ) -> OkResponseModel:
        """Method `fave.removeLink()`

        :param link: Link URL
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        """

        return await self._call("fave.removeLink", locals(), OkResponseModel)

    async def remove_page(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `fave.removePage()`

        :param group_id:
        :param user_id:
        """

        return await self._call("fave.removePage", locals(), OkResponseModel)

    async def remove_post(
        self,
        id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `fave.removePost()`

        :param id:
        :param owner_id:
        """

        return await self._call("fave.removePost", locals(), OkResponseModel)

    async def remove_product(
        self,
        id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `fave.removeProduct()`

        :param id:
        :param owner_id:
        """

        return await self._call("fave.removeProduct", locals(), OkResponseModel)

    async def remove_tag(
        self,
        id: int,
    ) -> OkResponseModel:
        """Method `fave.removeTag()`

        :param id:
        """

        return await self._call("fave.removeTag", locals(), OkResponseModel)

    async def remove_video(
        self,
        id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `fave.removeVideo()`

        :param id:
        :param owner_id:
        """

        return await self._call("fave.removeVideo", locals(), OkResponseModel)

    async def reorder_tags(
        self,
        ids: list[int],
    ) -> OkResponseModel:
        """Method `fave.reorderTags()`

        :param ids:
        """

        return await self._call("fave.reorderTags", locals(), OkResponseModel)

    async def set_page_tags(
        self,
        group_id: int | None = None,
        tag_ids: list[int] | None = None,
        user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `fave.setPageTags()`

        :param group_id:
        :param tag_ids:
        :param user_id:
        """

        return await self._call("fave.setPageTags", locals(), OkResponseModel)

    async def set_tags(
        self,
        item_id: int | None = None,
        item_owner_id: int | None = None,
        item_type: str | None = None,
        link_id: str | None = None,
        link_url: str | None = None,
        tag_ids: list[int] | None = None,
    ) -> OkResponseModel:
        """Method `fave.setTags()`

        :param item_id:
        :param item_owner_id:
        :param item_type:
        :param link_id:
        :param link_url:
        :param tag_ids:
        """

        return await self._call("fave.setTags", locals(), OkResponseModel)

    async def track_page_interaction(
        self,
        group_id: int | None = None,
        user_id: int | None = None,
    ) -> OkResponseModel:
        """Method `fave.trackPageInteraction()`

        :param group_id:
        :param user_id:
        """

        return await self._call("fave.trackPageInteraction", locals(), OkResponseModel)


__all__ = ("FaveCategory",)
