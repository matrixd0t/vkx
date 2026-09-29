from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    GlobalSearchFilters,
    GroupFull,
    MarketAlbum,
    MarketCategoryTree,
    MarketItem,
    MarketItemBasicWithGroup,
    MarketItemFull,
    MarketOrder,
    OrderItem,
    Photo,
    Property,
    ServicesViewType,
    UserFull,
    WallComment,
)


class MarketAddAlbumResponseModel(BaseModel):
    market_album_id: int | None = Field(
        default=None,
    )
    albums_count: int | None = Field(
        default=None,
    )

class AddPropertyVariantResponseModel(BaseModel):
    variant_id: int = Field()

class AddPropertyResponseModel(BaseModel):
    property_id: int = Field()

class MarketAddResponseModel(BaseModel):
    market_item_id: int = Field()

class GetAlbumByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketAlbum"] = Field()

class MarketGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketAlbum"] = Field()

class MarketGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketItemFull"] = Field()

class MarketGetByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketItem"] = Field()

class GetCategoriesNewResponseModel(BaseModel):
    items: list["MarketCategoryTree"] = Field()

class MarketGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallComment"] = Field()
    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )

class GetFavesForAttachResponseModel(BaseModel):
    market_items: list["MarketItem"] = Field()
    next_from: int | None = Field(
        default=None,
    )

class GetGroupOrdersResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()

class GetOrderByIdResponseModel(BaseModel):
    order: "MarketOrder | None" = Field(
        default=None,
    )

class GetOrderItemsResponseModel(BaseModel):
    count: int = Field()
    items: list["OrderItem"] = Field()

class GetOrdersExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()
    groups: list["GroupFull"] | None = Field(
        default=None,
    )

class GetOrdersResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()

class GetPropertiesResponseModel(BaseModel):
    items: list["Property"] = Field()
    count: int = Field()

class MarketGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketItemFull"] = Field()
    variants: list["MarketItemFull"] | None = Field(
        default=None,
    )

class MarketGetResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketItem"] = Field()
    variants: list["MarketItem"] | None = Field(
        default=None,
    )

class GroupItemsResponseModel(BaseModel):
    item_group_id: int = Field()

class PhotoIdResponseModel(BaseModel):
    photo_id: int = Field()
    photo: "Photo | None" = Field(
        default=None,
    )

class SearchBasicResponseModel(BaseModel):
    count: int = Field()
    total: int = Field()
    items: list["MarketItemBasicWithGroup"] = Field()
    has_more: bool | None = Field(
        default=None,
    )

class MarketSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    view_type: "ServicesViewType" = Field()
    items: list["MarketItemFull"] = Field()
    variants: list["MarketItemFull"] | None = Field(
        default=None,
    )

class MarketSearchResponseModel(BaseModel):
    count: int = Field()
    view_type: "ServicesViewType" = Field()
    items: list["MarketItem"] = Field()
    variants: list["MarketItem"] | None = Field(
        default=None,
    )
    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    filters: "GlobalSearchFilters | None" = Field(
        default=None,
    )

__all__ = (
    "AddPropertyResponseModel",
    "AddPropertyVariantResponseModel",
    "GetAlbumByIdResponseModel",
    "GetCategoriesNewResponseModel",
    "GetFavesForAttachResponseModel",
    "GetGroupOrdersResponseModel",
    "GetOrderByIdResponseModel",
    "GetOrderItemsResponseModel",
    "GetOrdersExtendedResponseModel",
    "GetOrdersResponseModel",
    "GetPropertiesResponseModel",
    "GroupItemsResponseModel",
    "MarketAddAlbumResponseModel",
    "MarketAddResponseModel",
    "MarketGetAlbumsResponseModel",
    "MarketGetByIdExtendedResponseModel",
    "MarketGetByIdResponseModel",
    "MarketGetCommentsResponseModel",
    "MarketGetExtendedResponseModel",
    "MarketGetResponseModel",
    "MarketSearchExtendedResponseModel",
    "MarketSearchResponseModel",
    "PhotoIdResponseModel",
    "SearchBasicResponseModel",
)
