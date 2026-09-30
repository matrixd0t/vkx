from ..base_model import BaseModel, Field
from ..objects import Bookmark, Group, Page, Tag, UserFull


class FaveGetPagesResponseModel(BaseModel):
    count: int = Field()
    items: list["Page"] = Field()


class GetTagsResponseModel(BaseModel):
    count: int = Field()
    items: list["Tag"] = Field()


class FaveGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["Bookmark"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["Group"] | None = Field(
        default=None,
    )


class FaveGetResponseModel(BaseModel):
    count: int = Field()
    items: list["Bookmark"] = Field()


__all__ = (
    "FaveGetExtendedResponseModel",
    "FaveGetPagesResponseModel",
    "FaveGetResponseModel",
    "GetTagsResponseModel",
)
