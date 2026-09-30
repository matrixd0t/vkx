from ..base_model import BaseModel, Field
from ..objects import LastShortenedLink


class GetLastShortenedLinksResponseModel(BaseModel):
    count: int = Field()
    items: list["LastShortenedLink"] = Field()


__all__ = (
    "GetLastShortenedLinksResponseModel",
)
