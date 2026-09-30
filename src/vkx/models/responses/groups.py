import datetime

from ..base_model import BaseModel, Field
from ..objects import (
    Address,
    CallbackServer,
    GroupAccess,
    GroupAgeLimits,
    GroupAudio,
    GroupCategory,
    GroupCategoryFull,
    GroupDocs,
    GroupFull,
    GroupFullSection,
    GroupPhotos,
    GroupPublicCategoryList,
    GroupSuggestedPrivacy,
    GroupTopics,
    GroupVideo,
    GroupWall,
    GroupWiki,
    MemberRole,
    OnlineStatusType,
    OwnerXtrBanInfo,
    ProfileItem,
    SectionsListItem,
    SettingsTwitter,
    SubjectItem,
    TokenPermissionSetting,
    UserFull,
    UserMin,
    UserXtrRole,
)


class AddCallbackServerResponseModel(BaseModel):
    server_id: int = Field()


class GetAddressesResponseModel(BaseModel):
    count: int = Field()
    items: list["Address"] = Field()


class GroupsGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: list["OwnerXtrBanInfo"] = Field()


class GetByIdObjectResponseModel(BaseModel):
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    profiles: list["ProfileItem"] | None = Field(
        default=None,
    )


class GetCallbackConfirmationCodeResponseModel(BaseModel):
    code: str = Field()


class GetCallbackServersResponseModel(BaseModel):
    count: int = Field()
    items: list["CallbackServer"] = Field()


class GetCatalogInfoExtendedResponseModel(BaseModel):
    enabled: bool = Field()
    categories: list["GroupCategoryFull"] | None = Field(
        default=None,
    )


class GetCatalogInfoResponseModel(BaseModel):
    enabled: bool = Field()
    categories: list["GroupCategory"] | None = Field(
        default=None,
    )


class GetInvitedUsersResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()


class GetInvitesExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupFull"] = Field()
    profiles: list["UserMin"] = Field()
    groups: list["GroupFull"] = Field()


class GetInvitesResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupFull"] = Field()


class GetMembersFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UserXtrRole"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GetMembersFilterResponseModel(BaseModel):
    count: int = Field()
    items: list["MemberRole"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GetMembersResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GetOnlineStatusResponseModel(BaseModel):
    status: "OnlineStatusType" = Field()
    minutes: int | None = Field(
        default=None,
    )


class GetRequestsFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UserFull"] = Field()


class GroupsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class GetSettingsResponseModel(BaseModel):
    audio: "GroupAudio" = Field()
    articles: int = Field()
    city_id: int = Field()
    city_name: str = Field()
    description: str = Field()
    docs: "GroupDocs" = Field()
    obscene_filter: bool = Field()
    obscene_stopwords: bool = Field()
    obscene_words: list[str] = Field()
    toxic_filter: bool = Field()
    disable_replies_from_groups: bool = Field()
    photos: "GroupPhotos" = Field()
    title: str = Field()
    topics: "GroupTopics" = Field()
    video: "GroupVideo" = Field()
    wall: "GroupWall" = Field()
    wiki: "GroupWiki" = Field()
    access: "GroupAccess | None" = Field(
        default=None,
    )
    address: str | None = Field(
        default=None,
    )
    recognize_photo: int | None = Field(
        default=None,
    )
    contacts: bool | None = Field(
        default=None,
    )
    links: bool | None = Field(
        default=None,
    )
    sections_list: list["SectionsListItem"] | None = Field(
        default=None,
    )
    main_section: "GroupFullSection | None" = Field(
        default=None,
    )
    secondary_section: "GroupFullSection | None" = Field(
        default=None,
    )
    age_limits: "GroupAgeLimits | None" = Field(
        default=None,
    )
    events: bool | None = Field(
        default=None,
    )
    addresses: bool | None = Field(
        default=None,
    )
    bots_capabilities: bool | None = Field(
        default=None,
    )
    bots_start_button: bool | None = Field(
        default=None,
    )
    bots_add_to_chat: bool | None = Field(
        default=None,
    )
    bot_online_booking_enabled: bool | None = Field(
        default=None,
    )
    event_group_id: int | None = Field(
        default=None,
    )
    public_category: int | None = Field(
        default=None,
    )
    public_category_list: list["GroupPublicCategoryList"] | None = Field(
        default=None,
    )
    public_date: str | None = Field(
        default=None,
    )
    public_date_label: str | None = Field(
        default=None,
    )
    public_subcategory: int | None = Field(
        default=None,
    )
    rss: str | None = Field(
        default=None,
    )
    start_date: datetime.datetime | None = Field(
        default=None,
    )
    finish_date: datetime.datetime | None = Field(
        default=None,
    )
    subject: int | None = Field(
        default=None,
    )
    subject_list: list["SubjectItem"] | None = Field(
        default=None,
    )
    suggested_privacy: "GroupSuggestedPrivacy | None" = Field(
        default=None,
    )
    twitter: "SettingsTwitter | None" = Field(
        default=None,
    )
    website: str | None = Field(
        default=None,
    )
    phone: str | None = Field(
        default=None,
    )
    email: str | None = Field(
        default=None,
    )


class GetTokenPermissionsResponseModel(BaseModel):
    mask: int = Field()
    permissions: list["TokenPermissionSetting"] = Field()


class GetObjectExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupFull"] = Field()


class GroupsGetResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class InviteUserIdsListResponseModel(BaseModel):
    invites_send_count: int = Field()


class IsMemberExtendedResponseModel(BaseModel):
    member: bool = Field()
    invitation: bool | None = Field(
        default=None,
    )
    can_invite: bool | None = Field(
        default=None,
    )
    can_recall: bool | None = Field(
        default=None,
    )
    request: bool | None = Field(
        default=None,
    )


class GroupsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupFull"] = Field()


class GetMembersFilterManagersResponseModel(BaseModel):
    count: int | None = None
    items: list[MemberRole] | None = None


class GetMembersFieldsFilterManagersResponseModel(BaseModel):
    count: int | None = None
    items: list[UserXtrRole] | None = None


__all__ = (
    "AddCallbackServerResponseModel",
    "GetAddressesResponseModel",
    "GetByIdObjectResponseModel",
    "GetCallbackConfirmationCodeResponseModel",
    "GetCallbackServersResponseModel",
    "GetCatalogInfoExtendedResponseModel",
    "GetCatalogInfoResponseModel",
    "GetInvitedUsersResponseModel",
    "GetInvitesExtendedResponseModel",
    "GetInvitesResponseModel",
    "GetMembersFieldsFilterManagersResponseModel",
    "GetMembersFieldsResponseModel",
    "GetMembersFilterManagersResponseModel",
    "GetMembersFilterResponseModel",
    "GetMembersResponseModel",
    "GetObjectExtendedResponseModel",
    "GetOnlineStatusResponseModel",
    "GetRequestsFieldsResponseModel",
    "GetSettingsResponseModel",
    "GetTokenPermissionsResponseModel",
    "GroupsGetBannedResponseModel",
    "GroupsGetRequestsResponseModel",
    "GroupsGetResponseModel",
    "GroupsSearchResponseModel",
    "InviteUserIdsListResponseModel",
    "IsMemberExtendedResponseModel",
)
