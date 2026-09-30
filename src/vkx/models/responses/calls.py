from ..base_model import BaseModel, Field
from ..objects import ShortCredentials


class StartResponseModel(BaseModel):
    join_link: str = Field()
    ok_join_link: str = Field()
    call_id: str | None = Field(
        default=None,
    )
    broadcast_video_id: str | None = Field(
        default=None,
    )
    broadcast_ov_id: str | None = Field(
        default=None,
    )
    short_credentials: "ShortCredentials | None" = Field(
        default=None,
    )


__all__ = (
    "StartResponseModel",
)
