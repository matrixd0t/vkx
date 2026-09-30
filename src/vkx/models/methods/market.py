import typing

from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.market import *  # type: ignore
from .base_category import BaseCategory


class MarketCategory(BaseCategory):
    async def add(
        self,
        category_id: int,
        description: str,
        name: str,
        owner_id: int,
        deleted: bool | None = None,
        dimension_height: int | None = None,
        dimension_length: int | None = None,
        dimension_width: int | None = None,
        is_main_variant: bool | None = None,
        main_photo_id: int | None = None,
        old_price: float | None = None,
        photo_ids: list[int] | None = None,
        price: float | None = None,
        sku: str | None = None,
        stock_amount: int | None = None,
        url: str | None = None,
        variant_ids: list[int] | None = None,
        video_ids: list[int] | None = None,
        weight: int | None = None,
    ) -> MarketAddResponseModel:
        """Method `market.add()`

        :param category_id: Item category ID.
        :param description: Item description.
        :param name: Item name.
        :param owner_id: ID of an item owner community.
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param dimension_height:
        :param dimension_length:
        :param dimension_width:
        :param is_main_variant: Is main in their group.
        :param main_photo_id: Cover photo ID.
        :param old_price:
        :param photo_ids: IDs of additional photos.
        :param price: Item price.
        :param sku:
        :param stock_amount:
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param video_ids: IDs of additional videos.
        :param weight:
        """

        return await self._call("market.add", locals(), MarketAddResponseModel)

    async def add_album(
        self,
        owner_id: int,
        title: str,
        is_hidden: bool | None = None,
        main_album: bool | None = None,
        photo_id: int | None = None,
    ) -> MarketAddAlbumResponseModel:
        """Method `market.addAlbum()`

        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param is_hidden: Set as hidden
        :param main_album: Set as main ('1' - set, '0' - no).
        :param photo_id: Cover photo ID.
        """

        return await self._call("market.addAlbum", locals(), MarketAddAlbumResponseModel)

    async def add_property(
        self,
        group_id: int,
        title: str,
    ) -> AddPropertyResponseModel:
        """Method `market.addProperty()`

        :param group_id: Group id.
        :param title: Property name.
        """

        return await self._call("market.addProperty", locals(), AddPropertyResponseModel)

    async def add_property_variant(
        self,
        group_id: int,
        property_id: int,
        title: str,
    ) -> AddPropertyVariantResponseModel:
        """Method `market.addPropertyVariant()`

        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Variant name.
        """

        return await self._call("market.addPropertyVariant", locals(), AddPropertyVariantResponseModel)

    async def add_to_album(
        self,
        album_ids: list[int],
        item_ids: list[int],
        owner_id: int,
    ) -> OkResponseModel:
        """Method `market.addToAlbum()`

        :param album_ids: Collections IDs to add item to.
        :param item_ids:
        :param owner_id: ID of an item owner community.
        """

        return await self._call("market.addToAlbum", locals(), OkResponseModel)

    async def create_comment(
        self,
        item_id: int,
        owner_id: int,
        attachments: list[str] | None = None,
        from_group: bool | None = None,
        guid: str | None = None,
        message: str | None = None,
        reply_to_comment: int | None = None,
        sticker_id: int | None = None,
    ) -> int:
        """Method `market.createComment()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param guid: Random value to avoid resending one comment.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        """

        return await self._call("market.createComment", locals(), int)

    async def delete(
        self,
        item_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `market.delete()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        """

        return await self._call("market.delete", locals(), OkResponseModel)

    async def delete_album(
        self,
        album_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `market.deleteAlbum()`

        :param album_id: Collection ID.
        :param owner_id: ID of an collection owner community.
        """

        return await self._call("market.deleteAlbum", locals(), OkResponseModel)

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: int,
    ) -> bool:
        """Method `market.deleteComment()`

        :param comment_id: comment id
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        """

        return await self._call("market.deleteComment", locals(), bool)

    async def delete_property(
        self,
        group_id: int,
        property_id: int,
    ) -> OkResponseModel:
        """Method `market.deleteProperty()`

        :param group_id: Group id.
        :param property_id: Property id.
        """

        return await self._call("market.deleteProperty", locals(), OkResponseModel)

    async def delete_property_variant(
        self,
        group_id: int,
        variant_id: int,
    ) -> OkResponseModel:
        """Method `market.deletePropertyVariant()`

        :param group_id: Group id.
        :param variant_id: Variant id.
        """

        return await self._call("market.deletePropertyVariant", locals(), OkResponseModel)

    async def edit(
        self,
        item_id: int,
        owner_id: int,
        category_id: int | None = None,
        deleted: bool | None = None,
        description: str | None = None,
        dimension_height: int | None = None,
        dimension_length: int | None = None,
        dimension_width: int | None = None,
        is_main_variant: bool | None = None,
        main_photo_id: int | None = None,
        name: str | None = None,
        old_price: float | None = None,
        photo_ids: list[int] | None = None,
        price: float | None = None,
        sku: str | None = None,
        stock_amount: int | None = None,
        url: str | None = None,
        variant_ids: list[int] | None = None,
        video_ids: list[int] | None = None,
        weight: int | None = None,
    ) -> OkResponseModel:
        """Method `market.edit()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param category_id: Item category ID.
        :param deleted: Item status ('1' - deleted, '0' - not deleted).
        :param description: Item description.
        :param dimension_height:
        :param dimension_length:
        :param dimension_width:
        :param is_main_variant: Is main in their group.
        :param main_photo_id: Cover photo ID.
        :param name: Item name.
        :param old_price:
        :param photo_ids: IDs of additional photos.
        :param price: Item price.
        :param sku:
        :param stock_amount:
        :param url: Url for button in market item.
        :param variant_ids: IDs of properties variants.
        :param video_ids: IDs of additional videos.
        :param weight:
        """

        return await self._call("market.edit", locals(), OkResponseModel)

    async def edit_album(
        self,
        album_id: int,
        owner_id: int,
        title: str,
        is_hidden: bool | None = None,
        main_album: bool | None = None,
        photo_id: int | None = None,
    ) -> OkResponseModel:
        """Method `market.editAlbum()`

        :param album_id: Collection ID.
        :param owner_id: ID of an collection owner community.
        :param title: Collection title.
        :param is_hidden: Set as hidden
        :param main_album: Set as main ('1' - set, '0' - no).
        :param photo_id: Cover photo id
        """

        return await self._call("market.editAlbum", locals(), OkResponseModel)

    async def edit_comment(
        self,
        comment_id: int,
        owner_id: int,
        attachments: list[str] | None = None,
        message: str | None = None,
    ) -> OkResponseModel:
        """Method `market.editComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of an item owner community.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        """

        return await self._call("market.editComment", locals(), OkResponseModel)

    async def edit_order(
        self,
        order_id: int,
        user_id: int,
        comment_for_user: str | None = None,
        delivery_price: int | None = None,
        height: int | None = None,
        length: int | None = None,
        merchant_comment: str | None = None,
        payment_status: str | None = None,
        receipt_link: str | None = None,
        status: int | None = None,
        track_number: str | None = None,
        weight: int | None = None,
        width: int | None = None,
    ) -> OkResponseModel:
        """Method `market.editOrder()`

        :param order_id:
        :param user_id:
        :param comment_for_user:
        :param delivery_price:
        :param height:
        :param length:
        :param merchant_comment:
        :param payment_status:
        :param receipt_link:
        :param status:
        :param track_number:
        :param weight:
        :param width:
        """

        return await self._call("market.editOrder", locals(), OkResponseModel)

    async def edit_property(
        self,
        group_id: int,
        property_id: int,
        title: str,
    ) -> OkResponseModel:
        """Method `market.editProperty()`

        :param group_id: Group id.
        :param property_id: Property id.
        :param title: Property name
        """

        return await self._call("market.editProperty", locals(), OkResponseModel)

    async def edit_property_variant(
        self,
        group_id: int,
        title: str,
        variant_id: int,
    ) -> OkResponseModel:
        """Method `market.editPropertyVariant()`

        :param group_id: Group id.
        :param title: Variant name.
        :param variant_id: Variant id.
        """

        return await self._call("market.editPropertyVariant", locals(), OkResponseModel)

    async def filter_categories(
        self,
        category_id: int | None = None,
        count: int | None = None,
        query: str | None = None,
    ) -> GetCategoriesNewResponseModel:
        """Method `market.filterCategories()`

        :param category_id: Category_id filter categories
        :param count: Number of results to return.
        :param query: Query filter categories
        """

        return await self._call("market.filterCategories", locals(), GetCategoriesNewResponseModel)

    @typing.overload
    async def get(
        self,
        owner_id: int,
        extended: typing.Literal[True],
        album_id: int | None = None,
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        fields: list[str] | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        with_disabled: bool | None = None,
    ) -> MarketGetExtendedResponseModel: ...

    @typing.overload
    async def get(
        self,
        owner_id: int,
        extended: typing.Literal[False] | None = None,
        album_id: int | None = None,
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        fields: list[str] | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        with_disabled: bool | None = None,
    ) -> MarketGetResponseModel: ...

    async def get(
        self,
        owner_id: int,
        extended: bool | None = None,
        album_id: int | None = None,
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        fields: list[str] | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        with_disabled: bool | None = None,
    ) -> MarketGetResponseModel | MarketGetExtendedResponseModel:
        """Method `market.get()`

        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param extended: '1' - method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        :param album_id:
        :param count: Number of items to return.
        :param date_from: Items update date from (format: yyyy-mm-dd)
        :param date_to: Items update date to (format: yyyy-mm-dd)
        :param fields:
        :param need_variants: Add variants to response if exist
        :param offset: Offset needed to return a specific subset of results.
        :param with_disabled: Add disabled items to response
        """

        return await self._call(
            "market.get",
            locals(),
            dependent=((("extended",), MarketGetExtendedResponseModel),),
            default=MarketGetResponseModel,
        )

    async def get_album_by_id(
        self,
        album_ids: list[int],
        owner_id: int,
    ) -> GetAlbumByIdResponseModel:
        """Method `market.getAlbumById()`

        :param album_ids: collections identifiers to obtain data from
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        """

        return await self._call("market.getAlbumById", locals(), GetAlbumByIdResponseModel)

    async def get_albums(
        self,
        owner_id: int,
        count: int | None = None,
        offset: int | None = None,
    ) -> MarketGetAlbumsResponseModel:
        """Method `market.getAlbums()`

        :param owner_id: ID of an items owner community.
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        return await self._call("market.getAlbums", locals(), MarketGetAlbumsResponseModel)

    @typing.overload
    async def get_by_id(
        self,
        item_ids: list[str],
        extended: typing.Literal[True],
    ) -> MarketGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
        self,
        item_ids: list[str],
        extended: typing.Literal[False] | None = None,
    ) -> MarketGetByIdResponseModel: ...

    async def get_by_id(
        self,
        item_ids: list[str],
        extended: bool | None = None,
    ) -> MarketGetByIdResponseModel | MarketGetByIdExtendedResponseModel:
        """Method `market.getById()`

        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """

        return await self._call(
            "market.getById",
            locals(),
            dependent=((("extended",), MarketGetByIdExtendedResponseModel),),
            default=MarketGetByIdResponseModel,
        )

    async def get_categories(
        self,
        album_id: int | None = None,
        group_id: int | None = None,
    ) -> GetCategoriesNewResponseModel:
        """Method `market.getCategories()`

        :param album_id:
        :param group_id: Group Id.
        """

        return await self._call("market.getCategories", locals(), GetCategoriesNewResponseModel)

    async def get_comments(
        self,
        item_id: int,
        owner_id: int,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        need_likes: bool | None = None,
        offset: int | None = None,
        sort: str | None = None,
        start_comment_id: int | None = None,
    ) -> MarketGetCommentsResponseModel:
        """Method `market.getComments()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community
        :param count: Number of results to return.
        :param extended: '1' - comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.com/dev/fields|details]
        :param need_likes: '1' - to return likes info.
        :param offset:
        :param sort: Sort order ('asc' - from old to new, 'desc' - from new to old)
        :param start_comment_id: ID of a comment to start a list from (details below).
        """

        return await self._call("market.getComments", locals(), MarketGetCommentsResponseModel)

    async def get_faves_for_attach(
        self,
        count: int | None = None,
        current_group_id: int | None = None,
        offset: int | None = None,
        public_only: bool | None = None,
    ) -> GetFavesForAttachResponseModel:
        """Method `market.getFavesForAttach()`

        :param count: Number of users to return.
        :param current_group_id: Group which represents content
        :param offset: Offset needed to return a specific subset of users.
        :param public_only:
        """

        return await self._call("market.getFavesForAttach", locals(), GetFavesForAttachResponseModel)

    async def get_group_orders(
        self,
        count: int | None = None,
        group_id: int | str | None = None,
        offset: int | None = None,
    ) -> GetGroupOrdersResponseModel:
        """Method `market.getGroupOrders()`

        :param count:
        :param group_id: ID or groups domain
        :param offset:
        """

        return await self._call("market.getGroupOrders", locals(), GetGroupOrdersResponseModel)

    async def get_order_by_id(
        self,
        order_id: int,
        extended: bool | None = None,
        user_id: int | None = None,
    ) -> GetOrderByIdResponseModel:
        """Method `market.getOrderById()`

        :param order_id:
        :param extended:
        :param user_id:
        """

        return await self._call("market.getOrderById", locals(), GetOrderByIdResponseModel)

    async def get_order_items(
        self,
        order_id: int,
        count: int | None = None,
        offset: int | None = None,
        user_id: int | None = None,
    ) -> GetOrderItemsResponseModel:
        """Method `market.getOrderItems()`

        :param order_id:
        :param count:
        :param offset:
        :param user_id:
        """

        return await self._call("market.getOrderItems", locals(), GetOrderItemsResponseModel)

    @typing.overload
    async def get_orders(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        offset: int | None = None,
    ) -> GetOrdersExtendedResponseModel: ...

    @typing.overload
    async def get_orders(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        offset: int | None = None,
    ) -> GetOrdersResponseModel: ...

    async def get_orders(
        self,
        extended: bool | None = None,
        count: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        offset: int | None = None,
    ) -> GetOrdersResponseModel | GetOrdersExtendedResponseModel:
        """Method `market.getOrders()`

        :param extended:
        :param count:
        :param date_from: Orders status updated date from (format: yyyy-mm-dd)
        :param date_to: Orders status updated date to (format: yyyy-mm-dd)
        :param offset:
        """

        return await self._call(
            "market.getOrders",
            locals(),
            dependent=((("extended",), GetOrdersExtendedResponseModel),),
            default=GetOrdersResponseModel,
        )

    async def get_product_photo_upload_server(
        self,
        group_id: int,
        bulk: bool | None = None,
    ) -> "UploadServer":
        """Method `market.getProductPhotoUploadServer()`

        :param group_id: Community ID.
        :param bulk:
        """

        return await self._call("market.getProductPhotoUploadServer", locals(), UploadServer)

    async def get_properties(
        self,
        group_id: int,
    ) -> GetPropertiesResponseModel:
        """Method `market.getProperties()`

        :param group_id:
        """

        return await self._call("market.getProperties", locals(), GetPropertiesResponseModel)

    async def group_items(
        self,
        group_id: int,
        item_ids: list[int],
        item_group_id: int | None = None,
    ) -> GroupItemsResponseModel:
        """Method `market.groupItems()`

        :param group_id: Group id.
        :param item_ids: Item ids.
        :param item_group_id: Items group id.
        """

        return await self._call("market.groupItems", locals(), GroupItemsResponseModel)

    async def remove_from_album(
        self,
        album_ids: list[int],
        item_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `market.removeFromAlbum()`

        :param album_ids: Collections IDs to remove item from.
        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        """

        return await self._call("market.removeFromAlbum", locals(), OkResponseModel)

    async def reorder_albums(
        self,
        album_id: int,
        owner_id: int,
        after: int | None = None,
        before: int | None = None,
    ) -> OkResponseModel:
        """Method `market.reorderAlbums()`

        :param album_id: Collection ID.
        :param owner_id: ID of an item owner community.
        :param after: ID of a collection to place current collection after it.
        :param before: ID of a collection to place current collection before it.
        """

        return await self._call("market.reorderAlbums", locals(), OkResponseModel)

    async def reorder_items(
        self,
        item_id: int,
        owner_id: int,
        after: int | None = None,
        album_id: int | None = None,
        before: int | None = None,
    ) -> OkResponseModel:
        """Method `market.reorderItems()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param after: ID of an item to place current item after it.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param before: ID of an item to place current item before it.
        """

        return await self._call("market.reorderItems", locals(), OkResponseModel)

    async def report(
        self,
        item_id: int,
        owner_id: int,
        reason: int | None = None,
    ) -> OkResponseModel:
        """Method `market.report()`

        :param item_id: Item ID.
        :param owner_id: ID of an item owner community.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """

        return await self._call("market.report", locals(), OkResponseModel)

    async def report_comment(
        self,
        comment_id: int,
        owner_id: int,
        reason: int,
    ) -> OkResponseModel:
        """Method `market.reportComment()`

        :param comment_id: Comment ID.
        :param owner_id: ID of an item owner community.
        :param reason: Complaint reason. Possible values: *'0' - spam,, *'1' - child porn,, *'2' - extremism,, *'3' - violence,, *'4' - drugs propaganda,, *'5' - adult materials,, *'6' - insult.
        """

        return await self._call("market.reportComment", locals(), OkResponseModel)

    async def restore(
        self,
        item_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `market.restore()`

        :param item_id: Deleted item ID.
        :param owner_id: ID of an item owner community.
        """

        return await self._call("market.restore", locals(), OkResponseModel)

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: int,
    ) -> bool:
        """Method `market.restoreComment()`

        :param comment_id: deleted comment id
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        """

        return await self._call("market.restoreComment", locals(), bool)

    async def save_product_photo(
        self,
        upload_response: str,
    ) -> PhotoIdResponseModel:
        """Method `market.saveProductPhoto()`

        :param upload_response: Upload response
        """

        return await self._call("market.saveProductPhoto", locals(), PhotoIdResponseModel)

    async def save_product_photo_bulk(
        self,
        upload_response: str,
    ) -> list[UploadPhotoData]:
        """Method `market.saveProductPhotoBulk()`

        :param upload_response: Upload response
        """

        return await self._call("market.saveProductPhotoBulk", locals(), list[UploadPhotoData])

    @typing.overload
    async def search(
        self,
        owner_id: int,
        extended: typing.Literal[True],
        album_id: int | None = None,
        count: int | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        price_from: int | None = None,
        price_to: int | None = None,
        q: str | None = None,
        rev: int | None = None,
        sort: int | None = None,
        status: list[int] | None = None,
    ) -> MarketSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        owner_id: int,
        extended: typing.Literal[False] | None = None,
        album_id: int | None = None,
        count: int | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        price_from: int | None = None,
        price_to: int | None = None,
        q: str | None = None,
        rev: int | None = None,
        sort: int | None = None,
        status: list[int] | None = None,
    ) -> MarketSearchResponseModel: ...

    async def search(
        self,
        owner_id: int,
        extended: bool | None = None,
        album_id: int | None = None,
        count: int | None = None,
        need_variants: bool | None = None,
        offset: int | None = None,
        price_from: int | None = None,
        price_to: int | None = None,
        q: str | None = None,
        rev: int | None = None,
        sort: int | None = None,
        status: list[int] | None = None,
    ) -> MarketSearchExtendedResponseModel | MarketSearchResponseModel:
        """Method `market.search()`

        :param owner_id: ID of an items owner community.
        :param extended: '1' - to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param album_id:
        :param count: Number of items to return.
        :param need_variants: Add variants to response if exist
        :param offset: Offset needed to return a specific subset of results.
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param q: Search query, for example "pink slippers".
        :param rev: '0' - do not use reverse order, '1' - use reverse order
        :param sort:
        :param status:
        """

        return await self._call(
            "market.search",
            locals(),
            dependent=((("extended",), MarketSearchExtendedResponseModel),),
            default=MarketSearchResponseModel,
        )

    async def search_items(
        self,
        q: str,
        category_id: int | None = None,
        city: int | None = None,
        count: int | None = None,
        country: int | None = None,
        offset: int | None = None,
        price_from: int | None = None,
        price_to: int | None = None,
        sort_by: int | None = None,
        sort_direction: int | None = None,
    ) -> MarketSearchResponseModel:
        """Method `market.searchItems()`

        :param q:
        :param category_id:
        :param city:
        :param count:
        :param country:
        :param offset:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        """

        return await self._call("market.searchItems", locals(), MarketSearchResponseModel)

    async def search_items_basic(
        self,
        q: str,
        category_id: int | None = None,
        city: int | None = None,
        count: int | None = None,
        country: int | None = None,
        offset: int | None = None,
        only_my_groups: bool | None = None,
        price_from: int | None = None,
        price_to: int | None = None,
        sort_by: int | None = None,
        sort_direction: int | None = None,
    ) -> SearchBasicResponseModel:
        """Method `market.searchItemsBasic()`

        :param q:
        :param category_id:
        :param city:
        :param count:
        :param country:
        :param offset:
        :param only_my_groups:
        :param price_from:
        :param price_to:
        :param sort_by:
        :param sort_direction:
        """

        return await self._call("market.searchItemsBasic", locals(), SearchBasicResponseModel)

    async def ungroup_items(
        self,
        group_id: int,
        item_group_id: int,
    ) -> OkResponseModel:
        """Method `market.ungroupItems()`

        :param group_id: Group id.
        :param item_group_id: Items group id.
        """

        return await self._call("market.ungroupItems", locals(), OkResponseModel)


__all__ = ("MarketCategory",)
