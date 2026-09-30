from ..base_model import BaseModel, Field
from ..objects import (
    FeedItem,
    GroupFull,
    Story,
    User,
    UserFull,
    ViewersItem,
)


class StoriesGetBannedExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()


class StoriesGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class StoriesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Story"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()


class GetPhotoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: list[int] = Field()


class GetVideoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: list[int] = Field()


class GetViewersExtendedV5115ResponseModel(BaseModel):
    count: int = Field()
    items: list["ViewersItem"] = Field()
    hidden_reason: str | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )


class GetV5113ResponseModel(BaseModel):
    count: int = Field()
    items: list["FeedItem"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    need_upload_screen: bool | None = Field(
        default=None,
    )
    track_code: str | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )


class StoriesSaveResponseModel(BaseModel):
    count: int = Field()
    items: list["Story"] = Field()
    profiles: list["User"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


class StoriesUploadResponseModel(BaseModel):
    upload_result: str | None = Field(
        default=None,
    )


__all__ = (
    "GetPhotoUploadServerResponseModel",
    "GetV5113ResponseModel",
    "GetVideoUploadServerResponseModel",
    "GetViewersExtendedV5115ResponseModel",
    "StoriesGetBannedExtendedResponseModel",
    "StoriesGetBannedResponseModel",
    "StoriesGetByIdExtendedResponseModel",
    "StoriesSaveResponseModel",
    "StoriesUploadResponseModel",
)
