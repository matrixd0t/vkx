from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import Lead


class LeadFormsCreateResponseModel(BaseModel):
    form_id: int = Field()
    url: str = Field()

class LeadFormsDeleteResponseModel(BaseModel):
    form_id: int = Field()

class GetLeadsResponseModel(BaseModel):
    leads: list["Lead"] = Field()
    next_page_token: str | None = Field(
        default=None,
    )

__all__ = (
    "GetLeadsResponseModel",
    "LeadFormsCreateResponseModel",
    "LeadFormsDeleteResponseModel",
)
