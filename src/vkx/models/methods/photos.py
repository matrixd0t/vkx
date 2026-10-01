import typing

from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.photos import *  # type: ignore
from .base_category import BaseCategory


class PhotosCategory(BaseCategory):
    async def confirm_tag(
        self,
        photo_id: str,
        tag_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.confirmTag()`

        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.confirmTag", locals(), OkResponseModel)

    async def copy(
        self,
        owner_id: int,
        photo_id: int,
        access_key: str | None = None,
    ) -> int:
        """Method `photos.copy()`

        :param owner_id: photo's owner ID
        :param photo_id: photo ID
        :param access_key: for private photos
        """

        return await self._call("photos.copy", locals(), int)

    async def create_album(
        self,
        title: str,
        comments_disabled: bool | None = None,
        description: str | None = None,
        group_id: int | None = None,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
        upload_by_admins_only: bool | None = None,
    ) -> "PhotoAlbumFull":
        """Method `photos.createAlbum()`

        :param title: Album title.
        :param comments_disabled:
        :param description: Album description.
        :param group_id: ID of the community in which the album will be created.
        :param privacy_comment:
        :param privacy_view:
        :param upload_by_admins_only:
        """

        return await self._call("photos.createAlbum", locals(), PhotoAlbumFull)

    async def create_comment(
        self,
        photo_id: int,
        access_key: str | None = None,
        attachments: list[str] | None = None,
        from_group: bool | None = None,
        guid: str | None = None,
        message: str | None = None,
        owner_id: int | None = None,
        reply_to_comment: int | None = None,
        sticker_id: int | None = None,
    ) -> int:
        """Method `photos.createComment()`

        :param photo_id: Photo ID.
        :param access_key:
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - Media attachment owner ID. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' - to post a comment from the community
        :param guid:
        :param message: Comment text.
        :param owner_id: ID of the user or community that owns the photo.
        :param reply_to_comment:
        :param sticker_id:
        """

        return await self._call("photos.createComment", locals(), int)

    async def delete(
        self,
        owner_id: int | None = None,
        photo_id: int | None = None,
        photos: list[str] | None = None,
    ) -> OkResponseModel:
        """Method `photos.delete()`

        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param photos:
        """

        return await self._call("photos.delete", locals(), OkResponseModel)

    async def delete_album(
        self,
        album_id: int,
        group_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.deleteAlbum()`

        :param album_id: Album ID.
        :param group_id: ID of the community that owns the album.
        """

        return await self._call("photos.deleteAlbum", locals(), OkResponseModel)

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> bool:
        """Method `photos.deleteComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.deleteComment", locals(), bool)

    async def edit(
        self,
        photo_id: int,
        caption: str | None = None,
        delete_place: bool | None = None,
        foursquare_id: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        owner_id: int | None = None,
        place_str: str | None = None,
    ) -> OkResponseModel:
        """Method `photos.edit()`

        :param photo_id: Photo ID.
        :param caption: New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param delete_place:
        :param foursquare_id:
        :param latitude:
        :param longitude:
        :param owner_id: ID of the user or community that owns the photo.
        :param place_str:
        """

        return await self._call("photos.edit", locals(), OkResponseModel)

    async def edit_album(
        self,
        album_id: int,
        comments_disabled: bool | None = None,
        description: str | None = None,
        owner_id: int | None = None,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
        title: str | None = None,
        upload_by_admins_only: bool | None = None,
    ) -> OkResponseModel:
        """Method `photos.editAlbum()`

        :param album_id: ID of the photo album to be edited.
        :param comments_disabled:
        :param description: New album description.
        :param owner_id: ID of the user or community that owns the album.
        :param privacy_comment:
        :param privacy_view:
        :param title: New album title.
        :param upload_by_admins_only:
        """

        return await self._call("photos.editAlbum", locals(), OkResponseModel)

    async def edit_comment(
        self,
        comment_id: int,
        attachments: list[str] | None = None,
        message: str | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.editComment()`

        :param comment_id: Comment ID.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - Media attachment owner ID. '<media_id>' - Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: New text of the comment.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.editComment", locals(), OkResponseModel)

    async def get(
        self,
        album_id: str | None = None,
        count: int | None = None,
        extended: bool | None = None,
        feed: int | None = None,
        feed_type: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        photo_ids: list[str] | None = None,
        photo_sizes: bool | None = None,
        rev: bool | None = None,
    ) -> PhotosGetResponseModel:
        """Method `photos.get()`

        :param album_id: Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param count:
        :param extended: '1' - to return additional 'likes', 'comments', and 'tags' fields, '0' - (default)
        :param feed: unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param feed_type: Type of feed obtained in 'feed' field of the method.
        :param offset:
        :param owner_id: ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param photo_ids: Photo IDs.
        :param photo_sizes: '1' - to return photo sizes in a [vk.com/dev/photo_sizes|special format]
        :param rev: Sort order: '1' - reverse chronological, '0' - chronological
        """

        return await self._call("photos.get", locals(), PhotosGetResponseModel)

    async def get_albums(
        self,
        album_ids: list[int] | None = None,
        count: int | None = None,
        need_covers: bool | None = None,
        need_system: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        photo_sizes: bool | None = None,
    ) -> PhotosGetAlbumsResponseModel:
        """Method `photos.getAlbums()`

        :param album_ids: Album IDs.
        :param count: Number of albums to return.
        :param need_covers: '1' - to return an additional 'thumb_src' field, '0' - (default)
        :param need_system: '1' - to return system albums with negative IDs
        :param offset: Offset needed to return a specific subset of albums.
        :param owner_id: ID of the user or community that owns the albums.
        :param photo_sizes: '1' - to return photo sizes in a
        """

        return await self._call("photos.getAlbums", locals(), PhotosGetAlbumsResponseModel)

    async def get_albums_count(
        self,
        group_id: int | None = None,
        need_system: bool | None = None,
        user_id: int | None = None,
    ) -> int:
        """Method `photos.getAlbumsCount()`

        :param group_id: Community ID.
        :param need_system:
        :param user_id: User ID.
        """

        return await self._call("photos.getAlbumsCount", locals(), int)

    async def get_all(
        self,
        count: int | None = None,
        extended: bool | None = None,
        need_hidden: bool | None = None,
        no_service_albums: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        photo_sizes: bool | None = None,
        skip_hidden: bool | None = None,
    ) -> GetAllResponseModel:
        """Method `photos.getAll()`

        :param count: Number of photos to return.
        :param extended: '1' - to return detailed information about photos
        :param need_hidden: '1' - to show information about photos being hidden from the block above the wall.
        :param no_service_albums: '1' - to return photos only from standard albums, '0' - to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param owner_id: ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param photo_sizes: '1' - to return image sizes in [vk.com/dev/photo_sizes|special format].
        :param skip_hidden: '1' - not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        """

        return await self._call("photos.getAll", locals(), GetAllResponseModel)

    async def get_all_comments(
        self,
        album_id: int | None = None,
        count: int | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> GetAllCommentsResponseModel:
        """Method `photos.getAllComments()`

        :param album_id: Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param count: Number of comments to return. By default, '20'. Maximum value, '100'.
        :param need_likes: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param owner_id: ID of the user or community that owns the album(s).
        """

        return await self._call("photos.getAllComments", locals(), GetAllCommentsResponseModel)

    async def get_by_id(
        self,
        photos: list[str],
        extended: bool | None = None,
        photo_sizes: bool | None = None,
    ) -> list[Photo]:
        """Method `photos.getById()`

        :param photos: IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: '1' - to return additional fields, '0' - (default)
        :param photo_sizes: '1' - to return photo sizes in a
        """

        return await self._call("photos.getById", locals(), list[Photo])

    async def get_chat_upload_server(
        self,
        chat_id: int,
        crop_width: int | None = None,
        crop_x: int | None = None,
        crop_y: int | None = None,
    ) -> "UploadServer":
        """Method `photos.getChatUploadServer()`

        :param chat_id: ID of the chat for which you want to upload a cover photo.
        :param crop_width: Width (in pixels) of the photo after cropping.
        :param crop_x:
        :param crop_y:
        """

        return await self._call("photos.getChatUploadServer", locals(), UploadServer)

    @typing.overload
    async def get_comments(
        self,
        photo_id: int,
        extended: typing.Literal[True],
        access_key: str | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> PhotosGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        photo_id: int,
        extended: typing.Literal[False] | None = None,
        access_key: str | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> PhotosGetCommentsResponseModel: ...

    async def get_comments(
        self,
        photo_id: int,
        extended: bool | None = None,
        access_key: str | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> PhotosGetCommentsExtendedResponseModel | PhotosGetCommentsResponseModel:
        """Method `photos.getComments()`

        :param photo_id: Photo ID.
        :param extended:
        :param access_key:
        :param count: Number of comments to return.
        :param fields:
        :param need_likes: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param owner_id: ID of the user or community that owns the photo.
        :param sort: Sort order: 'asc' - old first, 'desc' - new first
        :param start_comment_id:
        """

        return await self._call(
            "photos.getComments",
            locals(),
            dependent=((("extended",), PhotosGetCommentsExtendedResponseModel),),
            default=PhotosGetCommentsResponseModel,
        )

    async def get_market_album_upload_server(
        self,
        group_id: int,
    ) -> "UploadServer":
        """Method `photos.getMarketAlbumUploadServer()`

        :param group_id: Community ID.
        """

        return await self._call("photos.getMarketAlbumUploadServer", locals(), UploadServer)

    async def get_messages_upload_server(
        self,
        peer_id: int | None = None,
    ) -> "PhotoUpload":
        """Method `photos.getMessagesUploadServer()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        return await self._call("photos.getMessagesUploadServer", locals(), PhotoUpload)

    async def get_new_tags(
        self,
        count: int | None = None,
        offset: int | None = None,
    ) -> GetNewTagsResponseModel:
        """Method `photos.getNewTags()`

        :param count: Number of photos to return.
        :param offset: Offset needed to return a specific subset of photos.
        """

        return await self._call("photos.getNewTags", locals(), GetNewTagsResponseModel)

    async def get_owner_photo_upload_server(
        self,
        owner_id: int | None = None,
    ) -> "UploadServer":
        """Method `photos.getOwnerPhotoUploadServer()`

        :param owner_id: identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' - user, 'owner_id=-1' - community, "
        """

        return await self._call("photos.getOwnerPhotoUploadServer", locals(), UploadServer)

    async def get_tags(
        self,
        photo_id: int,
        access_key: str | None = None,
        owner_id: int | None = None,
    ) -> list[PhotoTag]:
        """Method `photos.getTags()`

        :param photo_id: Photo ID.
        :param access_key:
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.getTags", locals(), list[PhotoTag])

    async def get_upload_server(
        self,
        album_id: int | None = None,
        group_id: int | None = None,
    ) -> "PhotoUpload":
        """Method `photos.getUploadServer()`

        :param album_id:
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        """

        return await self._call("photos.getUploadServer", locals(), PhotoUpload)

    async def get_user_photos(
        self,
        count: int | None = None,
        extended: bool | None = None,
        offset: int | None = None,
        sort: str | None = None,
        user_id: int | None = None,
    ) -> GetUserPhotosResponseModel:
        """Method `photos.getUserPhotos()`

        :param count: Number of photos to return. Maximum value is 1000.
        :param extended: '1' - to return an additional 'likes' field, '0' - (default)
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param sort: Sort order: '1' - by date the tag was added in ascending order, '0' - by date the tag was added in descending order
        :param user_id: User ID.
        """

        return await self._call("photos.getUserPhotos", locals(), GetUserPhotosResponseModel)

    async def get_wall_upload_server(
        self,
        group_id: int | None = None,
    ) -> "PhotoUpload":
        """Method `photos.getWallUploadServer()`

        :param group_id: ID of community to whose wall the photo will be uploaded.
        """

        return await self._call("photos.getWallUploadServer", locals(), PhotoUpload)

    async def make_cover(
        self,
        photo_id: int,
        album_id: int | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.makeCover()`

        :param photo_id: Photo ID.
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.makeCover", locals(), OkResponseModel)

    async def move(
        self,
        photo_ids: list[int],
        target_album_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.move()`

        :param photo_ids:
        :param target_album_id: ID of the album to which the photo will be moved.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.move", locals(), OkResponseModel)

    async def put_tag(
        self,
        photo_id: int,
        user_id: int,
        owner_id: int | None = None,
        x: float | None = None,
        x2: float | None = None,
        y: float | None = None,
        y2: float | None = None,
    ) -> int:
        """Method `photos.putTag()`

        :param photo_id: Photo ID.
        :param user_id: ID of the user to be tagged.
        :param owner_id: ID of the user or community that owns the photo.
        :param x: Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param x2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param y2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        """

        return await self._call("photos.putTag", locals(), int)

    async def remove_tag(
        self,
        photo_id: int,
        tag_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.removeTag()`

        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.removeTag", locals(), OkResponseModel)

    async def reorder_albums(
        self,
        album_id: int,
        after: int | None = None,
        before: int | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.reorderAlbums()`

        :param album_id: Album ID.
        :param after: ID of the album after which the album in question shall be placed.
        :param before: ID of the album before which the album in question shall be placed.
        :param owner_id: ID of the user or community that owns the album.
        """

        return await self._call("photos.reorderAlbums", locals(), OkResponseModel)

    async def reorder_photos(
        self,
        photo_id: int,
        after: int | None = None,
        before: int | None = None,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.reorderPhotos()`

        :param photo_id: Photo ID.
        :param after: ID of the photo after which the photo in question shall be placed.
        :param before: ID of the photo before which the photo in question shall be placed.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.reorderPhotos", locals(), OkResponseModel)

    async def report(
        self,
        owner_id: int,
        photo_id: int,
        reason: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.report()`

        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse, '8' - suicide calls
        """

        return await self._call("photos.report", locals(), OkResponseModel)

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.reportComment()`

        :param comment_id: ID of the comment being reported.
        :param owner_id: ID of the user or community that owns the photo.
        :param reason: Reason for the complaint: '0' - spam, '1' - child pornography, '2' - extremism, '3' - violence, '4' - drug propaganda, '5' - adult material, '6' - insult, abuse
        """

        return await self._call("photos.reportComment", locals(), OkResponseModel)

    async def restore(
        self,
        photo_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `photos.restore()`

        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.restore", locals(), OkResponseModel)

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> bool:
        """Method `photos.restoreComment()`

        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the photo.
        """

        return await self._call("photos.restoreComment", locals(), bool)

    async def save(
        self,
        album_id: int | None = None,
        caption: str | None = None,
        group_id: int | None = None,
        hash: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        photos_list: str | None = None,
        server: int | None = None,
    ) -> list[Photo]:
        """Method `photos.save()`

        :param album_id: ID of the album to save photos to.
        :param caption: Text describing the photo. 2048 digits max.
        :param group_id: ID of the community to save photos to.
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param photos_list: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        return await self._call("photos.save", locals(), list[Photo])

    async def save_market_album_photo(
        self,
        group_id: int,
        hash: str,
        photo: str,
        server: int,
    ) -> list[Photo]:
        """Method `photos.saveMarketAlbumPhoto()`

        :param group_id: Community ID.
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        return await self._call("photos.saveMarketAlbumPhoto", locals(), list[Photo])

    async def save_messages_photo(
        self,
        photo: str,
        hash: str | None = None,
        server: int | None = None,
    ) -> list[Photo]:
        """Method `photos.saveMessagesPhoto()`

        :param photo: Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param hash:
        :param server:
        """

        return await self._call("photos.saveMessagesPhoto", locals(), list[Photo])

    async def save_owner_cover_photo(
        self,
        crop_height: int | None = None,
        crop_width: int | None = None,
        crop_x: int | None = None,
        crop_y: int | None = None,
        hash: str | None = None,
        is_video_cover: bool | None = None,
        photo: str | None = None,
        response_json: str | None = None,
    ) -> SaveOwnerCoverPhotoResponseModel:
        """Method `photos.saveOwnerCoverPhoto()`

        :param crop_height:
        :param crop_width:
        :param crop_x:
        :param crop_y:
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param is_video_cover:
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param response_json:
        """

        return await self._call("photos.saveOwnerCoverPhoto", locals(), SaveOwnerCoverPhotoResponseModel)

    async def save_owner_photo(
        self,
        hash: str | None = None,
        photo: str | None = None,
        server: str | None = None,
    ) -> SaveOwnerPhotoResponseModel:
        """Method `photos.saveOwnerPhoto()`

        :param hash: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param server: parameter returned after [vk.com/dev/upload_files|photo upload].
        """

        return await self._call("photos.saveOwnerPhoto", locals(), SaveOwnerPhotoResponseModel)

    async def save_wall_photo(
        self,
        photo: str,
        caption: str | None = None,
        group_id: int | None = None,
        hash: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        server: int | None = None,
        user_id: int | None = None,
    ) -> list[Photo]:
        """Method `photos.saveWallPhoto()`

        :param photo: Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param caption: Text describing the photo. 2048 digits max.
        :param group_id: ID of community on whose wall the photo will be saved.
        :param hash:
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param server:
        :param user_id: ID of the user on whose wall the photo will be saved.
        """

        return await self._call("photos.saveWallPhoto", locals(), list[Photo])

    async def search(
        self,
        count: int | None = None,
        end_time: float | None = None,
        lat: float | None = None,
        long: float | None = None,
        offset: int | None = None,
        q: str | None = None,
        radius: int | None = None,
        sort: int | None = None,
        start_time: float | None = None,
    ) -> PhotosSearchResponseModel:
        """Method `photos.search()`

        :param count: Number of photos to return.
        :param end_time:
        :param lat: Geographical latitude, in degrees (from '-90' to '90').
        :param long: Geographical longitude, in degrees (from '-180' to '180').
        :param offset: Offset needed to return a specific subset of photos.
        :param q: Search query string.
        :param radius: Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        :param sort: Sort order:
        :param start_time:
        """

        return await self._call("photos.search", locals(), PhotosSearchResponseModel)

    async def get_owner_cover_photo_upload_server(
        self,
        crop_width: int | None = None,
        crop_height: int | None = None,
        crop_x: int | None = None,
        crop_x2: int | None = None,
        crop_y: int | None = None,
        crop_y2: int | None = None,
        group_id: int | None = None,
        is_video_cover: bool | None = None,
    ) -> "UploadServer":
        """Method `photos.getOwnerCoverPhotoUploadServer()`

        :param crop_width: Width
        :param crop_height: Height
        :param crop_x: X coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_y2: Y coordinate of the right-bottom corner
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param is_video_cover:
        """

        return await self._call("photos.getOwnerCoverPhotoUploadServer", locals(), UploadServer)


__all__ = ("PhotosCategory",)
