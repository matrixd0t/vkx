from ..base_model import BaseModel, Field


class GetAppImageUploadServerResponseModel(BaseModel):
    upload_url: str | None = Field(
        default=None,
    )


class GetGroupImageUploadServerResponseModel(BaseModel):
    upload_url: str | None = Field(
        default=None,
    )


__all__ = (
    "GetAppImageUploadServerResponseModel",
    "GetGroupImageUploadServerResponseModel",
)
