from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    App,
    Group,
    NotificationItem,
    Photo,
    User,
    VideoFull,
)


class NotificationsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["NotificationItem"] = Field()
    profiles: list["User"] | None = Field(
        default=None,
    )
    groups: list["Group"] | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )
    photos: list["Photo"] | None = Field(
        default=None,
    )
    videos: list["VideoFull"] | None = Field(
        default=None,
    )
    apps: list["App"] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    ttl: int | None = Field(
        default=None,
    )

__all__ = (
    "NotificationsGetResponseModel",
)
