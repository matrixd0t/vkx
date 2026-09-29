from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    GroupFull,
    User,
    UserFull,
    WallComment,
    WallItem,
    WallpostAttachment,
    WallpostFull,
)


class CreateCommentResponseModel(BaseModel):
    comment_id: int = Field()
    parents_stack: list[int] | None = Field(
        default=None,
    )

class WallEditResponseModel(BaseModel):
    post_id: int = Field()

class WallGetByIdExtendedResponseModel(BaseModel):
    items: list["WallItem"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()

class WallGetByIdResponseModel(BaseModel):
    items: list["WallItem"] | None = Field(
        default=None,
    )

class GetCommentExtendedResponseModel(BaseModel):
    items: list["WallComment"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    post_author_id: int | None = Field(
        default=None,
    )

class GetCommentResponseModel(BaseModel):
    items: list["WallComment"] = Field()
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )

class WallGetCommentsExtendedResponseModel(BaseModel):
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
    post_author_id: int | None = Field(
        default=None,
    )

class WallGetCommentsResponseModel(BaseModel):
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

class GetRepostsResponseModel(BaseModel):
    items: list["WallpostFull"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()

class WallGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallItem"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()

class WallGetResponseModel(BaseModel):
    count: int = Field()
    items: list["WallItem"] = Field()

class ParseAttachedLinkResponseModel(BaseModel):
    data: list["WallpostAttachment"] = Field()
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    profiles: list["User"] | None = Field(
        default=None,
    )

class PostAdsStealthResponseModel(BaseModel):
    post_id: int = Field()

class PostResponseModel(BaseModel):
    post_id: int = Field()

class RepostResponseModel(BaseModel):
    success: int = Field(default=1)
    post_id: int = Field()
    reposts_count: int = Field()
    likes_count: int = Field()
    wall_repost_count: int | None = Field(
        default=None,
    )
    mail_repost_count: int | None = Field(
        default=None,
    )

class WallSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallItem"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()

class WallSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["WallItem"] = Field()

from vkx.models.base_model import Field


class WallGetByIdExtendedResponseModel(WallGetByIdExtendedResponseModel):
    items: list[WallpostFull] = Field()

class WallGetByIdResponseModel(WallGetByIdResponseModel):
    items: list[WallpostFull] | None = Field(
        default=None,
    )

class WallGetExtendedResponseModel(WallGetExtendedResponseModel):
    items: list[WallpostFull] = Field()

class WallGetResponseModel(WallGetResponseModel):
    items: list[WallpostFull] = Field()

class WallSearchExtendedResponseModel(WallSearchExtendedResponseModel):
    items: list[WallpostFull] = Field()

class WallSearchResponseModel(WallSearchResponseModel):
    items: list[WallpostFull] = Field()

__all__ = (
    "CreateCommentResponseModel",
    "GetCommentExtendedResponseModel",
    "GetCommentResponseModel",
    "GetRepostsResponseModel",
    "ParseAttachedLinkResponseModel",
    "PostAdsStealthResponseModel",
    "PostResponseModel",
    "RepostResponseModel",
    "WallEditResponseModel",
    "WallGetByIdExtendedResponseModel",
    "WallGetByIdResponseModel",
    "WallGetCommentsExtendedResponseModel",
    "WallGetCommentsResponseModel",
    "WallGetExtendedResponseModel",
    "WallGetResponseModel",
    "WallSearchExtendedResponseModel",
    "WallSearchResponseModel",
)
