import typing

from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import SubscriptionsItem


class LikesAddResponseModel(BaseModel):
    likes: int = Field()

class LikesDeleteResponseModel(BaseModel):
    likes: int = Field()

class GetListExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["SubscriptionsItem"] = Field()
    liked_by_author: dict[str, typing.Any] | None = Field(
        default=None,
    )
    liked_by_group: dict[str, typing.Any] | None = Field(
        default=None,
    )

class GetListResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()

class IsLikedResponseModel(BaseModel):
    liked: bool = Field()
    copied: bool = Field()

__all__ = (
    "GetListExtendedResponseModel",
    "GetListResponseModel",
    "IsLikedResponseModel",
    "LikesAddResponseModel",
    "LikesDeleteResponseModel",
)
