from ..base_model import BaseModel, Field
from ..objects import PrettyCard


class PrettyCardsCreateResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()


class PrettyCardsDeleteResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()
    error: str | None = Field(
        default=None,
    )


class PrettyCardsEditResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()


class PrettyCardsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["PrettyCard"] = Field()


__all__ = (
    "PrettyCardsCreateResponseModel",
    "PrettyCardsDeleteResponseModel",
    "PrettyCardsEditResponseModel",
    "PrettyCardsGetResponseModel",
)
