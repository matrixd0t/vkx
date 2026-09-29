import typing

from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import DefaultOrder, GroupFull, Topic, TopicComment, UserFull


class BoardGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["TopicComment"] = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()
    poll: dict[str, typing.Any] | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
        default=None,
    )

class BoardGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["TopicComment"] = Field()
    poll: dict[str, typing.Any] | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
        default=None,
    )

class GetTopicsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Topic"] = Field()
    default_order: "DefaultOrder" = Field()
    can_add_topics: bool = Field()
    profiles: list["UserFull"] = Field()
    groups: list["GroupFull"] = Field()

class GetTopicsResponseModel(BaseModel):
    count: int = Field()
    items: list["Topic"] = Field()
    default_order: "DefaultOrder" = Field()
    can_add_topics: bool = Field()

__all__ = (
    "BoardGetCommentsExtendedResponseModel",
    "BoardGetCommentsResponseModel",
    "GetTopicsExtendedResponseModel",
    "GetTopicsResponseModel",
)
