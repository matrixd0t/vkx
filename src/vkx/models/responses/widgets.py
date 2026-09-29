from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import WidgetComment, WidgetPage


class WidgetsGetCommentsResponseModel(BaseModel):
    count: int = Field()
    posts: list["WidgetComment"] = Field()

class WidgetsGetPagesResponseModel(BaseModel):
    count: int = Field()
    pages: list["WidgetPage"] = Field()

__all__ = (
    "WidgetsGetCommentsResponseModel",
    "WidgetsGetPagesResponseModel",
)
