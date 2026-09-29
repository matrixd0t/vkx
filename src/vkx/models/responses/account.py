from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    Group,
    NameRequest,
    Offer,
    UserFull,
)


class ChangePasswordResponseModel(BaseModel):
    token: str = Field()
    secret: str | None = Field(
        default=None,
    )

class GetActiveOffersResponseModel(BaseModel):
    count: int = Field()
    items: list["Offer"] = Field()

class AccountGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["Group"] | None = Field(
        default=None,
    )

class SaveProfileInfoResponseModel(BaseModel):
    changed: bool = Field()
    name_request: "NameRequest | None" = Field(
        default=None,
    )

__all__ = (
    "AccountGetBannedResponseModel",
    "ChangePasswordResponseModel",
    "GetActiveOffersResponseModel",
    "SaveProfileInfoResponseModel",
)
