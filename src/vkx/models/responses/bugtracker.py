from ..base_model import BaseModel, Field
from ..objects import (
    AddCompanyGroupsMembersError,
    Bugreport,
    BugreportSubscribeState,
    Comment,
    CompanyMember,
    UserFull,
)


class AddCompanyGroupsMembersResponseModel(BaseModel):
    errors: list["AddCompanyGroupsMembersError"] = Field()


class AddCompanyMembersResponseModel(BaseModel):
    errors: list[str] = Field()


class BugtrackerCreateCommentResponseModel(BaseModel):
    comment: "Comment" = Field()
    comment_flood: bool | None = Field(
        default=None,
    )
    subscribe_state: "BugreportSubscribeState | None" = Field(
        default=None,
    )


class GetBugreportByIdResponseModel(BaseModel):
    bugreport: "Bugreport | None" = Field(
        default=None,
    )
    profiles: list["UserFull"] | None = Field(
        default=None,
    )


class GetCompanyGroupMembersResponseModel(BaseModel):
    user_ids: list[int] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )


class GetCompanyMembersResponseModel(BaseModel):
    company_members: list["CompanyMember"] = Field()
    count: int = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )


class GetDownloadVersionUrlResponseModel(BaseModel):
    url: str = Field()
    app_title: str | None = Field(
        default=None,
    )
    bundle_name: str | None = Field(
        default=None,
    )
    build_id: int | None = Field(
        default=None,
    )
    build_name: str | None = Field(
        default=None,
    )
    build_title: str | None = Field(
        default=None,
    )


__all__ = (
    "AddCompanyGroupsMembersResponseModel",
    "AddCompanyMembersResponseModel",
    "BugtrackerCreateCommentResponseModel",
    "GetBugreportByIdResponseModel",
    "GetCompanyGroupMembersResponseModel",
    "GetCompanyMembersResponseModel",
    "GetDownloadVersionUrlResponseModel",
)
