from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    App,
    CustomSnippet,
    GroupFull,
    Leaderboard,
    Scope,
    User,
    UserFull,
)


class AddSnippetResponseModel(BaseModel):
    snippet_id: int = Field()

class CreatedGroupResponseModel(BaseModel):
    group_id: int = Field()

class GetFriendsListExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()

class GetFriendsListResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()

class GetLeaderboardExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Leaderboard"] = Field()
    profiles: list["User"] | None = Field(
        default=None,
    )

class GetLeaderboardResponseModel(BaseModel):
    count: int = Field()
    items: list["Leaderboard"] = Field()

class GetMiniAppPoliciesResponseModel(BaseModel):
    privacy_policy: str | None = Field(
        default=None,
    )
    terms: str | None = Field(
        default=None,
    )

class GetScopesResponseModel(BaseModel):
    count: int = Field()
    items: list["Scope"] = Field()

class GetSnippetsResponseModel(BaseModel):
    items: list["CustomSnippet"] | None = Field(
        default=None,
    )

class AppsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["App"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )

class ImageUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    image: str | None = Field(
        default=None,
    )

class IsNotificationsAllowedResponseModel(BaseModel):
    is_allowed: bool = Field()

__all__ = (
    "AddSnippetResponseModel",
    "AppsGetResponseModel",
    "CreatedGroupResponseModel",
    "GetFriendsListExtendedResponseModel",
    "GetFriendsListResponseModel",
    "GetLeaderboardExtendedResponseModel",
    "GetLeaderboardResponseModel",
    "GetMiniAppPoliciesResponseModel",
    "GetScopesResponseModel",
    "GetSnippetsResponseModel",
    "ImageUploadResponseModel",
    "IsNotificationsAllowedResponseModel",
)
