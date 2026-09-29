from vkx.models.base_model import BaseModel, Field


class GetVersionResponseModel(BaseModel):
    id: int = Field()
    page_id: int = Field()
    group_id: int = Field()
    title: str = Field()
    source: str = Field()
    current_user_can_edit: int = Field()
    who_can_view: int = Field()
    who_can_edit: int = Field()
    version_created: int = Field()
    creator_id: int | None = Field(
        default=None,
    )
    parent: str | None = Field(
        default=None,
    )
    parent2: str | None = Field(
        default=None,
    )
    html: str | None = Field(
        default=None,
    )

__all__ = (
    "GetVersionResponseModel",
)
