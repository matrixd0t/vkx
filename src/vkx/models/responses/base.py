
from ..base_model import BaseEnumMeta, IntEnum


class OkResponseModel(IntEnum, metaclass=BaseEnumMeta):
    OK = 1


__all__ = (
    "OkResponseModel",
)
