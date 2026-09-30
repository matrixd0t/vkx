from ..base_model import BaseModel, Field


class TranslationsTranslateResponseModel(BaseModel):
    texts: list[str] | None = Field(
        default=None,
    )
    source_lang: str | None = Field(
        default=None,
    )


__all__ = (
    "TranslationsTranslateResponseModel",
)
