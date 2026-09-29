from vkx.models.base_model import BaseModel, Field


class RestoreResponseModel(BaseModel):
    success: int | None = Field(
        default=None,
    )
    sid: str | None = Field(
        default=None,
    )

__all__ = (
    "RestoreResponseModel",
)
