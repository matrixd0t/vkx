from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import Gift


class GiftsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["Gift"] = Field()

__all__ = (
    "GiftsGetResponseModel",
)
