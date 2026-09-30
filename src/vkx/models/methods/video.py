from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.video import *  # type: ignore
from .base_category import BaseCategory


class VideoCategory(BaseCategory):
    async def add(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.add()`

        :param owner_id: ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :param video_id: Video ID.
        :param target_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        return await self._call("video.add", locals(), OkResponseModel)

    async def add_album(
        self,
        group_id: int | None = None,
        privacy: list[PlaylistPrivacyCategory] | None = None,
        title: str | None = None,
    ) -> VideoAddAlbumResponseModel:
        """Method `video.addAlbum()`

        :param group_id: Community ID (if the album will be created in a community).
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        :param title: Album title.
        """

        return await self._call("video.addAlbum", locals(), VideoAddAlbumResponseModel)


    async def create_comment(
        self,
        video_id: int,
        attachments: list[str] | None = None,
        from_group: bool | None = None,
        guid: str | None = None,
        message: str | None = None,
        owner_id: int | None = None,
        reply_to_comment: int | None = None,
        sticker_id: int | None = None,
        track_code: str | None = None,
    ) -> int:
        """Method `video.createComment()`

        :param video_id: Video ID.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media attachment owner. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' - to post the comment from a community name (only if 'owner_id'<0)
        :param guid:
        :param message: New comment text.
        :param owner_id: ID of the user or community that owns the video.
        :param reply_to_comment:
        :param sticker_id:
        :param track_code:
        """

        return await self._call("video.createComment", locals(), int)

    async def delete(
        self,
        video_id: int,
        owner_id: int | None = None,
        target_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.delete()`

        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param target_id:
        """

        return await self._call("video.delete", locals(), OkResponseModel)

    async def delete_album(
        self,
        album_id: int,
        group_id: int | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.deleteAlbum()`

        :param album_id: Album ID.
        :param group_id: Community ID (if the album is owned by a community).
        :param owner_id:
        """

        return await self._call("video.deleteAlbum", locals(), OkResponseModel)

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.deleteComment()`

        :param comment_id: ID of the comment to be deleted.
        :param owner_id: ID of the user or community that owns the video.
        """

        return await self._call("video.deleteComment", locals(), OkResponseModel)

    async def delete_thread(
        self,
        owner_id: int,
        thread_id: int,
    ) -> OkResponseModel:
        """Method `video.deleteThread()`

        :param owner_id: ID of the user or community that owns the video.
        :param thread_id: ID of the main comment to be deleted as thread.
        """

        return await self._call("video.deleteThread", locals(), OkResponseModel)

    async def edit(
        self,
        video_id: int,
        desc: str | None = None,
        name: str | None = None,
        no_comments: bool | None = None,
        ord_info: str | None = None,
        owner_id: int | None = None,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
        repeat: bool | None = None,
    ) -> VideoEditResponseModel:
        """Method `video.edit()`

        :param video_id: Video ID.
        :param desc: New video description.
        :param name: New video title.
        :param no_comments: Disable comments for the group video.
        :param ord_info:
        :param owner_id: ID of the user or community that owns the video.
        :param privacy_comment: Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param privacy_view: Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param repeat: '1' - to repeat the playback of the video, '0' - to play the video once,
        """

        return await self._call("video.edit", locals(), VideoEditResponseModel)

    async def edit_album(
        self,
        album_id: int,
        group_id: int | None = None,
        owner_id: int | None = None,
        privacy: list[PlaylistPrivacyCategory] | None = None,
        title: str | None = None,
    ) -> OkResponseModel:
        """Method `video.editAlbum()`

        :param album_id: Album ID.
        :param group_id: Community ID (if the album edited is owned by a community).
        :param owner_id:
        :param privacy: new access permissions for the album. Possible values: , *'0' - all users,, *'1' - friends only,, *'2' - friends and friends of friends,, *'3' - "only me".
        :param title: New album title.
        """

        return await self._call("video.editAlbum", locals(), OkResponseModel)

    async def edit_comment(
        self,
        comment_id: int,
        attachments: list[str] | None = None,
        message: str | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.editComment()`

        :param comment_id: Comment ID.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media attachment owner. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: New comment text.
        :param owner_id: ID of the user or community that owns the video.
        """

        return await self._call("video.editComment", locals(), OkResponseModel)

    async def get(
        self,
        album_id: int | None = None,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[str] | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort_album: int | None = None,
        videos: list[str] | None = None,
    ) -> VideoGetResponseModel:
        """Method `video.get()`

        :param album_id: ID of the album containing the video(s).
        :param count: Number of videos to return.
        :param extended: '1' - to return an extended response with additional fields
        :param fields:
        :param offset: Offset needed to return a specific subset of videos.
        :param owner_id: ID of the user or community that owns the video(s).
        :param sort_album: Sort order: '0' - newest video first, '1' - oldest video first
        :param videos: Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        """

        return await self._call("video.get", locals(), VideoGetResponseModel)

    async def get_album_by_id(
        self,
        album_id: int,
        owner_id: int | None = None,
    ) -> "VideoAlbumFull":
        """Method `video.getAlbumById()`

        :param album_id: Album ID.
        :param owner_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """

        return await self._call("video.getAlbumById", locals(), VideoAlbumFull)

    @typing.overload
    async def get_albums(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        need_system: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> GetAlbumsExtendedResponseModel: ...

    @typing.overload
    async def get_albums(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        need_system: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> VideoGetAlbumsResponseModel: ...

    async def get_albums(
        self,
        extended: bool | None = None,
        count: int | None = None,
        need_system: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> VideoGetAlbumsResponseModel | GetAlbumsExtendedResponseModel:
        """Method `video.getAlbums()`

        :param extended: '1' - to return additional information about album privacy settings for the current user
        :param count: Number of video albums to return.
        :param need_system:
        :param offset: Offset needed to return a specific subset of video albums.
        :param owner_id: ID of the user or community that owns the video album(s).
        """

        return await self._call(
            "video.getAlbums",
            locals(),
            dependent=((("extended",), GetAlbumsExtendedResponseModel),),
            default=VideoGetAlbumsResponseModel,
        )

    @typing.overload
    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: typing.Literal[True],
        target_id: int | None = None,
    ) -> GetAlbumsByVideoExtendedResponseModel: ...

    @typing.overload
    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: typing.Literal[False] | None = None,
        target_id: int | None = None,
    ) -> list[int]: ...

    async def get_albums_by_video(
        self,
        owner_id: int,
        video_id: int,
        extended: bool | None = None,
        target_id: int | None = None,
    ) -> list[int] | GetAlbumsByVideoExtendedResponseModel:
        """Method `video.getAlbumsByVideo()`

        :param owner_id:
        :param video_id:
        :param extended:
        :param target_id:
        """

        return await self._call(
            "video.getAlbumsByVideo",
            locals(),
            dependent=((("extended",), GetAlbumsByVideoExtendedResponseModel),),
            default=list[int],
        )

    @typing.overload
    async def get_comments(
        self,
        video_id: int,
        extended: typing.Literal[True],
        comment_id: int | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
        thread_items_count: int | None = None,
    ) -> VideoGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        video_id: int,
        extended: typing.Literal[False] | None = None,
        comment_id: int | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
        thread_items_count: int | None = None,
    ) -> VideoGetCommentsResponseModel: ...

    async def get_comments(
        self,
        video_id: int,
        extended: bool | None = None,
        comment_id: int | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
        thread_items_count: int | None = None,
    ) -> VideoGetCommentsExtendedResponseModel | VideoGetCommentsResponseModel:
        """Method `video.getComments()`

        :param video_id: Video ID.
        :param extended:
        :param comment_id:
        :param count: Number of comments to return.
        :param fields:
        :param need_likes: '1' - to return an additional 'likes' field
        :param offset: Offset needed to return a specific subset of comments.
        :param owner_id: ID of the user or community that owns the video.
        :param sort: Sort order: 'asc' - oldest comment first, 'desc' - newest comment first
        :param start_comment_id:
        :param thread_items_count:
        """

        return await self._call(
            "video.getComments",
            locals(),
            dependent=((("extended",), VideoGetCommentsExtendedResponseModel),),
            default=VideoGetCommentsResponseModel,
        )

    async def get_long_poll_server(
        self,
        video_id: int,
        owner_id: int | None = None,
    ) -> GetLongPollServerResponseModel:
        """Method `video.getLongPollServer()`

        :param video_id:
        :param owner_id:
        """

        return await self._call("video.getLongPollServer", locals(), GetLongPollServerResponseModel)

    async def get_oembed(
        self,
        url: str,
        maxheight: int | None = None,
        maxwidth: int | None = None,
    ) -> GetOembedResponseModel:
        """Method `video.getOembed()`

        :param url: Link to video
        :param maxheight: Maximum width of player
        :param maxwidth: Maximum width of player
        """

        return await self._call("video.getOembed", locals(), GetOembedResponseModel)

    async def get_thumb_upload_url(
        self,
        owner_id: int,
    ) -> GetThumbUploadUrlResponseModel:
        """Method `video.getThumbUploadUrl()`

        :param owner_id:
        """

        return await self._call("video.getThumbUploadUrl", locals(), GetThumbUploadUrlResponseModel)

    async def live_get_categories(
        self,
    ) -> list[LiveCategory]:
        """Method `video.liveGetCategories()`"""

        return await self._call("video.liveGetCategories", locals(), list[LiveCategory])


    async def reorder_albums(
        self,
        album_id: int,
        after: int | None = None,
        before: int | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.reorderAlbums()`

        :param album_id: Album ID.
        :param after: ID of the album after which the album in question shall be placed.
        :param before: ID of the album before which the album in question shall be placed.
        :param owner_id: ID of the user or community that owns the albums..
        """

        return await self._call("video.reorderAlbums", locals(), OkResponseModel)

    async def reorder_videos(
        self,
        owner_id: int,
        video_id: int,
        after_owner_id: int | None = None,
        after_video_id: int | None = None,
        album_id: int | None = None,
        before_owner_id: int | None = None,
        before_video_id: int | None = None,
        target_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.reorderVideos()`

        :param owner_id: ID of the user or community that owns the video.
        :param video_id: ID of the video.
        :param after_owner_id: ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: ID of the video after which the photo in question shall be placed.
        :param album_id: ID of the video album.
        :param before_owner_id: ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: ID of the video before which the video in question shall be placed.
        :param target_id: ID of the user or community that owns the album with videos.
        """

        return await self._call("video.reorderVideos", locals(), OkResponseModel)

    async def report(
        self,
        owner_id: int,
        video_id: int,
        comment: str | None = None,
        reason: int | None = None,
        search_query: str | None = None,
    ) -> OkResponseModel:
        """Method `video.report()`

        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param comment: Comment describing the complaint.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        :param search_query: (If the video was found in search results.) Search query string.
        """

        return await self._call("video.report", locals(), OkResponseModel)

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: int | None = None,
    ) -> OkResponseModel:
        """Method `video.reportComment()`

        :param comment_id: ID of the comment being reported.
        :param owner_id: ID of the user or community that owns the video.
        :param reason: Reason for the complaint: , 0 - spam , 1 - child pornography , 2 - extremism , 3 - violence , 4 - drug propaganda , 5 - adult material , 6 - insult, abuse
        """

        return await self._call("video.reportComment", locals(), OkResponseModel)

    async def restore(
        self,
        video_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `video.restore()`

        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        """

        return await self._call("video.restore", locals(), OkResponseModel)

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> bool:
        """Method `video.restoreComment()`

        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the video.
        """

        return await self._call("video.restoreComment", locals(), bool)

    async def restore_thread(
        self,
        owner_id: int,
        thread_id: int,
    ) -> OkResponseModel:
        """Method `video.restoreThread()`

        :param owner_id: ID of the user or community that owns the video.
        :param thread_id: ID of the main comment to be deleted as thread.
        """

        return await self._call("video.restoreThread", locals(), OkResponseModel)

    async def save(
        self,
        album_id: int | None = None,
        auto_publish: bool | None = None,
        compression: bool | None = None,
        description: str | None = None,
        group_id: int | None = None,
        is_private: bool | None = None,
        link: str | None = None,
        name: str | None = None,
        no_comments: bool | None = None,
        ord_info: str | None = None,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
        repeat: bool | None = None,
        wallpost: bool | None = None,
    ) -> "SaveResult":
        """Method `video.save()`

        :param album_id: ID of the album to which the saved video will be added.
        :param auto_publish:
        :param compression:
        :param description: Description of the video.
        :param group_id: ID of the community in which the video will be saved. By default, the current user's page.
        :param is_private: '1' - to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' - not to designate the video as private
        :param link: URL for embedding the video from an external website.
        :param name: Name of the video.
        :param no_comments:
        :param ord_info:
        :param privacy_comment:
        :param privacy_view:
        :param repeat: '1' - to repeat the playback of the video, '0' - to play the video once,
        :param wallpost: '1' - to post the saved video on a user's wall, '0' - not to post the saved video on a user's wall
        """

        return await self._call("video.save", locals(), SaveResult)

    async def save_uploaded_thumb(
        self,
        owner_id: int,
        thumb_json: str,
        random_tag: str | None = None,
        set_thumb: bool | None = None,
        thumb_size: str | None = None,
        video_id: int | None = None,
    ) -> SaveUploadedThumbResponseModel:
        """Method `video.saveUploadedThumb()`

        :param owner_id:
        :param thumb_json:
        :param random_tag:
        :param set_thumb: If flag passed uploaded thumb will automatically set to passed video. Work only with video_id.
        :param thumb_size:
        :param video_id: Video ID.
        """

        return await self._call("video.saveUploadedThumb", locals(), SaveUploadedThumbResponseModel)

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True],
        adult: bool | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        filters: list[typing.Literal["long", "short", "vimeo", "vk", "youtube"]] | None = None,
        hd: int | None = None,
        live: bool | None = None,
        longer: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        q: str | None = None,
        search_own: bool | None = None,
        shorter: int | None = None,
        sort: int | None = None,
    ) -> VideoSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[False] | None = None,
        adult: bool | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        filters: list[typing.Literal["long", "short", "vimeo", "vk", "youtube"]] | None = None,
        hd: int | None = None,
        live: bool | None = None,
        longer: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        q: str | None = None,
        search_own: bool | None = None,
        shorter: int | None = None,
        sort: int | None = None,
    ) -> VideoSearchResponseModel: ...

    async def search(
        self,
        extended: bool | None = None,
        adult: bool | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        filters: list[typing.Literal["long", "short", "vimeo", "vk", "youtube"]] | None = None,
        hd: int | None = None,
        live: bool | None = None,
        longer: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        q: str | None = None,
        search_own: bool | None = None,
        shorter: int | None = None,
        sort: int | None = None,
    ) -> VideoSearchExtendedResponseModel | VideoSearchResponseModel:
        """Method `video.search()`

        :param extended:
        :param adult: '1' - to disable the Safe Search filter, '0' - to enable the Safe Search filter
        :param count: Number of videos to return.
        :param fields:
        :param filters: Filters to apply: 'youtube' - return YouTube videos only, 'vimeo' - return Vimeo videos only, 'vk' - return VK videos only, 'short' - return short videos only, 'long' - return long videos only
        :param hd: If not null, only searches for high-definition videos.
        :param live:
        :param longer:
        :param offset: Offset needed to return a specific subset of videos.
        :param owner_id:
        :param q: Search query string (e.g., 'The Beatles').
        :param search_own:
        :param shorter:
        :param sort: Sort order: '1' - by duration, '2' - by relevance, '0' - by date added
        """

        return await self._call(
            "video.search",
            locals(),
            dependent=((("extended",), VideoSearchExtendedResponseModel),),
            default=VideoSearchResponseModel,
        )

    async def start_streaming(
        self,
        category_id: int | None = None,
        description: str | None = None,
        group_id: int | None = None,
        name: str | None = None,
        no_comments: bool | None = None,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
        publish: bool | None = None,
        video_id: int | None = None,
        wallpost: bool | None = None,
    ) -> StartStreamingResponseModel:
        """Method `video.startStreaming()`

        :param category_id:
        :param description:
        :param group_id:
        :param name:
        :param no_comments:
        :param privacy_comment:
        :param privacy_view:
        :param publish:
        :param video_id:
        :param wallpost:
        """

        return await self._call("video.startStreaming", locals(), StartStreamingResponseModel)

    async def stop_streaming(
        self,
        group_id: int | None = None,
        video_id: int | None = None,
    ) -> StopStreamingResponseModel:
        """Method `video.stopStreaming()`

        :param group_id:
        :param video_id:
        """

        return await self._call("video.stopStreaming", locals(), StopStreamingResponseModel)

    async def unpin_comment(
        self,
        comment_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `video.unpinComment()`

        :param comment_id:
        :param owner_id: ID of the user or community that owns the video.
        """

        return await self._call("video.unpinComment", locals(), OkResponseModel)
    def __init__(self, api: "typing.Any") -> None:
        super().__init__(api)

    @typing.overload  # type: ignore
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: int | None = ...,
        album_ids: None = None,
    ) -> OkResponseModel: ...

    @typing.overload
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: None = None,
        album_ids: list[int] | None = ...,
    ) -> list[int]: ...

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: int | None = None,
        album_ids: list[int] | None = None,
    ) -> OkResponseModel | list[int]:
        """video.addToAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        return await self._call(
            "video.addToAlbum",
            locals(),
            dependent=((("album_ids",), list[int]),),
            default=OkResponseModel,
        )

    @typing.overload  # type: ignore
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: int | None = ...,
        album_ids: None = None,
    ) -> OkResponseModel: ...

    @typing.overload
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: None = None,
        album_ids: list[int] | None = ...,
    ) -> list[int]: ...

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: int | None = None,
        album_id: int | None = None,
        album_ids: list[int] | None = None,
    ) -> OkResponseModel | list[int]:
        """video.removeFromAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        return await self._call(
            "video.removeFromAlbum",
            locals(),
            dependent=((("album_ids",), list[int]),),
            default=OkResponseModel,
        )


__all__ = ("VideoCategory",)


__all__ = ("VideoCategory",)
