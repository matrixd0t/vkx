from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import Product, StickerNew, StickersKeyword


class GetFavoriteStickersResponseModel(BaseModel):
    count: int = Field()
    items: list["StickerNew"] = Field()

class GetProductsResponseModel(BaseModel):
    items: list["Product"] = Field()
    count: int = Field()

class GetStickersKeywordsResponseModel(BaseModel):
    count: int = Field()
    dictionary: list["StickersKeyword"] = Field()
    chunks_count: int | None = Field(
        default=None,
    )
    chunks_hash: str | None = Field(
        default=None,
    )

__all__ = (
    "GetFavoriteStickersResponseModel",
    "GetProductsResponseModel",
    "GetStickersKeywordsResponseModel",
)
