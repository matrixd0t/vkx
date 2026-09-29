from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    GroupFull,
    StreamInputParams,
    User,
    UserFull,
    VideoAlbum,
    VideoAlbumFull,
    VideoFull,
    VideoImage,
    WallComment,
)


class VideoAddAlbumResponseModel(BaseModel):
    album_id: int = Field()

class VideoEditResponseModel(BaseModel):
    success: bool = Field()
    access_key: str | None = Field(
        default=None,
    )

class GetAlbumsByVideoExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoAlbumFull"] = Field()

class GetAlbumsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoAlbumFull"] = Field()

class VideoGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoAlbum"] = Field()

class VideoGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
        default=None,
    )

class VideoGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
        default=None,
    )

class GetLongPollServerResponseModel(BaseModel):
    url: str = Field()

class GetOembedResponseModel(BaseModel):
    version: str = Field()
    type: str = Field()
    html: str = Field()
    title: str | None = Field(
        default=None,
    )
    author_name: str | None = Field(
        default=None,
    )
    width: int | None = Field(
        default=None,
    )
    height: int | None = Field(
        default=None,
    )
    provider_name: str | None = Field(
        default=None,
    )
    provider_url: str | None = Field(
        default=None,
    )
    thumbnail_url: str | None = Field(
        default=None,
    )
    thumbnail_width: int | None = Field(
        default=None,
    )
    thumbnail_height: int | None = Field(
        default=None,
    )

class GetThumbUploadUrlResponseModel(BaseModel):
    upload_url: str = Field()

class VideoGetResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoFull"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    max_attached_short_videos: int | None = Field(
        default=None,
    )

class SaveUploadedThumbResponseModel(BaseModel):
    photo_id: int = Field()
    photo_hash: str = Field()
    image: list["VideoImage"] | None = Field(
        default=None,
    )
    photo_owner_id: int | None = Field(
        default=None,
    )

class VideoSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoFull"] = Field()
    profiles: list["User"] = Field()
    groups: list["GroupFull"] = Field()

class VideoSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoFull"] = Field()

class StartStreamingResponseModel(BaseModel):
    owner_id: int = Field()
    video_id: int = Field()
    name: str = Field()
    description: str = Field()
    access_key: str = Field()
    stream: "StreamInputParams" = Field()
    post_id: int | None = Field(
        default=None,
    )

class StopStreamingResponseModel(BaseModel):
    unique_viewers: int | None = Field(
        default=None,
    )

class VideoUploadResponseModel(BaseModel):
    size: int | None = Field(
        default=None,
    )
    video_id: int | None = Field(
        default=None,
    )

__all__ = (
    "GetAlbumsByVideoExtendedResponseModel",
    "GetAlbumsExtendedResponseModel",
    "GetLongPollServerResponseModel",
    "GetOembedResponseModel",
    "GetThumbUploadUrlResponseModel",
    "SaveUploadedThumbResponseModel",
    "StartStreamingResponseModel",
    "StopStreamingResponseModel",
    "VideoAddAlbumResponseModel",
    "VideoEditResponseModel",
    "VideoGetAlbumsResponseModel",
    "VideoGetCommentsExtendedResponseModel",
    "VideoGetCommentsResponseModel",
    "VideoGetResponseModel",
    "VideoSearchExtendedResponseModel",
    "VideoSearchResponseModel",
    "VideoUploadResponseModel",
)
