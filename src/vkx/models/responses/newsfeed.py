from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    CommentsItem,
    GroupFull,
    ListFull,
    NewsfeedItem,
    NewsfeedList,
    SubscriptionsItem,
    UserFull,
    WallpostFull,
)


class GenericResponseModel(BaseModel):
    items: list["NewsfeedItem"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    lives_items: list["NewsfeedItem"] | None = Field(
        default=None,
    )

class NewsfeedGetBannedExtendedResponseModel(BaseModel):
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )

class NewsfeedGetBannedResponseModel(BaseModel):
    groups: list[int] | None = Field(
        default=None,
    )
    members: list[int] | None = Field(
        default=None,
    )

class NewsfeedGetCommentsResponseModel(BaseModel):
    items: list["CommentsItem"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    next_from: str | None = Field(
        default=None,
    )

class GetListsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["ListFull"] = Field()

class NewsfeedGetListsResponseModel(BaseModel):
    count: int = Field()
    items: list["NewsfeedList"] = Field()

class GetMentionsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallpostFull"] = Field()

class GetSuggestedSourcesResponseModel(BaseModel):
    count: int = Field()
    items: list["SubscriptionsItem"] = Field()

class IgnoreItemResponseModel(BaseModel):
    status: bool = Field(default=1)

class NewsfeedSearchExtendedResponseModel(BaseModel):
    items: list["WallpostFull"] = Field()
    count: int = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )

class SearchExtendedStrictResponseModel(BaseModel):
    items: list["WallpostFull"] = Field()
    count: int = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )

class NewsfeedSearchResponseModel(BaseModel):
    items: list["WallpostFull"] = Field()
    count: int = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )

class SearchStrictResponseModel(BaseModel):
    items: list["WallpostFull"] = Field()
    count: int = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )

__all__ = (
    "GenericResponseModel",
    "GetListsExtendedResponseModel",
    "GetMentionsResponseModel",
    "GetSuggestedSourcesResponseModel",
    "IgnoreItemResponseModel",
    "NewsfeedGetBannedExtendedResponseModel",
    "NewsfeedGetBannedResponseModel",
    "NewsfeedGetCommentsResponseModel",
    "NewsfeedGetListsResponseModel",
    "NewsfeedSearchExtendedResponseModel",
    "NewsfeedSearchResponseModel",
    "SearchExtendedStrictResponseModel",
    "SearchStrictResponseModel",
)
