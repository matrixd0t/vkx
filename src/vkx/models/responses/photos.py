from ..base_model import BaseModel, Field
from ..objects import (
    BaseImage,
    GroupFull,
    Photo,
    PhotoAlbumFull,
    PhotoXtrTagInfo,
    UserFull,
    WallComment,
)


class PhotosGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotoAlbumFull"] = Field()


class GetAllCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()


class GetAllResponseModel(BaseModel):
    count: int = Field()
    items: list["Photo"] = Field()
    more: bool | None = Field(
        default=None,
    )


class PhotosGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    real_offset: int | None = Field(
        default=None,
    )


class PhotosGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()
    real_offset: int | None = Field(
        default=None,
    )


class GetNewTagsResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotoXtrTagInfo"] = Field()


class GetUserPhotosResponseModel(BaseModel):
    count: int = Field()
    items: list["Photo"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class PhotosGetResponseModel(BaseModel):
    count: int = Field()
    items: list["Photo"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class MarketAlbumUploadResponseModel(BaseModel):
    gid: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class MarketUploadResponseModel(BaseModel):
    crop_data: str | None = Field(
        default=None,
    )
    crop_hash: str | None = Field(
        default=None,
    )
    group_id: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class MessageUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class OwnerCoverUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )


class OwnerUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotoUploadResponseModel(BaseModel):
    aid: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    photos_list: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class SaveOwnerCoverPhotoResponseModel(BaseModel):
    images: list["BaseImage"] | None = Field(
        default=None,
    )


class SaveOwnerPhotoResponseModel(BaseModel):
    photo_hash: str = Field()
    photo_src: str = Field()
    photo_src_big: str | None = Field(
        default=None,
    )
    photo_src_small: str | None = Field(
        default=None,
    )
    saved: int | None = Field(
        default=None,
    )
    post_id: int | None = Field(
        default=None,
    )


class PhotosSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["Photo"] = Field()


class WallUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


__all__ = (
    "GetAllCommentsResponseModel",
    "GetAllResponseModel",
    "GetNewTagsResponseModel",
    "GetUserPhotosResponseModel",
    "MarketAlbumUploadResponseModel",
    "MarketUploadResponseModel",
    "MessageUploadResponseModel",
    "OwnerCoverUploadResponseModel",
    "OwnerUploadResponseModel",
    "PhotoUploadResponseModel",
    "PhotosGetAlbumsResponseModel",
    "PhotosGetCommentsExtendedResponseModel",
    "PhotosGetCommentsResponseModel",
    "PhotosGetResponseModel",
    "PhotosSearchResponseModel",
    "SaveOwnerCoverPhotoResponseModel",
    "SaveOwnerPhotoResponseModel",
    "WallUploadResponseModel",
)
