from ..base_model import BaseModel, Field
from ..objects import Subscription


class GetUserSubscriptionsResponseModel(BaseModel):
    count: int = Field()
    items: list["Subscription"] = Field()


__all__ = (
    "GetUserSubscriptionsResponseModel",
)
