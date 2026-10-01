import typing

from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.stories import *  # type: ignore
from .base_category import BaseCategory


class StoriesCategory(BaseCategory):
    async def ban_owner(
        self,
        owners_ids: list[int],
    ) -> OkResponseModel:
        """Method `stories.banOwner()`

        :param owners_ids: List of sources IDs
        """

        return await self._call("stories.banOwner", locals(), OkResponseModel)

    async def delete(
        self,
        owner_id: int | None = None,
        stories: list[str] | None = None,
        story_id: int | None = None,
    ) -> OkResponseModel:
        """Method `stories.delete()`

        :param owner_id: Story owner's ID. Current user id is used by default.
        :param stories:
        :param story_id: Story ID.
        """

        return await self._call("stories.delete", locals(), OkResponseModel)

    async def get(
        self,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        owner_id: int | None = None,
    ) -> GetV5113ResponseModel:
        """Method `stories.get()`

        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields:
        :param owner_id: Owner ID.
        """

        return await self._call("stories.get", locals(), GetV5113ResponseModel)

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Literal[True],
        fields: list[UserGroupFields] | None = None,
    ) -> StoriesGetBannedExtendedResponseModel: ...

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Literal[False] | None = None,
        fields: list[UserGroupFields] | None = None,
    ) -> StoriesGetBannedResponseModel: ...

    async def get_banned(
        self,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
    ) -> StoriesGetBannedExtendedResponseModel | StoriesGetBannedResponseModel:
        """Method `stories.getBanned()`

        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        return await self._call(
            "stories.getBanned",
            locals(),
            dependent=((("extended",), StoriesGetBannedExtendedResponseModel),),
            default=StoriesGetBannedResponseModel,
        )

    async def get_by_id(
        self,
        stories: list[str],
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
    ) -> StoriesGetByIdExtendedResponseModel:
        """Method `stories.getById()`

        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        return await self._call("stories.getById", locals(), StoriesGetByIdExtendedResponseModel)

    async def get_photo_upload_server(
        self,
        add_to_news: bool | None = None,
        clickable_stickers: str | None = None,
        group_id: int | None = None,
        link_text: str | None = None,
        link_url: str | None = None,
        reply_to_story: str | None = None,
        user_ids: list[int] | None = None,
    ) -> GetPhotoUploadServerResponseModel:
        """Method `stories.getPhotoUploadServer()`

        :param add_to_news: 1 - to add the story to friend's feed.
        :param clickable_stickers:
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param reply_to_story: ID of the story to reply with the current.
        :param user_ids: List of users IDs who can see the story.
        """

        return await self._call("stories.getPhotoUploadServer", locals(), GetPhotoUploadServerResponseModel)

    async def get_replies(
        self,
        owner_id: int,
        story_id: int,
        access_key: str | None = None,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
    ) -> GetV5113ResponseModel:
        """Method `stories.getReplies()`

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        return await self._call("stories.getReplies", locals(), GetV5113ResponseModel)

    async def get_stats(
        self,
        owner_id: int,
        story_id: int,
    ) -> "StoryStats":
        """Method `stories.getStats()`

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        """

        return await self._call("stories.getStats", locals(), StoryStats)

    async def get_video_upload_server(
        self,
        add_to_news: bool | None = None,
        clickable_stickers: str | None = None,
        group_id: int | None = None,
        link_text: str | None = None,
        link_url: str | None = None,
        reply_to_story: str | None = None,
        user_ids: list[int] | None = None,
    ) -> GetVideoUploadServerResponseModel:
        """Method `stories.getVideoUploadServer()`

        :param add_to_news: 1 - to add the story to friend's feed.
        :param clickable_stickers:
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param reply_to_story: ID of the story to reply with the current.
        :param user_ids: List of users IDs who can see the story.
        """

        return await self._call("stories.getVideoUploadServer", locals(), GetVideoUploadServerResponseModel)

    async def get_viewers(
        self,
        story_id: int,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> GetViewersExtendedV5115ResponseModel:
        """Method `stories.getViewers()`

        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param extended: '1' - to return detailed information about photos
        :param fields:
        :param offset: Offset needed to return a specific subset of results.
        :param owner_id: Story owner ID.
        """

        return await self._call("stories.getViewers", locals(), GetViewersExtendedV5115ResponseModel)

    async def hide_all_replies(
        self,
        owner_id: int,
        group_id: int | None = None,
    ) -> OkResponseModel:
        """Method `stories.hideAllReplies()`

        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id:
        """

        return await self._call("stories.hideAllReplies", locals(), OkResponseModel)

    async def hide_reply(
        self,
        owner_id: int,
        story_id: int,
    ) -> OkResponseModel:
        """Method `stories.hideReply()`

        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """

        return await self._call("stories.hideReply", locals(), OkResponseModel)

    async def save(
        self,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        upload_results: list[str] | None = None,
        upload_results_json: str | None = None,
    ) -> StoriesSaveResponseModel:
        """Method `stories.save()`

        :param extended:
        :param fields:
        :param upload_results:
        :param upload_results_json:
        """

        return await self._call("stories.save", locals(), StoriesSaveResponseModel)

    async def search(
        self,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        mentioned_id: int | None = None,
        place_id: int | None = None,
        q: str | None = None,
        radius: int | None = None,
    ) -> GetV5113ResponseModel:
        """Method `stories.search()`

        :param count:
        :param extended:
        :param fields:
        :param latitude:
        :param longitude:
        :param mentioned_id:
        :param place_id:
        :param q:
        :param radius:
        """

        return await self._call("stories.search", locals(), GetV5113ResponseModel)

    async def send_interaction(
        self,
        access_key: str,
        is_anonymous: bool | None = None,
        is_broadcast: bool | None = None,
        message: str | None = None,
        unseen_marker: bool | None = None,
    ) -> OkResponseModel:
        """Method `stories.sendInteraction()`

        :param access_key:
        :param is_anonymous:
        :param is_broadcast:
        :param message:
        :param unseen_marker:
        """

        return await self._call("stories.sendInteraction", locals(), OkResponseModel)

    async def unban_owner(
        self,
        owners_ids: list[int],
    ) -> OkResponseModel:
        """Method `stories.unbanOwner()`

        :param owners_ids: List of hidden sources to show stories from.
        """

        return await self._call("stories.unbanOwner", locals(), OkResponseModel)


__all__ = ("StoriesCategory",)
