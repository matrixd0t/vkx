from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    AdsCategory,
    LookalikeRequest,
    Musician,
)


class CreateLookalikeRequestResponseModel(BaseModel):
    request_id: int | None = Field(
        default=None,
    )

class CreateTargetGroupResponseModel(BaseModel):
    id: int | None = Field(
        default=None,
    )
    pixel: str | None = Field(
        default=None,
    )

class CreateTargetPixelResponseModel(BaseModel):
    id: int | None = Field(
        default=None,
    )
    pixel: str | None = Field(
        default=None,
    )

class GetCategoriesResponseModel(BaseModel):
    v1: list["AdsCategory"] | None = Field(
        default=None,
    )
    v2: list["AdsCategory"] | None = Field(
        default=None,
    )

class GetLookalikeRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list["LookalikeRequest"] = Field()

class GetMusiciansResponseModel(BaseModel):
    items: list["Musician"] = Field()

class RemoveTargetContactsResponseModel(BaseModel):
    result: int = Field()

class SaveLookalikeRequestResultResponseModel(BaseModel):
    retargeting_group_id: int = Field()
    audience_count: int = Field()

class ShareTargetGroupResponseModel(BaseModel):
    id: int = Field()

__all__ = (
    "CreateLookalikeRequestResponseModel",
    "CreateTargetGroupResponseModel",
    "CreateTargetPixelResponseModel",
    "GetCategoriesResponseModel",
    "GetLookalikeRequestsResponseModel",
    "GetMusiciansResponseModel",
    "RemoveTargetContactsResponseModel",
    "SaveLookalikeRequestResultResponseModel",
    "ShareTargetGroupResponseModel",
)
