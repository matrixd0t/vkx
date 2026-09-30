from ..base_model import BaseModel, Field
from ..objects import DonatorSubscriptionInfo, GroupFull, UserFull


class DonutGetSubscriptionsResponseModel(BaseModel):
    subscriptions: list["DonatorSubscriptionInfo"] = Field()
    count: int | None = Field(
        default=None,
    )
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )


from .groups import GetMembersFieldsResponseModel

__all__ = (
    "DonutGetSubscriptionsResponseModel",
    "GetMembersFieldsResponseModel",
)
