from ..base_model import BaseModel, Field


class GetServerUrlResponseModel(BaseModel):
    endpoint: str | None = Field(
        default=None,
    )
    key: str | None = Field(
        default=None,
    )


class GetStemResponseModel(BaseModel):
    stem: str | None = Field(
        default=None,
    )


__all__ = (
    "GetServerUrlResponseModel",
    "GetStemResponseModel",
)
