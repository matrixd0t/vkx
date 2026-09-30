from ..base_model import BaseModel, Field
from ..objects import Hint


class GetHintsResponseModel(BaseModel):
    count: int = Field()
    items: list["Hint"] = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )


__all__ = (
    "GetHintsResponseModel",
)
