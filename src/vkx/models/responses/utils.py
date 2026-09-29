from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    LastShortenedLink,
)


class GetLastShortenedLinksResponseModel(BaseModel):
    count: int = Field()
    items: list["LastShortenedLink"] = Field()

from vkx.models.base_model import Field

__all__ = (
    "GetLastShortenedLinksResponseModel",
)
