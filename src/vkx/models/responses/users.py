from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import GroupsArray, SubscriptionsItem, UserFull, UsersArray


class GetFollowersFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()
    friends_count: int | None = Field(
        default=None,
    )

class GetFollowersResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()

class GetSubscriptionsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["SubscriptionsItem"] = Field()

class GetSubscriptionsResponseModel(BaseModel):
    users: "UsersArray" = Field()
    groups: "GroupsArray" = Field()

class UsersSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()

__all__ = (
    "GetFollowersFieldsResponseModel",
    "GetFollowersResponseModel",
    "GetSubscriptionsExtendedResponseModel",
    "GetSubscriptionsResponseModel",
    "UsersSearchResponseModel",
)
