from ..base_model import BaseEnumMeta, BaseModel, Field, IntEnum
from ..objects import (
    FriendsList,
    RequestsXtrMessage,
    RequestsXtrMutual,
    UserFull,
)


class AddListResponseModel(BaseModel):
    list_id: int = Field()


class FriendsAddResponseModel(IntEnum, metaclass=BaseEnumMeta):
    SEND = 1
    APPROVED = 2
    RESEND = 4


class FriendsDeleteResponseModel(BaseModel):
    success: int = Field(default=1)
    friend_deleted: int | None = Field(
        default=None,
    )
    out_request_deleted: int | None = Field(
        default=None,
    )
    in_request_deleted: int | None = Field(
        default=None,
    )
    suggestion_deleted: int | None = Field(
        default=None,
    )


class FriendsGetListsResponseModel(BaseModel):
    count: int = Field()
    items: list["FriendsList"] = Field()


class GetOnlineOnlineMobileResponseModel(BaseModel):
    online: list[int] = Field()
    online_mobile: list[int] = Field()


class GetRequestsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["RequestsXtrMessage"] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class GetRequestsNeedMutualResponseModel(BaseModel):
    count: int = Field()
    items: list["RequestsXtrMutual"] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class FriendsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class GetSuggestionsResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()


class GetFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )


class FriendsGetResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class FriendsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()


__all__ = (
    "AddListResponseModel",
    "FriendsAddResponseModel",
    "FriendsDeleteResponseModel",
    "FriendsGetListsResponseModel",
    "FriendsGetRequestsResponseModel",
    "FriendsGetResponseModel",
    "FriendsSearchResponseModel",
    "GetFieldsResponseModel",
    "GetOnlineOnlineMobileResponseModel",
    "GetRequestsExtendedResponseModel",
    "GetRequestsNeedMutualResponseModel",
    "GetSuggestionsResponseModel",
)
