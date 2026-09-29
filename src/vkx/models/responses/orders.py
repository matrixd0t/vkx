from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import Subscription


class GetUserSubscriptionsResponseModel(BaseModel):
    count: int = Field()
    items: list["Subscription"] = Field()

__all__ = (
    "GetUserSubscriptionsResponseModel",
)
