from ..base_model import BaseModel, Field


class PaidStatusResponseModel(BaseModel):
    is_paid: bool = Field()


__all__ = (
    "PaidStatusResponseModel",
)
