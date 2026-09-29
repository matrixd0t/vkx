from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import PodcastExternalData


class SearchPodcastResponseModel(BaseModel):
    podcasts: list["PodcastExternalData"] = Field()
    results_total: int = Field()

__all__ = (
    "SearchPodcastResponseModel",
)
