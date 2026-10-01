import typing

from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.board import *  # type: ignore
from .base_category import BaseCategory


class BoardCategory(BaseCategory):
    async def add_topic(
        self,
        group_id: int,
        title: str,
        attachments: AttachmentsInput | None = None,
        from_group: bool | None = None,
        text: str | None = None,
    ) -> int:
        """Method `board.addTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        :param from_group: For a community: '1' - to post the topic as by the community, '0' - to post the topic as by the user (default)
        :param text: Text of the topic.
        """

        return await self._call("board.addTopic", locals(), int)

    async def close_topic(
        self,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.closeTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.closeTopic", locals(), OkResponseModel)

    async def create_comment(
        self,
        group_id: int,
        topic_id: int,
        attachments: AttachmentsInput | None = None,
        from_group: bool | None = None,
        guid: str | None = None,
        message: str | None = None,
        sticker_id: int | None = None,
    ) -> int:
        """Method `board.createComment()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: ID of the topic to be commented on.
        :param attachments: (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID.
        :param from_group: '1' - to post the comment as by the community, '0' - to post the comment as by the user (default)
        :param guid: Unique identifier to avoid repeated comments.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param sticker_id: Sticker ID.
        """

        return await self._call("board.createComment", locals(), int)

    async def delete_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.deleteComment()`

        :param comment_id: Comment ID.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.deleteComment", locals(), OkResponseModel)

    async def delete_topic(
        self,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.deleteTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.deleteTopic", locals(), OkResponseModel)

    async def edit_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
        attachments: AttachmentsInput | None = None,
        message: str | None = None,
    ) -> OkResponseModel:
        """Method `board.editComment()`

        :param comment_id: ID of the comment on the topic.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: (Required if 'attachments' is not set). New comment text.
        """

        return await self._call("board.editComment", locals(), OkResponseModel)

    async def edit_topic(
        self,
        group_id: int,
        title: str,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.editTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param title: New title of the topic.
        :param topic_id: Topic ID.
        """

        return await self._call("board.editTopic", locals(), OkResponseModel)

    async def fix_topic(
        self,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.fixTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.fixTopic", locals(), OkResponseModel)

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: typing.Literal[True],
        count: int | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> BoardGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> BoardGetCommentsResponseModel: ...

    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: bool | None = None,
        count: int | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> BoardGetCommentsExtendedResponseModel | BoardGetCommentsResponseModel:
        """Method `board.getComments()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param extended: '1' - to return information about users who posted comments, '0' - to return no additional fields (default)
        :param count: Number of comments to return.
        :param need_likes: '1' - to return the 'likes' field, '0' - not to return the 'likes' field (default)
        :param offset: Offset needed to return a specific subset of comments.
        :param sort: Sort order: 'asc' - by creation date in chronological order, 'desc' - by creation date in reverse chronological order,
        :param start_comment_id:
        """

        return await self._call(
            "board.getComments",
            locals(),
            dependent=((("extended",), BoardGetCommentsExtendedResponseModel),),
            default=BoardGetCommentsResponseModel,
        )

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        extended: typing.Literal[True],
        count: int | None = None,
        offset: int | None = None,
        order: int | None = None,
        preview: int | None = None,
        preview_length: int | None = None,
        topic_ids: list[int] | None = None,
    ) -> GetTopicsExtendedResponseModel: ...

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        offset: int | None = None,
        order: int | None = None,
        preview: int | None = None,
        preview_length: int | None = None,
        topic_ids: list[int] | None = None,
    ) -> GetTopicsResponseModel: ...

    async def get_topics(
        self,
        group_id: int,
        extended: bool | None = None,
        count: int | None = None,
        offset: int | None = None,
        order: int | None = None,
        preview: int | None = None,
        preview_length: int | None = None,
        topic_ids: list[int] | None = None,
    ) -> GetTopicsResponseModel | GetTopicsExtendedResponseModel:
        """Method `board.getTopics()`

        :param group_id: ID of the community that owns the discussion board.
        :param extended: '1' - to return information about users who created topics or who posted there last, '0' - to return no additional fields (default)
        :param count: Number of topics to return.
        :param offset: Offset needed to return a specific subset of topics.
        :param order: Sort order: '1' - by date updated in reverse chronological order. '2' - by date created in reverse chronological order. '-1' - by date updated in chronological order. '-2' - by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param preview: '1' - to return the first comment in each topic,, '2' - to return the last comment in each topic,, '0' - to return no comments. By default: '0'.
        :param preview_length: Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        :param topic_ids: IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        """

        return await self._call(
            "board.getTopics",
            locals(),
            dependent=((("extended",), GetTopicsExtendedResponseModel),),
            default=GetTopicsResponseModel,
        )

    async def open_topic(
        self,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.openTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.openTopic", locals(), OkResponseModel)

    async def restore_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.restoreComment()`

        :param comment_id: Comment ID.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.restoreComment", locals(), OkResponseModel)

    async def unfix_topic(
        self,
        group_id: int,
        topic_id: int,
    ) -> OkResponseModel:
        """Method `board.unfixTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        return await self._call("board.unfixTopic", locals(), OkResponseModel)


__all__ = ("BoardCategory",)
