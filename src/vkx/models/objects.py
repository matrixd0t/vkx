import datetime
import json
import typing

import pydantic

from .base_model import (
    BaseEnumMeta,
    BaseModel,
    Field,
    IntEnum,
    StrEnum,
    attachment_string,
)


class BoolInt(IntEnum, metaclass=BaseEnumMeta):
    NO = 0
    YES = 1


class BaseCity(BaseModel):
    """Model: `BaseCity`"""

    id: int = Field()
    """City ID."""

    title: str = Field()
    """City title."""


class CommentsInfo(BaseModel):
    """Model: `CommentsInfo`"""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    can_open: bool | None = Field(
        default=None,
    )
    """Property `CommentsInfo.can_open`."""

    can_close: bool | None = Field(
        default=None,
    )
    """Property `CommentsInfo.can_close`."""

    can_view: bool | None = Field(
        default=None,
    )
    """Information whether current user can view the comments."""

    count: int | None = Field(
        default=None,
    )
    """Comments number."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    donut: "WallpostCommentsDonut | None" = Field(
        default=None,
    )
    """Property `CommentsInfo.donut`."""

    list_: list["WallComment"] | None = Field(
        default=None,
        alias="list",
    )
    """Property `CommentsInfo.list`."""


class BaseCountry(BaseModel):
    """Model: `BaseCountry`"""

    id: int = Field()
    """Country ID."""

    title: str = Field()
    """Country title."""


class CropPhoto(BaseModel):
    """Model: `CropPhoto`"""
    crop: "CropPhotoCrop" = Field()
    """Property `CropPhoto.crop`."""
    rect: "CropPhotoRect" = Field()
    """Property `CropPhoto.rect`."""
    photo: 'Photo' = Field()


class CropPhotoCrop(BaseModel):
    """Model: `CropPhotoCrop`"""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class CropPhotoRect(BaseModel):
    """Model: `CropPhotoRect`"""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class ErrorInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_ERROR = "base_error"


class Error(BaseModel):
    """Model: `Error`"""

    inner_type: "ErrorInnerType" = Field()
    """Property `Error.inner_type`."""

    error_code: int = Field()
    """Error code."""

    error_subcode: int | None = Field(
        default=None,
    )
    """Error subcode."""

    error_msg: str | None = Field(
        default=None,
    )
    """Error message."""

    error_text: str | None = Field(
        default=None,
    )
    """Localized error message."""

    request_params: list["RequestParam"] | None = Field(
        default=None,
    )
    """Property `Error.request_params`."""


class BaseGeo(BaseModel):
    """Model: `BaseGeo`"""

    coordinates: "GeoCoordinates | None" = Field(
        default=None,
    )
    """Property `BaseGeo.coordinates`."""

    place: "Place | None" = Field(
        default=None,
    )
    """Property `BaseGeo.place`."""

    showmap: int | None = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: str | None = Field(
        default=None,
    )
    """Place type."""


class GeoCoordinates(BaseModel):
    """Model: `GeoCoordinates`"""

    latitude: float = Field()
    """Property `GeoCoordinates.latitude`."""

    longitude: float = Field()
    """Property `GeoCoordinates.longitude`."""


class GradientPoint(BaseModel):
    """Model: `GradientPoint`"""

    color: str = Field()
    """Hex color code without #."""

    position: float = Field()
    """Point position."""


class ImageTheme(StrEnum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class BaseImage(BaseModel):
    """Model: `BaseImage`"""

    url: str = Field()
    """Image url."""

    width: int = Field()
    """Image width."""

    height: int = Field()
    """Image height."""

    id: str | None = Field(
        default=None,
    )
    """Property `BaseImage.id`."""

    theme: "ImageTheme | None" = Field(
        default=None,
    )
    """Property `BaseImage.theme`."""


class Lang(StrEnum, metaclass=BaseEnumMeta):
    RU = "ru"
    UA = "ua"
    BE = "be"
    EN = "en"
    ES = "es"
    FI = "fi"
    DE = "de"
    IT = "it"


class Likes(BaseModel):
    """Model: `Likes`"""

    count: int | None = Field(
        default=None,
    )
    """Likes number."""

    user_likes: bool | None = Field(
        default=None,
    )
    """Information whether current user likes the photo."""


class LikesInfo(BaseModel):
    """Model: `LikesInfo`"""

    can_like: bool = Field()
    """Information whether current user can like the post."""

    count: int = Field()
    """Likes number."""

    user_likes: bool = Field()
    """Information whether current uer has liked the post."""

    can_publish: bool | None = Field(
        default=None,
    )
    """Information whether current user can repost."""

    can_like_as_author: bool | None = Field(
        default=None,
    )
    """Whether user can like comment as author."""

    can_like_by_group: bool | None = Field(
        default=None,
    )
    """Whether current owner of the group can like the reply."""

    author_liked: bool | None = Field(
        default=None,
    )
    """Information whether post author liked the reply."""

    group_liked: bool | None = Field(
        default=None,
    )
    """Information whether group liked the reply."""

    repost_disabled: bool | None = Field(
        default=None,
    )
    """Remove repost feature for post."""


class LinkApplication(BaseModel):
    """Model: `LinkApplication`"""

    app_id: float | None = Field(
        default=None,
    )
    """Application Id."""

    store: "LinkApplicationStore | None" = Field(
        default=None,
    )
    """Property `LinkApplication.store`."""


class LinkApplicationStore(BaseModel):
    """Model: `LinkApplicationStore`"""

    id: float | None = Field(
        default=None,
    )
    """Store Id."""

    name: str | None = Field(
        default=None,
    )
    """Store name."""


class LinkButton(BaseModel):
    """Model: `LinkButton`"""

    action: "LinkButtonAction | None" = Field(
        default=None,
    )
    """Button action."""

    title: str | None = Field(
        default=None,
    )
    """Button title."""

    block_id: str | None = Field(
        default=None,
    )
    """Target block id."""

    section_id: str | None = Field(
        default=None,
    )
    """Target section id."""

    artist_id: str | None = Field(
        default=None,
    )
    """artist id."""

    curator_id: int | None = Field(
        default=None,
    )
    """curator id."""

    album_id: int | None = Field(
        default=None,
    )
    """Video album id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    icon: str | None = Field(
        default=None,
    )
    """Button icon name, e.g. \'phone\' or \'gift\'."""

    style: "LinkButtonStyle | None" = Field(
        default=None,
    )
    """Property `LinkButton.style`."""

    audio_id: int | None = Field(
        default=None,
    )
    """Property `LinkButton.audio_id`."""

    hashtag: str | None = Field(
        default=None,
    )
    """Property `LinkButton.hashtag`."""


class LinkButtonAction(BaseModel):
    """Model: `LinkButtonAction`"""

    type: "LinkButtonActionType" = Field()
    """Property `LinkButtonAction.type`."""

    url: str | None = Field(
        default=None,
    )
    """Action URL."""

    consume_reason: str | None = Field(
        default=None,
    )
    """Property `LinkButtonAction.consume_reason`."""


class LinkButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    UPDATES = "updates"
    DEFAULT = "default"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    NEGATIVE = "negative"
    TERTIARY = "tertiary"
    FLOAT_BOTTOM = "float_bottom"
    CELL_BUTTON_CENTERED_ICON = "cell_button_centered_icon"
    BORDERLESS_WITH_ICON = "borderless_with_icon"
    GRAY = "gray"
    FLAT = "flat"
    OUTLINE_WITH_CHEVRON = "outline_with_chevron"
    INLINE = "inline"
    MODAL = "modal"
    RIGHT_BUTTON = "right_button"
    AFTER_TOOLBAR = "after_toolbar"


class LinkNoProduct(BaseModel):
    """Model: `LinkNoProduct`"""
    url: 'str' = Field()
    """Link URL."""
    application: "LinkApplication | None" = Field(
        default=None,
    )
    """Property `LinkNoProduct.application`."""
    button: "LinkButton | None" = Field(
        default=None,
    )
    """Property `LinkNoProduct.button`."""
    caption: 'str | None' = Field(
        default=None,
    )
    """Link caption."""
    description: 'str | None' = Field(
        default=None,
    )
    """Link description."""
    id: 'str | None' = Field(
        default=None,
    )
    """Link ID."""
    is_favorite: 'bool | None' = Field(
        default=None,
    )
    """Property `LinkNoProduct.is_favorite`."""
    preview_page: 'str | None' = Field(
        default=None,
    )
    """String ID of the page with article preview."""
    preview_url: 'str | None' = Field(
        default=None,
    )
    """URL of the page with article preview."""
    rating: "LinkRating | None" = Field(
        default=None,
    )
    """Property `LinkNoProduct.rating`."""
    title: 'str | None' = Field(
        default=None,
    )
    """Link title."""
    target_object: "LinkTargetObject | None" = Field(
        default=None,
    )
    """Property `LinkNoProduct.target_object`."""
    is_external: 'bool | None' = Field(
        default=None,
    )
    """Information whether the current link is external."""
    video: "VideoFull | None" = Field(
        default=None,
    )
    """Video from link."""
    photo: 'Photo | None' = None


class LinkProductType(StrEnum, metaclass=BaseEnumMeta):
    PRODUCT = "product"


class LinkProduct(BaseModel):
    """Model: `LinkProduct`"""

    price: "Price" = Field()
    """Property `LinkProduct.price`."""

    merchant: str | None = Field(
        default=None,
    )
    """Property `LinkProduct.merchant`."""

    category: "LinkProductCategory | None" = Field(
        default=None,
    )
    """Property `LinkProduct.category`."""

    geo: "GeoCoordinates | None" = Field(
        default=None,
    )
    """Property `LinkProduct.geo`."""

    distance: int | None = Field(
        default=None,
    )
    """Property `LinkProduct.distance`."""

    city: str | None = Field(
        default=None,
    )
    """Property `LinkProduct.city`."""

    status: "LinkProductStatus | None" = Field(
        default=None,
    )
    """Property `LinkProduct.status`."""

    orders_count: int | None = Field(
        default=None,
    )
    """Property `LinkProduct.orders_count`."""

    type: "LinkProductType | None" = Field(
        default=None,
    )
    """Property `LinkProduct.type`."""


class LinkProductCategory(BaseModel):
    """Model: `LinkProductCategory`"""


class LinkProductStatus(StrEnum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class LinkRatingType(StrEnum, metaclass=BaseEnumMeta):
    RATING = "rating"


class LinkRating(BaseModel):
    """Model: `LinkRating`"""

    reviews_count: int | None = Field(
        default=None,
    )
    """Count of reviews."""

    stars: float | None = Field(
        default=None,
    )
    """Count of stars."""

    type: "LinkRatingType | None" = Field(
        default=None,
    )
    """Property `LinkRating.type`."""


class MessageError(BaseModel):
    """Model: `MessageError`"""

    code: int | None = Field(
        default=None,
    )
    """Error code."""

    description: str | None = Field(
        default=None,
    )
    """Error message."""


class NameCase(StrEnum, metaclass=BaseEnumMeta):
    NOM = "Nom"
    GEN = "Gen"
    DAT = "Dat"
    ACC = "Acc"
    INS = "Ins"
    ABL = "Abl"


class BaseObject(BaseModel):
    """Model: `BaseObject`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class ObjectCount(BaseModel):
    """Model: `ObjectCount`"""

    count: int | None = Field(
        default=None,
    )
    """Items count."""


class ObjectWithName(BaseModel):
    """Model: `ObjectWithName`"""

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""


class OwnerCover(BaseModel):
    """Model: `OwnerCover`"""

    enabled: bool = Field()
    """Information whether cover is enabled."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `OwnerCover.images`."""

    crop_params: "OwnerCoverCropParams | None" = Field(
        default=None,
    )
    """Property `OwnerCover.crop_params`."""

    original_image: "BaseImage | None" = Field(
        default=None,
    )
    """Property `OwnerCover.original_image`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `OwnerCover.photo_id`."""


class OwnerCoverCropParams(BaseModel):
    """Model: `OwnerCoverCropParams`"""

    x: int | None = Field(
        default=None,
    )
    """Property `OwnerCoverCropParams.x`."""

    y: int | None = Field(
        default=None,
    )
    """Property `OwnerCoverCropParams.y`."""

    width: int | None = Field(
        default=None,
    )
    """Property `OwnerCoverCropParams.width`."""

    height: int | None = Field(
        default=None,
    )
    """Property `OwnerCoverCropParams.height`."""


class Place(BaseModel):
    """Model: `Place`"""

    address: str | None = Field(
        default=None,
    )
    """Place address."""

    checkins: int | None = Field(
        default=None,
    )
    """Checkins number."""

    city: str | None = Field(
        default=None,
    )
    """City name."""

    created: int | None = Field(
        default=None,
    )
    """Date of the place creation in Unixtime."""

    icon: str | None = Field(
        default=None,
    )
    """URL of the place\'s icon."""

    id: int | None = Field(
        default=None,
    )
    """Place ID."""

    latitude: float | None = Field(
        default=None,
    )
    """Place latitude."""

    longitude: float | None = Field(
        default=None,
    )
    """Place longitude."""

    title: str | None = Field(
        default=None,
    )
    """Place title."""

    type: str | None = Field(
        default=None,
    )
    """Place type."""


class PropertyExists(IntEnum, metaclass=BaseEnumMeta):
    PROPERTY_EXISTS = 1


class RepostsInfo(BaseModel):
    """Count of views
    Model: `RepostsInfo`
    """

    count: int = Field()
    """Total reposts counter. Sum of wall and mail reposts counters."""

    wall_count: int | None = Field(
        default=None,
    )
    """Wall reposts counter."""

    mail_count: int | None = Field(
        default=None,
    )
    """Mail reposts counter."""

    user_reposted: bool | None = Field(
        default=None,
    )
    """Information whether current user has reposted the post."""


class RequestParam(BaseModel):
    """Model: `RequestParam`"""

    key: str = Field()
    """Parameter name."""

    value: str = Field()
    """Parameter value."""


class Sex(IntEnum, metaclass=BaseEnumMeta):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class StickerInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class Sticker(BaseModel):
    """Model: `Sticker`"""

    inner_type: "StickerInnerType" = Field()
    """Property `Sticker.inner_type`."""

    sticker_id: int | None = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: int | None = Field(
        default=None,
    )
    """Pack ID."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `Sticker.images`."""

    images_with_background: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `Sticker.images_with_background`."""

    animation_url: str | None = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: list["StickerAnimation"] | None = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: bool | None = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class StickerAnimationType(StrEnum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class StickerAnimation(BaseModel):
    """Model: `StickerAnimation`"""

    type: "StickerAnimationType | None" = Field(
        default=None,
    )
    """Type of animation script."""

    url: str | None = Field(
        default=None,
    )
    """URL of animation script."""


class StickerNewInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class StickerNew(BaseModel):
    """Model: `StickerNew`"""

    inner_type: "StickerNewInnerType" = Field()
    """Property `StickerNew.inner_type`."""

    sticker_id: int | None = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: int | None = Field(
        default=None,
    )
    """Pack ID."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `StickerNew.images`."""

    images_with_background: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `StickerNew.images_with_background`."""

    animation_url: str | None = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: list["StickerAnimation"] | None = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: bool | None = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class UploadServer(BaseModel):
    """Model: `UploadServer`"""

    upload_url: str = Field()
    """Upload URL."""


class UserGroupFields(StrEnum, metaclass=BaseEnumMeta):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_BAN = "can_ban"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_BEST_FRIEND = "is_best_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_AVG_COLOR = "photo_avg_color"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    FIRST_NAME = "first_name"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_GEN = "first_name_gen"
    LAST_NAME = "last_name"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_GEN = "last_name_gen"
    CAN_SUBSCRIBE_STORIES = "can_subscribe_stories"
    IS_SUBSCRIBED_STORIES = "is_subscribed_stories"
    VK_ADMIN_STATUS = "vk_admin_status"
    CAN_UPLOAD_STORY = "can_upload_story"
    CLIPS_COUNT = "clips_count"
    IMAGE_STATUS = "image_status"
    IS_NFT = "is_nft"
    IS_NFT_PHOTO = "is_nft_photo"
    IS_VERIFIED = "is_verified"
    URL = "url"


class UserId(BaseModel):
    """Model: `UserId`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""


class Career(BaseModel):
    """Model: `Career`"""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    city_name: str | None = Field(
        default=None,
    )
    """City name."""

    company: str | None = Field(
        default=None,
    )
    """Company name."""

    from_: int | None = Field(
        default=None,
        alias="from",
    )
    """From year."""

    group_id: int | None = Field(
        default=None,
    )
    """Community ID."""

    id: int | None = Field(
        default=None,
    )
    """Career ID."""

    position: str | None = Field(
        default=None,
    )
    """Position."""

    until: int | None = Field(
        default=None,
    )
    """Till year."""


class Exports(BaseModel):
    """Model: `Exports`"""

    facebook: int | None = Field(
        default=None,
    )
    """Property `Exports.facebook`."""

    livejournal: int | None = Field(
        default=None,
    )
    """Property `Exports.livejournal`."""

    twitter: int | None = Field(
        default=None,
    )
    """Property `Exports.twitter`."""


class UsersFields(StrEnum, metaclass=BaseEnumMeta):
    FIRST_NAME_NOM = "first_name_nom"
    FIRST_NAME_GEN = "first_name_gen"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_INS = "first_name_ins"
    FIRST_NAME_ABL = "first_name_abl"
    LAST_NAME_NOM = "last_name_nom"
    LAST_NAME_GEN = "last_name_gen"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_INS = "last_name_ins"
    LAST_NAME_ABL = "last_name_abl"
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    BDATE_VISIBILITY = "bdate_visibility"
    CITY = "city"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO = "photo"
    PHOTO_REC = "photo_rec"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_BIG = "photo_big"
    PHOTO_MEDIUM = "photo_medium"
    PHOTO_MEDIUM_REC = "photo_medium_rec"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    THIRD_PARTY_BUTTONS = "third_party_buttons"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    LANGUAGE = "language"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    ONLINE_INFO = "online_info"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    WALL_DEFAULT = "wall_default"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    IS_NO_INDEX = "is_no_index"
    NO_INDEX = "no_index"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEE_GIFTS = "can_see_gifts"
    WORK = "work"
    PLACES = "places"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_BAN = "can_ban"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    IS_BEST_FRIEND = "is_best_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    VIDEO_LIVE = "video_live"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    CAN_SEE_WISHES = "can_see_wishes"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    ANIMATED_AVATAR = "animated_avatar"
    OWNER_STATE = "owner_state"
    IS_VERIFIED = "is_verified"
    OAUTH_LINKED = "oauth_linked"
    OAUTH_VERIFICATION = "oauth_verification"
    PROMOTION_ALLOWANCE = "promotion_allowance"


class LastSeen(BaseModel):
    """Model: `LastSeen`"""

    platform: int | None = Field(
        default=None,
    )
    """Type of the platform that used for the last authorization."""

    time: int | None = Field(
        default=None,
    )
    """Last visit date (in Unix time)."""


class Military(BaseModel):
    """Model: `Military`"""

    unit: str = Field()
    """Unit name."""

    unit_id: int = Field()
    """Unit ID."""

    from_: int | None = Field(
        default=None,
        alias="from",
    )
    """From year."""

    id: int | None = Field(
        default=None,
    )
    """Military ID."""

    until: int | None = Field(
        default=None,
    )
    """Till year."""


class OccupationType(StrEnum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    WORK = "work"


class Occupation(BaseModel):
    """Model: `Occupation`"""

    id: int | None = Field(
        default=None,
    )
    """ID of school, university, company group."""

    name: str | None = Field(
        default=None,
    )
    """Name of occupation."""

    type: "OccupationType | None" = Field(
        default=None,
    )
    """Type of occupation."""

    graduate_year: int | None = Field(
        default=None,
    )
    """Property `Occupation.graduate_year`."""

    city_id: int | None = Field(
        default=None,
    )
    """Property `Occupation.city_id`."""


class OnlineInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class OnlineInfo(BaseModel):
    """Model: `OnlineInfo`"""

    visible: bool = Field()
    """Whether you can see real online status of user or not."""

    last_seen: int | None = Field(
        default=None,
    )
    """Last time we saw user being active."""

    is_online: bool | None = Field(
        default=None,
    )
    """Whether user is currently online or not."""

    app_id: int | None = Field(
        default=None,
    )
    """Application id from which user is currently online or was last seen online."""

    is_mobile: bool | None = Field(
        default=None,
    )
    """Is user online from desktop app or mobile app."""

    status: "OnlineInfoStatus | None" = Field(
        default=None,
    )
    """In case user online is not visible, it indicates approximate timeframe of user online."""


class Personal(BaseModel):
    """Model: `Personal`"""

    alcohol: int | None = Field(
        default=None,
    )
    """User\'s views on alcohol."""

    inspired_by: str | None = Field(
        default=None,
    )
    """User\'s inspired by."""

    langs: list[str] | None = Field(
        default=None,
    )
    """Property `Personal.langs`."""

    langs_full: list["LanguageFull"] | None = Field(
        default=None,
    )
    """User\'s languages with full info."""

    life_main: int | None = Field(
        default=None,
    )
    """User\'s personal priority in life."""

    people_main: int | None = Field(
        default=None,
    )
    """User\'s personal priority in people."""

    political: int | None = Field(
        default=None,
    )
    """User\'s political views."""

    religion: str | None = Field(
        default=None,
    )
    """User\'s religion."""

    religion_id: int | None = Field(
        default=None,
    )
    """User\'s religion id."""

    smoking: int | None = Field(
        default=None,
    )
    """User\'s views on smoking."""


class RelativeType(StrEnum, metaclass=BaseEnumMeta):
    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class Relative(BaseModel):
    """Model: `Relative`"""

    type: "RelativeType" = Field()
    """Relative type."""

    birth_date: str | None = Field(
        default=None,
    )
    """Date of child birthday (format dd.mm.yyyy)."""

    id: int | None = Field(
        default=None,
    )
    """Relative ID."""

    name: str | None = Field(
        default=None,
    )
    """Name of relative."""


class UsersSchool(BaseModel):
    """Model: `UsersSchool`"""

    city: int | None = Field(
        default=None,
    )
    """City ID."""

    class_: str | None = Field(
        default=None,
        alias="class",
    )
    """School class letter."""

    class_id: int | None = Field(
        default=None,
    )
    """School class id."""

    id: str | None = Field(
        default=None,
    )
    """School ID."""

    name: str | None = Field(
        default=None,
    )
    """School name."""

    type: int | None = Field(
        default=None,
    )
    """School type ID."""

    type_str: str | None = Field(
        default=None,
    )
    """School type name."""

    year_from: int | None = Field(
        default=None,
    )
    """Year the user started to study."""

    year_graduated: int | None = Field(
        default=None,
    )
    """Graduation year."""

    year_to: int | None = Field(
        default=None,
    )
    """Year the user finished to study."""

    speciality: str | None = Field(
        default=None,
    )
    """Property `UsersSchool.speciality`."""


class UsersUniversity(BaseModel):
    """Model: `UsersUniversity`"""

    chair: int | None = Field(
        default=None,
    )
    """Chair ID."""

    chair_name: str | None = Field(
        default=None,
    )
    """Chair name."""

    city: int | None = Field(
        default=None,
    )
    """City ID."""

    education_form: str | None = Field(
        default=None,
    )
    """Education form."""

    education_form_id: int | None = Field(
        default=None,
    )
    """Education form id."""

    education_status: str | None = Field(
        default=None,
    )
    """Education status."""

    education_status_id: int | None = Field(
        default=None,
    )
    """Education status id."""

    faculty: int | None = Field(
        default=None,
    )
    """Faculty ID."""

    faculty_name: str | None = Field(
        default=None,
    )
    """Faculty name."""

    graduation: int | None = Field(
        default=None,
    )
    """Graduation year."""

    id: int | None = Field(
        default=None,
    )
    """University ID."""

    name: str | None = Field(
        default=None,
    )
    """University name."""

    university_group_id: int | None = Field(
        default=None,
    )
    """Property `UsersUniversity.university_group_id`."""


class UserConnections(BaseModel):
    """Model: `UserConnections`"""

    skype: str = Field()
    """User\'s Skype nickname."""

    facebook: str = Field()
    """User\'s Facebook account."""

    twitter: str = Field()
    """User\'s Twitter account."""

    instagram: str = Field()
    """User\'s Instagram account."""

    facebook_name: str | None = Field(
        default=None,
    )
    """User\'s Facebook name."""

    livejournal: str | None = Field(
        default=None,
    )
    """User\'s Livejournal account."""


class UserCounters(BaseModel):
    """Model: `UserCounters`"""

    albums: int | None = Field(
        default=None,
    )
    """Albums number."""

    badges: int | None = Field(
        default=None,
    )
    """Badges number."""

    audios: int | None = Field(
        default=None,
    )
    """Audios number."""

    followers: int | None = Field(
        default=None,
    )
    """Followers number."""

    friends: int | None = Field(
        default=None,
    )
    """Friends number."""

    gifts: int | None = Field(
        default=None,
    )
    """Gifts number."""

    groups: int | None = Field(
        default=None,
    )
    """Communities number."""

    notes: int | None = Field(
        default=None,
    )
    """Notes number."""

    online_friends: int | None = Field(
        default=None,
    )
    """Online friends number."""

    pages: int | None = Field(
        default=None,
    )
    """Public pages number."""

    photos: int | None = Field(
        default=None,
    )
    """Photos number."""

    subscriptions: int | None = Field(
        default=None,
    )
    """Subscriptions number."""

    user_photos: int | None = Field(
        default=None,
    )
    """Number of photos with user."""

    user_videos: int | None = Field(
        default=None,
    )
    """Number of videos with user."""

    videos: int | None = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: int | None = Field(
        default=None,
    )
    """Playlists number."""

    new_photo_tags: int | None = Field(
        default=None,
    )
    """Property `UserCounters.new_photo_tags`."""

    new_recognition_tags: int | None = Field(
        default=None,
    )
    """Property `UserCounters.new_recognition_tags`."""

    mutual_friends: int | None = Field(
        default=None,
    )
    """Property `UserCounters.mutual_friends`."""

    friends_followers: int | None = Field(
        default=None,
    )
    """Property `UserCounters.friends_followers`."""

    posts: int | None = Field(
        default=None,
    )
    """Property `UserCounters.posts`."""

    articles: int | None = Field(
        default=None,
    )
    """Property `UserCounters.articles`."""

    wishes: int | None = Field(
        default=None,
    )
    """Property `UserCounters.wishes`."""

    podcasts: int | None = Field(
        default=None,
    )
    """Property `UserCounters.podcasts`."""

    clips: int | None = Field(
        default=None,
    )
    """Property `UserCounters.clips`."""

    clips_followers: int | None = Field(
        default=None,
    )
    """Property `UserCounters.clips_followers`."""

    videos_followers: int | None = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: int | None = Field(
        default=None,
    )
    """Property `UserCounters.clips_views`."""

    clips_likes: int | None = Field(
        default=None,
    )
    """Property `UserCounters.clips_likes`."""


class UserMin(BaseModel):
    """Model: `UserMin`"""

    id: int = Field()
    """User ID."""

    deactivated: str | None = Field(
        default=None,
    )
    """Returns if a profile is deleted or blocked."""

    first_name: str | None = Field(
        default=None,
    )
    """User first name."""

    hidden: int | None = Field(
        default=None,
    )
    """Returns if a profile is hidden.."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    can_access_closed: bool | None = Field(
        default=None,
    )
    """Property `UserMin.can_access_closed`."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Property `UserMin.is_closed`."""


class UserRelation(IntEnum, metaclass=BaseEnumMeta):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


class UserSettingsXtr(BaseModel):
    """Model: `UserSettingsXtr`"""

    home_town: str = Field()
    """User\'s hometown."""

    status: str = Field()
    """User status."""

    connections: "UserConnections | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.connections`."""

    bdate: str | None = Field(
        default=None,
    )
    """User\'s date of birth."""

    bdate_visibility: int | None = Field(
        default=None,
    )
    """Information whether user\'s birthdate are hidden."""

    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.city`."""

    first_name: str | None = Field(
        default=None,
    )
    """User first name."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    maiden_name: str | None = Field(
        default=None,
    )
    """User maiden name."""

    name_request: "NameRequest | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.name_request`."""

    personal: "Personal | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.personal`."""

    phone: str | None = Field(
        default=None,
    )
    """User phone number with some hidden digits."""

    relation: "UserRelation | None" = Field(
        default=None,
    )
    """User relationship status."""

    relation_partner: "UserMin | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.relation_partner`."""

    relation_pending: bool | None = Field(
        default=None,
    )
    """Information whether relation status is pending."""

    relation_requests: list["UserMin"] | None = Field(
        default=None,
    )
    """Property `UserSettingsXtr.relation_requests`."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    sex: "Sex | None" = Field(
        default=None,
    )
    """User sex."""

    status_audio: "Audio | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.status_audio`."""

    interests: "UserSettingsInterests | None" = Field(
        default=None,
    )
    """Property `UserSettingsXtr.interests`."""

    languages: list[str] | None = Field(
        default=None,
    )
    """Property `UserSettingsXtr.languages`."""


class UserType(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"


class UsersArray(BaseModel):
    """Model: `UsersArray`"""

    count: int = Field()
    """Users number."""

    items: list[int] = Field()
    """Property `UsersArray.items`."""


class ActionOneOf(BaseModel):
    """Model: `ActionOneOf`"""

    type: "MessageActionStatus" = Field()
    """Property `ActionOneOf.type`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Message ID."""

    email: str | None = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""

    member_id: int | None = Field(
        default=None,
    )
    """User or email peer ID."""

    message: str | None = Field(
        default=None,
    )
    """Message body of related message."""

    photo: "MessageActionPhoto | None" = Field(
        default=None,
    )
    """Property `ActionOneOf.photo`."""

    text: str | None = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""


class AudioMessage(BaseModel):
    """Model: `AudioMessage`"""
    duration: 'int' = Field()
    """Audio message duration in seconds."""
    id: 'int' = Field()
    """Audio message ID."""
    link_mp3: 'str' = Field()
    """MP3 file URL."""
    link_ogg: 'str' = Field()
    """OGG file URL."""
    owner_id: 'int' = Field()
    """Audio message owner ID."""
    waveform: 'list[int]' = Field()
    """Property `AudioMessage.waveform`."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Access key for audio message."""
    transcript_error: 'int | None' = Field(
        default=None,
    )
    """Property `AudioMessage.transcript_error`."""
    transcript_state: 'str | None' = None
    transcript: 'str | None' = None

    @property
    def as_att(self) -> str:
        """Строка-вложение VK: ``audio_message{owner_id}_{id}[_{access_key}]``."""
        return attachment_string(
            "audio_message", self.owner_id, self.id, self.access_key
        )


class BaseMessage(BaseModel):
    """Model: `BaseMessage`"""

    conversation_message_id: int = Field()
    """Unique auto-incremented number for all messages with this peer."""

    date: datetime.datetime = Field()
    """Date when the message has been sent in Unixtime."""

    from_id: int = Field()
    """Message author\'s ID."""

    id: int = Field()
    """Message ID."""

    text: str = Field()
    """Message text."""

    version: int = Field()
    """Property `BaseMessage.version`."""

    out: bool = Field()
    """Information whether the message is outcoming."""

    peer_id: int = Field()
    """Peer ID."""

    action: "ActionOneOf | None" = Field(
        default=None,
    )
    """Property `BaseMessage.action`."""

    admin_author_id: int | None = Field(
        default=None,
    )
    """Only for messages from community. Contains user ID of community admin, who sent this message.."""

    attachments: list["MessageAttachment"] | None = Field(
        default=None,
    )
    """Property `BaseMessage.attachments`."""

    deleted: bool | None = Field(
        default=None,
    )
    """Is it an deleted message."""

    fwd_messages: "MessagesFwdMessages | None" = Field(
        default=None,
    )
    """Property `BaseMessage.fwd_messages`."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `BaseMessage.geo`."""

    is_cropped: bool | None = Field(
        default=None,
    )
    """this message is cropped for bot."""

    keyboard: "Keyboard | None" = Field(
        default=None,
    )
    """Property `BaseMessage.keyboard`."""

    payload: str | None = Field(
        default=None,
    )
    """Property `BaseMessage.payload`."""

    update_time: int | None = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""

    is_silent: bool | None = Field(
        default=None,
    )
    """Is silent message, push without sound."""

    is_unavailable: bool | None = Field(
        default=None,
    )
    """Is message unavailable for some reason, including its id equals 0."""

    random_id: int | None = Field(
        default=None,
    )
    """ID used for sending messages. It returned only for outgoing messages."""

    ref: str | None = Field(
        default=None,
    )
    """Property `BaseMessage.ref`."""

    ref_source: str | None = Field(
        default=None,
    )
    """Property `BaseMessage.ref_source`."""


class Chat(BaseModel):
    """Model: `Chat`"""

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: list[int] = Field()
    """Property `Chat.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: bool | None = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: bool | None = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: "ChatPushSettings | None" = Field(
        default=None,
    )
    """Property `Chat.push_settings`."""

    title: str | None = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """If chat is group channel."""


class ChatFull(BaseModel):
    """Model: `ChatFull`"""

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: list["UserXtrInvitedBy"] = Field()
    """Property `ChatFull.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: bool | None = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: bool | None = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: "ChatPushSettings | None" = Field(
        default=None,
    )
    """Property `ChatFull.push_settings`."""

    title: str | None = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """If chat is group channel."""


class ChatPreview(BaseModel):
    """Model: `ChatPreview`"""

    admin_id: int = Field()
    """Property `ChatPreview.admin_id`."""

    members: list[int] = Field()
    """Property `ChatPreview.members`."""

    title: str = Field()
    """Property `ChatPreview.title`."""

    joined: bool | None = Field(
        default=None,
    )
    """Property `ChatPreview.joined`."""

    local_id: int | None = Field(
        default=None,
    )
    """Property `ChatPreview.local_id`."""

    members_count: int | None = Field(
        default=None,
    )
    """Property `ChatPreview.members_count`."""

    is_member: bool | None = Field(
        default=None,
    )
    """Property `ChatPreview.is_member`."""

    photo: "ChatSettingsPhoto | None" = Field(
        default=None,
    )
    """Property `ChatPreview.photo`."""

    is_don: bool | None = Field(
        default=None,
    )
    """Property `ChatPreview.is_don`."""

    is_nft: bool | None = Field(
        default=None,
    )
    """Property `ChatPreview.is_nft`."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """Property `ChatPreview.is_group_channel`."""

    button: "LinkButton | None" = Field(
        default=None,
    )
    """Property `ChatPreview.button`."""


class ChatPushSettings(BaseModel):
    """Model: `ChatPushSettings`"""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until that notifications are disabled."""

    sound: bool | None = Field(
        default=None,
    )
    """Information whether the sound is on."""


class ChatRestrictions(BaseModel):
    """Model: `ChatRestrictions`"""

    admins_promote_users: bool | None = Field(
        default=None,
    )
    """Only admins can promote users to admins."""

    only_admins_edit_info: bool | None = Field(
        default=None,
    )
    """Only admins can change chat info."""

    only_admins_edit_pin: bool | None = Field(
        default=None,
    )
    """Only admins can edit pinned message."""

    only_admins_invite: bool | None = Field(
        default=None,
    )
    """Only admins can invite users to this chat."""

    only_admins_kick: bool | None = Field(
        default=None,
    )
    """Only admins can kick users from this chat."""


class ChatSettings(BaseModel):
    """Model: `ChatSettings`"""

    owner_id: int = Field()
    """Property `ChatSettings.owner_id`."""

    title: str = Field()
    """Chat title."""

    state: "ChatSettingsState" = Field()
    """Property `ChatSettings.state`."""

    acl: "ChatSettingsAcl" = Field()
    """Property `ChatSettings.acl`."""

    members_count: int | None = Field(
        default=None,
    )
    """Property `ChatSettings.members_count`."""

    friends_count: int | None = Field(
        default=None,
    )
    """Property `ChatSettings.friends_count`."""

    pinned_messages_count: int | None = Field(
        default=None,
    )
    """Property `ChatSettings.pinned_messages_count`."""

    pinned_message: "PinnedMessage | None" = Field(
        default=None,
    )
    """Property `ChatSettings.pinned_message`."""

    photo: "ChatSettingsPhoto | None" = Field(
        default=None,
    )
    """Property `ChatSettings.photo`."""

    admin_ids: list[int] | None = Field(
        default=None,
    )
    """Ids of chat admins."""

    active_ids: list[int] | None = Field(
        default=None,
    )
    """Property `ChatSettings.active_ids`."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """Property `ChatSettings.is_group_channel`."""

    permissions: "ChatSettingsPermissions | None" = Field(
        default=None,
    )
    """Property `ChatSettings.permissions`."""

    is_disappearing: bool | None = Field(
        default=None,
    )
    """Property `ChatSettings.is_disappearing`."""

    theme: str | None = Field(
        default=None,
    )
    """Property `ChatSettings.theme`."""

    disappearing_chat_link: str | None = Field(
        default=None,
    )
    """Property `ChatSettings.disappearing_chat_link`."""

    is_service: bool | None = Field(
        default=None,
    )
    """Property `ChatSettings.is_service`."""


class ChatSettingsAcl(BaseModel):
    """Model: `ChatSettingsAcl`"""

    can_change_info: bool = Field()
    """Can you change photo, description and name."""

    can_change_invite_link: bool = Field()
    """Can you change invite link for this chat."""

    can_change_pin: bool = Field()
    """Can you pin/unpin message for this chat."""

    can_invite: bool = Field()
    """Can you invite other peers in chat."""

    can_promote_users: bool = Field()
    """Can you promote simple users to chat admins."""

    can_see_invite_link: bool = Field()
    """Can you see invite link for this chat."""

    can_moderate: bool = Field()
    """Can you moderate (delete) other users\' messages."""

    can_copy_chat: bool = Field()
    """Can you copy chat."""

    can_call: bool = Field()
    """Can you init group call in the chat."""

    can_use_mass_mentions: bool = Field()
    """Can you use mass mentions."""

    can_change_service_type: bool | None = Field(
        default=None,
    )
    """Can you change chat service type."""


class ChatSettingsPermissionsInvite(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsChangeInfo(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsChangePin(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsUseMassMentions(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsSeeInviteLink(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsCall(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class ChatSettingsPermissionsChangeAdmins(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class ChatSettingsPermissions(BaseModel):
    """Model: `ChatSettingsPermissions`"""

    invite: "ChatSettingsPermissionsInvite | None" = Field(
        default=None,
    )
    """Who can invite users to chat."""

    change_info: "ChatSettingsPermissionsChangeInfo | None" = Field(
        default=None,
    )
    """Who can change chat info."""

    change_pin: "ChatSettingsPermissionsChangePin | None" = Field(
        default=None,
    )
    """Who can change pinned message."""

    use_mass_mentions: "ChatSettingsPermissionsUseMassMentions | None" = Field(
        default=None,
    )
    """Who can use mass mentions."""

    see_invite_link: "ChatSettingsPermissionsSeeInviteLink | None" = Field(
        default=None,
    )
    """Who can see invite link."""

    call: "ChatSettingsPermissionsCall | None" = Field(
        default=None,
    )
    """Who can make calls."""

    change_admins: "ChatSettingsPermissionsChangeAdmins | None" = Field(
        default=None,
    )
    """Who can change admins."""


class ChatSettingsPhoto(BaseModel):
    """Model: `ChatSettingsPhoto`"""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50px in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200px in width."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_default_call_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default call photo."""


class ChatSettingsState(StrEnum, metaclass=BaseEnumMeta):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"
    OUT = "out"


class ConversationSpecialServiceType(StrEnum, metaclass=BaseEnumMeta):
    BUSINESS_NOTIFY = "business_notify"


class Conversation(BaseModel):
    """Model: `Conversation`"""
    peer: "ConversationPeer" = Field()
    """Property `Conversation.peer`."""
    last_message_id: 'int' = Field()
    """ID of the last message in conversation."""
    last_conversation_message_id: 'int' = Field()
    """Conversation message ID of the last message in conversation."""
    in_read: 'int' = Field()
    """Last message user have read."""
    out_read: 'int' = Field()
    """Last outcoming message have been read by the opponent."""
    version: 'int' = Field()
    """Property `Conversation.version`."""
    sort_id: "ConversationSortId | None" = Field(
        default=None,
    )
    """Property `Conversation.sort_id`."""
    unread_count: 'int | None' = Field(
        default=None,
    )
    """Unread messages number."""
    is_marked_unread: 'bool | None' = Field(
        default=None,
    )
    """Is this conversation unread."""
    out_read_by: "OutReadBy | None" = Field(
        default=None,
    )
    """Property `Conversation.out_read_by`."""
    important: 'bool | None' = Field(
        default=None,
    )
    """Property `Conversation.important`."""
    unanswered: 'bool | None' = Field(
        default=None,
    )
    """Property `Conversation.unanswered`."""
    special_service_type: "ConversationSpecialServiceType | None" = Field(
        default=None,
    )
    """Property `Conversation.special_service_type`."""
    message_request_data: "MessageRequestData | None" = Field(
        default=None,
    )
    """Property `Conversation.message_request_data`."""
    mentions: 'list[int] | None' = Field(
        default=None,
    )
    """Ids of messages with mentions."""
    current_keyboard: "Keyboard | None" = Field(
        default=None,
    )
    """Property `Conversation.current_keyboard`."""
    push_settings: "MessagesPushSettings | None" = Field(
        default=None,
    )
    """Property `Conversation.push_settings`."""
    can_write: "ConversationCanWrite | None" = Field(
        default=None,
    )
    """Property `Conversation.can_write`."""
    chat_settings: "ChatSettings | None" = Field(
        default=None,
    )
    """Property `Conversation.chat_settings`."""
    style: 'str | None' = Field(
        default=None,
    )
    """Property `Conversation.style`."""
    peer_flags: 'int | None' = Field(
        default=None,
    )
    """Property `Conversation.peer_flags`."""


class ConversationCanWrite(BaseModel):
    """Model: `ConversationCanWrite`"""

    allowed: bool = Field()
    """Property `ConversationCanWrite.allowed`."""

    reason: int | None = Field(
        default=None,
    )
    """Property `ConversationCanWrite.reason`."""

    until: int | None = Field(
        default=None,
    )
    """Property `ConversationCanWrite.until`."""


class ConversationMember(BaseModel):
    """Model: `ConversationMember`"""

    member_id: int = Field()
    """Property `ConversationMember.member_id`."""

    can_kick: bool | None = Field(
        default=None,
    )
    """Is it possible for user to kick this member."""

    is_restricted_to_write: bool | None = Field(
        default=None,
    )
    """Does this member have write permission."""

    invited_by: int | None = Field(
        default=None,
    )
    """Property `ConversationMember.invited_by`."""

    is_admin: bool | None = Field(
        default=None,
    )
    """Property `ConversationMember.is_admin`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `ConversationMember.is_owner`."""

    is_message_request: bool | None = Field(
        default=None,
    )
    """Property `ConversationMember.is_message_request`."""

    join_date: datetime.datetime | None = Field(
        default=None,
    )
    """Property `ConversationMember.join_date`."""

    request_date: datetime.datetime | None = Field(
        default=None,
    )
    """Message request date."""


class ConversationPeer(BaseModel):
    """Model: `ConversationPeer`"""

    id: int = Field()
    """Property `ConversationPeer.id`."""

    type: "ConversationPeerType" = Field()
    """Property `ConversationPeer.type`."""

    local_id: int | None = Field(
        default=None,
    )
    """Property `ConversationPeer.local_id`."""


class ConversationPeerType(StrEnum, metaclass=BaseEnumMeta):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class ConversationSortId(BaseModel):
    """Model: `ConversationSortId`"""

    major_id: int = Field()
    """Major id for sorting conversations."""

    minor_id: int = Field()
    """Minor id for sorting conversations."""


class ConversationWithMessage(BaseModel):
    """Model: `ConversationWithMessage`"""

    conversation: "Conversation" = Field()
    """Property `ConversationWithMessage.conversation`."""

    last_message: "Message | None" = Field(
        default=None,
    )
    """Property `ConversationWithMessage.last_message`."""


class DeleteFullResponseItem(BaseModel):
    """Model: `DeleteFullResponseItem`"""

    peer_id: int | None = Field(
        default=None,
    )
    """Property `DeleteFullResponseItem.peer_id`."""

    message_id: int | None = Field(
        default=None,
    )
    """Property `DeleteFullResponseItem.message_id`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Property `DeleteFullResponseItem.conversation_message_id`."""

    response: bool | None = Field(
        default=None,
    )
    """Property `DeleteFullResponseItem.response`."""

    error: "MessageError | None" = Field(
        default=None,
    )
    """Property `DeleteFullResponseItem.error`."""


class ForeignMessage(BaseModel):
    """Model: `ForeignMessage`"""
    conversation_message_id: 'int' = Field()
    """Conversation message ID."""
    date: 'datetime.datetime' = Field()
    """Date when the message was created."""
    from_id: 'int' = Field()
    """Message author\'s ID."""
    text: 'str' = Field()
    """Message text."""
    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `ForeignMessage.geo`."""
    id: 'int | None' = Field(
        default=None,
    )
    """Message ID."""
    peer_id: 'int | None' = Field(
        default=None,
    )
    """Peer ID."""
    update_time: 'int | None' = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""
    was_listened: 'bool | None' = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""
    payload: 'str | None' = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""
    attachments: 'list[MessageAttachment] | None' = None
    reply_message: "ForeignMessage | None" = None
    fwd_messages: 'list["ForeignMessage"] | None' = None


class Forward(BaseModel):
    """Model: `Forward`"""

    owner_id: int | None = Field(
        default=None,
    )
    """Messages owner_id."""

    peer_id: int | None = Field(
        default=None,
    )
    """Messages peer_id."""

    conversation_message_ids: list[int] | None = Field(
        default=None,
    )
    """Property `Forward.conversation_message_ids`."""

    cmids: list[int] | None = Field(
        default=None,
    )
    """Property `Forward.cmids`."""

    message_ids: list[int] | None = Field(
        default=None,
    )
    """Property `Forward.message_ids`."""

    is_reply: bool | None = Field(
        default=None,
    )
    """If you need to reply to a message."""


type MessagesFwdMessages = list[list["ForeignMessage"]]


class GetConversationById(BaseModel):
    """Model: `GetConversationById`"""

    count: int = Field()
    """Total number."""

    items: list["Conversation"] = Field()
    """Property `GetConversationById.items`."""


class GetConversationMembers(BaseModel):
    """Model: `GetConversationMembers`"""

    items: list["ConversationMember"] = Field()
    """Property `GetConversationMembers.items`."""

    count: int = Field()
    """Chat members count."""

    chat_restrictions: "ChatRestrictions | None" = Field(
        default=None,
    )
    """Property `GetConversationMembers.chat_restrictions`."""

    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    """Property `GetConversationMembers.profiles`."""

    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    """Property `GetConversationMembers.groups`."""


class GetInviteLinkByOwnerResponseItem(BaseModel):
    """Model: `GetInviteLinkByOwnerResponseItem`"""

    owner_id: int = Field()
    """Property `GetInviteLinkByOwnerResponseItem.owner_id`."""

    link: str | None = Field(
        default=None,
    )
    """Property `GetInviteLinkByOwnerResponseItem.link`."""

    error: "MessageError | None" = Field(
        default=None,
    )
    """Property `GetInviteLinkByOwnerResponseItem.error`."""


class MessagesGraffiti(BaseModel):
    """Model: `MessagesGraffiti`"""

    id: int = Field()
    """Graffiti ID."""

    owner_id: int = Field()
    """Graffiti owner ID."""

    url: str = Field()
    """Graffiti URL."""

    width: int = Field()
    """Graffiti width."""

    height: int = Field()
    """Graffiti height."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for graffiti."""

    @property
    def as_att(self) -> str:
        """Строка-вложение VK: ``graffiti{owner_id}_{id}[_{access_key}]``."""
        return attachment_string("graffiti", self.owner_id, self.id, self.access_key)


class HistoryAttachment(BaseModel):
    """Model: `HistoryAttachment`"""

    attachment: "HistoryMessageAttachment" = Field()
    """Property `HistoryAttachment.attachment`."""

    date: datetime.datetime = Field()
    """Message sending time."""

    message_id: int = Field()
    """Message ID."""

    cmid: int = Field()
    """Conversation Message ID."""

    from_id: int = Field()
    """Message author\'s ID."""

    message_expire_ttl: int | None = Field(
        default=None,
    )
    """Message Exipire ttl."""

    forward_level: int | None = Field(
        default=None,
    )
    """Forward level (optional)."""

    was_listened: bool | None = Field(
        default=None,
    )
    """Property `HistoryAttachment.was_listened`."""

    position: int | None = Field(
        default=None,
    )
    """Attachment position in the Message."""


class HistoryMessageAttachment(BaseModel):
    """Model: `HistoryMessageAttachment`"""
    type: "HistoryMessageAttachmentType" = Field()
    """Property `HistoryMessageAttachment.type`."""
    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `HistoryMessageAttachment.audio`."""
    audio_message: "AudioMessage | None" = Field(
        default=None,
    )
    """Property `HistoryMessageAttachment.audio_message`."""
    doc: "Doc | None" = Field(
        default=None,
    )
    """Property `HistoryMessageAttachment.doc`."""
    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )
    """Property `HistoryMessageAttachment.graffiti`."""
    market: "MarketItem | None" = Field(
        default=None,
    )
    """Property `HistoryMessageAttachment.market`."""
    photo: 'Photo | None' = None


class HistoryMessageAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    APP_ACTION = "app_action"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    PHOTO = "photo"
    VIDEO = "video"
    WALL = "wall"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


def _dump_button_payload(value: typing.Any) -> str | None:
    """Привести payload кнопки к строке: dict/список -> компактный JSON, str — как есть."""
    if value is None or isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


ButtonPayload = typing.Annotated[str | None, pydantic.BeforeValidator(_dump_button_payload)]
"""Payload кнопки: принимается dict/список/str, хранится JSON-строкой."""

KEYBOARD_MAX_BUTTONS_ON_ROW: typing.Final = 5
KEYBOARD_MAX_ROWS_DEFAULT: typing.Final = 10
KEYBOARD_MAX_ROWS_INLINE: typing.Final = 6


class Keyboard(BaseModel):
    """Клавиатура VK: разбор входящих и сборка исходящих. Неизменяема.

    При сборке ``inline`` по умолчанию ``True``; для отправки —
    ``keyboard=keyboard.to_json()``. Для обычной (чатовой) клавиатуры
    передайте ``inline=False``.
    """

    buttons: list[list["KeyboardButton"]] = Field(default_factory=list)
    """Ряды кнопок (не более 5 кнопок в ряду)."""

    one_time: bool = Field(default=False)
    """Скрыть клавиатуру после первого нажатия."""

    inline: bool | None = Field(default=None)
    """Inline-клавиатура; при сборке по умолчанию ``True``."""

    author_id: int | None = Field(default=None)
    """Сообщество/бот, установившие клавиатуру (только для входящих)."""

    def __init__(
            self,
            buttons: list[list["KeyboardButton"]] | None = None,
            *,
            one_time: bool = False,
            inline: bool = True,
            author_id: int | None = None,
            **kwargs: typing.Any,
    ) -> None:
        super().__init__(
            buttons=[] if buttons is None else buttons,
            one_time=one_time,
            inline=inline,
            author_id=author_id,
            **kwargs,
        )

    @classmethod
    def from_rows(
            cls,
            rows: list[list["KeyboardButton"]],
            /,
            *,
            one_time: bool = False,
            inline: bool = True,
    ) -> typing.Self:
        """Собрать клавиатуру из рядов: ``Keyboard.from_rows([[b1, b2], [b3]])``."""
        return cls(rows, one_time=one_time, inline=inline)

    @pydantic.model_validator(mode="after")
    def _check_limits(self) -> typing.Self:
        max_rows = KEYBOARD_MAX_ROWS_INLINE if self.inline else KEYBOARD_MAX_ROWS_DEFAULT
        if len(self.buttons) > max_rows:
            kind = "inline" if self.inline else "обычной"
            raise ValueError(f"клавиатура: не больше {max_rows} рядов для {kind} клавиатуры")
        for index, row in enumerate(self.buttons):
            if not row:
                raise ValueError(f"клавиатура: ряд {index} пустой")
            if len(row) > KEYBOARD_MAX_BUTTONS_ON_ROW:
                raise ValueError(
                    f"клавиатура: в ряду {index} больше {KEYBOARD_MAX_BUTTONS_ON_ROW} кнопок"
                )
        return self

    def to_json(self) -> str:
        """Строка для параметра ``keyboard`` (компактная, без ``None``)."""
        return self.to_raw(exclude_none=True, exclude={"author_id"})


class KeyboardButtonColor(StrEnum, metaclass=BaseEnumMeta):
    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class KeyboardButton(BaseModel):
    """Кнопка клавиатуры. Неизменяема.

    Обычно собирается фабриками: ``KeyboardButton.callback(...)``,
    ``.text(...)``, ``.link(...)``, ``.location(...)``, ``.vkpay(...)``,
    ``.open_app(...)``, ``.open_photo(...)`` — либо через ``Button(...)``.
    При разборе действие выбирается по ``type``; неизвестные типы
    сохраняются как есть в ``KeyboardButtonPropertyAction``.
    """

    action: "ButtonAction" = Field()
    """Описание действия кнопки."""

    color: "KeyboardButtonColor | None" = Field(default=None)
    """Цвет кнопки."""

    @pydantic.model_validator(mode="before")
    @classmethod
    def _dispatch_action(cls, data: typing.Any) -> typing.Any:
        if isinstance(data, dict):
            action = data.get("action")
            if isinstance(action, dict):
                model = BUTTON_ACTION_MODELS.get(str(action.get("type")), KeyboardButtonPropertyAction)
                data = {**data, "action": model(**action)}
        return data

    @classmethod
    def callback(cls, label: str, payload: typing.Any = None, *, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Callback-кнопка: нажатие приходит событием, сообщение не отправляется."""
        return cls(action=KeyboardButtonActionCallback(label=label, payload=payload), color=color)

    @classmethod
    def text(cls, label: str, payload: typing.Any = None, *, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Текстовая кнопка: по нажатию отправляет текст как сообщение."""
        return cls(action=KeyboardButtonActionText(label=label, payload=payload), color=color)

    @classmethod
    def link(cls, label: str, link: str, *, payload: typing.Any = None, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Кнопка-ссылка."""
        return cls(action=KeyboardButtonActionOpenLink(label=label, link=link, payload=payload), color=color)

    @classmethod
    def location(cls, payload: typing.Any = None, *, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Кнопка отправки геолокации (занимает весь ряд)."""
        return cls(action=KeyboardButtonActionLocation(payload=payload), color=color)

    @classmethod
    def vkpay(cls, hash: str, *, payload: typing.Any = None, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Кнопка оплаты через VK Pay (занимает весь ряд)."""
        return cls(action=KeyboardButtonActionVkpay(hash=hash, payload=payload), color=color)

    @classmethod
    def open_app(
            cls,
            app_id: int,
            owner_id: int,
            label: str,
            *,
            hash: str | None = None,
            payload: typing.Any = None,
            color: "KeyboardButtonColor | None" = None,
    ) -> typing.Self:
        """Кнопка запуска VK Mini App (занимает весь ряд)."""
        return cls(
            action=KeyboardButtonActionOpenApp(app_id=app_id, owner_id=owner_id, label=label, hash=hash, payload=payload),
            color=color,
        )

    @classmethod
    def open_photo(cls, *, color: "KeyboardButtonColor | None" = None) -> typing.Self:
        """Кнопка открытия фото."""
        return cls(action=KeyboardButtonActionOpenPhoto(), color=color)


class Button(KeyboardButton):
    """Кнопка с удобным конструктором. Тип по умолчанию — ``callback``.

    ``Button("Да", payload={"cmd": "yes"})``; остальные типы через ``type=``:
    ``Button("Сайт", type="open_link", link="https://vk.com")``.
    """

    def __init__(
            self,
            label: str | None = None,
            *,
            type: str = "callback",
            payload: typing.Any = None,
            color: "KeyboardButtonColor | None" = None,
            action: "ButtonAction | None" = None,
            **fields: typing.Any,
    ) -> None:
        if action is None:
            action = BUTTON_ACTION_MODELS[str(type)](label=label, payload=payload, **fields)
        super().__init__(action=action, color=color)


class KeyboardButtonActionCallbackType(StrEnum, metaclass=BaseEnumMeta):
    CALLBACK = "callback"


class KeyboardButtonActionCallback(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionCallback`
    """

    label: str = Field()
    """Label for button."""

    type: "KeyboardButtonActionCallbackType" = Field(default=KeyboardButtonActionCallbackType.CALLBACK)
    """Property `KeyboardButtonActionCallback.type`."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonActionLocationType(StrEnum, metaclass=BaseEnumMeta):
    LOCATION = "location"


class KeyboardButtonActionLocation(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionLocation`
    """

    type: "KeyboardButtonActionLocationType" = Field(default=KeyboardButtonActionLocationType.LOCATION)
    """Property `KeyboardButtonActionLocation.type`."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonActionOpenAppType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_APP = "open_app"


class KeyboardButtonActionOpenApp(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionOpenApp`
    """

    app_id: int = Field()
    """Fragment value in app link like vk.com/app{app_id}_-654321#hash."""

    label: str = Field()
    """Label for button."""

    owner_id: int = Field()
    """Fragment value in app link like vk.com/app123456_{owner_id}#hash."""

    type: "KeyboardButtonActionOpenAppType" = Field(default=KeyboardButtonActionOpenAppType.OPEN_APP)
    """Property `KeyboardButtonActionOpenApp.type`."""

    hash: str | None = Field(default=None)
    """Fragment value in app link like vk.com/app123456_-654321#{hash}."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonActionOpenLinkType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_LINK = "open_link"


class KeyboardButtonActionOpenLink(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionOpenLink`
    """

    label: str = Field()
    """Label for button."""

    link: str = Field()
    """link for button."""

    type: "KeyboardButtonActionOpenLinkType" = Field(default=KeyboardButtonActionOpenLinkType.OPEN_LINK)
    """Property `KeyboardButtonActionOpenLink.type`."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonActionOpenPhotoType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_PHOTO = "open_photo"


class KeyboardButtonActionOpenPhoto(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionOpenPhoto`
    """

    type: "KeyboardButtonActionOpenPhotoType" = Field(default=KeyboardButtonActionOpenPhotoType.OPEN_PHOTO)
    """Property `KeyboardButtonActionOpenPhoto.type`."""


class KeyboardButtonActionTextType(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"


class KeyboardButtonActionText(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionText`
    """

    label: str = Field()
    """Label for button."""

    type: "KeyboardButtonActionTextType" = Field(default=KeyboardButtonActionTextType.TEXT)
    """Property `KeyboardButtonActionText.type`."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonActionVkpayType(StrEnum, metaclass=BaseEnumMeta):
    VKPAY = "vkpay"


class KeyboardButtonActionVkpay(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `KeyboardButtonActionVkpay`
    """

    hash: str = Field()
    """Fragment value in app link like vk.com/app123456_-654321#{hash}."""

    type: "KeyboardButtonActionVkpayType" = Field(default=KeyboardButtonActionVkpayType.VKPAY)
    """Property `KeyboardButtonActionVkpay.type`."""

    payload: ButtonPayload = Field(default=None)
    """Additional data sent along with message for developer convenience."""


class KeyboardButtonPropertyAction(BaseModel):
    """Fallback-действие: сохраняет неизвестные типы (``start``, ``open_modal_view``, ...)."""

    model_config = pydantic.ConfigDict(frozen=True, extra="allow", defer_build=True)

    label: str | None = Field(default=None)
    type: str = Field()
    payload: ButtonPayload = Field(default=None)


ButtonAction = (
        KeyboardButtonActionCallback
        | KeyboardButtonActionText
        | KeyboardButtonActionLocation
        | KeyboardButtonActionOpenLink
        | KeyboardButtonActionOpenApp
        | KeyboardButtonActionOpenPhoto
        | KeyboardButtonActionVkpay
        | KeyboardButtonPropertyAction
)
"""Действие кнопки: типизированный union с fallback на неизвестные типы."""

BUTTON_ACTION_MODELS: dict[str, type[BaseModel]] = {
    "callback": KeyboardButtonActionCallback,
    "text": KeyboardButtonActionText,
    "location": KeyboardButtonActionLocation,
    "open_link": KeyboardButtonActionOpenLink,
    "open_app": KeyboardButtonActionOpenApp,
    "open_photo": KeyboardButtonActionOpenPhoto,
    "vkpay": KeyboardButtonActionVkpay,
}
"""Соответствие ``type`` кнопки и её модели действия (для разбора)."""


class LastActivity(BaseModel):
    """Model: `LastActivity`"""

    online: bool = Field()
    """Information whether user is online."""

    time: int = Field()
    """Time when user was online in Unixtime."""


class LongpollMessages(BaseModel):
    """Model: `LongpollMessages`"""


class LongpollParams(BaseModel):
    """Model: `LongpollParams`"""

    server: str = Field()
    """Server URL."""

    key: str = Field()
    """Key."""

    ts: int = Field()
    """Timestamp."""

    pts: int | None = Field(
        default=None,
    )
    """Persistent timestamp."""


class MessageAction(BaseModel):
    """Model: `MessageAction`"""
    conversation_message_id: 'int | None' = Field(
        default=None,
    )
    """Message ID."""
    email: 'str | None' = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""
    member_id: 'int | None' = Field(
        default=None,
    )
    """User or email peer ID."""
    message: 'str | None' = Field(
        default=None,
    )
    """Message body of related message."""
    photo: "MessageActionPhoto | None" = Field(
        default=None,
    )
    """Property `MessageAction.photo`."""
    text: 'str | None' = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""
    type: 'MessageActionStatus'
    style: 'str | None' = None


class MessageActionPhoto(BaseModel):
    """Model: `MessageActionPhoto`"""

    photo_50: str = Field()
    """URL of the preview image with 50px in width."""

    photo_100: str = Field()
    """URL of the preview image with 100px in width."""

    photo_200: str = Field()
    """URL of the preview image with 200px in width."""


class MessageAttachment(BaseModel):
    """Model: `MessageAttachment`"""
    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.audio`."""
    call: "CallsCall | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.call`."""
    doc: "Doc | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.doc`."""
    gift: "Layout | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.gift`."""
    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.graffiti`."""
    market: "MarketItem | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.market`."""
    market_market_album: "MarketAlbum | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.market_market_album`."""
    wall_reply: "WallComment | None" = Field(
        default=None,
    )
    """Property `MessageAttachment.wall_reply`."""
    type: 'MessageAttachmentType'
    audio_message: 'AudioMessage | None' = None
    story: 'Story | None' = None
    group_call_in_progress: 'GroupCallInProgress | None' = None
    link: 'LinkAttachment | None' = None
    wall: 'WallpostFull | None' = None
    photo: 'Photo | None' = None
    mini_app: 'App | None' = None
    sticker: 'Sticker | None' = None
    video: 'VideoFull | None' = None
    poll: 'Poll | None' = None


class MessageRequestData(BaseModel):
    """Model: `MessageRequestData`"""

    status: str | None = Field(
        default=None,
    )
    """Status of message request."""

    inviter_id: int | None = Field(
        default=None,
    )
    """Message request sender id."""

    request_date: datetime.datetime | None = Field(
        default=None,
    )
    """Message request date."""


class MessagesArray(BaseModel):
    """Model: `MessagesArray`"""

    count: int | None = Field(
        default=None,
    )
    """Property `MessagesArray.count`."""

    items: list["Message"] | None = Field(
        default=None,
    )
    """Property `MessagesArray.items`."""


class OutReadBy(BaseModel):
    """Model: `OutReadBy`"""

    count: int | None = Field(
        default=None,
    )
    """Property `OutReadBy.count`."""

    member_ids: list[int] | None = Field(
        default=None,
    )
    """Property `OutReadBy.member_ids`."""


class PinnedMessage(BaseModel):
    """Model: `PinnedMessage`"""
    conversation_message_id: 'int' = Field()
    """Unique auto-incremented number for all messages with this peer."""
    id: 'int' = Field()
    """Message ID."""
    date: 'datetime.datetime' = Field()
    """Date when the message has been sent in Unixtime."""
    from_id: 'int' = Field()
    """Message author\'s ID."""
    peer_id: 'int' = Field()
    """Peer ID."""
    text: 'str' = Field()
    """Message text."""
    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `PinnedMessage.geo`."""
    keyboard: "Keyboard | None" = Field(
        default=None,
    )
    """Property `PinnedMessage.keyboard`."""
    out: 'bool | None' = Field(
        default=None,
    )
    """Information whether the message is outcoming."""
    important: 'bool | None' = Field(
        default=None,
    )
    """Is it an important message."""
    attachments: 'list[MessageAttachment] | None' = None
    reply_message: 'ForeignMessage | None' = None
    fwd_messages: 'list[ForeignMessage] | None' = None


class MessagesPushSettings(BaseModel):
    """Model: `MessagesPushSettings`"""

    disabled_forever: bool = Field()
    """Information whether push notifications are disabled forever."""

    no_sound: bool = Field()
    """Information whether the sound is on."""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until what notifications are disabled."""

    disabled_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled."""


class ReactionAssetItem(BaseModel):
    """Model: `ReactionAssetItem`"""

    reaction_id: int = Field()
    """Property `ReactionAssetItem.reaction_id`."""

    links: "ReactionAssetItemLinks" = Field()
    """Liks to reactions assets for each asset type."""


class ReactionAssetItemLinks(BaseModel):
    """Model: `ReactionAssetItemLinks`"""

    big_animation: str = Field()
    """Big reaction animation json file."""

    small_animation: str = Field()
    """Small reaction animation json file."""

    static: str = Field()
    """Reaction image file."""


class ReactionCounterResponseItem(BaseModel):
    """Model: `ReactionCounterResponseItem`"""

    reaction_id: int = Field()
    """Property `ReactionCounterResponseItem.reaction_id`."""

    count: int = Field()
    """Property `ReactionCounterResponseItem.count`."""

    user_ids: list[int] = Field()
    """Property `ReactionCounterResponseItem.user_ids`."""


class ReactionCountersResponseItem(BaseModel):
    """Model: `ReactionCountersResponseItem`"""

    cmid: int = Field()
    """Property `ReactionCountersResponseItem.cmid`."""

    counters: list["ReactionCounterResponseItem"] = Field()
    """Property `ReactionCountersResponseItem.counters`."""


class ReactionResponseItem(BaseModel):
    """Model: `ReactionResponseItem`"""

    user_id: int = Field()
    """Property `ReactionResponseItem.user_id`."""

    reaction_id: int = Field()
    """Property `ReactionResponseItem.reaction_id`."""


class TemplateActionTypeNames(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"
    INTENT_SUBSCRIBE = "intent_subscribe"
    INTENT_UNSUBSCRIBE = "intent_unsubscribe"
    OPEN_MODAL_VIEW = "open_modal_view"


class UserTypeForXtrInvitedBy(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"


class AccountCounters(BaseModel):
    """Model: `AccountCounters`"""

    app_requests: int | None = Field(
        default=None,
    )
    """New app requests number."""

    events: int | None = Field(
        default=None,
    )
    """New events number."""

    faves: int | None = Field(
        default=None,
    )
    """New faves number."""

    friends: int | None = Field(
        default=None,
    )
    """New friends requests number."""

    friends_recommendations: int | None = Field(
        default=None,
    )
    """New friends recommendations number."""

    gifts: int | None = Field(
        default=None,
    )
    """New gifts number."""

    groups: int | None = Field(
        default=None,
    )
    """New groups number."""

    messages: int | None = Field(
        default=None,
    )
    """New messages number. Will be removed when messages.getCounters is released.."""

    memories: int | None = Field(
        default=None,
    )
    """New memories number."""

    notes: int | None = Field(
        default=None,
    )
    """New notes number."""

    notifications: int | None = Field(
        default=None,
    )
    """New notifications number."""

    photos: int | None = Field(
        default=None,
    )
    """New photo tags number."""


class CountersFilter(StrEnum, metaclass=BaseEnumMeta):
    APP_REQUESTS = "app_requests"
    EVENTS = "events"
    FRIENDS = "friends"
    FRIENDS_RECOMMENDATIONS = "friends_recommendations"
    GAMES = "games"
    GIFTS = "gifts"
    GROUPS = "groups"
    MESSAGES = "messages"
    NOTES = "notes"
    NOTIFICATIONS = "notifications"
    PHOTOS = "photos"
    FAVES = "faves"
    MEMORIES = "memories"


class AccountInfo(BaseModel):
    """Model: `AccountInfo`"""

    f__2fa_required: bool | None = Field(
        default=None,
        alias="2fa_required",
    )
    """Two factor authentication is enabled."""

    https_required: bool | None = Field(
        default=None,
    )
    """Information whether HTTPS-only is enabled."""

    intro: int | None = Field(
        default=None,
    )
    """Information whether user has been processed intro."""

    lang: int | None = Field(
        default=None,
    )
    """Language ID."""

    no_wall_replies: bool | None = Field(
        default=None,
    )
    """Information whether wall comments should be hidden."""

    own_posts_default: bool | None = Field(
        default=None,
    )
    """Information whether only owners posts should be shown."""


class NameRequest(BaseModel):
    """Model: `NameRequest`"""

    first_name: str | None = Field(
        default=None,
    )
    """First name in request."""

    id: int | None = Field(
        default=None,
    )
    """Request ID needed to cancel the request."""

    last_name: str | None = Field(
        default=None,
    )
    """Last name in request."""

    status: "NameRequestStatus | None" = Field(
        default=None,
    )
    """Property `NameRequest.status`."""

    lang: str | None = Field(
        default=None,
    )
    """Text to display to user."""

    link_href: str | None = Field(
        default=None,
    )
    """href for link in lang field."""

    link_label: str | None = Field(
        default=None,
    )
    """label to display for link in lang field."""


class NameRequestStatus(StrEnum, metaclass=BaseEnumMeta):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class OfferLinkType(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class Offer(BaseModel):
    """Model: `Offer`"""

    description: str | None = Field(
        default=None,
    )
    """Offer description."""

    id: int | None = Field(
        default=None,
    )
    """Offer ID."""

    img: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    instruction: str | None = Field(
        default=None,
    )
    """Instruction how to process the offer."""

    instruction_html: str | None = Field(
        default=None,
    )
    """Instruction how to process the offer (HTML format)."""

    price: int | None = Field(
        default=None,
    )
    """Offer price."""

    short_description: str | None = Field(
        default=None,
    )
    """Offer short description."""

    tag: str | None = Field(
        default=None,
    )
    """Offer tag."""

    title: str | None = Field(
        default=None,
    )
    """Offer title."""

    currency_amount: float | None = Field(
        default=None,
    )
    """Currency amount."""

    link_id: int | None = Field(
        default=None,
    )
    """Link id."""

    link_type: "OfferLinkType | None" = Field(
        default=None,
    )
    """Link type."""


class PushConversations(BaseModel):
    """Model: `PushConversations`"""

    count: int | None = Field(
        default=None,
    )
    """Items count."""

    items: list["PushConversationsItem"] | None = Field(
        default=None,
    )
    """Property `PushConversations.items`."""


class PushConversationsItem(BaseModel):
    """Model: `PushConversationsItem`"""

    disabled_until: int = Field()
    """Time until that notifications are disabled in seconds."""

    peer_id: int = Field()
    """Peer ID."""

    sound: bool = Field()
    """Information whether the sound are enabled."""

    disabled_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled. Can be affected by \'disabled_mentions\'."""


class PushParams(BaseModel):
    """Model: `PushParams`"""

    msg: list["PushParamsMode"] | None = Field(
        default=None,
    )
    """Property `PushParams.msg`."""

    chat: list["PushParamsMode"] | None = Field(
        default=None,
    )
    """Property `PushParams.chat`."""

    like: list["PushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `PushParams.like`."""

    repost: list["PushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `PushParams.repost`."""

    comment: list["PushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `PushParams.comment`."""

    mention: list["PushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `PushParams.mention`."""

    reply: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.reply`."""

    new_post: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.new_post`."""

    wall_post: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.wall_post`."""

    wall_publish: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.wall_publish`."""

    friend: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.friend`."""

    friend_found: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.friend_found`."""

    friend_accepted: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.friend_accepted`."""

    group_invite: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.group_invite`."""

    group_accepted: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.group_accepted`."""

    birthday: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.birthday`."""

    event_soon: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.event_soon`."""

    app_request: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.app_request`."""

    sdk_open: list["PushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `PushParams.sdk_open`."""


class PushParamsMode(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class PushParamsOnoff(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"


class PushParamsSettings(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"
    NO_SOUND = "no_sound"


class AccountPushSettings(BaseModel):
    """Model: `AccountPushSettings`"""

    disabled: bool | None = Field(
        default=None,
    )
    """Information whether notifications are disabled."""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until that notifications are disabled in Unixtime."""

    settings: "PushParams | None" = Field(
        default=None,
    )
    """Property `AccountPushSettings.settings`."""

    conversations: "PushConversations | None" = Field(
        default=None,
    )
    """Property `AccountPushSettings.conversations`."""


class UserSettingsInterest(BaseModel):
    """Model: `UserSettingsInterest`"""

    title: str = Field()
    """Property `UserSettingsInterest.title`."""

    value: str = Field()
    """Property `UserSettingsInterest.value`."""


class UserSettingsInterests(BaseModel):
    """Model: `UserSettingsInterests`"""

    activities: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.activities`."""

    interests: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.interests`."""

    music: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.music`."""

    tv: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.tv`."""

    movies: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.movies`."""

    books: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.books`."""

    games: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.games`."""

    quotes: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.quotes`."""

    about: "UserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `UserSettingsInterests.about`."""


class AddressFields(StrEnum, metaclass=BaseEnumMeta):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    CITY = "city"
    METRO_STATION_ID = "metro_station_id"
    METRO_STATION = "metro_station"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"


class AccessRole(StrEnum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AccessRolePublic(StrEnum, metaclass=BaseEnumMeta):
    MANAGER = "manager"
    REPORTS = "reports"


class Accesses(BaseModel):
    """Model: `Accesses`"""

    client_id: str | None = Field(
        default=None,
    )
    """Client ID."""

    role: "AccessRole | None" = Field(
        default=None,
    )
    """Property `Accesses.role`."""


class Account(BaseModel):
    """Model: `Account`"""

    access_role: "AccessRole" = Field()
    """Property `Account.access_role`."""

    account_id: int = Field()
    """Account ID."""

    account_status: bool = Field()
    """Information whether account is active."""

    account_type: "AccountType" = Field()
    """Property `Account.account_type`."""

    account_name: str = Field()
    """Account name."""

    can_view_budget: bool = Field()
    """Can user view account budget."""


class AccountType(StrEnum, metaclass=BaseEnumMeta):
    GENERAL = "general"
    AGENCY = "agency"


class Ad(BaseModel):
    """Model: `Ad`"""

    ad_format: int = Field()
    """Ad format."""

    ad_platform: int | str = Field()
    """Ad platform."""

    all_limit: str = Field()
    """Total limit."""

    approved: "AdApproved" = Field()
    """Property `Ad.approved`."""

    campaign_id: int = Field()
    """Campaign ID."""

    cost_type: "AdCostType" = Field()
    """Property `Ad.cost_type`."""

    id: int = Field()
    """Ad ID."""

    name: str = Field()
    """Ad title."""

    status: "AdStatus" = Field()
    """Property `Ad.status`."""

    category1_id: int | None = Field(
        default=None,
    )
    """Category ID."""

    category2_id: int | None = Field(
        default=None,
    )
    """Additional category ID."""

    cpc: str | None = Field(
        default=None,
    )
    """Cost of a click, kopecks."""

    cpm: str | None = Field(
        default=None,
    )
    """Cost of 1000 impressions, kopecks."""

    cpa: str | None = Field(
        default=None,
    )
    """Cost of an action, kopecks."""

    ocpm: str | None = Field(
        default=None,
    )
    """Cost of 1000 impressions optimized, kopecks."""

    autobidding: bool | None = Field(
        default=None,
    )
    """Autobidding."""

    autobidding_max_cost: str | None = Field(
        default=None,
    )
    """Max cost of target actions for autobidding, kopecks."""

    disclaimer_medical: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_specialist: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_supplements: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_credits: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    impressions_limit: int | None = Field(
        default=None,
    )
    """Impressions limit."""

    impressions_limit_period: int | None = Field(
        default=None,
    )
    """Impressions limit period."""

    impressions_limited: bool | None = Field(
        default=None,
    )
    """Information whether impressions are limited."""

    video: bool | None = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    day_limit: str | None = Field(
        default=None,
    )
    """Day limit."""

    goal_type: int | None = Field(
        default=None,
    )
    """Goal type."""

    user_goal_type: int | None = Field(
        default=None,
    )
    """User goal type."""

    age_restriction: int | None = Field(
        default=None,
    )
    """Age restriction."""

    conversion_pixel_id: int | None = Field(
        default=None,
    )
    """Conversion pixel id."""

    conversion_event_id: int | None = Field(
        default=None,
    )
    """Conversion event id."""

    create_time: int | None = Field(
        default=None,
    )
    """Create time."""

    update_time: int | None = Field(
        default=None,
    )
    """Update time."""

    start_time: int | None = Field(
        default=None,
    )
    """Start time."""

    stop_time: int | None = Field(
        default=None,
    )
    """Stop time."""

    publisher_platforms_auto: bool | None = Field(
        default=None,
    )
    """Publisher platform auto."""

    publisher_platforms: str | None = Field(
        default=None,
    )
    """Publisher platforms."""

    link_url: str | None = Field(
        default=None,
    )
    """Link url."""

    link_owner_id: int | None = Field(
        default=None,
    )
    """Link owner id."""

    link_id: int | None = Field(
        default=None,
    )
    """Link id."""

    has_campaign_budget_optimization: bool | None = Field(
        default=None,
    )
    """Has campaign budget optimization."""

    events_retargeting_groups: list["EventsRetargetingGroup"] | None = Field(
        default=None,
    )
    """Events retargeting groups."""

    weekly_schedule_hours: list[str] | None = Field(
        default=None,
    )
    """Weekly schedule hours."""

    weekly_schedule_use_holidays: int | None = Field(
        default=None,
    )
    """Weekly schedule use holidays."""

    ad_platform_no_ad_network: int | None = Field(
        default=None,
    )
    """Ad platform no ad network."""

    ad_platform_no_wall: int | None = Field(
        default=None,
    )
    """Ad platform no wall."""

    disclaimer_finance: int | None = Field(
        default=None,
    )
    """Disclaimer finance."""

    disclaimer_finance_name: str | None = Field(
        default=None,
    )
    """Disclaimer finance name."""

    disclaimer_finance_license_no: str | None = Field(
        default=None,
    )
    """Disclaimer finance license no."""

    is_promo: bool | None = Field(
        default=None,
    )
    """is promo."""

    suggested_criteria: int | None = Field(
        default=None,
    )
    """Suggested criteria."""

    link_type: int | None = Field(
        default=None,
    )
    """Link type."""


class AdApproved(IntEnum, metaclass=BaseEnumMeta):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdCostType(IntEnum, metaclass=BaseEnumMeta):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdLayout(BaseModel):
    """Model: `AdLayout`"""

    ad_format: int = Field()
    """Ad format."""

    campaign_id: int = Field()
    """Campaign ID."""

    cost_type: "AdCostType" = Field()
    """Property `AdLayout.cost_type`."""

    description: str = Field()
    """Ad description."""

    id: int = Field()
    """Ad ID."""

    image_src: str = Field()
    """Image URL."""

    link_url: str = Field()
    """URL of advertised object."""

    link_type: int = Field()
    """Type of advertised object."""

    title: str = Field()
    """Ad title."""

    image_src_2x: str | None = Field(
        default=None,
    )
    """URL of the preview image in double size."""

    link_domain: str | None = Field(
        default=None,
    )
    """Domain of advertised object."""

    preview_link: str | None = Field(
        default=None,
    )
    """link to preview an ad as it is shown on the website."""

    video: bool | None = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    social: bool | None = Field(
        default=None,
    )
    """Social."""

    okved: str | None = Field(
        default=None,
    )
    """Okved."""

    age_restriction: int | None = Field(
        default=None,
    )
    """Age restriction."""

    goal_type: int | None = Field(
        default=None,
    )
    """Goal type."""

    link_title: str | None = Field(
        default=None,
    )
    """Link title."""

    link_button: str | None = Field(
        default=None,
    )
    """Link button."""

    repeat_video: int | None = Field(
        default=None,
    )
    """Repeat video."""

    video_src_240: str | None = Field(
        default=None,
    )
    """Video source 240p."""

    video_src_360: str | None = Field(
        default=None,
    )
    """Video source 360p."""

    video_src_480: str | None = Field(
        default=None,
    )
    """Video source 480p."""

    video_src_720: str | None = Field(
        default=None,
    )
    """Video source 720p."""

    video_src_1080: str | None = Field(
        default=None,
    )
    """Video source 1080p."""

    video_src_1440: str | None = Field(
        default=None,
    )
    """Video source 1440p."""

    video_src_2160: str | None = Field(
        default=None,
    )
    """Video source 2160p."""

    video_image_src: str | None = Field(
        default=None,
    )
    """Video image source."""

    video_image_src_2x: str | None = Field(
        default=None,
    )
    """Video image source 2x."""

    video_duration: int | None = Field(
        default=None,
    )
    """Video duration."""

    icon_src: str | None = Field(
        default=None,
    )
    """Icon source."""

    icon_src_2x: str | None = Field(
        default=None,
    )
    """Icon source 2x."""

    post: "Post | None" = Field(
        default=None,
    )
    """Property `AdLayout.post`."""

    stories_data: "Stories | None" = Field(
        default=None,
    )
    """Property `AdLayout.stories_data`."""

    clips_list: list["ClipItem"] | None = Field(
        default=None,
    )
    """Property `AdLayout.clips_list`."""


class AdStatus(IntEnum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class Campaign(BaseModel):
    """Model: `Campaign`"""

    all_limit: str = Field()
    """Campaign\'s total limit, rubles."""

    day_limit: str = Field()
    """Campaign\'s day limit, rubles."""

    id: int = Field()
    """Campaign ID."""

    name: str = Field()
    """Campaign title."""

    start_time: int = Field()
    """Campaign start time, as Unixtime."""

    status: "CampaignStatus" = Field()
    """Property `Campaign.status`."""

    stop_time: int = Field()
    """Campaign stop time, as Unixtime."""

    type: "CampaignType" = Field()
    """Property `Campaign.type`."""

    ads_count: int | None = Field(
        default=None,
    )
    """Amount of active ads in campaign."""

    create_time: int | None = Field(
        default=None,
    )
    """Campaign create time, as Unixtime."""

    goal_type: int | None = Field(
        default=None,
    )
    """Campaign goal type."""

    user_goal_type: int | None = Field(
        default=None,
    )
    """Campaign user goal type."""

    is_cbo_enabled: bool | None = Field(
        default=None,
    )
    """Shows if Campaign Budget Optimization is on."""

    update_time: int | None = Field(
        default=None,
    )
    """Campaign update time, as Unixtime."""

    views_limit: int | None = Field(
        default=None,
    )
    """Limit of views per user per campaign."""


class CampaignStatus(IntEnum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class CampaignType(StrEnum, metaclass=BaseEnumMeta):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


class AdsCategory(BaseModel):
    """Model: `AdsCategory`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: list["AdsCategory"] | None = Field(
        default=None,
    )
    """Property `AdsCategory.subcategories`."""


class Client(BaseModel):
    """Model: `Client`"""

    all_limit: str = Field()
    """Client\'s total limit, rubles."""

    day_limit: str = Field()
    """Client\'s day limit, rubles."""

    id: int = Field()
    """Client ID."""

    name: str = Field()
    """Client name."""

    ord_data: "OrdData | None" = Field(
        default=None,
    )
    """Ord data."""


class ClipItem(BaseModel):
    """Model: `ClipItem`"""

    video_id: int | None = Field(
        default=None,
    )
    """Video id."""

    preview_url: str | None = Field(
        default=None,
    )
    """Preview url."""

    link: "ClipItemLink | None" = Field(
        default=None,
    )
    """Property `ClipItem.link`."""


class ClipItemLink(BaseModel):
    """Link
    Model: `ClipItemLink`
    """

    text: str | None = Field(
        default=None,
    )
    """Text."""

    key: str | None = Field(
        default=None,
    )
    """Key."""

    url: str | None = Field(
        default=None,
    )
    """Url."""


class CreateAdStatus(BaseModel):
    """Model: `CreateAdStatus`"""

    id: int = Field()
    """Ad ID."""

    post_id: int | None = Field(
        default=None,
    )
    """Stealth Post ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class CreateCampaignStatus(BaseModel):
    """Model: `CreateCampaignStatus`"""

    id: int = Field()
    """Campaign ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class CreateClientsStatus(BaseModel):
    """Model: `CreateClientsStatus`"""

    id: int = Field()
    """Client ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class Criteria(BaseModel):
    """Model: `Criteria`"""

    age_from: str | None = Field(
        default=None,
    )
    """Age from."""

    age_to: str | None = Field(
        default=None,
    )
    """Age to."""

    apps: str | None = Field(
        default=None,
    )
    """Apps IDs."""

    apps_not: str | None = Field(
        default=None,
    )
    """Apps IDs to except."""

    birthday: str | None = Field(
        default=None,
    )
    """Days to birthday."""

    cities: str | None = Field(
        default=None,
    )
    """Cities IDs."""

    cities_not: str | None = Field(
        default=None,
    )
    """Cities IDs to except."""

    districts: str | None = Field(
        default=None,
    )
    """Districts IDs."""

    groups: str | None = Field(
        default=None,
    )
    """Communities IDs."""

    interest_categories: str | None = Field(
        default=None,
    )
    """Interests categories IDs."""

    interests: str | None = Field(
        default=None,
    )
    """Interests."""

    paying: str | None = Field(
        default=None,
    )
    """Information whether the user has proceeded VK payments before."""

    positions: str | None = Field(
        default=None,
    )
    """Positions IDs."""

    religions: str | None = Field(
        default=None,
    )
    """Religions IDs."""

    retargeting_groups: str | None = Field(
        default=None,
    )
    """Retargeting groups ids."""

    retargeting_groups_not: str | None = Field(
        default=None,
    )
    """Retargeting groups NOT ids."""

    school_from: str | None = Field(
        default=None,
    )
    """School graduation year from."""

    school_to: str | None = Field(
        default=None,
    )
    """School graduation year to."""

    schools: str | None = Field(
        default=None,
    )
    """Schools IDs."""

    sex: "CriteriaSex | None" = Field(
        default=None,
    )
    """Property `Criteria.sex`."""

    stations: str | None = Field(
        default=None,
    )
    """Stations IDs."""

    statuses: str | None = Field(
        default=None,
    )
    """Relationship statuses."""

    streets: str | None = Field(
        default=None,
    )
    """Streets IDs."""

    travellers: str | None = Field(
        default=None,
    )
    """Travellers."""

    ab_test: str | None = Field(
        default=None,
    )
    """AB test."""

    uni_from: str | None = Field(
        default=None,
    )
    """University graduation year from."""

    uni_to: str | None = Field(
        default=None,
    )
    """University graduation year to."""

    user_browsers: str | None = Field(
        default=None,
    )
    """Browsers."""

    user_devices: str | None = Field(
        default=None,
    )
    """Devices."""

    user_os: str | None = Field(
        default=None,
    )
    """Operating systems."""

    suggested_criteria: str | None = Field(
        default=None,
    )
    """Suggested criteria."""

    groups_not: str | None = Field(
        default=None,
    )
    """Group not."""

    price_list_audience_type: str | None = Field(
        default=None,
    )
    """Price list audience type."""

    count: str | None = Field(
        default=None,
    )
    """Count."""

    groups_active_formula: str | None = Field(
        default=None,
    )
    """Group active formula."""

    interest_categories_formula: str | None = Field(
        default=None,
    )
    """Interest categories formula."""

    groups_formula: str | None = Field(
        default=None,
    )
    """Groups formula."""

    groups_active: str | None = Field(
        default=None,
    )
    """Groups active."""

    group_types: str | None = Field(
        default=None,
    )
    """Group types."""

    key_phrases: str | None = Field(
        default=None,
    )
    """Key phrases."""

    key_phrases_days: str | None = Field(
        default=None,
    )
    """Key phrases days."""

    geo_near: str | None = Field(
        default=None,
    )
    """Geo near."""

    geo_point_type: str | None = Field(
        default=None,
    )
    """Geo point type."""

    price_list_id: str | None = Field(
        default=None,
    )
    """Price list id."""

    groups_recommended: str | None = Field(
        default=None,
    )
    """Groups recommended ids."""

    groups_active_recommended: str | None = Field(
        default=None,
    )
    """Groups active recommended ids."""

    music_artists_formula: str | None = Field(
        default=None,
    )
    """Music artists formula."""

    price_list_retargeting_formula: str | None = Field(
        default=None,
    )
    """Price list retargeting formula."""

    tags: str | None = Field(
        default=None,
    )
    """Tags."""

    browsers: str | None = Field(
        default=None,
    )
    """Browsers."""

    mobile_os_min_version: str | None = Field(
        default=None,
    )
    """Mobile os min version."""

    mobile_apps_events_formula: str | None = Field(
        default=None,
    )
    """Mobile apps events formula."""

    mobile_os_max_version: str | None = Field(
        default=None,
    )
    """Mobile os max version."""

    operators: str | None = Field(
        default=None,
    )
    """operators."""

    wifi_only: str | None = Field(
        default=None,
    )
    """wifi_only."""

    mobile_manufacturers: str | None = Field(
        default=None,
    )
    """mobile_manufacturers."""


class CriteriaSex(StrEnum, metaclass=BaseEnumMeta):
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"


class DemoStats(BaseModel):
    """Model: `DemoStats`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    stats: list["DemostatsFormat"] | None = Field(
        default=None,
    )
    """Property `DemoStats.stats`."""

    type: "ObjectType | None" = Field(
        default=None,
    )
    """Property `DemoStats.type`."""


class DemographicStatsPeriodItemBase(BaseModel):
    """Model: `DemographicStatsPeriodItemBase`"""

    clicks_rate: float | None = Field(
        default=None,
    )
    """Clicks rate."""

    impressions_rate: float | None = Field(
        default=None,
    )
    """Impressions rate."""


class DemostatsFormat(BaseModel):
    """Model: `DemostatsFormat`"""

    age: list["StatsAge"] | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.age`."""

    cities: list["StatsCities"] | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.cities`."""

    day: str | None = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    day_from: str | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.day_from`."""

    day_to: str | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.day_to`."""

    month: str | None = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    overall: int | None = Field(
        default=None,
    )
    """1 if period=overall."""

    sex: list["StatsSex"] | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.sex`."""

    sex_age: list["AdsStatsSexAge"] | None = Field(
        default=None,
    )
    """Property `DemostatsFormat.sex_age`."""


class EventsRetargetingGroup(BaseModel):
    """Model: `EventsRetargetingGroup`"""

    id: int | None = Field(
        default=None,
    )
    """Property `EventsRetargetingGroup.id`."""

    value: list[int] | None = Field(
        default=None,
    )
    """Property `EventsRetargetingGroup.value`."""


class FloodStats(BaseModel):
    """Model: `FloodStats`"""

    left: int = Field()
    """Requests left."""

    refresh: int = Field()
    """Time to refresh in seconds."""

    stats_by_user: list["FloodStatsByUserItem"] | None = Field(
        default=None,
    )
    """Used requests per user."""


class FloodStatsByUserItem(BaseModel):
    """Model: `FloodStatsByUserItem`"""

    user_id: int = Field()
    """User ID."""

    requests_count: int = Field()
    """Used requests."""


class LinkStatus(BaseModel):
    """Model: `LinkStatus`"""

    status: str = Field()
    """Link status."""

    description: str | None = Field(
        default=None,
    )
    """Reject reason."""

    redirect_url: str | None = Field(
        default=None,
    )
    """URL."""


class LookalikeRequestStatus(StrEnum, metaclass=BaseEnumMeta):
    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class LookalikeRequestSourceType(StrEnum, metaclass=BaseEnumMeta):
    RETARGETING_GROUP = "retargeting_group"


class LookalikeRequest(BaseModel):
    """Model: `LookalikeRequest`"""

    id: int = Field()
    """Lookalike request ID."""

    create_time: int = Field()
    """Lookalike request create time, as Unixtime."""

    update_time: int = Field()
    """Lookalike request update time, as Unixtime."""

    status: "LookalikeRequestStatus" = Field()
    """Lookalike request status."""

    source_type: "LookalikeRequestSourceType" = Field()
    """Lookalike request source type."""

    scheduled_delete_time: int | None = Field(
        default=None,
    )
    """Time by which lookalike request would be deleted, as Unixtime."""

    source_retargeting_group_id: int | None = Field(
        default=None,
    )
    """Retargeting group id, which was used as lookalike seed."""

    source_name: str | None = Field(
        default=None,
    )
    """Lookalike request seed name (retargeting group name)."""

    audience_count: int | None = Field(
        default=None,
    )
    """Lookalike request seed audience size."""

    save_audience_levels: list["LookalikeRequestSaveAudienceLevel"] | None = Field(
        default=None,
    )
    """Property `LookalikeRequest.save_audience_levels`."""


class LookalikeRequestSaveAudienceLevel(BaseModel):
    """Model: `LookalikeRequestSaveAudienceLevel`"""

    level: int | None = Field(
        default=None,
    )
    """Save audience level id, which is used in save audience queries."""

    audience_count: int | None = Field(
        default=None,
    )
    """Saved audience audience size for according level."""


class MobileStatItem(BaseModel):
    """Model: `MobileStatItem`"""

    key: str | None = Field(
        default=None,
    )
    """Property `MobileStatItem.key`."""

    value: float | None = Field(
        default=None,
    )
    """Property `MobileStatItem.value`."""


class Musician(BaseModel):
    """Model: `Musician`"""

    id: int = Field()
    """Targeting music artist ID."""

    original_id: str = Field()
    """Music artist ID as in VKMusic."""

    name: str = Field()
    """Music artist name."""

    avatar: str | None = Field(
        default=None,
    )
    """Music artist photo."""


class ObjectType(StrEnum, metaclass=BaseEnumMeta):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class OrdClientType(StrEnum, metaclass=BaseEnumMeta):
    PERSON = "person"
    INDIVIDUAL = "individual"
    LEGAL = "legal"
    FOREIGN = "foreign"
    UNKNOWN = "unknown"


class OrdData(BaseModel):
    """Model: `OrdData`"""

    client_type: "OrdClientType" = Field()
    """Property `OrdData.client_type`."""

    client_name: str = Field()
    """Property `OrdData.client_name`."""

    phone: str = Field()
    """Property `OrdData.phone`."""

    contract_number: str = Field()
    """Property `OrdData.contract_number`."""

    contract_date: str = Field()
    """Property `OrdData.contract_date`."""

    contract_type: str = Field()
    """Property `OrdData.contract_type`."""

    contract_object: str = Field()
    """Property `OrdData.contract_object`."""

    with_vat: bool = Field()
    """Property `OrdData.with_vat`."""

    inn: str | None = Field(
        default=None,
    )
    """Property `OrdData.inn`."""

    agency_phone: str | None = Field(
        default=None,
    )
    """Property `OrdData.agency_phone`."""

    subagent: "OrdSubagent | None" = Field(
        default=None,
    )
    """Property `OrdData.subagent`."""


class OrdSubagent(BaseModel):
    """Model: `OrdSubagent`"""

    type: "OrdClientType" = Field()
    """Property `OrdSubagent.type`."""

    name: str = Field()
    """Property `OrdSubagent.name`."""

    phone: str = Field()
    """Property `OrdSubagent.phone`."""

    inn: str | None = Field(
        default=None,
    )
    """Property `OrdSubagent.inn`."""


class Post(BaseModel):
    """Model: `Post`"""

    id: int | None = Field(
        default=None,
    )
    """Post id."""

    from_id: int | None = Field(
        default=None,
    )
    """From id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date."""

    edited: int | None = Field(
        default=None,
    )
    """Edited date."""

    is_pinned: int | None = Field(
        default=None,
    )
    """Is pinned."""

    marked_as_ads: int | None = Field(
        default=None,
    )
    """Marked as ads."""

    ads_easy_promote: "PostEasyPromote | None" = Field(
        default=None,
    )
    """Property `Post.ads_easy_promote`."""

    donut: "PostDonut | None" = Field(
        default=None,
    )
    """Property `Post.donut`."""

    comments: "PostComments | None" = Field(
        default=None,
    )
    """Property `Post.comments`."""

    copyright: "PostCopyright | None" = Field(
        default=None,
    )
    """Property `Post.copyright`."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Short text rate."""

    type: str | None = Field(
        default=None,
    )
    """Type."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Is favorite."""

    likes: "PostLikes | None" = Field(
        default=None,
    )
    """Property `Post.likes`."""

    views: "PostViews | None" = Field(
        default=None,
    )
    """Property `Post.views`."""

    post_type: str | None = Field(
        default=None,
    )
    """Post type."""

    reposts: "PostReposts | None" = Field(
        default=None,
    )
    """Property `Post.reposts`."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    is_promoted_post_stealth: bool | None = Field(
        default=None,
    )
    """Is promoted post stealth."""

    hash: str | None = Field(
        default=None,
    )
    """Hash."""

    owner: "PostOwner | None" = Field(
        default=None,
    )
    """Property `Post.owner`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `Post.attachments`."""

    created_by: int | None = Field(
        default=None,
    )
    """Created by."""

    carousel_offset: int | None = Field(
        default=None,
    )
    """Carousel offset."""

    can_edit: int | None = Field(
        default=None,
    )
    """Can edit."""

    can_delete: int | None = Field(
        default=None,
    )
    """Can delete."""

    can_pin: int | None = Field(
        default=None,
    )
    """Can pin."""


class PostComments(BaseModel):
    """Comments
    Model: `PostComments`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""


class PostDonut(BaseModel):
    """Donut
    Model: `PostDonut`
    """

    is_donut: bool | None = Field(
        default=None,
    )
    """Is donut."""


class PostEasyPromote(BaseModel):
    """Ads easy promote
    Model: `PostEasyPromote`
    """

    type: int | None = Field(
        default=None,
    )
    """Type."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    label_text: str | None = Field(
        default=None,
    )
    """Label text."""

    button_text: str | None = Field(
        default=None,
    )
    """Button text."""

    is_ad_not_easy: bool | None = Field(
        default=None,
    )
    """Is ad not easy."""

    ad_id: int | None = Field(
        default=None,
    )
    """Ad id."""

    top_union_id: int | None = Field(
        default=None,
    )
    """Top union id."""


class PostLikes(BaseModel):
    """Likes
    Model: `PostLikes`
    """

    can_like: int | None = Field(
        default=None,
    )
    """Can like."""

    count: int | None = Field(
        default=None,
    )
    """Count."""

    user_likes: int | None = Field(
        default=None,
    )
    """User likes."""


class PostOwner(BaseModel):
    """Owner
    Model: `PostOwner`
    """

    id: int | None = Field(
        default=None,
    )
    """Owner id."""

    name: str | None = Field(
        default=None,
    )
    """Name."""

    photo: str | None = Field(
        default=None,
    )
    """Photo url."""

    url: str | None = Field(
        default=None,
    )
    """Profile url."""


class PostReposts(BaseModel):
    """Reposts
    Model: `PostReposts`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""

    wall_count: int | None = Field(
        default=None,
    )
    """Wall count."""

    mail_count: int | None = Field(
        default=None,
    )
    """Mail count."""


class PostViews(BaseModel):
    """Views
    Model: `PostViews`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""


class PromotedPostReach(BaseModel):
    """Model: `PromotedPostReach`"""

    hide: int = Field()
    """Hides amount."""

    id: int = Field()
    """Object ID from \'ids\' parameter."""

    join_group: int = Field()
    """Community joins."""

    links: int = Field()
    """Link clicks."""

    reach_subscribers: int = Field()
    """Subscribers reach."""

    reach_total: int = Field()
    """Total reach."""

    report: int = Field()
    """Reports amount."""

    to_group: int = Field()
    """Community clicks."""

    unsubscribe: int = Field()
    """\'Unsubscribe\' events amount."""

    video_views_100p: int | None = Field(
        default=None,
    )
    """Video views for 100 percent."""

    video_views_25p: int | None = Field(
        default=None,
    )
    """Video views for 25 percent."""

    video_views_3s: int | None = Field(
        default=None,
    )
    """Video views for 3 seconds."""

    video_views_10s: int | None = Field(
        default=None,
    )
    """Video views for 10 seconds."""

    video_views_50p: int | None = Field(
        default=None,
    )
    """Video views for 50 percent."""

    video_views_75p: int | None = Field(
        default=None,
    )
    """Video views for 75 percent."""

    video_views_start: int | None = Field(
        default=None,
    )
    """Video starts."""

    pretty_cards_clicks: int | None = Field(
        default=None,
    )
    """Pretty cards clicks."""


class RejectReason(BaseModel):
    """Model: `RejectReason`"""

    comment: str | None = Field(
        default=None,
    )
    """Comment text."""

    rules: list["Rules"] | None = Field(
        default=None,
    )
    """Property `RejectReason.rules`."""


class Rules(BaseModel):
    """Model: `Rules`"""

    help_url: str | bool | None = Field(
        default=None,
    )
    """Help url."""

    help_label: str | None = Field(
        default=None,
    )
    """Label."""

    content_html: str | None = Field(
        default=None,
    )
    """Content Html."""

    help_chat: bool | None = Field(
        default=None,
    )
    """Help chat."""


class StatisticClickActionType(StrEnum, metaclass=BaseEnumMeta):
    LOAD = "load"
    IMPRESSION = "impression"
    CLICK_DEEPLINK = "click_deeplink"
    CLICK = "click"
    CLICK_POST_OWNER = "click_post_owner"
    CLICK_POST_LINK = "click_post_link"
    CLICK_PRETTY_CARD = "click_pretty_card"
    LIKE_POST = "like_post"
    SHARE_POST = "share_post"
    VIDEO_START = "video_start"
    VIDEO_PAUSE = "video_pause"
    VIDEO_RESUME = "video_resume"
    VIDEO_PLAY_3S = "video_play_3s"
    VIDEO_PLAY_10S = "video_play_10s"
    VIDEO_PLAY_25 = "video_play_25"
    VIDEO_PLAY_50 = "video_play_50"
    VIDEO_PLAY_75 = "video_play_75"
    VIDEO_PLAY_95 = "video_play_95"
    VIDEO_PLAY_100 = "video_play_100"
    VIDEO_VOLUME_ON = "video_volume_on"
    VIDEO_VOLUME_OFF = "video_volume_off"
    VIDEO_FULLSCREEN_ON = "video_fullscreen_on"
    VIDEO_FULLSCREEN_OFF = "video_fullscreen_off"
    HIDE = "hide"


class StatisticClickAction(BaseModel):
    """Model: `StatisticClickAction`"""

    type: "StatisticClickActionType | None" = Field(
        default=None,
    )
    """Property `StatisticClickAction.type`."""

    url: str | None = Field(
        default=None,
    )
    """Property `StatisticClickAction.url`."""


class AdsStats(BaseModel):
    """Model: `AdsStats`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    stats: list["StatsFormat"] | None = Field(
        default=None,
    )
    """Property `AdsStats.stats`."""

    type: "ObjectType | None" = Field(
        default=None,
    )
    """Property `AdsStats.type`."""

    views_times: "StatsViewsTimes | None" = Field(
        default=None,
    )
    """Property `AdsStats.views_times`."""


class StatsFormat(BaseModel):
    """Model: `StatsFormat`"""

    clicks: int | None = Field(
        default=None,
    )
    """Clicks number."""

    link_external_clicks: int | None = Field(
        default=None,
    )
    """External clicks number."""

    day: str | None = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    impressions: int | None = Field(
        default=None,
    )
    """Impressions number."""

    join_rate: int | None = Field(
        default=None,
    )
    """Events number."""

    month: str | None = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    year: int | None = Field(
        default=None,
    )
    """Year as YYYY."""

    overall: int | None = Field(
        default=None,
    )
    """1 if period=overall."""

    reach: int | None = Field(
        default=None,
    )
    """Reach ."""

    spent: str | None = Field(
        default=None,
    )
    """Spent funds."""

    video_plays_unique_started: int | None = Field(
        default=None,
    )
    """Video plays unique started count."""

    video_plays_unique_3_seconds: int | None = Field(
        default=None,
    )
    """Video plays unique 3 seconds count."""

    video_plays_unique_10_seconds: int | None = Field(
        default=None,
    )
    """Video plays unique 10 seconds count."""

    video_plays_unique_25_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 25 percents count."""

    video_plays_unique_50_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 50 percents count."""

    video_plays_unique_75_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 75 percents count."""

    video_plays_unique_100_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 100 percents count."""

    effective_cost_per_click: str | None = Field(
        default=None,
    )
    """Effective cost per click."""

    effective_cost_per_mille: str | None = Field(
        default=None,
    )
    """Effective cost per mille."""

    effective_cpf: str | None = Field(
        default=None,
    )
    """Effective cpf."""

    effective_cost_per_message: str | None = Field(
        default=None,
    )
    """Effective cost per message."""

    message_sends: int | None = Field(
        default=None,
    )
    """Message sends count."""

    message_sends_by_any_user: int | None = Field(
        default=None,
    )
    """Message sends by anu user."""

    conversions_external: int | None = Field(
        default=None,
    )
    """Conversions external."""

    conversion_count: int | None = Field(
        default=None,
    )
    """Conversions count."""

    conversion_cr: str | None = Field(
        default=None,
    )
    """Conversions CR."""

    day_from: str | None = Field(
        default=None,
    )
    """Day from."""

    day_to: str | None = Field(
        default=None,
    )
    """Day to."""

    ctr: str | None = Field(
        default=None,
    )
    """Ctr."""

    uniq_views_count: int | None = Field(
        default=None,
    )
    """Unique views count."""

    mobile_app_stat: list["MobileStatItem"] | None = Field(
        default=None,
    )
    """Mobile app stat."""


class StatsSexValue(StrEnum, metaclass=BaseEnumMeta):
    F = "f"
    M = "m"


class StatsViewsTimes(BaseModel):
    """Model: `StatsViewsTimes`"""

    views_ads_times_1: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_1`."""

    views_ads_times_2: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_2`."""

    views_ads_times_3: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_3`."""

    views_ads_times_4: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_4`."""

    views_ads_times_5: str | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_5`."""

    views_ads_times_6: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_6`."""

    views_ads_times_7: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_7`."""

    views_ads_times_8: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_8`."""

    views_ads_times_9: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_9`."""

    views_ads_times_10: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_10`."""

    views_ads_times_11_plus: int | None = Field(
        default=None,
    )
    """Property `StatsViewsTimes.views_ads_times_11_plus`."""


class Stories(BaseModel):
    """Model: `Stories`"""

    stories: list["StoryItem"] | None = Field(
        default=None,
    )
    """Property `Stories.stories`."""

    owner: "StoriesOwner | None" = Field(
        default=None,
    )
    """Property `Stories.owner`."""

    stories_disclaimers_text: str | None = Field(
        default=None,
    )
    """Stories disclaimers text."""


class StoriesOwner(BaseModel):
    """Model: `StoriesOwner`"""

    id: int | bool | None = Field(
        default=None,
    )
    """Owner id."""

    href: str | None = Field(
        default=None,
    )
    """Href."""

    name: str | None = Field(
        default=None,
    )
    """Name."""

    photo: str | None = Field(
        default=None,
    )
    """Photo."""

    verify: str | None = Field(
        default=None,
    )
    """Verify."""

    gender: str | None = Field(
        default=None,
    )
    """Gender."""

    name_get: str | None = Field(
        default=None,
    )
    """Name get."""

    first_name: str | None = Field(
        default=None,
        alias="firstName",
    )
    """First name."""

    first_name_gen: str | None = Field(
        default=None,
    )
    """First name gen."""

    first_name_ins: str | None = Field(
        default=None,
    )
    """First name ins."""

    can_follow: bool | None = Field(
        default=None,
    )
    """Can follow."""


class StoryItem(BaseModel):
    """Model: `StoryItem`"""

    id: int | None = Field(
        default=None,
    )
    """Story id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    raw_id: str | None = Field(
        default=None,
    )
    """Story raw id."""

    date: str | None = Field(
        default=None,
    )
    """Date."""

    time: int | None = Field(
        default=None,
    )
    """Time."""

    type: str | None = Field(
        default=None,
    )
    """Type."""

    unread: bool | None = Field(
        default=None,
    )
    """Is unread."""

    can_like: bool | None = Field(
        default=None,
        alias="canLike",
    )
    """Can like."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Can comment."""

    can_share: bool | None = Field(
        default=None,
    )
    """Can share."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Can remove."""

    can_manage: bool | None = Field(
        default=None,
    )
    """Can manage."""

    can_ask: bool | None = Field(
        default=None,
    )
    """Can ask."""

    can_ask_anonymous: bool | None = Field(
        default=None,
    )
    """Can ask anonymous."""

    is_profile_question: bool | None = Field(
        default=None,
        alias="isProfileQuestion",
    )
    """Is profile question."""

    stats: "StoryItemStats | None" = Field(
        default=None,
    )
    """Property `StoryItem.stats`."""

    link: "StoryItemLink | None" = Field(
        default=None,
    )
    """Property `StoryItem.link`."""

    photo_url: str | None = Field(
        default=None,
    )
    """Photo url."""

    preview_url: str | None = Field(
        default=None,
    )
    """Preview url."""

    track_code: str | None = Field(
        default=None,
    )
    """Track code."""

    is_part_of_narrative: bool | None = Field(
        default=None,
        alias="isPartOfNarrative",
    )
    """Is part of narrative."""

    is_ads: bool | None = Field(
        default=None,
        alias="isAds",
    )
    """Is ads."""

    video_url: str | None = Field(
        default=None,
    )
    """Video url."""

    first_frame: str | None = Field(
        default=None,
    )
    """First frame."""

    small_preview: str | None = Field(
        default=None,
    )
    """Small preview."""

    is_liked: bool | None = Field(
        default=None,
        alias="isLiked",
    )
    """Is liked."""


class StoryItemLink(BaseModel):
    """Model: `StoryItemLink`"""

    key: str | None = Field(
        default=None,
    )
    """Key."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    url: str | None = Field(
        default=None,
    )
    """Url."""

    raw_url: str | None = Field(
        default=None,
    )
    """Raw url."""


class StoryItemStats(BaseModel):
    """Model: `StoryItemStats`"""

    follow: "StoryItemStatsFollow | None" = Field(
        default=None,
    )
    """Property `StoryItemStats.follow`."""

    url_view: "StoryItemStatsUrlView | None" = Field(
        default=None,
    )
    """Property `StoryItemStats.url_view`."""


class StoryItemStatsFollow(BaseModel):
    """Follow event stats
    Model: `StoryItemStatsFollow`
    """

    event_type: str | None = Field(
        default=None,
    )
    """Event type."""

    rhash: str | None = Field(
        default=None,
    )
    """Event hash."""


class StoryItemStatsUrlView(BaseModel):
    """Url view event stats
    Model: `StoryItemStatsUrlView`
    """

    event_type: str | None = Field(
        default=None,
    )
    """Event type."""

    rhash: str | None = Field(
        default=None,
    )
    """Event hash."""


class TargStats(BaseModel):
    """Model: `TargStats`"""

    audience_count: int = Field()
    """Audience."""

    recommended_cpc: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach (old format)."""

    recommended_cpm: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach (old format)."""

    recommended_cpc_50: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach."""

    recommended_cpm_50: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach."""

    recommended_cpc_70: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 70% reach."""

    recommended_cpm_70: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 70% reach."""

    recommended_cpc_90: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 90% reach."""

    recommended_cpm_90: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 90% reach."""

    total_alive_audience: int | None = Field(
        default=None,
    )
    """Total alive audience."""


class TargSuggestions(BaseModel):
    """Model: `TargSuggestions`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    type: str | None = Field(
        default=None,
    )
    """Object type."""

    parent: str | None = Field(
        default=None,
    )
    """Parent."""


class TargSuggestionsCities(BaseModel):
    """Model: `TargSuggestionsCities`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    parent: str | None = Field(
        default=None,
    )
    """Parent object."""


class TargSuggestionsRegions(BaseModel):
    """Model: `TargSuggestionsRegions`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    type: str | None = Field(
        default=None,
    )
    """Object type."""


class TargSuggestionsSchools(BaseModel):
    """Model: `TargSuggestionsSchools`"""

    desc: str | None = Field(
        default=None,
    )
    """Full school title."""

    id: int | None = Field(
        default=None,
    )
    """School ID."""

    name: str | None = Field(
        default=None,
    )
    """School title."""

    parent: str | None = Field(
        default=None,
    )
    """City name."""

    type: "TargSuggestionsSchoolsType | None" = Field(
        default=None,
    )
    """Property `TargSuggestionsSchools.type`."""


class TargSuggestionsSchoolsType(StrEnum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class TargetGroup(BaseModel):
    """Model: `TargetGroup`"""

    id: int | None = Field(
        default=None,
    )
    """Group ID."""

    name: str | None = Field(
        default=None,
    )
    """Group name."""

    is_audience: bool | None = Field(
        default=None,
    )
    """Is audience."""

    is_shared: bool | None = Field(
        default=None,
    )
    """Is shared."""

    file_source: bool | None = Field(
        default=None,
    )
    """File source."""

    api_source: bool | None = Field(
        default=None,
    )
    """API source."""

    lookalike_source: bool | None = Field(
        default=None,
    )
    """File source."""

    audience_count: int | None = Field(
        default=None,
    )
    """Audience."""

    domain: str | None = Field(
        default=None,
    )
    """Site domain."""

    lifetime: int | None = Field(
        default=None,
    )
    """Number of days for user to be in group."""

    pixel: str | None = Field(
        default=None,
    )
    """Pixel code."""

    target_pixel_id: int | None = Field(
        default=None,
    )
    """Target Pixel id."""

    target_pixel_rules: list["TargetGroupTargetPixelRule"] | None = Field(
        default=None,
    )
    """Target Pixel rules."""

    last_updated: int | None = Field(
        default=None,
    )
    """Last updated."""


class TargetGroupTargetPixelRule(BaseModel):
    """Model: `TargetGroupTargetPixelRule`"""

    url_full_match: str | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.url_full_match`."""

    event_full_match: str | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.event_full_match`."""

    url_substrings_match: list[str] | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.url_substrings_match`."""

    event_substrings_match: list[str] | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.event_substrings_match`."""

    url_regex_match: str | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.url_regex_match`."""

    event_regex_match: str | None = Field(
        default=None,
    )
    """Property `TargetGroupTargetPixelRule.event_regex_match`."""


class TargetPixelInfo(BaseModel):
    """Model: `TargetPixelInfo`"""

    target_pixel_id: int = Field()
    """Property `TargetPixelInfo.target_pixel_id`."""

    name: str = Field()
    """Property `TargetPixelInfo.name`."""

    domain: str = Field()
    """Property `TargetPixelInfo.domain`."""

    category_id: int = Field()
    """Property `TargetPixelInfo.category_id`."""

    last_updated: int = Field()
    """Property `TargetPixelInfo.last_updated`."""

    pixel: str = Field()
    """Property `TargetPixelInfo.pixel`."""


class UpdateOfficeUsersResult(BaseModel):
    """Model: `UpdateOfficeUsersResult`"""

    user_id: int = Field()
    """Property `UpdateOfficeUsersResult.user_id`."""

    is_success: bool = Field()
    """Property `UpdateOfficeUsersResult.is_success`."""

    error: "Error | None" = Field(
        default=None,
    )
    """Property `UpdateOfficeUsersResult.error`."""


class UpdateAdsStatus(BaseModel):
    """Model: `UpdateAdsStatus`"""

    id: int = Field()
    """Ad ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class UpdateClientsStatus(BaseModel):
    """Model: `UpdateClientsStatus`"""

    id: int = Field()
    """Client ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class UserSpecification(BaseModel):
    """Model: `UserSpecification`"""

    user_id: int = Field()
    """Property `UserSpecification.user_id`."""

    role: "AccessRolePublic" = Field()
    """Property `UserSpecification.role`."""

    grant_access_to_all_clients: bool | None = Field(
        default=None,
    )
    """Property `UserSpecification.grant_access_to_all_clients`."""

    client_ids: list[int] | None = Field(
        default=None,
    )
    """Property `UserSpecification.client_ids`."""

    view_budget: bool | None = Field(
        default=None,
    )
    """Property `UserSpecification.view_budget`."""


class UserSpecificationCutted(BaseModel):
    """Model: `UserSpecificationCutted`"""

    user_id: int = Field()
    """Property `UserSpecificationCutted.user_id`."""

    role: "AccessRolePublic" = Field()
    """Property `UserSpecificationCutted.role`."""

    client_id: int | None = Field(
        default=None,
    )
    """Property `UserSpecificationCutted.client_id`."""

    view_budget: bool | None = Field(
        default=None,
    )
    """Property `UserSpecificationCutted.view_budget`."""


class Users(BaseModel):
    """Model: `Users`"""

    accesses: list["Accesses"] = Field()
    """Property `Users.accesses`."""

    user_id: int = Field()
    """User ID."""


class AppWidgetsPhoto(BaseModel):
    """Model: `AppWidgetsPhoto`"""

    id: str = Field()
    """Image ID."""

    images: list["BaseImage"] = Field()
    """Property `AppWidgetsPhoto.images`."""


class Photos(BaseModel):
    """Model: `Photos`"""

    count: int | None = Field(
        default=None,
    )
    """Property `Photos.count`."""

    items: list["AppWidgetsPhoto"] | None = Field(
        default=None,
    )
    """Property `Photos.items`."""


class AppFields(StrEnum, metaclass=BaseEnumMeta):
    AUTHOR_GROUP = "author_group"
    AUTHOR_ID = "author_id"
    AUTHOR_URL = "author_url"
    BANNER_1120 = "banner_1120"
    BANNER_560 = "banner_560"
    BANNER_186 = "banner_186"
    BANNER_896 = "banner_896"
    ICON_16 = "icon_16"
    ICON_25 = "icon_25"
    ICON_50 = "icon_50"
    ICON_100 = "icon_100"
    ICON_200 = "icon_200"
    ICON_128 = "icon_128"
    ICON_256 = "icon_256"
    IS_NEW = "is_new"
    NEW = "new"
    IS_HTML5_APP = "is_html5_app"
    PUSH_ENABLED = "push_enabled"
    CATALOG_BANNER = "catalog_banner"
    FRIENDS = "friends"
    CATALOG_POSITION = "catalog_position"
    DESCRIPTION = "description"
    GENRE = "genre"
    GENRE_ID = "genre_id"
    INTERNATIONAL = "international"
    IS_IN_CATALOG = "is_in_catalog"
    INSTALLED = "installed"
    LEADERBOARD_TYPE = "leaderboard_type"
    MEMBERS_COUNT = "members_count"
    PLATFORM_ID = "platform_id"
    PUBLISHED_DATE = "published_date"
    SCREEN_NAME = "screen_name"
    SECTION = "section"
    TYPE = "type"
    ID = "id"
    TITLE = "title"
    AUTHOR_OWNER_ID = "author_owner_id"
    IS_INSTALLED = "is_installed"
    ICON_139 = "icon_139"
    ICON_150 = "icon_150"
    ICON_278 = "icon_278"
    ICON_576 = "icon_576"
    BACKGROUND_LOADER_COLOR = "background_loader_color"
    LOADER_ICON = "loader_icon"
    ICON_75 = "icon_75"
    OPEN_IN_EXTERNAL_BROWSER = "open_in_external_browser"
    AD_CONFIG = "ad_config"
    SCREEN_ORIENTATION = "screen_orientation"


class AppLeaderboardType(IntEnum, metaclass=BaseEnumMeta):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppMin(BaseModel):
    """Model: `AppMin`"""

    type: "AppType" = Field()
    """Property `AppMin.type`."""

    id: int = Field()
    """Application ID."""

    title: str = Field()
    """Application title."""

    author_owner_id: int | None = Field(
        default=None,
    )
    """Application author\'s ID."""

    is_installed: bool | None = Field(
        default=None,
    )
    """Is application installed."""

    icon_139: str | None = Field(
        default=None,
    )
    """URL of the app icon with 139 px in width."""

    icon_150: str | None = Field(
        default=None,
    )
    """URL of the app icon with 150 px in width."""

    icon_278: str | None = Field(
        default=None,
    )
    """URL of the app icon with 278 px in width."""

    icon_576: str | None = Field(
        default=None,
    )
    """URL of the app icon with 576 px in width."""

    background_loader_color: str | None = Field(
        default=None,
    )
    """Hex color code without hash sign."""

    loader_icon: str | None = Field(
        default=None,
    )
    """SVG data."""

    icon_75: str | None = Field(
        default=None,
    )
    """URL of the app icon with 75 px in width."""

    screen_orientation: int | None = Field(
        default=None,
    )
    """Screen orientation."""


class AppType(StrEnum, metaclass=BaseEnumMeta):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class CatalogList(BaseModel):
    """Model: `CatalogList`"""

    count: int = Field()
    """Total number."""

    items: list["App"] = Field()
    """Property `CatalogList.items`."""

    profiles: list["UserMin"] | None = Field(
        default=None,
    )
    """Property `CatalogList.profiles`."""


class CustomSnippetButton(StrEnum, metaclass=BaseEnumMeta):
    BUY = "buy"
    BUY_TICKET = "buy_ticket"
    CONTACT = "contact"
    CREATE = "create"
    ENROLL = "enroll"
    FILL = "fill"
    GO = "go"
    OPEN = "open"
    PLAY = "play"


class CustomSnippet(BaseModel):
    """Model: `CustomSnippet`"""

    vk_ref: list[typing.Literal["snippet_im", "snippet_post"]] | None = Field(
        default=None,
    )
    """Property `CustomSnippet.vk_ref`."""

    group_id: list[int] | None = Field(
        default=None,
    )
    """Property `CustomSnippet.group_id`."""

    hash: list[str] | None = Field(
        default=None,
    )
    """Property `CustomSnippet.hash`."""

    snippet_id: int | None = Field(
        default=None,
    )
    """Property `CustomSnippet.snippet_id`."""

    title: str | None = Field(
        default=None,
    )
    """Property `CustomSnippet.title`."""

    description: str | None = Field(
        default=None,
    )
    """Property `CustomSnippet.description`."""

    expired_at: int | None = Field(
        default=None,
    )
    """Property `CustomSnippet.expired_at`."""

    image_url: str | None = Field(
        default=None,
    )
    """Property `CustomSnippet.image_url`."""

    small_image_url: str | None = Field(
        default=None,
    )
    """Property `CustomSnippet.small_image_url`."""

    button: "CustomSnippetButton | None" = Field(
        default=None,
    )
    """Property `CustomSnippet.button`."""


class Leaderboard(BaseModel):
    """Model: `Leaderboard`"""

    user_id: int = Field()
    """User ID."""

    level: int | None = Field(
        default=None,
    )
    """Level."""

    points: int | None = Field(
        default=None,
    )
    """Points number."""

    score: int | None = Field(
        default=None,
    )
    """Score number."""


class ScopeName(StrEnum, metaclass=BaseEnumMeta):
    FRIENDS = "friends"
    PHOTOS = "photos"
    VIDEO = "video"
    PAGES = "pages"
    STATUS = "status"
    NOTES = "notes"
    WALL = "wall"
    DOCS = "docs"
    GROUPS = "groups"
    STATS = "stats"
    MARKET = "market"
    STORIES = "stories"
    APP_WIDGET = "app_widget"
    MESSAGES = "messages"
    MANAGE = "manage"
    NOTIFY = "notify"
    AUDIO = "audio"
    SUPPORT = "support"
    MENU = "menu"
    WALLMENU = "wallmenu"
    ADS = "ads"
    OFFLINE = "offline"
    NOTIFICATIONS = "notifications"
    EMAIL = "email"
    ADSWEB = "adsweb"
    LEADS = "leads"
    GROUP_MESSAGES = "group_messages"
    EXCHANGE = "exchange"
    PHONE = "phone"


class Scope(BaseModel):
    """Scope description
    Model: `Scope`
    """

    name: "ScopeName" = Field()
    """Scope name."""

    title: str | None = Field(
        default=None,
    )
    """Scope title."""


class TestingGroup(BaseModel):
    """Model: `TestingGroup`"""

    user_ids: list[int] = Field()
    """Property `TestingGroup.user_ids`."""

    group_id: int = Field()
    """Property `TestingGroup.group_id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `TestingGroup.name`."""

    webview: str | None = Field(
        default=None,
    )
    """Property `TestingGroup.webview`."""

    platforms: list[typing.Literal["mobile", "web", "mvk"]] | None = Field(
        default=None,
    )
    """Property `TestingGroup.platforms`."""


class Audio(BaseModel):
    """Model: `Audio`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class DefaultOrder(IntEnum, metaclass=BaseEnumMeta):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class Topic(BaseModel):
    """Model: `Topic`"""

    comments: int | None = Field(
        default=None,
    )
    """Comments number."""

    created: int | None = Field(
        default=None,
    )
    """Date when the topic has been created in Unixtime."""

    created_by: int | None = Field(
        default=None,
    )
    """Creator ID."""

    id: int | None = Field(
        default=None,
    )
    """Topic ID."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Information whether the topic is closed."""

    is_fixed: bool | None = Field(
        default=None,
    )
    """Information whether the topic is fixed."""

    title: str | None = Field(
        default=None,
    )
    """Topic title."""

    updated: int | None = Field(
        default=None,
    )
    """Date when the topic has been updated in Unixtime."""

    updated_by: int | None = Field(
        default=None,
    )
    """ID of user who updated the topic."""

    first_comment: str | None = Field(
        default=None,
    )
    """First comment text."""

    last_comment: str | None = Field(
        default=None,
    )
    """Last comment text."""


class TopicComment(BaseModel):
    """Model: `TopicComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["CommentAttachment"] | None = Field(
        default=None,
    )
    """Property `TopicComment.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `TopicComment.likes`."""


class AddCompanyGroupsMembersError(BaseModel):
    """Model: `AddCompanyGroupsMembersError`"""

    group_id: int = Field()
    """Property `AddCompanyGroupsMembersError.group_id`."""

    user_id: int = Field()
    """Property `AddCompanyGroupsMembersError.user_id`."""


class AttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    DOC = "doc"


class Attachment(BaseModel):
    """Model: `Attachment`"""
    type: "AttachmentType" = Field()
    """Property `Attachment.type`."""
    doc: "Doc | None" = Field(
        default=None,
    )
    """Property `Attachment.doc`."""
    photo: 'Photo | None' = None


class Bugreport(BaseModel):
    """Model: `Bugreport`"""

    id: int = Field()
    """Property `Bugreport.id`."""

    title: str = Field()
    """Property `Bugreport.title`."""

    owner_id: int = Field()
    """Property `Bugreport.owner_id`."""

    created: int = Field()
    """Property `Bugreport.created`."""

    updated: int = Field()
    """Property `Bugreport.updated`."""

    company_id: int = Field()
    """Property `Bugreport.company_id`."""

    original_id: int | None = Field(
        default=None,
    )
    """Property `Bugreport.original_id`."""

    clones_count: int | None = Field(
        default=None,
    )
    """Property `Bugreport.clones_count`."""

    description: str | None = Field(
        default=None,
    )
    """Property `Bugreport.description`."""

    state_actual: str | None = Field(
        default=None,
    )
    """Property `Bugreport.state_actual`."""

    state_supposed: str | None = Field(
        default=None,
    )
    """Property `Bugreport.state_supposed`."""

    phone: str | None = Field(
        default=None,
    )
    """Property `Bugreport.phone`."""

    comments_count: int | None = Field(
        default=None,
    )
    """Property `Bugreport.comments_count`."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_remove`."""

    can_change_status: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_change_status`."""

    can_bookmark: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_bookmark`."""

    is_bookmarked: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.is_bookmarked`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_edit`."""

    can_export_to_trackers: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_export_to_trackers`."""

    can_export_to_csv: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_export_to_csv`."""

    can_add_moder_comment: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_add_moder_comment`."""

    can_add_hidden_comment: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_add_hidden_comment`."""

    can_view_history: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_view_history`."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.is_deleted`."""

    can_restore: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_restore`."""

    is_vulnerability: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.is_vulnerability`."""

    is_severity_by_moderator: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.is_severity_by_moderator`."""

    hidden_docs: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.hidden_docs`."""

    is_confidential: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.is_confidential`."""

    private_comment: str | None = Field(
        default=None,
    )
    """Property `Bugreport.private_comment`."""

    can_change_product: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.can_change_product`."""

    tournament_score: int | None = Field(
        default=None,
    )
    """Property `Bugreport.tournament_score`."""

    moderator_user_id: int | None = Field(
        default=None,
    )
    """Property `Bugreport.moderator_user_id`."""

    moderated: int | None = Field(
        default=None,
    )
    """Property `Bugreport.moderated`."""

    screen_reader: int | None = Field(
        default=None,
    )
    """Property `Bugreport.screen_reader`."""

    status_auto_update_ts: int | None = Field(
        default=None,
    )
    """Property `Bugreport.status_auto_update_ts`."""

    status_auto_update_reason: int | None = Field(
        default=None,
    )
    """Property `Bugreport.status_auto_update_reason`."""

    product_has_wishes: bool | None = Field(
        default=None,
    )
    """Property `Bugreport.product_has_wishes`."""


class BugreportSubscribeState(BaseModel):
    """Model: `BugreportSubscribeState`"""

    can_set_subscribe: bool = Field()
    """Property `BugreportSubscribeState.can_set_subscribe`."""

    is_subscribed: bool | None = Field(
        default=None,
    )
    """Property `BugreportSubscribeState.is_subscribed`."""

    set_subscribe_hash: str | None = Field(
        default=None,
    )
    """Property `BugreportSubscribeState.set_subscribe_hash`."""


class Comment(BaseModel):
    """Model: `Comment`"""

    bugreport_id: int = Field()
    """Property `Comment.bugreport_id`."""

    comment_id: int = Field()
    """Property `Comment.comment_id`."""

    created: int = Field()
    """Property `Comment.created`."""

    text: str = Field()
    """Property `Comment.text`."""

    meta_text: str | None = Field(
        default=None,
    )
    """Property `Comment.meta_text`."""

    from_id: int | None = Field(
        default=None,
    )
    """Property `Comment.from_id`."""

    author_name: str | None = Field(
        default=None,
    )
    """Property `Comment.author_name`."""

    author_photo: str | None = Field(
        default=None,
    )
    """Property `Comment.author_photo`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `Comment.can_edit`."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Property `Comment.can_remove`."""

    is_hidden: bool | None = Field(
        default=None,
    )
    """Property `Comment.is_hidden`."""

    attachments: list["Attachment"] | None = Field(
        default=None,
    )
    """Property `Comment.attachments`."""

    is_unread: bool | None = Field(
        default=None,
    )
    """Property `Comment.is_unread`."""

    author: "CommentAuthor | None" = Field(
        default=None,
    )
    """Property `Comment.author`."""

    is_attachments_hidden: bool | None = Field(
        default=None,
    )
    """Property `Comment.is_attachments_hidden`."""


class CommentAuthor(BaseModel):
    """Model: `CommentAuthor`"""

    author_id: int | None = Field(
        default=None,
    )
    """Property `CommentAuthor.author_id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `CommentAuthor.name`."""

    photo: str | None = Field(
        default=None,
    )
    """Property `CommentAuthor.photo`."""

    moder_name: str | None = Field(
        default=None,
    )
    """Property `CommentAuthor.moder_name`."""

    moder_number: int | None = Field(
        default=None,
    )
    """Property `CommentAuthor.moder_number`."""

    link: str | None = Field(
        default=None,
    )
    """Property `CommentAuthor.link`."""


class CompanyMember(BaseModel):
    """Model: `CompanyMember`"""

    user_id: int = Field()
    """Property `CompanyMember.user_id`."""

    company_id: int = Field()
    """Property `CompanyMember.company_id`."""

    role: int = Field()
    """Property `CompanyMember.role`."""

    role_name: str = Field()
    """Property `CompanyMember.role_name`."""

    ts: int = Field()
    """Property `CompanyMember.ts`."""

    groups_count: int = Field()
    """Property `CompanyMember.groups_count`."""

    products_count: int = Field()
    """Property `CompanyMember.products_count`."""

    reporter_url: str = Field()
    """Property `CompanyMember.reporter_url`."""

    groups: list[int] | None = Field(
        default=None,
    )
    """Property `CompanyMember.groups`."""

    products: list["CompanyMemberProduct"] | None = Field(
        default=None,
    )
    """Property `CompanyMember.products`."""


class CompanyMemberProduct(BaseModel):
    """Model: `CompanyMemberProduct`"""

    id: int = Field()
    """Property `CompanyMemberProduct.id`."""

    access: int = Field()
    """Property `CompanyMemberProduct.access`."""

    status: int = Field()
    """Property `CompanyMemberProduct.status`."""

    title: str | None = Field(
        default=None,
    )
    """Property `CompanyMemberProduct.title`."""

    photo_url: str | None = Field(
        default=None,
    )
    """Property `CompanyMemberProduct.photo_url`."""

    licence_status_text: str | None = Field(
        default=None,
    )
    """Property `CompanyMemberProduct.licence_status_text`."""


class CallbackAppPayload(BaseModel):
    """Model: `CallbackAppPayload`"""

    user_id: int = Field()
    """Property `CallbackAppPayload.user_id`."""

    app_id: int = Field()
    """Property `CallbackAppPayload.app_id`."""

    payload: str = Field()
    """Property `CallbackAppPayload.payload`."""


class CallbackAudioNew(BaseModel):
    """Model: `CallbackAudioNew`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class Base(BaseModel):
    """Model: `Base`"""

    type: "CallbackType" = Field()
    """Property `Base.type`."""

    group_id: int = Field()
    """Property `Base.group_id`."""

    event_id: str = Field()
    """Unique event id. If it passed twice or more - you should ignore it.."""

    v: str = Field()
    """API object version."""

    secret: str | None = Field(
        default=None,
    )
    """Property `Base.secret`."""


class CallbackBoardPostDelete(BaseModel):
    """Model: `CallbackBoardPostDelete`"""

    topic_owner_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_owner_id`."""

    topic_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_id`."""

    id: int = Field()
    """Property `CallbackBoardPostDelete.id`."""

    deleter_id: int | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostDelete.deleter_id`."""


class CallbackBoardPostEdit(BaseModel):
    """Model: `CallbackBoardPostEdit`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["CommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.likes`."""


class CallbackBoardPostNew(BaseModel):
    """Model: `CallbackBoardPostNew`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["CommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.likes`."""


class CallbackBoardPostRestore(BaseModel):
    """Model: `CallbackBoardPostRestore`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["CommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.likes`."""


class CallbackDonutMoneyWithdraw(BaseModel):
    """Model: `CallbackDonutMoneyWithdraw`"""

    amount: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount_without_fee`."""


class CallbackDonutMoneyWithdrawError(BaseModel):
    """Model: `CallbackDonutMoneyWithdrawError`"""

    reason: str = Field()
    """Property `CallbackDonutMoneyWithdrawError.reason`."""


class CallbackDonutSubscriptionCancelled(BaseModel):
    """Model: `CallbackDonutSubscriptionCancelled`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCancelled.user_id`."""


class CallbackDonutSubscriptionCreate(BaseModel):
    """Model: `CallbackDonutSubscriptionCreate`"""

    amount: int = Field()
    """Property `CallbackDonutSubscriptionCreate.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionCreate.amount_without_fee`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCreate.user_id`."""


class CallbackDonutSubscriptionExpired(BaseModel):
    """Model: `CallbackDonutSubscriptionExpired`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionExpired.user_id`."""


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    """Model: `CallbackDonutSubscriptionPriceChanged`"""

    amount_old: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_old`."""

    amount_new: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_new`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.user_id`."""

    amount_diff: float | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff`."""

    amount_diff_without_fee: float | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff_without_fee`."""


class CallbackDonutSubscriptionProlonged(BaseModel):
    """Model: `CallbackDonutSubscriptionProlonged`"""

    amount: int = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount_without_fee`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionProlonged.user_id`."""


type CallbackFwdMessages = list[list["CallbackForeignMessage"]]


class CallbackGroupChangePhoto(BaseModel):
    """Model: `CallbackGroupChangePhoto`"""
    user_id: 'int' = Field()
    """Property `CallbackGroupChangePhoto.user_id`."""
    photo: 'Photo' = Field()


class CallbackGroupChangeSettings(BaseModel):
    """Model: `CallbackGroupChangeSettings`"""

    user_id: int = Field()
    """Property `CallbackGroupChangeSettings.user_id`."""

    changes: "GroupSettingsChanges | None" = Field(
        default=None,
    )
    """Property `CallbackGroupChangeSettings.changes`."""


class CallbackGroupJoin(BaseModel):
    """Model: `CallbackGroupJoin`"""

    user_id: int = Field()
    """Property `CallbackGroupJoin.user_id`."""

    join_type: "GroupJoinType" = Field()
    """Property `CallbackGroupJoin.join_type`."""


class GroupJoinType(StrEnum, metaclass=BaseEnumMeta):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    """Model: `CallbackGroupLeave`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.user_id`."""

    self: bool | None = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.self`."""


class GroupMarket(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1


class GroupOfficerRole(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(BaseModel):
    """Model: `CallbackGroupOfficersEdit`"""

    admin_id: int = Field()
    """Property `CallbackGroupOfficersEdit.admin_id`."""

    user_id: int = Field()
    """Property `CallbackGroupOfficersEdit.user_id`."""

    level_old: "GroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_old`."""

    level_new: "GroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_new`."""


class GroupSettingsChanges(BaseModel):
    """Model: `GroupSettingsChanges`"""

    title: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.title`."""

    screen_name: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.screen_name`."""

    event_start_date: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.event_start_date`."""

    event_finish_date: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.event_finish_date`."""

    event_group_id: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.event_group_id`."""

    donations: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.donations`."""

    wall: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.wall`."""

    replies: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.replies`."""

    topics: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.topics`."""

    photos: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.photos`."""

    docs: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.docs`."""

    messages: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.messages`."""

    market: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.market`."""

    market_wiki: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.market_wiki`."""

    board: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.board`."""

    links: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.links`."""

    audio: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.audio`."""

    video: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.video`."""

    can_post_topics: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.can_post_topics`."""

    can_post_albums: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.can_post_albums`."""

    can_post_video: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.can_post_video`."""

    disable_market_comments: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.disable_market_comments`."""

    status_default: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.status_default`."""

    access: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.access`."""

    email: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.email`."""

    country_id: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.country_id`."""

    city_id: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.city_id`."""

    address: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.address`."""

    description: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.description`."""

    website: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.website`."""

    phone: "GroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.phone`."""

    age_limits: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.age_limits`."""

    category_v2: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.category_v2`."""

    public_category: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.public_category`."""

    public_subcategory: "GroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `GroupSettingsChanges.public_subcategory`."""


class GroupSettingsChangesIntegerValues(BaseModel):
    """Model: `GroupSettingsChangesIntegerValues`"""

    old_value: int | None = Field(
        default=None,
    )
    """Property `GroupSettingsChangesIntegerValues.old_value`."""

    new_value: int | None = Field(
        default=None,
    )
    """Property `GroupSettingsChangesIntegerValues.new_value`."""


class GroupSettingsChangesStringValues(BaseModel):
    """Model: `GroupSettingsChangesStringValues`"""

    old_value: str | None = Field(
        default=None,
    )
    """Property `GroupSettingsChangesStringValues.old_value`."""

    new_value: str | None = Field(
        default=None,
    )
    """Property `GroupSettingsChangesStringValues.new_value`."""


class InfoForBots(BaseModel):
    """Model: `InfoForBots`"""

    button_actions: list["TemplateActionTypeNames"] | None = Field(
        default=None,
    )
    """Property `InfoForBots.button_actions`."""

    keyboard: bool | None = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: bool | None = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: bool | None = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: int | None = Field(
        default=None,
    )
    """client or user language id."""


class LikeAddRemove(BaseModel):
    """Model: `LikeAddRemove`"""

    liker_id: int = Field()
    """Property `LikeAddRemove.liker_id`."""

    object_type: "LikeAddRemoveObjectType" = Field()
    """Property `LikeAddRemove.object_type`."""

    object_owner_id: int = Field()
    """Property `LikeAddRemove.object_owner_id`."""

    object_id: int = Field()
    """Property `LikeAddRemove.object_id`."""

    post_id: int = Field()
    """Property `LikeAddRemove.post_id`."""

    thread_reply_id: int | None = Field(
        default=None,
    )
    """Property `LikeAddRemove.thread_reply_id`."""


class MarketComment(BaseModel):
    """Model: `MarketComment`"""

    id: int = Field()
    """Property `MarketComment.id`."""

    from_id: int = Field()
    """Property `MarketComment.from_id`."""

    date: datetime.datetime = Field()
    """Property `MarketComment.date`."""

    text: str | None = Field(
        default=None,
    )
    """Property `MarketComment.text`."""

    market_owner_id: int | None = Field(
        default=None,
    )
    """Property `MarketComment.market_owner_id`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `MarketComment.photo_id`."""


class CallbackMarketCommentDelete(BaseModel):
    """Model: `CallbackMarketCommentDelete`"""

    owner_id: int = Field()
    """Property `CallbackMarketCommentDelete.owner_id`."""

    id: int = Field()
    """Property `CallbackMarketCommentDelete.id`."""

    user_id: int = Field()
    """Property `CallbackMarketCommentDelete.user_id`."""

    item_id: int = Field()
    """Property `CallbackMarketCommentDelete.item_id`."""


class CallbackMessageAllow(BaseModel):
    """Model: `CallbackMessageAllow`"""

    user_id: int = Field()
    """Property `CallbackMessageAllow.user_id`."""

    key: str = Field()
    """Property `CallbackMessageAllow.key`."""


class CallbackMessageDeny(BaseModel):
    """Model: `CallbackMessageDeny`"""

    user_id: int = Field()
    """Property `CallbackMessageDeny.user_id`."""


class CallbackMessageEvent(BaseModel):
    """Model: `CallbackMessageEvent`"""

    user_id: int = Field()
    """Property `CallbackMessageEvent.user_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageEvent.peer_id`."""

    event_id: str = Field()
    """Property `CallbackMessageEvent.event_id`."""

    payload: str = Field()
    """Property `CallbackMessageEvent.payload`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMessageEvent.conversation_message_id`."""


class CallbackMessageNew(BaseModel):
    """Model: `CallbackMessageNew`"""

    client_info: "InfoForBots | None" = Field(
        default=None,
    )
    """Property `CallbackMessageNew.client_info`."""

    message: "CallbackMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessageNew.message`."""


class CallbackMessageObject(BaseModel):
    """Model: `CallbackMessageObject`"""

    client_info: "InfoForBots | None" = Field(
        default=None,
    )
    """Property `CallbackMessageObject.client_info`."""

    message: "CallbackMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessageObject.message`."""


class CallbackMessageReactionEvent(BaseModel):
    """Model: `CallbackMessageReactionEvent`"""

    reacted_id: int = Field()
    """Property `CallbackMessageReactionEvent.reacted_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageReactionEvent.peer_id`."""

    cmid: int = Field()
    """Property `CallbackMessageReactionEvent.cmid`."""

    reaction_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMessageReactionEvent.reaction_id`."""


class CallbackMessageRead(BaseModel):
    """Model: `CallbackMessageRead`"""

    from_id: int = Field()
    """Property `CallbackMessageRead.from_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageRead.peer_id`."""

    read_message_id: int = Field()
    """Property `CallbackMessageRead.read_message_id`."""

    conversation_message_id: int = Field()
    """Property `CallbackMessageRead.conversation_message_id`."""


class MessageTypingStateState(StrEnum, metaclass=BaseEnumMeta):
    MESSAGE_TYPING_STATE = "message_typing_state"
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"
    f__3 = "3"
    f__4 = "4"
    f__5 = "5"


class CallbackMessageTypingState(BaseModel):
    """Model: `CallbackMessageTypingState`"""

    from_id: int = Field()
    """Property `CallbackMessageTypingState.from_id`."""

    to_id: int = Field()
    """Property `CallbackMessageTypingState.to_id`."""

    state: "MessageTypingStateState" = Field()
    """Property `CallbackMessageTypingState.state`."""


class CallbackPhotoCommentDelete(BaseModel):
    """Model: `CallbackPhotoCommentDelete`"""

    id: int = Field()
    """Property `CallbackPhotoCommentDelete.id`."""

    owner_id: int = Field()
    """Property `CallbackPhotoCommentDelete.owner_id`."""

    user_id: int = Field()
    """Property `CallbackPhotoCommentDelete.user_id`."""

    photo_id: int = Field()
    """Property `CallbackPhotoCommentDelete.photo_id`."""

    deleter_id: int = Field()
    """Property `CallbackPhotoCommentDelete.deleter_id`."""


class PhotoNewVerticalAlign(StrEnum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class CallbackPhotoNew(BaseModel):
    """Model: `CallbackPhotoNew`"""

    album_id: int = Field()
    """Album ID."""

    date: datetime.datetime = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    has_tags: bool = Field()
    """Whether photo has attached tag links."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the photo."""

    height: int | None = Field(
        default=None,
    )
    """Original photo height."""

    images: list["Image"] | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.images`."""

    lat: float | None = Field(
        default=None,
    )
    """Latitude."""

    long: float | None = Field(
        default=None,
    )
    """Longitude."""

    photo_256: str | None = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    thumb_hash: str | None = Field(
        default=None,
    )
    """Thumb Hash."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""

    place: str | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.place`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""

    sizes: list["PhotoSizes"] | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.sizes`."""

    square_crop: str | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.square_crop`."""

    text: str | None = Field(
        default=None,
    )
    """Photo caption."""

    user_id: int | None = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: int | None = Field(
        default=None,
    )
    """Original photo width."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.likes`."""

    comments: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.comments`."""

    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.reposts`."""

    tags: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.tags`."""

    hidden: "PropertyExists | None" = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the photo."""

    vertical_align: "PhotoNewVerticalAlign | None" = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""


class CallbackPollVoteNew(BaseModel):
    """Model: `CallbackPollVoteNew`"""

    owner_id: int = Field()
    """Property `CallbackPollVoteNew.owner_id`."""

    poll_id: int = Field()
    """Property `CallbackPollVoteNew.poll_id`."""

    option_id: int = Field()
    """Property `CallbackPollVoteNew.option_id`."""

    user_id: int = Field()
    """Property `CallbackPollVoteNew.user_id`."""


class CallbackType(StrEnum, metaclass=BaseEnumMeta):
    AUDIO_NEW = "audio_new"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    CONFIRMATION = "confirmation"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MARKET_ORDER_NEW = "market_order_new"
    MARKET_ORDER_EDIT = "market_order_edit"
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    MESSAGE_REACTION_EVENT = "message_reaction_event"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"
    WALL_SCHEDULE_POST_NEW = "wall_schedule_post_new"
    WALL_SCHEDULE_POST_DELETE = "wall_schedule_post_delete"


class CallbackUserBlock(BaseModel):
    """Model: `CallbackUserBlock`"""

    admin_id: int = Field()
    """Property `CallbackUserBlock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserBlock.user_id`."""

    unblock_date: datetime.datetime = Field()
    """Property `CallbackUserBlock.unblock_date`."""

    reason: int = Field()
    """Property `CallbackUserBlock.reason`."""

    comment: str | None = Field(
        default=None,
    )
    """Property `CallbackUserBlock.comment`."""


class CallbackUserUnblock(BaseModel):
    """Model: `CallbackUserUnblock`"""

    admin_id: int = Field()
    """Property `CallbackUserUnblock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserUnblock.user_id`."""

    by_end_date: datetime.datetime = Field()
    """Property `CallbackUserUnblock.by_end_date`."""


class CallbackVideoCommentDelete(BaseModel):
    """Model: `CallbackVideoCommentDelete`"""

    id: int = Field()
    """Property `CallbackVideoCommentDelete.id`."""

    owner_id: int = Field()
    """Property `CallbackVideoCommentDelete.owner_id`."""

    deleter_id: int = Field()
    """Property `CallbackVideoCommentDelete.deleter_id`."""

    video_id: int = Field()
    """Property `CallbackVideoCommentDelete.video_id`."""


class CallbackVideoNew(BaseModel):
    """Model: `CallbackVideoNew`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class CallbackVkpayTransaction(BaseModel):
    """Model: `CallbackVkpayTransaction`"""

    amount: int = Field()
    """Property `CallbackVkpayTransaction.amount`."""

    from_id: int = Field()
    """Property `CallbackVkpayTransaction.from_id`."""

    description: str = Field()
    """Property `CallbackVkpayTransaction.description`."""

    date: datetime.datetime = Field()
    """Property `CallbackVkpayTransaction.date`."""

    payload: str | None = Field(
        default=None,
    )
    """Property `CallbackVkpayTransaction.payload`."""


class WallCommentDelete(BaseModel):
    """Model: `WallCommentDelete`"""

    owner_id: int = Field()
    """Property `WallCommentDelete.owner_id`."""

    id: int = Field()
    """Property `WallCommentDelete.id`."""

    user_id: int = Field()
    """Property `WallCommentDelete.user_id`."""

    post_id: int = Field()
    """Property `WallCommentDelete.post_id`."""


class WallPostNewInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallPostNew(BaseModel):
    """Model: `CallbackWallPostNew`"""

    inner_type: "WallPostNewInnerType" = Field()
    """Property `CallbackWallPostNew.inner_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.is_deleted`."""

    deleted_reason: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_reason`."""

    deleted_details: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_details`."""

    donut_miniapp_url: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.donut_miniapp_url`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.attachments`."""

    copyright: "PostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: int | None = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Post author ID."""

    geo: "Geo | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Post ID."""

    is_archived: bool | None = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: int | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: "PostSource | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_source`."""

    post_type: "PostType | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_type`."""

    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.reposts`."""

    signer_id: int | None = Field(
        default=None,
    )
    """Post signer ID."""

    text: str | None = Field(
        default=None,
    )
    """Post text."""

    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""


class CallbackWallReplyEdit(BaseModel):
    """Model: `CallbackWallReplyEdit`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.video_id`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.attachments`."""

    donut: "WallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.donut`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyNew(BaseModel):
    """Model: `CallbackWallReplyNew`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.video_id`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.attachments`."""

    donut: "WallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.donut`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyRestore(BaseModel):
    """Model: `CallbackWallReplyRestore`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.video_id`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.attachments`."""

    donut: "WallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.donut`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class WallRepostInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallRepost(BaseModel):
    """Model: `CallbackWallRepost`"""

    inner_type: "WallRepostInnerType" = Field()
    """Property `CallbackWallRepost.inner_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.is_deleted`."""

    deleted_reason: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_reason`."""

    deleted_details: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_details`."""

    donut_miniapp_url: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.donut_miniapp_url`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.attachments`."""

    copyright: "PostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: int | None = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Post author ID."""

    geo: "Geo | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Post ID."""

    is_archived: bool | None = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: int | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: "PostSource | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_source`."""

    post_type: "PostType | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_type`."""

    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.reposts`."""

    signer_id: int | None = Field(
        default=None,
    )
    """Post signer ID."""

    text: str | None = Field(
        default=None,
    )
    """Post text."""

    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""


class CallsCall(BaseModel):
    """Model: `CallsCall`"""

    initiator_id: int = Field()
    """Caller initiator."""

    receiver_id: int = Field()
    """Caller receiver."""

    state: "EndState" = Field()
    """Property `CallsCall.state`."""

    time: int = Field()
    """Timestamp for call."""

    duration: int | None = Field(
        default=None,
    )
    """CallEvent duration."""

    video: bool | None = Field(
        default=None,
    )
    """Was this call initiated as video call."""

    participants: "Participants | None" = Field(
        default=None,
    )
    """Property `CallsCall.participants`."""


class EndState(StrEnum, metaclass=BaseEnumMeta):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class Participants(BaseModel):
    """Model: `Participants`"""

    list_: list[int] | None = Field(
        default=None,
        alias="list",
    )
    """Property `Participants.list`."""

    count: int | None = Field(
        default=None,
    )
    """Participants count."""


class ShortCredentials(BaseModel):
    """These credentials may be used to join a call without knowing a VK Join Link
    Model: `ShortCredentials`
    """

    id: str = Field()
    """Short numeric ID of a call."""

    password: str = Field()
    """Password that can be used to join a call by short numeric ID."""

    link_without_password: str = Field()
    """Link without a password."""

    link_with_password: str = Field()
    """Link with a password."""


class CommentThread(BaseModel):
    """Model: `CommentThread`"""

    count: int = Field()
    """Comments number."""

    items: list["WallComment"] | None = Field(
        default=None,
    )
    """Property `CommentThread.items`."""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    show_reply_button: bool | None = Field(
        default=None,
    )
    """Information whether recommended to display reply button."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    author_replied: bool | None = Field(
        default=None,
    )
    """Information whether author commented the thread."""


type DatabaseCitiesFields = str


class CityById(BaseModel):
    """Model: `CityById`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class Faculty(BaseModel):
    """Model: `Faculty`"""

    id: int | None = Field(
        default=None,
    )
    """Faculty ID."""

    title: str | None = Field(
        default=None,
    )
    """Faculty title."""


class LanguageFull(BaseModel):
    """Model: `LanguageFull`"""

    id: int = Field()
    """Language ID."""

    native_name: str = Field()
    """Language native name."""


class Region(BaseModel):
    """Model: `Region`"""

    id: int | None = Field(
        default=None,
    )
    """Region ID."""

    title: str | None = Field(
        default=None,
    )
    """Region title."""


class DatabaseSchool(BaseModel):
    """Model: `DatabaseSchool`"""

    id: int | None = Field(
        default=None,
    )
    """School ID."""

    title: str | None = Field(
        default=None,
    )
    """School title."""


class SchoolClass(BaseModel):
    """Model: `SchoolClass`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class Station(BaseModel):
    """Model: `Station`"""

    id: int = Field()
    """Station ID."""

    name: str = Field()
    """Station name."""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    color: str | None = Field(
        default=None,
    )
    """Hex color code without #."""


class DatabaseUniversity(BaseModel):
    """Model: `DatabaseUniversity`"""

    id: int | None = Field(
        default=None,
    )
    """University ID."""

    title: str | None = Field(
        default=None,
    )
    """University title."""


class Doc(BaseModel):
    """Model: `Doc`"""

    id: int = Field()
    """Document ID."""

    owner_id: int = Field()
    """Document owner ID."""

    title: str = Field()
    """Document title."""

    size: int = Field()
    """File size in bites."""

    ext: str = Field()
    """File extension."""

    date: datetime.datetime = Field()
    """Date when file has been uploaded in Unixtime."""

    type: int = Field()
    """Document type."""

    url: str | None = Field(
        default=None,
    )
    """File URL."""

    preview: "DocPreview | None" = Field(
        default=None,
    )
    """Property `Doc.preview`."""

    is_licensed: bool | None = Field(
        default=None,
    )
    """Property `Doc.is_licensed`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the document."""

    tags: list[str] | None = Field(
        default=None,
    )
    """Document tags."""

    @property
    def as_att(self) -> str:
        """Строка-вложение VK: ``doc{owner_id}_{id}[_{access_key}]``."""
        return attachment_string("doc", self.owner_id, self.id, self.access_key)


class DocAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocPreview(BaseModel):
    """Model: `DocPreview`"""

    audio_msg: "DocPreviewAudioMsg | None" = Field(
        default=None,
    )
    """Property `DocPreview.audio_msg`."""

    graffiti: "DocPreviewGraffiti | None" = Field(
        default=None,
    )
    """Property `DocPreview.graffiti`."""

    photo: "DocPreviewPhoto | None" = Field(
        default=None,
    )
    """Property `DocPreview.photo`."""

    video: "DocPreviewVideo | None" = Field(
        default=None,
    )
    """Property `DocPreview.video`."""


class DocPreviewAudioMsg(BaseModel):
    """Model: `DocPreviewAudioMsg`"""

    duration: int = Field()
    """Audio message duration in seconds."""

    link_mp3: str = Field()
    """MP3 file URL."""

    link_ogg: str = Field()
    """OGG file URL."""

    waveform: list[int] = Field()
    """Property `DocPreviewAudioMsg.waveform`."""


class DocPreviewGraffiti(BaseModel):
    """Model: `DocPreviewGraffiti`"""

    src: str = Field()
    """Graffiti file URL."""

    width: int = Field()
    """Graffiti width."""

    height: int = Field()
    """Graffiti height."""


class DocPreviewPhoto(BaseModel):
    """Model: `DocPreviewPhoto`"""

    sizes: list["DocPreviewPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `DocPreviewPhoto.sizes`."""


class DocPreviewPhotoSizes(BaseModel):
    """Model: `DocPreviewPhotoSizes`"""

    src: str = Field()
    """URL of the image."""

    width: int = Field()
    """Width in px."""

    height: int = Field()
    """Height in px."""

    type: "PhotoSizesType" = Field()
    """Property `DocPreviewPhotoSizes.type`."""


class DocPreviewVideo(BaseModel):
    """Model: `DocPreviewVideo`"""

    src: str = Field()
    """Video URL."""

    width: int = Field()
    """Video\'s width in pixels."""

    height: int = Field()
    """Video\'s height in pixels."""

    file_size: int = Field()
    """Video file size in bites."""


class DocTypes(BaseModel):
    """Model: `DocTypes`"""

    id: int = Field()
    """Doc type ID."""

    name: str = Field()
    """Doc type title."""

    count: int = Field()
    """Number of docs."""


class DonatorSubscriptionInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    EXPIRING = "expiring"


class DonatorSubscriptionInfo(BaseModel):
    """Info about user VK Donut subscription
    Model: `DonatorSubscriptionInfo`
    """

    owner_id: int = Field()
    """Property `DonatorSubscriptionInfo.owner_id`."""

    next_payment_date: datetime.datetime = Field()
    """Property `DonatorSubscriptionInfo.next_payment_date`."""

    amount: int = Field()
    """Property `DonatorSubscriptionInfo.amount`."""

    status: "DonatorSubscriptionInfoStatus" = Field()
    """Property `DonatorSubscriptionInfo.status`."""


class EventsEventAttach(BaseModel):
    """Model: `EventsEventAttach`"""

    button_text: str = Field()
    """text of attach."""

    friends: list[int] = Field()
    """array of friends ids."""

    id: int = Field()
    """event ID."""

    is_favorite: bool = Field()
    """is favorite."""

    text: str = Field()
    """text of attach."""

    address: str | None = Field(
        default=None,
    )
    """address of event."""

    member_status: "GroupFullMemberStatus | None" = Field(
        default=None,
    )
    """Current user\'s member status."""

    time: int | None = Field(
        default=None,
    )
    """event start time."""


class Bookmark(BaseModel):
    """Model: `Bookmark`"""

    added_date: datetime.datetime = Field()
    """Timestamp, when this item was bookmarked."""

    seen: bool = Field()
    """Has user seen this item."""

    tags: list["Tag"] = Field()
    """Property `Bookmark.tags`."""

    type: "BookmarkType" = Field()
    """Item type."""

    link: "Link | None" = Field(
        default=None,
    )
    """Property `Bookmark.link`."""

    post: "WallpostFull | None" = Field(
        default=None,
    )
    """Property `Bookmark.post`."""

    product: "MarketItemFull | None" = Field(
        default=None,
    )
    """Property `Bookmark.product`."""

    video: "VideoFull | None" = Field(
        default=None,
    )
    """Property `Bookmark.video`."""


class BookmarkType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"
    CLIP = "clip"
    GAME = "game"
    MINI_APP = "mini_app"


class Page(BaseModel):
    """Model: `Page`"""

    description: str = Field()
    """Some info about user or group."""

    tags: list["Tag"] = Field()
    """Property `Page.tags`."""

    type: "PageType" = Field()
    """Item type."""

    group: "GroupFull | None" = Field(
        default=None,
    )
    """Property `Page.group`."""

    updated_date: datetime.datetime | None = Field(
        default=None,
    )
    """Timestamp, when this page was bookmarked."""

    user: "UserFull | None" = Field(
        default=None,
    )
    """Property `Page.user`."""


class PageType(StrEnum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class Tag(BaseModel):
    """Model: `Tag`"""

    id: int | None = Field(
        default=None,
    )
    """Tag id."""

    name: str | None = Field(
        default=None,
    )
    """Tag name."""


class Gift(BaseModel):
    """Model: `Gift`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when gist has been sent in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Gift sender ID."""

    gift: "Layout | None" = Field(
        default=None,
    )
    """Property `Gift.gift`."""

    gift_hash: str | None = Field(
        default=None,
    )
    """Hash."""

    id: int | None = Field(
        default=None,
    )
    """Gift ID."""

    message: str | None = Field(
        default=None,
    )
    """Comment text."""

    privacy: "GiftPrivacy | None" = Field(
        default=None,
    )
    """Property `Gift.privacy`."""


class GiftPrivacy(IntEnum, metaclass=BaseEnumMeta):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class Layout(BaseModel):
    """Model: `Layout`"""

    id: int = Field()
    """Gift ID."""

    thumb_512: str | None = Field(
        default=None,
    )
    """URL of the preview image with 512 px in width."""

    thumb_256: str | None = Field(
        default=None,
    )
    """URL of the preview image with 256 px in width."""

    thumb_48: str | None = Field(
        default=None,
    )
    """URL of the preview image with 48 px in width."""

    thumb_96: str | None = Field(
        default=None,
    )
    """URL of the preview image with 96 px in width."""

    stickers_product_id: int | None = Field(
        default=None,
    )
    """ID of the sticker pack, if the gift is representing one."""

    is_stickers_style: bool | None = Field(
        default=None,
    )
    """Information whether gift represents a stickers style."""

    build_id: str | None = Field(
        default=None,
    )
    """ID of the build of constructor gift."""

    keywords: str | None = Field(
        default=None,
    )
    """Keywords used for search."""


class Address(BaseModel):
    """Model: `Address`"""

    id: int = Field()
    """Address id."""

    additional_address: str | None = Field(
        default=None,
    )
    """Additional address to the place (6 floor, left door)."""

    address: str | None = Field(
        default=None,
    )
    """String address to the place (Nevsky, 28)."""

    city_id: int | None = Field(
        default=None,
    )
    """City id of address."""

    city: "CityById | None" = Field(
        default=None,
    )
    """City for address."""

    metro_station: "Station | None" = Field(
        default=None,
    )
    """Metro for address."""

    country: "BaseCountry | None" = Field(
        default=None,
    )
    """Country for address."""

    distance: int | None = Field(
        default=None,
    )
    """Distance from the point."""

    latitude: float | None = Field(
        default=None,
    )
    """Address latitude."""

    longitude: float | None = Field(
        default=None,
    )
    """Address longitude."""

    metro_station_id: int | None = Field(
        default=None,
    )
    """Metro id of address."""

    phone: str | None = Field(
        default=None,
    )
    """Address phone."""

    time_offset: int | None = Field(
        default=None,
    )
    """Time offset int minutes from utc time."""

    timetable: "AddressTimetable | None" = Field(
        default=None,
    )
    """Week timetable for the address."""

    title: str | None = Field(
        default=None,
    )
    """Title of the place (Zinger, etc)."""

    work_info_status: "AddressWorkInfoStatus | None" = Field(
        default=None,
    )
    """Status of information about timetable."""

    place_id: int | None = Field(
        default=None,
    )
    """Property `Address.place_id`."""


class AddressTimetable(BaseModel):
    """Timetable for a week
    Model: `AddressTimetable`
    """

    fri: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for friday."""

    mon: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for monday."""

    sat: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for saturday."""

    sun: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for sunday."""

    thu: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for thursday."""

    tue: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for tuesday."""

    wed: "AddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for wednesday."""


class AddressTimetableDay(BaseModel):
    """Timetable for one day
    Model: `AddressTimetableDay`
    """

    close_time: int = Field()
    """Close time in minutes."""

    open_time: int = Field()
    """Open time in minutes."""

    break_close_time: int | None = Field(
        default=None,
    )
    """Close time of the break in minutes."""

    break_open_time: int | None = Field(
        default=None,
    )
    """Start time of the break in minutes."""


class AddressWorkInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class AddressesInfo(BaseModel):
    """Model: `AddressesInfo`"""

    is_enabled: bool = Field()
    """Information whether addresses is enabled."""

    main_address_id: int | None = Field(
        default=None,
    )
    """Main address id for group."""

    main_address: "Address | None" = Field(
        default=None,
    )
    """Main address."""

    count: int | None = Field(
        default=None,
    )
    """Count of addresses."""


class BanInfo(BaseModel):
    """Model: `BanInfo`"""

    admin_id: int | None = Field(
        default=None,
    )
    """Administrator ID."""

    comment: str | None = Field(
        default=None,
    )
    """Comment for a ban."""

    comment_visible: bool | None = Field(
        default=None,
    )
    """Show comment for user."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Property `BanInfo.is_closed`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when user has been added to blacklist in Unixtime."""

    end_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when user will be removed from blacklist in Unixtime."""

    reason: "BanInfoReason | None" = Field(
        default=None,
    )
    """Property `BanInfo.reason`."""


class BanInfoReason(IntEnum, metaclass=BaseEnumMeta):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


class CallbackServerStatus(StrEnum, metaclass=BaseEnumMeta):
    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class CallbackServer(BaseModel):
    """Model: `CallbackServer`"""

    id: int = Field()
    """Property `CallbackServer.id`."""

    title: str = Field()
    """Property `CallbackServer.title`."""

    creator_id: int = Field()
    """Property `CallbackServer.creator_id`."""

    url: str = Field()
    """Property `CallbackServer.url`."""

    secret_key: str = Field()
    """Property `CallbackServer.secret_key`."""

    status: "CallbackServerStatus" = Field()
    """Property `CallbackServer.status`."""


class CallbackSettings(BaseModel):
    """Model: `CallbackSettings`"""

    api_version: str | None = Field(
        default=None,
    )
    """API version used for the events."""

    events: "LongPollEvents | None" = Field(
        default=None,
    )
    """Property `CallbackSettings.events`."""


class ContactsItem(BaseModel):
    """Model: `ContactsItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""

    desc: str | None = Field(
        default=None,
    )
    """Contact description."""

    phone: str | None = Field(
        default=None,
    )
    """Contact phone."""

    email: str | None = Field(
        default=None,
    )
    """Contact email."""


class CountersGroup(BaseModel):
    """Model: `CountersGroup`"""

    addresses: int | None = Field(
        default=None,
    )
    """Addresses number."""

    albums: int | None = Field(
        default=None,
    )
    """Photo albums number."""

    audios: int | None = Field(
        default=None,
    )
    """Audios number."""

    audio_playlists: int | None = Field(
        default=None,
    )
    """Audio playlists number."""

    docs: int | None = Field(
        default=None,
    )
    """Docs number."""

    market: int | None = Field(
        default=None,
    )
    """Market items number."""

    photos: int | None = Field(
        default=None,
    )
    """Photos number."""

    topics: int | None = Field(
        default=None,
    )
    """Topics number."""

    videos: int | None = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: int | None = Field(
        default=None,
    )
    """Playlists number."""

    market_services: int | None = Field(
        default=None,
    )
    """Market services number."""

    podcasts: int | None = Field(
        default=None,
    )
    """Podcasts number."""

    articles: int | None = Field(
        default=None,
    )
    """Articles number."""

    narratives: int | None = Field(
        default=None,
    )
    """Narratives number."""

    clips: int | None = Field(
        default=None,
    )
    """Clips number."""

    clips_followers: int | None = Field(
        default=None,
    )
    """Clips followers number."""

    videos_followers: int | None = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: int | None = Field(
        default=None,
    )
    """Clips views number."""

    clips_likes: int | None = Field(
        default=None,
    )
    """Clips likes number."""


class GroupsFields(StrEnum, metaclass=BaseEnumMeta):
    ID = "id"
    NAME = "name"
    SCREEN_NAME = "screen_name"
    IS_CLOSED = "is_closed"
    TYPE = "type"
    IS_ADMIN = "is_admin"
    ADMIN_LEVEL = "admin_level"
    IS_MEMBER = "is_member"
    IS_ADVERTISER = "is_advertiser"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    DEACTIVATED = "deactivated"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    EST_DATE = "est_date"
    PUBLIC_DATE_LABEL = "public_date_label"
    PHOTO_MAX_SIZE = "photo_max_size"
    IS_VIDEO_LIVE_NOTIFICATIONS_BLOCKED = "is_video_live_notifications_blocked"
    VIDEO_LIVE = "video_live"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_ADULT = "is_adult"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    CITY = "city"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    MEMBERS_COUNT_TEXT = "members_count_text"
    REQUESTS_COUNT = "requests_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    TEXTLIVES_COUNT = "textlives_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SUGGEST = "can_suggest"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_UPLOAD_CLIP = "can_upload_clip"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_CREATE_TOPIC = "can_create_topic"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    CROP_PHOTO = "crop_photo"
    STATUS = "status"
    STATUS_AUDIO = "status_audio"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    WALL = "wall"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    ONLINE_STATUS = "online_status"
    INVITED_BY = "invited_by"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    HAS_MARKET_APP = "has_market_app"
    USING_VKPAY_MARKET_APP = "using_vkpay_market_app"
    HAS_GROUP_CHANNEL = "has_group_channel"
    ADDRESSES = "addresses"
    MESSAGES = "messages"
    BUSINESS_RATING = "business_rating"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    LIVE_COVERS = "live_covers"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    CATEGORY = "category"
    CATEGORY0 = "category0"
    CATEGORY1 = "category1"
    RATING = "rating"
    IS_MARKET_MARKET_LINK_ATTACHMENT_ENABLED = "is_market_market_link_attachment_enabled"
    IS_MARKET_MESSAGE_TO_BC_ATTACHMENT_ENABLED = "is_market_message_to_bc_attachment_enabled"
    UNREAD_COUNT = "unread_count"
    VIDEOS_COUNT = "videos_count"


class Filter(StrEnum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class Group(BaseModel):
    """Model: `Group`"""

    id: int = Field()
    """Community ID."""

    name: str | None = Field(
        default=None,
    )
    """Community name."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain of the community page."""

    is_closed: "GroupIsClosed | None" = Field(
        default=None,
    )
    """Property `Group.is_closed`."""

    type: "GroupType | None" = Field(
        default=None,
    )
    """Property `Group.type`."""

    is_admin: bool | None = Field(
        default=None,
    )
    """Information whether current user is administrator."""

    admin_level: "GroupAdminLevel | None" = Field(
        default=None,
    )
    """Property `Group.admin_level`."""

    is_member: bool | None = Field(
        default=None,
    )
    """Information whether current user is member."""

    is_advertiser: bool | None = Field(
        default=None,
    )
    """Information whether current user is advertiser."""

    start_date: datetime.datetime | None = Field(
        default=None,
    )
    """Start date in Unixtime format."""

    finish_date: datetime.datetime | None = Field(
        default=None,
    )
    """Finish date in Unixtime format."""

    verified: bool | None = Field(
        default=None,
    )
    """Information whether community is verified."""

    deactivated: str | None = Field(
        default=None,
    )
    """Information whether community is banned."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 50 pixels in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 100 pixels in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width."""

    photo_200_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width original."""

    photo_400: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width."""

    photo_400_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width original."""

    photo_max: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width."""

    photo_max_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width original."""

    est_date: str | None = Field(
        default=None,
    )
    """Established date."""

    public_date_label: str | None = Field(
        default=None,
    )
    """Public date label."""

    photo_max_size: "PhotoSize | None" = Field(
        default=None,
    )
    """Property `Group.photo_max_size`."""

    is_video_live_notifications_blocked: bool | None = Field(
        default=None,
    )
    """Property `Group.is_video_live_notifications_blocked`."""

    video_live: "LiveInfo | None" = Field(
        default=None,
    )
    """Property `Group.video_live`."""


class GroupAccess(IntEnum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupAdminLevel(IntEnum, metaclass=BaseEnumMeta):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupAgeLimits(IntEnum, metaclass=BaseEnumMeta):
    UNLIMITED = 1
    F__16_PLUS = 2
    F__18_PLUS = 3


class GroupAttach(BaseModel):
    """Model: `GroupAttach`"""

    id: int = Field()
    """group ID."""

    text: str = Field()
    """text of attach."""

    status: str = Field()
    """activity or category of group."""

    size: int = Field()
    """size of group."""

    is_favorite: bool = Field()
    """is favorite."""


class GroupAudio(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupBanInfo(BaseModel):
    """Model: `GroupBanInfo`"""

    comment: str | None = Field(
        default=None,
    )
    """Ban comment."""

    end_date: datetime.datetime | None = Field(
        default=None,
    )
    """End date of ban in Unixtime."""

    reason: "BanInfoReason | None" = Field(
        default=None,
    )
    """Property `GroupBanInfo.reason`."""


class GroupCategory(BaseModel):
    """Model: `GroupCategory`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: list["GroupSubcategory"] | None = Field(
        default=None,
    )
    """Property `GroupCategory.subcategories`."""


class GroupCategoryFull(BaseModel):
    """Model: `GroupCategoryFull`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    page_count: int = Field()
    """Pages number."""

    page_previews: list["Group"] = Field()
    """Property `GroupCategoryFull.page_previews`."""

    subcategories: list["GroupCategory"] | None = Field(
        default=None,
    )
    """Property `GroupCategoryFull.subcategories`."""


class GroupCategoryType(BaseModel):
    """Model: `GroupCategoryType`"""

    id: int = Field()
    """Property `GroupCategoryType.id`."""

    name: str = Field()
    """Property `GroupCategoryType.name`."""


class GroupDocs(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupFullAgeLimits(IntEnum, metaclass=BaseEnumMeta):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupFullMemberStatus(IntEnum, metaclass=BaseEnumMeta):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupFullSection(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIOS = 3
    VIDEOS = 4
    MARKET = 5
    STORIES = 6
    APPS = 7
    FOLLOWERS = 8
    LINKS = 9
    EVENTS = 10
    PLACES = 11
    CONTACTS = 12
    APP_BTNS = 13
    DOCS = 14
    EVENT_COUNTERS = 15
    GROUP_MESSAGES = 16
    ALBUMS = 24
    CATEGORIES = 26
    ADMIN_HELP = 27
    APP_WIDGET = 31
    PUBLIC_HELP = 32
    HS_DONATION_APP = 33
    HS_MARKET_APP = 34
    ADDRESSES = 35
    ARTIST_PAGE = 36
    PODCAST = 37
    ARTICLES = 39
    ADMIN_TIPS = 40
    MENU = 41
    FIXED_POST = 42
    CHATS = 43
    EVERGREEN_NOTICE = 44
    MUSICIANS = 45
    NARRATIVES = 46
    DONUT_DONATE = 47
    CLIPS = 48
    MARKET_CART = 49
    CURATORS = 50
    MARKET_SERVICES = 51
    CLASSIFIEDS = 53
    TEXTLIVES = 54
    DONUT_FOR_DONS = 55
    BADGES = 57
    CHATS_CREATION = 58
    STREAM_CREATION = 59
    RATING = 60
    SERVICE_RATING = 61
    RECOMMENDED_TIPS_WIDGET = 62


class GroupIsClosed(IntEnum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupMarketCurrency(IntEnum, metaclass=BaseEnumMeta):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupPhotos(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupPublicCategoryList(BaseModel):
    """Model: `GroupPublicCategoryList`"""

    id: int | None = Field(
        default=None,
    )
    """Property `GroupPublicCategoryList.id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `GroupPublicCategoryList.name`."""

    subcategories: list["GroupCategoryType"] | None = Field(
        default=None,
    )
    """Property `GroupPublicCategoryList.subcategories`."""


class GroupRole(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupSubcategory(BaseModel):
    """Model: `GroupSubcategory`"""

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""

    genders: list["ObjectWithName"] | None = Field(
        default=None,
    )
    """Property `GroupSubcategory.genders`."""


class GroupSubject(IntEnum, metaclass=BaseEnumMeta):
    AUTO = 1
    ACTIVITY_HOLIDAYS = 2
    BUSINESS = 3
    PETS = 4
    HEALTH = 5
    DATING_AND_COMMUNICATION = 6
    GAMES = 7
    IT = 8
    CINEMA = 9
    BEAUTY_AND_FASHION = 10
    COOKING = 11
    ART_AND_CULTURE = 12
    LITERATURE = 13
    MOBILE_SERVICES_AND_INTERNET = 14
    MUSIC = 15
    SCIENCE_AND_TECHNOLOGY = 16
    REAL_ESTATE = 17
    NEWS_AND_MEDIA = 18
    SECURITY = 19
    EDUCATION = 20
    HOME_AND_RENOVATIONS = 21
    POLITICS = 22
    FOOD = 23
    INDUSTRY = 24
    TRAVEL = 25
    WORK = 26
    ENTERTAINMENT = 27
    RELIGION = 28
    FAMILY = 29
    SPORTS = 30
    INSURANCE = 31
    TELEVISION = 32
    GOODS_AND_SERVICES = 33
    HOBBIES = 34
    FINANCE = 35
    PHOTO = 36
    ESOTERICS = 37
    ELECTRONICS_AND_APPLIANCES = 38
    EROTIC = 39
    HUMOR = 40
    SOCIETY_HUMANITIES = 41
    DESIGN_AND_GRAPHICS = 42


class GroupSuggestedPrivacy(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    ALL = 1
    SUBSCRIBERS = 2


class GroupTagColor(StrEnum, metaclass=BaseEnumMeta):
    f__454647 = "454647"
    f__45678f = "45678f"
    f__4bb34b = "4bb34b"
    f__5181b8 = "5181b8"
    f__539b9c = "539b9c"
    f__5c9ce6 = "5c9ce6"
    f__63b9ba = "63b9ba"
    f__6bc76b = "6bc76b"
    f__76787a = "76787a"
    f__792ec0 = "792ec0"
    f__7a6c4f = "7a6c4f"
    f__7ececf = "7ececf"
    f__9e8d6b = "9e8d6b"
    A162DE = "a162de"
    AAAEB3 = "aaaeb3"
    BBAA84 = "bbaa84"
    E64646 = "e64646"
    FF5C5C = "ff5c5c"
    FFA000 = "ffa000"
    FFC107 = "ffc107"


class GroupTag(BaseModel):
    """Model: `GroupTag`"""

    id: int = Field()
    """Property `GroupTag.id`."""

    name: str = Field()
    """Property `GroupTag.name`."""

    color: "GroupTagColor" = Field()
    """Property `GroupTag.color`."""

    uses: int | None = Field(
        default=None,
    )
    """Property `GroupTag.uses`."""


class GroupTopics(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupVideo(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupWall(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupWiki(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsArray(BaseModel):
    """Model: `GroupsArray`"""

    count: int = Field()
    """Communities number."""

    items: list[int] = Field()
    """Property `GroupsArray.items`."""


class LinksItem(BaseModel):
    """Model: `LinksItem`"""

    name: str | None = Field(
        default=None,
    )
    """Link title."""

    desc: str | None = Field(
        default=None,
    )
    """Link description."""

    edit_title: bool | None = Field(
        default=None,
    )
    """Information whether the link title can be edited."""

    id: int | None = Field(
        default=None,
    )
    """Link ID."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square image of the link with 100 pixels in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square image of the link with 50 pixels in width."""

    url: str | None = Field(
        default=None,
    )
    """Link URL."""

    image_processing: bool | None = Field(
        default=None,
    )
    """Information whether the image on processing."""


class LiveCovers(BaseModel):
    """Model: `LiveCovers`"""

    is_enabled: bool = Field()
    """Information whether live covers is enabled."""

    is_scalable: bool | None = Field(
        default=None,
    )
    """Information whether live covers photo scaling is enabled."""

    story_ids: list[str] | None = Field(
        default=None,
    )
    """Property `LiveCovers.story_ids`."""


class LongPollEvents(BaseModel):
    """Model: `LongPollEvents`"""

    audio_new: bool = Field()
    """Property `LongPollEvents.audio_new`."""

    board_post_delete: bool = Field()
    """Property `LongPollEvents.board_post_delete`."""

    board_post_edit: bool = Field()
    """Property `LongPollEvents.board_post_edit`."""

    board_post_new: bool = Field()
    """Property `LongPollEvents.board_post_new`."""

    board_post_restore: bool = Field()
    """Property `LongPollEvents.board_post_restore`."""

    group_change_photo: bool = Field()
    """Property `LongPollEvents.group_change_photo`."""

    group_change_settings: bool = Field()
    """Property `LongPollEvents.group_change_settings`."""

    group_join: bool = Field()
    """Property `LongPollEvents.group_join`."""

    group_leave: bool = Field()
    """Property `LongPollEvents.group_leave`."""

    group_officers_edit: bool = Field()
    """Property `LongPollEvents.group_officers_edit`."""

    market_comment_delete: bool = Field()
    """Property `LongPollEvents.market_comment_delete`."""

    market_comment_edit: bool = Field()
    """Property `LongPollEvents.market_comment_edit`."""

    market_comment_new: bool = Field()
    """Property `LongPollEvents.market_comment_new`."""

    market_comment_restore: bool = Field()
    """Property `LongPollEvents.market_comment_restore`."""

    message_allow: bool = Field()
    """Property `LongPollEvents.message_allow`."""

    message_deny: bool = Field()
    """Property `LongPollEvents.message_deny`."""

    message_new: bool = Field()
    """Property `LongPollEvents.message_new`."""

    message_read: bool = Field()
    """Property `LongPollEvents.message_read`."""

    message_reply: bool = Field()
    """Property `LongPollEvents.message_reply`."""

    message_typing_state: bool = Field()
    """Property `LongPollEvents.message_typing_state`."""

    message_edit: bool = Field()
    """Property `LongPollEvents.message_edit`."""

    photo_comment_delete: bool = Field()
    """Property `LongPollEvents.photo_comment_delete`."""

    photo_comment_edit: bool = Field()
    """Property `LongPollEvents.photo_comment_edit`."""

    photo_comment_new: bool = Field()
    """Property `LongPollEvents.photo_comment_new`."""

    photo_comment_restore: bool = Field()
    """Property `LongPollEvents.photo_comment_restore`."""

    photo_new: bool = Field()
    """Property `LongPollEvents.photo_new`."""

    poll_vote_new: bool = Field()
    """Property `LongPollEvents.poll_vote_new`."""

    user_block: bool = Field()
    """Property `LongPollEvents.user_block`."""

    user_unblock: bool = Field()
    """Property `LongPollEvents.user_unblock`."""

    video_comment_delete: bool = Field()
    """Property `LongPollEvents.video_comment_delete`."""

    video_comment_edit: bool = Field()
    """Property `LongPollEvents.video_comment_edit`."""

    video_comment_new: bool = Field()
    """Property `LongPollEvents.video_comment_new`."""

    video_comment_restore: bool = Field()
    """Property `LongPollEvents.video_comment_restore`."""

    video_new: bool = Field()
    """Property `LongPollEvents.video_new`."""

    message_reaction_event: bool = Field()
    """Property `LongPollEvents.message_reaction_event`."""

    wall_post_new: bool = Field()
    """Property `LongPollEvents.wall_post_new`."""

    wall_reply_delete: bool = Field()
    """Property `LongPollEvents.wall_reply_delete`."""

    wall_reply_edit: bool = Field()
    """Property `LongPollEvents.wall_reply_edit`."""

    wall_reply_new: bool = Field()
    """Property `LongPollEvents.wall_reply_new`."""

    wall_reply_restore: bool = Field()
    """Property `LongPollEvents.wall_reply_restore`."""

    wall_repost: bool = Field()
    """Property `LongPollEvents.wall_repost`."""

    wall_schedule_post_new: bool = Field()
    """Property `LongPollEvents.wall_schedule_post_new`."""

    wall_schedule_post_delete: bool = Field()
    """Property `LongPollEvents.wall_schedule_post_delete`."""

    donut_subscription_create: bool = Field()
    """Property `LongPollEvents.donut_subscription_create`."""

    donut_subscription_prolonged: bool = Field()
    """Property `LongPollEvents.donut_subscription_prolonged`."""

    donut_subscription_cancelled: bool = Field()
    """Property `LongPollEvents.donut_subscription_cancelled`."""

    donut_subscription_expired: bool = Field()
    """Property `LongPollEvents.donut_subscription_expired`."""

    donut_subscription_price_changed: bool = Field()
    """Property `LongPollEvents.donut_subscription_price_changed`."""

    donut_money_withdraw: bool = Field()
    """Property `LongPollEvents.donut_money_withdraw`."""

    donut_money_withdraw_error: bool = Field()
    """Property `LongPollEvents.donut_money_withdraw_error`."""

    lead_forms_new: bool | None = Field(
        default=None,
    )
    """Property `LongPollEvents.lead_forms_new`."""

    market_order_new: bool | None = Field(
        default=None,
    )
    """Property `LongPollEvents.market_order_new`."""

    market_order_edit: bool | None = Field(
        default=None,
    )
    """Property `LongPollEvents.market_order_edit`."""


class LongPollServer(BaseModel):
    """Model: `LongPollServer`"""

    key: str = Field()
    """Long Poll key."""

    server: str = Field()
    """Long Poll server address."""

    ts: str = Field()
    """Number of the last event."""


class LongPollSettings(BaseModel):
    """Model: `LongPollSettings`"""

    events: "LongPollEvents" = Field()
    """Property `LongPollSettings.events`."""

    is_enabled: bool = Field()
    """Shows whether Long Poll is enabled."""

    api_version: str | None = Field(
        default=None,
    )
    """API version used for the events."""


class MarketInfo(BaseModel):
    """Model: `MarketInfo`"""

    type: str | None = Field(
        default=None,
    )
    """Market type."""

    contact_id: int | None = Field(
        default=None,
    )
    """Contact person ID."""

    currency: "Currency | None" = Field(
        default=None,
    )
    """Property `MarketInfo.currency`."""

    currency_text: str | None = Field(
        default=None,
    )
    """Currency name."""

    enabled: bool | None = Field(
        default=None,
    )
    """Information whether the market is enabled."""

    main_album_id: int | None = Field(
        default=None,
    )
    """Main market album ID."""

    price_max: str | None = Field(
        default=None,
    )
    """Maximum price."""

    price_min: str | None = Field(
        default=None,
    )
    """Minimum price."""

    min_order_price: "Price | None" = Field(
        default=None,
    )
    """Property `MarketInfo.min_order_price`."""


class MarketProperties(BaseModel):
    """Model: `MarketProperties`"""

    market: "MarketInfo | None" = Field(
        default=None,
    )
    """Property `MarketProperties.market`."""

    has_market_app: bool | None = Field(
        default=None,
    )
    """Information whether community has installed market app."""

    using_vkpay_market_app: bool | None = Field(
        default=None,
    )
    """Property `MarketProperties.using_vkpay_market_app`."""


class MarketState(StrEnum, metaclass=BaseEnumMeta):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class MemberRole(BaseModel):
    """Model: `MemberRole`"""

    id: int = Field()
    """User ID."""

    is_call_operator: bool | None = Field(
        default=None,
    )
    """Allow the manager to accept community calls.."""

    permissions: list["MemberRolePermission"] | None = Field(
        default=None,
    )
    """Property `MemberRole.permissions`."""

    role: "MemberRoleStatus | None" = Field(
        default=None,
    )
    """Property `MemberRole.role`."""


class MemberRolePermission(StrEnum, metaclass=BaseEnumMeta):
    ADS = "ads"


class MemberRoleStatus(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


class MemberStatus(BaseModel):
    """Model: `MemberStatus`"""

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""


class MemberStatusFull(BaseModel):
    """Model: `MemberStatusFull`"""

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""

    can_invite: bool | None = Field(
        default=None,
    )
    """Information whether user can be invited."""

    can_recall: bool | None = Field(
        default=None,
    )
    """Information whether user\'s invite to the group can be recalled."""

    invitation: bool | None = Field(
        default=None,
    )
    """Information whether user has been invited to the group."""

    request: bool | None = Field(
        default=None,
    )
    """Information whether user has send request to the group."""


class OnlineStatus(BaseModel):
    """Online status of group
    Model: `OnlineStatus`
    """

    status: "OnlineStatusType" = Field()
    """Property `OnlineStatus.status`."""

    minutes: int | None = Field(
        default=None,
    )
    """Estimated time of answer (for status = answer_mark)."""


class OnlineStatusType(StrEnum, metaclass=BaseEnumMeta):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class OwnerXtrBanInfoType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"


class OwnerXtrBanInfo(BaseModel):
    """Model: `OwnerXtrBanInfo`"""

    ban_info: "BanInfo | None" = Field(
        default=None,
    )
    """Property `OwnerXtrBanInfo.ban_info`."""

    group: "Group | None" = Field(
        default=None,
    )
    """Information about group if type = group."""

    profile: "User | None" = Field(
        default=None,
    )
    """Information about group if type = profile."""

    type: "OwnerXtrBanInfoType | None" = Field(
        default=None,
    )
    """Property `OwnerXtrBanInfo.type`."""


class PhotoSize(BaseModel):
    """Model: `PhotoSize`"""

    height: int = Field()
    """Image height."""

    width: int = Field()
    """Image width."""


class ProfileItem(BaseModel):
    """Model: `ProfileItem`"""

    id: int = Field()
    """User id."""

    photo_50: str = Field()
    """Url for user photo."""

    photo_100: str = Field()
    """Url for user photo."""

    first_name: str = Field()
    """User first name."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain of the user page."""


class RoleOptions(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class SectionsListItem(BaseModel):
    """Model: `SectionsListItem`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class SettingsTwitterStatus(StrEnum, metaclass=BaseEnumMeta):
    LOADING = "loading"
    SYNC = "sync"


class SettingsTwitter(BaseModel):
    """Model: `SettingsTwitter`"""

    status: "SettingsTwitterStatus" = Field()
    """Property `SettingsTwitter.status`."""

    name: str | None = Field(
        default=None,
    )
    """Property `SettingsTwitter.name`."""


class SubjectItem(BaseModel):
    """Model: `SubjectItem`"""

    id: int = Field()
    """Subject ID."""

    name: str = Field()
    """Subject title."""


class TokenPermissionSetting(BaseModel):
    """Model: `TokenPermissionSetting`"""

    name: str = Field()
    """Property `TokenPermissionSetting.name`."""

    setting: int = Field()
    """Property `TokenPermissionSetting.setting`."""


class LeadFormsAnswer(BaseModel):
    """Model: `LeadFormsAnswer`"""

    key: str = Field()
    """Property `LeadFormsAnswer.key`."""

    answer: "AnswerOneOf" = Field()
    """Property `LeadFormsAnswer.answer`."""


class AnswerItem(BaseModel):
    """Model: `AnswerItem`"""

    value: str = Field()
    """Property `AnswerItem.value`."""

    key: str | None = Field(
        default=None,
    )
    """Property `AnswerItem.key`."""


class AnswerOneOf(BaseModel):
    """Model: `AnswerOneOf`"""


class Form(BaseModel):
    """Model: `Form`"""

    form_id: int = Field()
    """Property `Form.form_id`."""

    group_id: int = Field()
    """Property `Form.group_id`."""

    leads_count: int = Field()
    """Property `Form.leads_count`."""

    url: str = Field()
    """Property `Form.url`."""

    photo: str | None = Field(
        default=None,
    )
    """Property `Form.photo`."""

    name: str | None = Field(
        default=None,
    )
    """Property `Form.name`."""

    title: str | None = Field(
        default=None,
    )
    """Property `Form.title`."""

    description: str | None = Field(
        default=None,
    )
    """Property `Form.description`."""

    confirmation: str | None = Field(
        default=None,
    )
    """Property `Form.confirmation`."""

    site_link_url: str | None = Field(
        default=None,
    )
    """Property `Form.site_link_url`."""

    policy_link_url: str | None = Field(
        default=None,
    )
    """Property `Form.policy_link_url`."""

    questions: list["QuestionItem"] | None = Field(
        default=None,
    )
    """Property `Form.questions`."""

    active: bool | None = Field(
        default=None,
    )
    """Property `Form.active`."""

    pixel_code: str | None = Field(
        default=None,
    )
    """Property `Form.pixel_code`."""

    once_per_user: int | None = Field(
        default=None,
    )
    """Property `Form.once_per_user`."""

    notify_admins: str | None = Field(
        default=None,
    )
    """Property `Form.notify_admins`."""

    notify_emails: str | None = Field(
        default=None,
    )
    """Property `Form.notify_emails`."""


class Lead(BaseModel):
    """Model: `Lead`"""

    lead_id: int = Field()
    """Property `Lead.lead_id`."""

    user_id: int = Field()
    """Property `Lead.user_id`."""

    date: datetime.datetime = Field()
    """Property `Lead.date`."""

    answers: list["LeadFormsAnswer"] = Field()
    """Property `Lead.answers`."""

    ad_id: int | None = Field(
        default=None,
    )
    """Property `Lead.ad_id`."""


class QuestionItemType(StrEnum, metaclass=BaseEnumMeta):
    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class QuestionItem(BaseModel):
    """Model: `QuestionItem`"""

    key: str = Field()
    """Property `QuestionItem.key`."""

    type: "QuestionItemType" = Field()
    """Property `QuestionItem.type`."""

    label: str | None = Field(
        default=None,
    )
    """Property `QuestionItem.label`."""

    options: list["QuestionItemOption"] | None = Field(
        default=None,
    )
    """Опции выбора для типов radio, checkbox, select."""


class QuestionItemOption(BaseModel):
    """Model: `QuestionItemOption`"""

    label: str = Field()
    """Property `QuestionItemOption.label`."""

    key: str | None = Field(
        default=None,
    )
    """Property `QuestionItemOption.key`."""


class LikesType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"
    TEXTPOST = "textpost"
    COMMUNITY_REVIEW = "community_review"
    STORY = "story"
    GROUP_LIKE = "group_like"


class LinkTargetObject(BaseModel):
    """Model: `LinkTargetObject`"""

    type: str | None = Field(
        default=None,
    )
    """Object type."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner ID."""

    item_id: int | None = Field(
        default=None,
    )
    """Item ID."""


class Currency(BaseModel):
    """Model: `Currency`"""

    id: int = Field()
    """Currency ID."""

    name: str = Field()
    """Currency sign."""

    title: str = Field()
    """Currency title."""


class GlobalSearchFilters(BaseModel):
    """Model: `GlobalSearchFilters`"""

    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `GlobalSearchFilters.city`."""

    country: "BaseCountry | None" = Field(
        default=None,
    )
    """Property `GlobalSearchFilters.country`."""


class ItemOwnerInfo(BaseModel):
    """Information about the group where the item is placed
    Model: `ItemOwnerInfo`
    """

    avatar: list["BaseImage"] | None = Field(
        default=None,
    )
    """Avatar of the group."""

    name: str | None = Field(
        default=None,
    )
    """Name of the group."""

    category: str | None = Field(
        default=None,
    )
    """Category of the item or description of the group."""

    category_url: str | None = Field(
        default=None,
    )
    """Link to the section of the group."""

    is_corporated_market: bool | None = Field(
        default=None,
    )
    """Is the group is VK corporated market."""

    market_type: "OwnerType | None" = Field(
        default=None,
    )
    """Type of the market group."""


class ItemPromotionInfo(BaseModel):
    """Information about promotion of the market item
    Model: `ItemPromotionInfo`
    """

    is_available: bool | None = Field(
        default=None,
    )
    """Can the item be promoted?."""


class MarketAlbum(BaseModel):
    """Model: `MarketAlbum`"""
    id: 'int' = Field()
    """Market album ID."""
    owner_id: 'int' = Field()
    """Market album owner\'s ID."""
    title: 'str' = Field()
    """Market album title."""
    count: 'int' = Field()
    """Items number."""
    updated_time: 'int' = Field()
    """Date when album has been updated last time in Unixtime."""
    is_main: 'bool | None' = Field(
        default=None,
    )
    """Is album main for owner."""
    is_hidden: 'bool | None' = Field(
        default=None,
    )
    """Is album hidden."""
    type: 'int | None' = Field(
        default=None,
    )
    """Type of album."""
    is_blur_enabled: 'bool | None' = Field(
        default=None,
    )
    """Is album needed to be blurred (18+) or not."""
    photo: 'Photo | None' = None


class MarketCategoryInnerType(StrEnum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketMarketCategory(BaseModel):
    """Model: `MarketMarketCategory`"""

    inner_type: "MarketCategoryInnerType" = Field()
    """Property `MarketMarketCategory.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: bool | None = Field(
        default=None,
    )
    """Is v2 category."""

    parent: "MarketCategoryNested | None" = Field(
        default=None,
    )
    """Property `MarketMarketCategory.parent`."""


class MarketCategoryNestedInnerType(StrEnum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketCategoryNested(BaseModel):
    """Model: `MarketCategoryNested`"""

    inner_type: "MarketCategoryNestedInnerType" = Field()
    """Property `MarketCategoryNested.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: bool | None = Field(
        default=None,
    )
    """Is v2 category."""

    parent: "MarketCategoryNested | None" = Field(
        default=None,
    )
    """Property `MarketCategoryNested.parent`."""


class MarketCategoryTree(BaseModel):
    """Model: `MarketCategoryTree`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    icon_name: str | None = Field(
        default=None,
    )
    """Icon name."""

    children: list["MarketCategoryTree"] | None = Field(
        default=None,
    )
    """Property `MarketCategoryTree.children`."""

    view: "MarketCategoryTreeView | None" = Field(
        default=None,
    )
    """Property `MarketCategoryTree.view`."""

    url: str | None = Field(
        default=None,
    )
    """SEO-friendly URL to page with category\'s items."""

    seo_name: str | None = Field(
        default=None,
    )
    """SEO-friendly variant of category\'s name."""

    page_title: str | None = Field(
        default=None,
    )
    """Title for category\'s page. Used for SEO."""

    page_description: str | None = Field(
        default=None,
    )
    """Description for category\'s page. Used for SEO."""


class MarketCategoryTreeViewType(StrEnum, metaclass=BaseEnumMeta):
    TAB_ROOT = "tab_root"


class MarketCategoryTreeView(BaseModel):
    """Model: `MarketCategoryTreeView`"""

    type: "MarketCategoryTreeViewType | None" = Field(
        default=None,
    )
    """Property `MarketCategoryTreeView.type`."""

    selected: bool | None = Field(
        default=None,
    )
    """Property `MarketCategoryTreeView.selected`."""

    root_path: list[str] | None = Field(
        default=None,
    )
    """Property `MarketCategoryTreeView.root_path`."""


class MarketItem(BaseModel):
    """Model: `MarketItem`"""

    availability: "MarketItemAvailability" = Field()
    """Property `MarketItem.availability`."""

    category: "MarketMarketCategory" = Field()
    """Property `MarketItem.category`."""

    description: str = Field()
    """Item description."""

    id: int = Field()
    """Item ID."""

    owner_id: int = Field()
    """Item owner\'s ID."""

    price: "Price" = Field()
    """Property `MarketItem.price`."""

    title: str = Field()
    """Item title."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the market item."""

    button_title: str | None = Field(
        default=None,
    )
    """Title for button for url."""

    category_v2: "MarketMarketCategory | None" = Field(
        default=None,
    )
    """Property `MarketItem.category_v2`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the item has been created in Unixtime."""

    external_id: str | None = Field(
        default=None,
    )
    """Property `MarketItem.external_id`."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Property `MarketItem.is_favorite`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `MarketItem.is_owner`."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Property `MarketItem.is_adult`."""

    thumb_photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    url: str | None = Field(
        default=None,
    )
    """URL to item."""

    variants_grouping_id: int | None = Field(
        default=None,
    )
    """Property `MarketItem.variants_grouping_id`."""

    is_main_variant: bool | None = Field(
        default=None,
    )
    """Property `MarketItem.is_main_variant`."""

    sku: str | None = Field(
        default=None,
    )
    """Property `MarketItem.sku`."""

    stock_amount: int | None = Field(
        default=None,
    )
    """Inventory balances."""

    post_id: int | None = Field(
        default=None,
    )
    """Attach for post id."""

    post_owner_id: int | None = Field(
        default=None,
    )
    """Attach for post owner id."""


class MarketItemAvailability(IntEnum, metaclass=BaseEnumMeta):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketItemBasic(BaseModel):
    """Model: `MarketItemBasic`"""

    id: int = Field()
    """Item ID."""

    owner_id: int = Field()
    """Item owner\'s ID."""

    title: str = Field()
    """Item title."""

    price: "Price" = Field()
    """Property `MarketItemBasic.price`."""

    thumb_photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Property `MarketItemBasic.is_favorite`."""


class MarketOrder(BaseModel):
    """Model: `MarketOrder`"""

    id: int = Field()
    """Property `MarketOrder.id`."""

    group_id: int = Field()
    """Property `MarketOrder.group_id`."""

    user_id: int = Field()
    """Property `MarketOrder.user_id`."""

    date: datetime.datetime = Field()
    """Property `MarketOrder.date`."""

    status: int = Field()
    """Property `MarketOrder.status`."""

    items_count: int = Field()
    """Property `MarketOrder.items_count`."""

    total_price: "Price" = Field()
    """Property `MarketOrder.total_price`."""

    display_order_id: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.display_order_id`."""

    track_number: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.track_number`."""

    track_link: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.track_link`."""

    comment: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.comment`."""

    address: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.address`."""

    merchant_comment: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.merchant_comment`."""

    weight: int | None = Field(
        default=None,
    )
    """Property `MarketOrder.weight`."""

    discount: "Price | None" = Field(
        default=None,
    )
    """Property `MarketOrder.discount`."""

    preview_order_items: list["OrderItem"] | None = Field(
        default=None,
    )
    """Several order items for preview."""

    cancel_info: "Link | None" = Field(
        default=None,
    )
    """Information for cancel and revert order."""

    comment_for_user: str | None = Field(
        default=None,
    )
    """Seller comment for user."""

    is_viewed_by_admin: bool | None = Field(
        default=None,
    )
    """Property `MarketOrder.is_viewed_by_admin`."""

    date_viewed: int | None = Field(
        default=None,
    )
    """Property `MarketOrder.date_viewed`."""

    can_add_review: bool | None = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for at least one item in this order."""


class OrderItem(BaseModel):
    """Model: `OrderItem`"""
    owner_id: 'int' = Field()
    """Property `OrderItem.owner_id`."""
    item_id: 'int' = Field()
    """Property `OrderItem.item_id`."""
    price: "Price" = Field()
    """Property `OrderItem.price`."""
    quantity: 'int' = Field()
    """Property `OrderItem.quantity`."""
    item: "MarketItem" = Field()
    """Property `OrderItem.item`."""
    title: 'str | None' = Field(
        default=None,
    )
    """Property `OrderItem.title`."""
    variants: 'list[str] | None' = Field(
        default=None,
    )
    """Property `OrderItem.variants`."""
    can_add_review: 'bool | None' = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for this ordered item."""
    photo: 'Photo | None' = None


class OwnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE = "base"
    PRO = "pro"
    DISABLED = "disabled"


class Price(BaseModel):
    """Model: `Price`"""

    amount: str = Field()
    """Amount."""

    currency: "Currency" = Field()
    """Property `Price.currency`."""

    text: str = Field()
    """Text."""

    amount_to: str | None = Field(
        default=None,
    )
    """Amount to for price_type=2."""

    price_type: int | None = Field(
        default=None,
    )
    """Property `Price.price_type`."""

    price_unit: int | None = Field(
        default=None,
    )
    """Property `Price.price_unit`."""

    discount_rate: int | None = Field(
        default=None,
    )
    """Property `Price.discount_rate`."""

    old_amount: str | None = Field(
        default=None,
    )
    """Property `Price.old_amount`."""

    old_amount_text: str | None = Field(
        default=None,
    )
    """Textual representation of old price."""


class PropertyType(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    COLOR = "color"


class Property(BaseModel):
    """Model: `Property`"""

    id: int = Field()
    """Property `Property.id`."""

    title: str = Field()
    """Property name."""

    variants: list["PropertyVariant"] = Field()
    """Property `Property.variants`."""

    type: "PropertyType | None" = Field(
        default=None,
    )
    """Property type."""


class PropertyVariant(BaseModel):
    """Model: `PropertyVariant`"""

    id: int = Field()
    """Property `PropertyVariant.id`."""

    title: str = Field()
    """Property name."""

    value: str | None = Field(
        default=None,
    )
    """Property value corresponding to property type."""


class ServicesViewType(IntEnum, metaclass=BaseEnumMeta):
    CARDS = 1
    ROWS = 2


class UploadPhotoData(BaseModel):
    """Model: `UploadPhotoData`"""

    photo_id: int = Field()
    """Photo ID."""

    photo: "Photo | None" = Field(
        default=None,
    )
    """Property `UploadPhotoData.photo`."""


class Note(BaseModel):
    """Model: `Note`"""

    comments: int = Field()
    """Comments number."""

    date: datetime.datetime = Field()
    """Date when the note has been created in Unixtime."""

    id: int = Field()
    """Note ID."""

    owner_id: int = Field()
    """Note owner\'s ID."""

    title: str = Field()
    """Note title."""

    view_url: str = Field()
    """URL of the page with note preview."""

    read_comments: int | None = Field(
        default=None,
    )
    """Property `Note.read_comments`."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the note."""

    text: str | None = Field(
        default=None,
    )
    """Note text."""

    text_wiki: str | None = Field(
        default=None,
    )
    """Note text in wiki format."""

    privacy_view: list[str] | None = Field(
        default=None,
    )
    """Property `Note.privacy_view`."""

    privacy_comment: list[str] | None = Field(
        default=None,
    )
    """Property `Note.privacy_comment`."""


class NoteComment(BaseModel):
    """Model: `NoteComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has beed added in Unixtime."""

    id: int = Field()
    """Comment ID."""

    message: str = Field()
    """Comment text."""

    nid: int = Field()
    """Note ID."""

    oid: int = Field()
    """Note ID."""

    uid: int = Field()
    """Comment author\'s ID."""

    reply_to: int | None = Field(
        default=None,
    )
    """ID of replied comment ."""


class Feedback(BaseModel):
    """Model: `Feedback`"""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `Feedback.attachments`."""

    from_id: int | None = Field(
        default=None,
    )
    """Reply author\'s ID."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `Feedback.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Item ID."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `Feedback.likes`."""

    text: str | None = Field(
        default=None,
    )
    """Reply text."""

    to_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""


class NotificationInnerType(StrEnum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class Notification(BaseModel):
    """Model: `Notification`"""

    inner_type: "NotificationInnerType" = Field()
    """Property `Notification.inner_type`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: "Feedback | None" = Field(
        default=None,
    )
    """Property `Notification.feedback`."""

    parent: "Notification | None" = Field(
        default=None,
    )
    """Property `Notification.parent`."""

    reply: "Reply | None" = Field(
        default=None,
    )
    """Property `Notification.reply`."""

    type: str | None = Field(
        default=None,
    )
    """Notification type."""


class NotificationItemInnerType(StrEnum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class NotificationItem(BaseModel):
    """Model: `NotificationItem`"""

    inner_type: "NotificationItemInnerType" = Field()
    """Property `NotificationItem.inner_type`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: "Feedback | None" = Field(
        default=None,
    )
    """Property `NotificationItem.feedback`."""

    parent: "Notification | None" = Field(
        default=None,
    )
    """Property `NotificationItem.parent`."""

    reply: "Reply | None" = Field(
        default=None,
    )
    """Property `NotificationItem.reply`."""

    type: str | None = Field(
        default=None,
    )
    """Notification type."""


class Reply(BaseModel):
    """Model: `Reply`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the reply has been created in Unixtime."""

    id: int | None = Field(
        default=None,
    )
    """Reply ID."""

    text: int | None = Field(
        default=None,
    )
    """Reply text."""


class SendMessageError(BaseModel):
    """Model: `SendMessageError`"""

    code: int | None = Field(
        default=None,
    )
    """Error code."""

    description: str | None = Field(
        default=None,
    )
    """Error description."""


class SendMessageItem(BaseModel):
    """Model: `SendMessageItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""

    status: bool | None = Field(
        default=None,
    )
    """Notification status."""

    error: "SendMessageError | None" = Field(
        default=None,
    )
    """Property `SendMessageItem.error`."""


class OauthError(BaseModel):
    """Model: `OauthError`"""

    error: str = Field()
    """Error type."""

    error_description: str = Field()
    """Error description."""

    redirect_uri: str | None = Field(
        default=None,
    )
    """URI for validation."""


class Amount(BaseModel):
    """Model: `Amount`"""

    amounts: list["AmountItem"] | None = Field(
        default=None,
    )
    """Property `Amount.amounts`."""

    currency: str | None = Field(
        default=None,
    )
    """Currency name."""


class AmountItem(BaseModel):
    """Model: `AmountItem`"""

    amount: float | None = Field(
        default=None,
    )
    """Votes amount in user\'s currency."""

    description: str | None = Field(
        default=None,
    )
    """Amount description."""

    votes: str | None = Field(
        default=None,
    )
    """Votes number."""


class OrderStatus(StrEnum, metaclass=BaseEnumMeta):
    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    """Model: `OrdersOrder`"""

    amount: str = Field()
    """Amount."""

    app_order_id: str = Field()
    """App order ID."""

    date: str = Field()
    """Date of creation in Unixtime."""

    id: str = Field()
    """Order ID."""

    item: str = Field()
    """Order item."""

    receiver_id: str = Field()
    """Receiver ID."""

    status: "OrderStatus" = Field()
    """Order status."""

    user_id: str = Field()
    """User ID."""

    cancel_transaction_id: str | None = Field(
        default=None,
    )
    """Cancel transaction ID."""

    transaction_id: str | None = Field(
        default=None,
    )
    """Transaction ID."""


class Subscription(BaseModel):
    """Model: `Subscription`"""

    create_time: int = Field()
    """Date of creation in Unixtime."""

    id: int = Field()
    """Subscription ID."""

    item_id: str = Field()
    """Subscription order item."""

    period: int = Field()
    """Subscription period."""

    period_start_time: int = Field()
    """Date of last period start in Unixtime."""

    price: int = Field()
    """Subscription price."""

    status: str = Field()
    """Subscription status."""

    update_time: int = Field()
    """Date of last change in Unixtime."""

    cancel_reason: str | None = Field(
        default=None,
    )
    """Cancel reason."""

    next_bill_time: int | None = Field(
        default=None,
    )
    """Date of next bill in Unixtime."""

    expire_time: int | None = Field(
        default=None,
    )
    """Subscription expiration time in Unixtime."""

    pending_cancel: bool | None = Field(
        default=None,
    )
    """Pending cancel state."""

    title: str | None = Field(
        default=None,
    )
    """Subscription name."""

    app_id: int | None = Field(
        default=None,
    )
    """Subscription\'s application id."""

    application_name: str | None = Field(
        default=None,
    )
    """Subscription\'s application name."""

    photo_url: str | None = Field(
        default=None,
    )
    """Item photo image url."""

    test_mode: bool | None = Field(
        default=None,
    )
    """Is test subscription."""

    trial_expire_time: int | None = Field(
        default=None,
    )
    """Date of trial expire in Unixtime."""

    is_game: bool | None = Field(
        default=None,
    )
    """Is game (not miniapp) subscription."""


class OwnerState(BaseModel):
    """Model: `OwnerState`"""

    state: int | None = Field(
        default=None,
    )
    """Property `OwnerState.state`."""

    description: str | None = Field(
        default=None,
    )
    """wiki text to describe user state."""


class PrivacySettings(IntEnum, metaclass=BaseEnumMeta):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class Wikipage(BaseModel):
    """Model: `Wikipage`"""

    group_id: int = Field()
    """Community ID."""

    id: int = Field()
    """Page ID."""

    title: str = Field()
    """Page title."""

    views: int = Field()
    """Views number."""

    who_can_edit: "PrivacySettings" = Field()
    """Edit settings of the page."""

    who_can_view: "PrivacySettings" = Field()
    """View settings of the page."""

    created: int = Field()
    """Property `Wikipage.created`."""

    edited: int = Field()
    """Property `Wikipage.edited`."""

    creator_id: int | None = Field(
        default=None,
    )
    """Page creator ID."""

    creator_name: str | None = Field(
        default=None,
    )
    """Page creator name."""

    editor_id: int | None = Field(
        default=None,
    )
    """Last editor ID."""

    editor_name: str | None = Field(
        default=None,
    )
    """Last editor name."""


class WikipageFull(BaseModel):
    """Model: `WikipageFull`"""

    created: int = Field()
    """Date when the page has been created in Unixtime."""

    edited: int = Field()
    """Date when the page has been edited in Unixtime."""

    group_id: int = Field()
    """Community ID."""

    id: int = Field()
    """Page ID."""

    title: str = Field()
    """Page title."""

    view_url: str = Field()
    """URL of the page preview."""

    views: int = Field()
    """Views number."""

    who_can_edit: "PrivacySettings" = Field()
    """Edit settings of the page."""

    who_can_view: "PrivacySettings" = Field()
    """View settings of the page."""

    creator_id: int | None = Field(
        default=None,
    )
    """Page creator ID."""

    current_user_can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the page."""

    current_user_can_edit_access: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the page access settings."""

    editor_id: int | None = Field(
        default=None,
    )
    """Last editor ID."""

    html: str | None = Field(
        default=None,
    )
    """Page content, HTML."""

    source: str | None = Field(
        default=None,
    )
    """Page content, wiki."""

    url: str | None = Field(
        default=None,
    )
    """URL."""

    parent: str | None = Field(
        default=None,
    )
    """Parent."""

    parent2: str | None = Field(
        default=None,
    )
    """Parent2."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner ID."""


class WikipageHistory(BaseModel):
    """Model: `WikipageHistory`"""

    id: int = Field()
    """Version ID."""

    length: int = Field()
    """Page size in bytes."""

    date: datetime.datetime = Field()
    """Date when the page has been edited in Unixtime."""

    editor_id: int = Field()
    """Last editor ID."""

    editor_name: str = Field()
    """Last editor name."""


class Image(BaseModel):
    """Model: `Image`"""

    height: int | None = Field(
        default=None,
    )
    """Height of the photo in px.."""

    type: "ImageType | None" = Field(
        default=None,
    )
    """Property `Image.type`."""

    url: str | None = Field(
        default=None,
    )
    """Photo URL.."""

    width: int | None = Field(
        default=None,
    )
    """Width of the photo in px.."""


class ImageType(StrEnum, metaclass=BaseEnumMeta):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"
    BASE = "base"


class PhotoVerticalAlign(StrEnum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class Photo(BaseModel):
    """Model: `Photo`"""
    album_id: 'int' = Field()
    """Album ID."""
    date: 'datetime.datetime' = Field()
    """Date when uploaded."""
    id: 'int' = Field()
    """Photo ID."""
    owner_id: 'int' = Field()
    """Photo owner\'s ID."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Access key for the photo."""
    height: 'int | None' = Field(
        default=None,
    )
    """Original photo height."""
    images: 'list["Image"] | None' = Field(
        default=None,
    )
    """Property `Photo.images`."""
    lat: 'float | None' = Field(
        default=None,
    )
    """Latitude."""
    long: 'float | None' = Field(
        default=None,
    )
    """Longitude."""
    photo_256: 'str | None' = Field(
        default=None,
    )
    """URL of image with 2560 px width."""
    thumb_hash: 'str | None' = Field(
        default=None,
    )
    """Thumb Hash."""
    can_comment: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""
    place: 'str | None' = Field(
        default=None,
    )
    """Property `Photo.place`."""
    post_id: 'int | None' = Field(
        default=None,
    )
    """Post ID."""
    sizes: 'list["PhotoSizes"] | None' = Field(
        default=None,
    )
    """Property `Photo.sizes`."""
    square_crop: 'str | None' = Field(
        default=None,
    )
    """Property `Photo.square_crop`."""
    text: 'str | None' = Field(
        default=None,
    )
    """Photo caption."""
    user_id: 'int | None' = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""
    width: 'int | None' = Field(
        default=None,
    )
    """Original photo width."""
    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `Photo.likes`."""
    comments: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `Photo.comments`."""
    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `Photo.reposts`."""
    tags: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `Photo.tags`."""
    hidden: "PropertyExists | None" = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""
    real_offset: 'int | None' = Field(
        default=None,
    )
    """Real position of the photo."""
    vertical_align: "PhotoVerticalAlign | None" = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""
    has_tags: 'bool | None' = None
    orig_photo: 'PhotoSizes | None' = None

    @property
    def as_att(self) -> str:
        """Строка-вложение VK: ``photo{owner_id}_{id}[_{access_key}]``."""
        return attachment_string("photo", self.owner_id, self.id, self.access_key)


class PhotoAlbum(BaseModel):
    """Model: `PhotoAlbum`"""
    created: 'int' = Field()
    """Date when the album has been created in Unixtime."""
    id: 'int' = Field()
    """Photo album ID."""
    owner_id: 'int' = Field()
    """Album owner\'s ID."""
    size: 'int' = Field()
    """Photos number."""
    title: 'str' = Field()
    """Photo album title."""
    updated: 'int' = Field()
    """Date when the album has been updated last time in Unixtime."""
    description: 'str | None' = Field(
        default=None,
    )
    """Photo album description."""
    thumb: 'Photo | None' = None


class PhotoAlbumFull(BaseModel):
    """Model: `PhotoAlbumFull`"""
    id: 'int' = Field()
    """Photo album ID."""
    owner_id: 'int' = Field()
    """Album owner\'s ID."""
    size: 'int' = Field()
    """Photos number."""
    title: 'str' = Field()
    """Photo album title."""
    can_upload: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can upload photo to the album."""
    comments_disabled: 'bool | None' = Field(
        default=None,
    )
    """Information whether album comments are disabled."""
    description: 'str | None' = Field(
        default=None,
    )
    """Photo album description."""
    can_delete: 'bool | None' = Field(
        default=None,
    )
    """album can delete."""
    can_include_to_feed: 'bool | None' = Field(
        default=None,
    )
    """album can be selected to feed."""
    is_locked: 'bool | None' = Field(
        default=None,
    )
    """Need show privacy lock at album."""
    sizes: 'list["PhotoSizes"] | None' = Field(
        default=None,
    )
    """Property `PhotoAlbumFull.sizes`."""
    thumb_id: 'int | None' = Field(
        default=None,
    )
    """Thumb photo ID."""
    thumb_is_last: 'bool | None' = Field(
        default=None,
    )
    """Information whether the album thumb is last photo."""
    thumb_src: 'str | None' = Field(
        default=None,
    )
    """URL of the thumb image."""
    upload_by_admins_only: 'bool | None' = Field(
        default=None,
    )
    """Information whether only community administrators can upload photos."""
    created: 'int | None' = None
    updated: 'int | None' = None


class PhotoSizes(BaseModel):
    """Model: `PhotoSizes`"""

    height: int = Field()
    """Height in px."""

    type: "PhotoSizesType" = Field()
    """Property `PhotoSizes.type`."""

    width: int = Field()
    """Width in px."""

    url: str | None = Field(
        default=None,
    )
    """URL of the image."""

    src: str | None = Field(
        default=None,
    )
    """URL of the image."""


class PhotoSizesType(StrEnum, metaclass=BaseEnumMeta):
    T = "t"
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"
    BASE = "base"
    U = "u"
    V = "v"
    ORIG = "orig"


class PhotoTag(BaseModel):
    """Model: `PhotoTag`"""

    date: datetime.datetime = Field()
    """Date when tag has been added in Unixtime."""

    id: int = Field()
    """Tag ID."""

    placer_id: int = Field()
    """ID of the tag creator."""

    tagged_name: str = Field()
    """Tag description."""

    user_id: int = Field()
    """Tagged user ID."""

    viewed: bool = Field()
    """Information whether the tag is reviewed."""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""

    description: str | None = Field(
        default=None,
    )
    """Tagged description.."""


class PhotoUpload(BaseModel):
    """Model: `PhotoUpload`"""

    album_id: int = Field()
    """Album ID."""

    upload_url: str = Field()
    """URL to upload photo."""

    user_id: int = Field()
    """User ID."""

    fallback_upload_url: str | None = Field(
        default=None,
    )
    """Fallback URL if upload_url returned error."""

    group_id: int | None = Field(
        default=None,
    )
    """Group ID."""


class PhotoXtrTagInfo(BaseModel):
    """Model: `PhotoXtrTagInfo`"""

    album_id: int = Field()
    """Album ID."""

    date: datetime.datetime = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the photo."""

    height: int | None = Field(
        default=None,
    )
    """Original photo height."""

    lat: float | None = Field(
        default=None,
    )
    """Latitude."""

    long: float | None = Field(
        default=None,
    )
    """Longitude."""

    photo_1280: str | None = Field(
        default=None,
    )
    """URL of image with 1280 px width."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of image with 130 px width."""

    photo_2560: str | None = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of image with 604 px width."""

    photo_75: str | None = Field(
        default=None,
    )
    """URL of image with 75 px width."""

    photo_807: str | None = Field(
        default=None,
    )
    """URL of image with 807 px width."""

    placer_id: int | None = Field(
        default=None,
    )
    """ID of the tag creator."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""

    sizes: list["PhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PhotoXtrTagInfo.sizes`."""

    tag_created: int | None = Field(
        default=None,
    )
    """Date when tag has been added in Unixtime."""

    tag_id: int | None = Field(
        default=None,
    )
    """Tag ID."""

    text: str | None = Field(
        default=None,
    )
    """Photo caption."""

    user_id: int | None = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: int | None = Field(
        default=None,
    )
    """Original photo width."""

    has_tags: bool | None = Field(
        default=None,
    )
    """Whether photo has attached tag links."""


class TagsSuggestionItem(BaseModel):
    """Model: `TagsSuggestionItem`"""

    title: str | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.title`."""

    caption: str | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.caption`."""

    type: str | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.type`."""

    buttons: list["TagsSuggestionItemButton"] | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.buttons`."""

    photo: "Photo | None" = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.photo`."""

    tags: list["PhotoTag"] | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.tags`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItem.track_code`."""


class TagsSuggestionItemButtonAction(StrEnum, metaclass=BaseEnumMeta):
    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class TagsSuggestionItemButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class TagsSuggestionItemButton(BaseModel):
    """Model: `TagsSuggestionItemButton`"""

    title: str | None = Field(
        default=None,
    )
    """Property `TagsSuggestionItemButton.title`."""

    action: "TagsSuggestionItemButtonAction | None" = Field(
        default=None,
    )
    """Property `TagsSuggestionItemButton.action`."""

    style: "TagsSuggestionItemButtonStyle | None" = Field(
        default=None,
    )
    """Property `TagsSuggestionItemButton.style`."""


class PodcastCover(BaseModel):
    """Model: `PodcastCover`"""

    sizes: list["PhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PodcastCover.sizes`."""


class PodcastExternalData(BaseModel):
    """Model: `PodcastExternalData`"""

    url: str | None = Field(
        default=None,
    )
    """Url of the podcast page."""

    owner_url: str | None = Field(
        default=None,
    )
    """Url of the podcasts owner community."""

    title: str | None = Field(
        default=None,
    )
    """Podcast title."""

    owner_name: str | None = Field(
        default=None,
    )
    """Name of the podcasts owner community."""

    cover: "PodcastCover | None" = Field(
        default=None,
    )
    """Podcast cover."""


class Answer(BaseModel):
    """Model: `Answer`"""

    id: int = Field()
    """Answer ID."""

    rate: float = Field()
    """Answer rate in percents."""

    text: str = Field()
    """Answer text."""

    votes: int = Field()
    """Votes number."""


class BackgroundType(StrEnum, metaclass=BaseEnumMeta):
    GRADIENT = "gradient"
    TILE = "tile"
    COLOR = "color"


class Background(BaseModel):
    """Model: `Background`"""

    angle: int | None = Field(
        default=None,
    )
    """Gradient angle with 0 on positive X axis."""

    color: str | None = Field(
        default=None,
    )
    """Hex color code without #."""

    height: int | None = Field(
        default=None,
    )
    """Original height of pattern tile."""

    id: int | None = Field(
        default=None,
    )
    """Property `Background.id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `Background.name`."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Pattern tiles."""

    points: list["GradientPoint"] | None = Field(
        default=None,
    )
    """Gradient points."""

    type: "BackgroundType | None" = Field(
        default=None,
    )
    """Property `Background.type`."""

    width: int | None = Field(
        default=None,
    )
    """Original with of pattern tile."""


class FieldsVoters(BaseModel):
    """Model: `FieldsVoters`"""

    answer_id: int | None = Field(
        default=None,
    )
    """Answer ID."""

    users: "VotersFieldsUsers | None" = Field(
        default=None,
    )
    """Property `FieldsVoters.users`."""

    answer_offset: str | None = Field(
        default=None,
    )
    """Answer offset."""


class Friend(BaseModel):
    """Model: `Friend`"""

    id: int = Field()
    """Property `Friend.id`."""


class Poll(BaseModel):
    """Model: `Poll`"""
    multiple: 'bool' = Field()
    """Information whether the poll with multiple choices."""
    end_date: 'datetime.datetime' = Field()
    """Property `Poll.end_date`."""
    closed: 'bool' = Field()
    """Property `Poll.closed`."""
    is_board: 'bool' = Field()
    """Property `Poll.is_board`."""
    can_edit: 'bool' = Field()
    """Property `Poll.can_edit`."""
    can_vote: 'bool' = Field()
    """Property `Poll.can_vote`."""
    can_report: 'bool' = Field()
    """Property `Poll.can_report`."""
    can_share: 'bool' = Field()
    """Property `Poll.can_share`."""
    answers: 'list["Answer"]' = Field()
    """Property `Poll.answers`."""
    created: 'int' = Field()
    """Date when poll has been created in Unixtime."""
    id: 'int' = Field()
    """Poll ID."""
    owner_id: 'int' = Field()
    """Poll owner\'s ID."""
    question: 'str' = Field()
    """Poll question."""
    votes: 'int' = Field()
    """Votes number."""
    disable_unvote: 'bool' = Field()
    """Property `Poll.disable_unvote`."""
    friends: 'list["Friend"] | None' = Field(
        default=None,
    )
    """Property `Poll.friends`."""
    answer_id: 'int | None' = Field(
        default=None,
    )
    """Current user\'s answer ID."""
    answer_ids: 'list[int] | None' = Field(
        default=None,
    )
    """Current user\'s answer IDs."""
    embed_hash: 'str | None' = Field(
        default=None,
    )
    """Property `Poll.embed_hash`."""
    photo: "Background | None" = Field(
        default=None,
    )
    """Property `Poll.photo`."""
    author_id: 'int | None' = Field(
        default=None,
    )
    """Poll author\'s ID."""
    background: "Background | None" = Field(
        default=None,
    )
    """Property `Poll.background`."""
    anonymous: 'bool | None' = None


type PollsPollAnonymous = bool


class Voters(BaseModel):
    """Model: `Voters`"""

    answer_id: int | None = Field(
        default=None,
    )
    """Answer ID."""

    users: "VotersUsers | None" = Field(
        default=None,
    )
    """Property `Voters.users`."""

    answer_offset: str | None = Field(
        default=None,
    )
    """Answer offset."""


class VotersFieldsUsers(BaseModel):
    """Model: `VotersFieldsUsers`"""

    count: int | None = Field(
        default=None,
    )
    """Votes number."""

    items: list["UserFull"] | None = Field(
        default=None,
    )
    """Property `VotersFieldsUsers.items`."""


class VotersUsers(BaseModel):
    """Model: `VotersUsers`"""

    count: int | None = Field(
        default=None,
    )
    """Votes number."""

    items: list[int] | None = Field(
        default=None,
    )
    """Property `VotersUsers.items`."""


class ButtonOneOf(BaseModel):
    """Model: `ButtonOneOf`"""


class PrettyCardInnerType(StrEnum, metaclass=BaseEnumMeta):
    PRETTYCARDS_PRETTYCARD = "prettyCards_prettyCard"


class PrettyCard(BaseModel):
    """Model: `PrettyCard`"""

    inner_type: "PrettyCardInnerType" = Field()
    """Property `PrettyCard.inner_type`."""

    card_id: str = Field()
    """Card ID (long int returned as string)."""

    link_url: str = Field()
    """Link URL."""

    photo: str = Field()
    """Photo ID (format \"<owner_id>_<media_id>\")."""

    title: str = Field()
    """Title."""

    button: "ButtonOneOf | None" = Field(
        default=None,
    )
    """Button key."""

    button_text: str | None = Field(
        default=None,
    )
    """Button text in current language."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `PrettyCard.images`."""

    price: str | None = Field(
        default=None,
    )
    """Price if set (decimal number returned as string)."""

    price_old: str | None = Field(
        default=None,
    )
    """Old price if set (decimal number returned as string)."""


class PrettyCardOrError(BaseModel):
    """Model: `PrettyCardOrError`"""


class Hint(BaseModel):
    """Model: `Hint`"""

    description: str = Field()
    """Object description."""

    type: "HintType" = Field()
    """Property `Hint.type`."""

    app: "App | None" = Field(
        default=None,
    )
    """Property `Hint.app`."""

    global_: bool | None = Field(
        default=None,
        alias="global",
    )
    """Information whether the object has been found globally."""

    group: "Group | None" = Field(
        default=None,
    )
    """Property `Hint.group`."""

    profile: "UserMin | None" = Field(
        default=None,
    )
    """Property `Hint.profile`."""

    section: "HintSection | None" = Field(
        default=None,
    )
    """Property `Hint.section`."""

    link: "Link | None" = Field(
        default=None,
    )
    """Property `Hint.link`."""


class HintSection(StrEnum, metaclass=BaseEnumMeta):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class HintType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"


class GiveEventStickerItem(BaseModel):
    """Model: `GiveEventStickerItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `GiveEventStickerItem.user_id`."""

    status: str | None = Field(
        default=None,
    )
    """Property `GiveEventStickerItem.status`."""


class Level(BaseModel):
    """Model: `Level`"""

    level: int | None = Field(
        default=None,
    )
    """Level."""

    uid: int | None = Field(
        default=None,
    )
    """User ID."""


class SetCounterItem(BaseModel):
    """Model: `SetCounterItem`"""

    id: int = Field()
    """User ID."""

    result: bool = Field()
    """Property `SetCounterItem.result`."""


class SmsNotification(BaseModel):
    """Model: `SmsNotification`"""

    app_id: str | None = Field(
        default=None,
    )
    """Application ID."""

    date: str | None = Field(
        default=None,
    )
    """Date when message has been sent in Unixtime."""

    id: str | None = Field(
        default=None,
    )
    """Notification ID."""

    message: str | None = Field(
        default=None,
    )
    """Messsage text."""

    user_id: str | None = Field(
        default=None,
    )
    """User ID."""


class TokenChecked(BaseModel):
    """Model: `TokenChecked`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when access_token has been generated in Unixtime."""

    expire: int | None = Field(
        default=None,
    )
    """Date when access_token will expire in Unixtime."""

    success: int | None = Field(
        default=None,
    )
    """Returns if successfully processed."""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""


class Transaction(BaseModel):
    """Model: `Transaction`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Transaction date in Unixtime."""

    id: int | None = Field(
        default=None,
    )
    """Transaction ID."""

    uid_from: int | None = Field(
        default=None,
    )
    """From ID."""

    uid_to: int | None = Field(
        default=None,
    )
    """To ID."""

    votes: int | None = Field(
        default=None,
    )
    """Votes number."""


class Activity(BaseModel):
    """Activity stats
    Model: `Activity`
    """

    comments: int | None = Field(
        default=None,
    )
    """Comments number."""

    copies: int | None = Field(
        default=None,
    )
    """Reposts number."""

    hidden: int | None = Field(
        default=None,
    )
    """Hidden from news count."""

    likes: int | None = Field(
        default=None,
    )
    """Likes number."""

    subscribed: int | None = Field(
        default=None,
    )
    """New subscribers count."""

    unsubscribed: int | None = Field(
        default=None,
    )
    """Unsubscribed count."""


class StatsCity(BaseModel):
    """Model: `StatsCity`"""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    name: str | None = Field(
        default=None,
    )
    """City name."""

    value: int | None = Field(
        default=None,
    )
    """City ID."""


class Country(BaseModel):
    """Model: `Country`"""

    code: str | None = Field(
        default=None,
    )
    """Country code."""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    name: str | None = Field(
        default=None,
    )
    """Country name."""

    value: int | None = Field(
        default=None,
    )
    """Country ID."""


class Period(BaseModel):
    """Model: `Period`"""

    activity: "Activity | None" = Field(
        default=None,
    )
    """Property `Period.activity`."""

    period_from: "StatsPeriodFromOneOf | None" = Field(
        default=None,
    )
    """Property `Period.period_from`."""

    period_to: "StatsPeriodToOneOf | None" = Field(
        default=None,
    )
    """Property `Period.period_to`."""

    reach: "Reach | None" = Field(
        default=None,
    )
    """Property `Period.reach`."""

    visitors: "StatsViews | None" = Field(
        default=None,
    )
    """Property `Period.visitors`."""


type StatsPeriodFromOneOf = datetime.datetime

type StatsPeriodToOneOf = datetime.datetime


class Reach(BaseModel):
    """Reach stats
    Model: `Reach`
    """

    age: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `Reach.age`."""

    cities: list["StatsCity"] | None = Field(
        default=None,
    )
    """Property `Reach.cities`."""

    countries: list["Country"] | None = Field(
        default=None,
    )
    """Property `Reach.countries`."""

    mobile_reach: int | None = Field(
        default=None,
    )
    """Reach count from mobile devices."""

    reach: int | None = Field(
        default=None,
    )
    """Reach count."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Subscribers reach count."""

    sex: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `Reach.sex`."""

    sex_age: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `Reach.sex_age`."""


class SexAge(BaseModel):
    """Model: `SexAge`"""

    value: str = Field()
    """Sex/age value."""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    reach: int | None = Field(
        default=None,
    )
    """Property `SexAge.reach`."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Property `SexAge.reach_subscribers`."""

    count_subscribers: int | None = Field(
        default=None,
    )
    """Property `SexAge.count_subscribers`."""


class StatsViews(BaseModel):
    """Views stats
    Model: `StatsViews`
    """

    age: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.age`."""

    cities: list["StatsCity"] | None = Field(
        default=None,
    )
    """Property `StatsViews.cities`."""

    countries: list["Country"] | None = Field(
        default=None,
    )
    """Property `StatsViews.countries`."""

    mobile_views: int | None = Field(
        default=None,
    )
    """Number of views from mobile devices."""

    sex: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.sex`."""

    sex_age: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.sex_age`."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""

    visitors: int | None = Field(
        default=None,
    )
    """Visitors number."""


class WallpostStat(BaseModel):
    """Model: `WallpostStat`"""

    post_id: int | None = Field(
        default=None,
    )
    """Property `WallpostStat.post_id`."""

    hide: int | None = Field(
        default=None,
    )
    """Hidings number."""

    join_group: int | None = Field(
        default=None,
    )
    """People have joined the group."""

    links: int | None = Field(
        default=None,
    )
    """Link clickthrough."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Subscribers reach."""

    reach_subscribers_count: int | None = Field(
        default=None,
    )
    """Property `WallpostStat.reach_subscribers_count`."""

    reach_total: int | None = Field(
        default=None,
    )
    """Total reach."""

    reach_total_count: int | None = Field(
        default=None,
    )
    """Property `WallpostStat.reach_total_count`."""

    reach_viral: int | None = Field(
        default=None,
    )
    """Property `WallpostStat.reach_viral`."""

    reach_ads: int | None = Field(
        default=None,
    )
    """Property `WallpostStat.reach_ads`."""

    report: int | None = Field(
        default=None,
    )
    """Reports number."""

    to_group: int | None = Field(
        default=None,
    )
    """Clickthrough to community."""

    unsubscribe: int | None = Field(
        default=None,
    )
    """Unsubscribed members."""

    sex_age: list["SexAge"] | None = Field(
        default=None,
    )
    """Property `WallpostStat.sex_age`."""


class Status(BaseModel):
    """Model: `Status`"""

    text: str = Field()
    """Status text."""

    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `Status.audio`."""


class StickersImageSet(BaseModel):
    """Model: `StickersImageSet`"""

    base_url: str = Field()
    """Base URL for images in set."""

    version: int | None = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `StickersImageSet.images`."""


class Value(BaseModel):
    """Model: `Value`"""

    key: str = Field()
    """Property `Value.key`."""

    value: str = Field()
    """Property `Value.value`."""


class ProductType(StrEnum, metaclass=BaseEnumMeta):
    STICKERS = "stickers"


class Product(BaseModel):
    """Model: `Product`"""

    id: int = Field()
    """Id of the product."""

    type: "ProductType" = Field()
    """Product type."""

    is_new: bool | None = Field(
        default=None,
    )
    """Information whether sticker product wasn\'t used after being purchased."""

    copyright: str | None = Field(
        default=None,
    )
    """Product copyright information."""

    base_id: int | None = Field(
        default=None,
    )
    """Id of the base pack (for sticker pack styles)."""

    style_ids: list[int] | None = Field(
        default=None,
    )
    """Array of style ids available for the sticker pack."""

    purchased: bool | None = Field(
        default=None,
    )
    """Information whether the product is purchased (1 - yes, 0 - no)."""

    active: bool | None = Field(
        default=None,
    )
    """Information whether the product is active (1 - yes, 0 - no)."""

    promoted: bool | None = Field(
        default=None,
    )
    """Information whether the product is promoted (1 - yes, 0 - no)."""

    purchase_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date (Unix time) when the product was purchased."""

    title: str | None = Field(
        default=None,
    )
    """Title of the product."""

    stickers: list["StickerNew"] | None = Field(
        default=None,
    )
    """Property `Product.stickers`."""

    style_sticker_ids: list[int] | None = Field(
        default=None,
    )
    """Array of style sticker ids (for sticker pack styles)."""

    icon: "ProductIcon | None" = Field(
        default=None,
    )
    """Array of icon images or icon set object of the product (for stickers product type)."""

    previews: list["BaseImage"] | None = Field(
        default=None,
    )
    """Array of preview images of the product (for stickers product type)."""

    has_animation: bool | None = Field(
        default=None,
    )
    """Information whether the product is an animated sticker pack (for stickers product type)."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the product."""

    payment_region: str | None = Field(
        default=None,
    )
    """Property `Product.payment_region`."""

    is_vmoji: bool | None = Field(
        default=None,
    )
    """Information whether sticker pack is a vmoji pack."""

    title_lang_key: str | None = Field(
        default=None,
    )
    """Property `Product.title_lang_key`."""

    description_lang_key: str | None = Field(
        default=None,
    )
    """Property `Product.description_lang_key`."""

    url: str | None = Field(
        default=None,
    )
    """Property `Product.url`."""

    is_popup: bool | None = Field(
        default=None,
    )
    """Information whether the product is a sticker pack with popup stickers (for stickers product type)."""


class ProductIcon(BaseModel):
    """Model: `ProductIcon`"""

    base_url: str = Field()
    """Base URL for images in set."""

    version: int | None = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `ProductIcon.images`."""


class StickersKeyword(BaseModel):
    """Model: `StickersKeyword`"""

    words: list[str] = Field()
    """Property `StickersKeyword.words`."""

    user_stickers: list["StickerNew"] | None = Field(
        default=None,
    )
    """Property `StickersKeyword.user_stickers`."""

    promoted_stickers: list["StickerNew"] | None = Field(
        default=None,
    )
    """Property `StickersKeyword.promoted_stickers`."""

    stickers: list["StickersKeywordSticker"] | None = Field(
        default=None,
    )
    """Property `StickersKeyword.stickers`."""


class StickersKeywordSticker(BaseModel):
    """Model: `StickersKeywordSticker`"""

    pack_id: int = Field()
    """Pack id."""

    sticker_id: int = Field()
    """Sticker id."""


class ClickableArea(BaseModel):
    """Model: `ClickableArea`"""

    x: int = Field()
    """Property `ClickableArea.x`."""

    y: int = Field()
    """Property `ClickableArea.y`."""


class ClickableStickerType(StrEnum, metaclass=BaseEnumMeta):
    HASHTAG = "hashtag"
    MENTION = "mention"
    LINK = "link"
    QUESTION = "question"
    PLACE = "place"
    MARKET_ITEM = "market_item"
    MUSIC = "music"
    STORY_REPLY = "story_reply"
    OWNER = "owner"
    POST = "post"
    POLL = "poll"
    STICKER = "sticker"
    APP = "app"
    SITUATIONAL_THEME = "situational_theme"
    PLAYLIST = "playlist"
    CLIP = "clip"
    VK_VIDEO = "vk_video"
    SITUATIONAL_TEMPLATE = "situational_template"
    SPOILER = "spoiler"
    SERVICE_YC_ITEM = "service_yc_item"


class ClickableStickerStyle(StrEnum, metaclass=BaseEnumMeta):
    TRANSPARENT = "transparent"
    BLUE_GRADIENT = "blue_gradient"
    RED_GRADIENT = "red_gradient"
    UNDERLINE = "underline"
    BLUE = "blue"
    GREEN = "green"
    WHITE = "white"
    QUESTION_REPLY = "question_reply"
    LIGHT = "light"
    IMPRESSIVE = "impressive"
    DARK = "dark"
    ACCENT_BACKGROUND = "accent_background"
    ACCENT_TEXT = "accent_text"
    DARK_UNIQUE = "dark_unique"
    LIGHT_UNIQUE = "light_unique"
    LIGHT_TEXT = "light_text"
    DARK_TEXT = "dark_text"
    BLACK = "black"
    DARK_WITHOUT_BG = "dark_without_bg"
    LIGHT_WITHOUT_BG = "light_without_bg"
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    POOP = "poop"
    HEART = "heart"
    STAR = "star"
    ALBUM = "album"
    HORIZONTAL = "horizontal"
    EQUALIZER = "equalizer"
    HEADER_META = "header_meta"
    PREVIEW = "preview"
    MINIATURE = "miniature"
    FULLVIEW = "fullview"
    CTA = "cta"
    STICKER = "sticker"
    STICKER_AND_CTA = "sticker_and_cta"
    ACCENT = "accent"


class ClickableStickerSubtype(StrEnum, metaclass=BaseEnumMeta):
    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class ClickableSticker(BaseModel):
    """Model: `ClickableSticker`"""
    clickable_area: 'list["ClickableArea"]' = Field()
    """Property `ClickableSticker.clickable_area`."""
    id: 'int' = Field()
    """Clickable sticker ID."""
    type: "ClickableStickerType" = Field()
    """Property `ClickableSticker.type`."""
    hashtag: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.hashtag`."""
    link_object: "Link | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.link_object`."""
    mention: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.mention`."""
    tooltip_text: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.tooltip_text`."""
    owner_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.owner_id`."""
    story_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.story_id`."""
    clip_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.clip_id`."""
    video_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.video_id`."""
    question: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.question`."""
    question_button: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.question_button`."""
    place_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.place_id`."""
    market_item: "MarketItem | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.market_item`."""
    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.audio`."""
    audio_start_time: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.audio_start_time`."""
    style: "ClickableStickerStyle | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.style`."""
    subtype: "ClickableStickerSubtype | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.subtype`."""
    post_owner_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.post_owner_id`."""
    post_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.post_id`."""
    color: 'str | None' = Field(
        default=None,
    )
    """Color, hex format."""
    sticker_id: 'int | None' = Field(
        default=None,
    )
    """Sticker ID."""
    sticker_pack_id: 'int | None' = Field(
        default=None,
    )
    """Sticker pack ID."""
    app: "AppMin | None" = Field(
        default=None,
    )
    """Property `ClickableSticker.app`."""
    app_context: 'str | None' = Field(
        default=None,
    )
    """Additional context for app sticker."""
    has_new_interactions: 'bool | None' = Field(
        default=None,
    )
    """Whether current user has unread interaction with this app."""
    is_broadcast_notify_allowed: 'bool | None' = Field(
        default=None,
    )
    """Whether current user allowed broadcast notify from this app."""
    situational_theme_id: 'int | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.situational_theme_id`."""
    situational_app_url: 'str | None' = Field(
        default=None,
    )
    """Property `ClickableSticker.situational_app_url`."""
    poll: 'Poll | None' = None


class ClickableStickers(BaseModel):
    """Model: `ClickableStickers`"""

    clickable_stickers: list["ClickableSticker"] = Field()
    """Property `ClickableStickers.clickable_stickers`."""

    original_height: int = Field()
    """Property `ClickableStickers.original_height`."""

    original_width: int = Field()
    """Property `ClickableStickers.original_width`."""


class FeedItemType(StrEnum, metaclass=BaseEnumMeta):
    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    APP_GROUPED_STORIES = "app_grouped_stories"
    DISCOVER = "discover"


class FeedItem(BaseModel):
    """Model: `FeedItem`"""

    type: "FeedItemType" = Field()
    """Type of Feed Item."""

    id: str | None = Field(
        default=None,
    )
    """Property `FeedItem.id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `FeedItem.owner_id`."""

    stories: list["Story"] | None = Field(
        default=None,
    )
    """Author stories."""

    grouped: list["FeedItem"] | None = Field(
        default=None,
    )
    """Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)."""

    app: "AppMin | None" = Field(
        default=None,
    )
    """App, which stories has been grouped (for type app_grouped_stories)."""

    promo_data: "PromoBlock | None" = Field(
        default=None,
    )
    """Additional data for promo stories (for type promo_stories)."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `FeedItem.track_code`."""

    has_unseen: bool | None = Field(
        default=None,
    )
    """Property `FeedItem.has_unseen`."""

    name: str | None = Field(
        default=None,
    )
    """Property `FeedItem.name`."""


class PromoBlock(BaseModel):
    """Additional data for promo stories
    Model: `PromoBlock`
    """

    name: str = Field()
    """Promo story title."""

    photo_50: str = Field()
    """RL of square photo of the story with 50 pixels in width."""

    photo_100: str = Field()
    """RL of square photo of the story with 100 pixels in width."""

    not_animated: bool = Field()
    """Hide animation for promo story."""

    is_advice: bool = Field()
    """Promo story from advice."""


class Replies(BaseModel):
    """Model: `Replies`"""

    count: int = Field()
    """Replies number.."""

    new: int | None = Field(
        default=None,
    )
    """New replies number.."""


class Story(BaseModel):
    """Model: `Story`"""
    id: 'int' = Field()
    """Story ID.."""
    owner_id: 'int' = Field()
    """Story owner\'s ID.."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Access key for private object.."""
    can_comment: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can comment the story (0 - no, 1 - yes).."""
    can_reply: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can reply to the story (0 - no, 1 - yes).."""
    can_see: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can see the story (0 - no, 1 - yes).."""
    can_like: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can like the story.."""
    can_share: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can share the story (0 - no, 1 - yes).."""
    can_hide: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can hide the story (0 - no, 1 - yes).."""
    date: 'datetime.datetime | None' = Field(
        default=None,
    )
    """Date when story has been added in Unixtime.."""
    expires_at: 'int | None' = Field(
        default=None,
    )
    """Story expiration time. Unixtime.."""
    is_deleted: 'bool | None' = Field(
        default=None,
    )
    """Information whether the story is deleted (false - no, true - yes).."""
    is_expired: 'bool | None' = Field(
        default=None,
    )
    """Information whether the story is expired (false - no, true - yes).."""
    link: "StoryLink | None" = Field(
        default=None,
    )
    """Property `Story.link`."""
    parent_story: "Story | None" = Field(
        default=None,
    )
    """Property `Story.parent_story`."""
    parent_story_access_key: 'str | None' = Field(
        default=None,
    )
    """Access key for private object.."""
    parent_story_id: 'int | None' = Field(
        default=None,
    )
    """Parent story ID.."""
    parent_story_owner_id: 'int | None' = Field(
        default=None,
    )
    """Parent story owner\'s ID.."""
    blurred_preview: 'str | None' = Field(
        default=None,
    )
    """url with blured preview image.."""
    replies: "Replies | None" = Field(
        default=None,
    )
    """Replies counters to current story.."""
    seen: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user has seen the story or not (0 - no, 1 - yes).."""
    type: "StoryType | None" = Field(
        default=None,
    )
    """Property `Story.type`."""
    clickable_stickers: "ClickableStickers | None" = Field(
        default=None,
    )
    """Property `Story.clickable_stickers`."""
    video: "VideoFull | None" = Field(
        default=None,
    )
    """Property `Story.video`."""
    views: 'int | None' = Field(
        default=None,
    )
    """Views number.."""
    can_ask: 'bool | None' = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send question to the author."""
    can_ask_anonymous: 'bool | None' = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send anonymous question to the author."""
    narratives_count: 'int | None' = Field(
        default=None,
    )
    """Property `Story.narratives_count`."""
    first_narrative_title: 'str | None' = Field(
        default=None,
    )
    """Property `Story.first_narrative_title`."""
    first_narrative_id: 'int | None' = Field(
        default=None,
    )
    """Property `Story.first_narrative_id`."""
    can_use_in_narrative: 'bool | None' = Field(
        default=None,
    )
    """Property `Story.can_use_in_narrative`."""
    photo: 'Photo | None' = None


class StoryLink(BaseModel):
    """Model: `StoryLink`"""

    text: str = Field()
    """Link text."""

    url: str = Field()
    """Link URL."""

    link_url_target: str | None = Field(
        default=None,
    )
    """How to open url."""


class StoryStats(BaseModel):
    """Model: `StoryStats`"""

    answer: "StoryStatsStat" = Field()
    """Property `StoryStats.answer`."""

    bans: "StoryStatsStat" = Field()
    """Property `StoryStats.bans`."""

    open_link: "StoryStatsStat" = Field()
    """Property `StoryStats.open_link`."""

    replies: "StoryStatsStat" = Field()
    """Property `StoryStats.replies`."""

    shares: "StoryStatsStat" = Field()
    """Property `StoryStats.shares`."""

    subscribers: "StoryStatsStat" = Field()
    """Property `StoryStats.subscribers`."""

    views: "StoryStatsStat" = Field()
    """Property `StoryStats.views`."""

    likes: "StoryStatsStat" = Field()
    """Property `StoryStats.likes`."""


class StoryStatsStat(BaseModel):
    """Model: `StoryStatsStat`"""

    state: "StoryStatsState" = Field()
    """Property `StoryStatsStat.state`."""

    count: int | None = Field(
        default=None,
    )
    """Stat value."""


class StoryStatsState(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoryType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"


class UploadLinkText(StrEnum, metaclass=BaseEnumMeta):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"
    MARKET_ONLINE_BOOKING = "market_online_booking"
    MARKET_LINK = "market_link"
    MESSAGE_TO_BC = "message_to_bc"


class UploadResult(BaseModel):
    """Model: `UploadResult`"""

    upload_result: str | None = Field(
        default=None,
    )
    """Property `UploadResult.upload_result`."""


class ViewersItem(BaseModel):
    """Model: `ViewersItem`"""

    is_liked: bool = Field()
    """user has like for this object."""

    user_id: int = Field()
    """user id."""

    user: "UserFull | None" = Field(
        default=None,
    )
    """Property `ViewersItem.user`."""


class StatsEventType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COMMENT = "comment"
    SHARE = "share"


class StreamingStats(BaseModel):
    """Model: `StreamingStats`"""

    event_type: "StatsEventType" = Field()
    """Events type."""

    stats: list["StatsPoint"] = Field()
    """Statistics."""


class StatsPoint(BaseModel):
    """Model: `StatsPoint`"""

    timestamp: int = Field()
    """Property `StatsPoint.timestamp`."""

    value: int = Field()
    """Property `StatsPoint.value`."""


class FriendStatus(BaseModel):
    """Model: `FriendStatus`"""

    friend_status: "FriendStatusStatus" = Field()
    """Property `FriendStatus.friend_status`."""

    user_id: int = Field()
    """User ID."""

    sign: str | None = Field(
        default=None,
    )
    """MD5 hash for the result validation."""


class FriendStatusStatus(IntEnum, metaclass=BaseEnumMeta):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsList(BaseModel):
    """Model: `FriendsList`"""

    id: int = Field()
    """List ID."""

    name: str = Field()
    """List title."""


class MutualFriend(BaseModel):
    """Model: `MutualFriend`"""

    common_count: int | None = Field(
        default=None,
    )
    """Total mutual friends number."""

    common_friends: list[int] | None = Field(
        default=None,
    )
    """Property `MutualFriend.common_friends`."""

    id: int | None = Field(
        default=None,
    )
    """User ID."""


class OnlineUsers(BaseModel):
    """Model: `OnlineUsers`"""

    online: list[int] = Field()
    """Property `OnlineUsers.online`."""

    total_count: int | None = Field(
        default=None,
    )
    """Total online friends number."""


class OnlineUsersWithMobile(BaseModel):
    """Model: `OnlineUsersWithMobile`"""

    online: list[int] = Field()
    """Property `OnlineUsersWithMobile.online`."""

    online_mobile: list[int] = Field()
    """Property `OnlineUsersWithMobile.online_mobile`."""

    total_count: int | None = Field(
        default=None,
    )
    """Total online friends number."""


class RequestsMutual(BaseModel):
    """Model: `RequestsMutual`"""

    count: int | None = Field(
        default=None,
    )
    """Total mutual friends number."""

    users: list[int] | None = Field(
        default=None,
    )
    """Property `RequestsMutual.users`."""


class DomainResolved(BaseModel):
    """Model: `DomainResolved`"""

    object_id: int | None = Field(
        default=None,
    )
    """Object ID."""

    group_id: int | None = Field(
        default=None,
    )
    """Group ID."""

    type: "DomainResolvedType | None" = Field(
        default=None,
    )
    """Property `DomainResolved.type`."""


class DomainResolvedType(StrEnum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    EVENT = "event"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class LastShortenedLink(BaseModel):
    """Model: `LastShortenedLink`"""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for private stats."""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: str | None = Field(
        default=None,
    )
    """Short link URL."""

    timestamp: int | None = Field(
        default=None,
    )
    """Creation time in Unixtime."""

    url: str | None = Field(
        default=None,
    )
    """Full URL."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class LinkChecked(BaseModel):
    """Model: `LinkChecked`"""

    link: str | None = Field(
        default=None,
    )
    """Link URL."""

    status: "LinkCheckedStatus | None" = Field(
        default=None,
    )
    """Property `LinkChecked.status`."""


class LinkCheckedStatus(StrEnum, metaclass=BaseEnumMeta):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class LinkStats(BaseModel):
    """Model: `LinkStats`"""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: list["UtilsStats"] | None = Field(
        default=None,
    )
    """Property `LinkStats.stats`."""


class LinkStatsExtended(BaseModel):
    """Model: `LinkStatsExtended`"""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: list["StatsExtended"] | None = Field(
        default=None,
    )
    """Property `LinkStatsExtended.stats`."""


class ShortLink(BaseModel):
    """Model: `ShortLink`"""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for private stats."""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: str | None = Field(
        default=None,
    )
    """Short link URL."""

    url: str | None = Field(
        default=None,
    )
    """Full URL."""


class UtilsStats(BaseModel):
    """Model: `UtilsStats`"""

    timestamp: int | None = Field(
        default=None,
    )
    """Start time."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsCity(BaseModel):
    """Model: `UtilsStatsCity`"""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""


class UtilsStatsCountry(BaseModel):
    """Model: `UtilsStatsCountry`"""

    country_id: int | None = Field(
        default=None,
    )
    """Country ID."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""


class StatsExtended(BaseModel):
    """Model: `StatsExtended`"""

    cities: list["UtilsStatsCity"] | None = Field(
        default=None,
    )
    """Property `StatsExtended.cities`."""

    countries: list["UtilsStatsCountry"] | None = Field(
        default=None,
    )
    """Property `StatsExtended.countries`."""

    sex_age: list["UtilsStatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsExtended.sex_age`."""

    timestamp: int | None = Field(
        default=None,
    )
    """Start time."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsSexAge(BaseModel):
    """Model: `UtilsStatsSexAge`"""

    age_range: str | None = Field(
        default=None,
    )
    """Age denotation."""

    female: int | None = Field(
        default=None,
    )
    """ Views by female users."""

    male: int | None = Field(
        default=None,
    )
    """ Views by male users."""


class Episode(BaseModel):
    """Model: `Episode`"""

    time: int | None = Field(
        default=None,
    )
    """Seconds from start of the video."""

    text: str | None = Field(
        default=None,
    )
    """Description of episode."""


class LiveCategory(BaseModel):
    """Model: `LiveCategory`"""

    id: int = Field()
    """Property `LiveCategory.id`."""

    label: str = Field()
    """Property `LiveCategory.label`."""

    sublist: list["LiveCategory"] | None = Field(
        default=None,
    )
    """Property `LiveCategory.sublist`."""


class LiveInfo(BaseModel):
    """Model: `LiveInfo`"""

    enabled: bool = Field()
    """Property `LiveInfo.enabled`."""

    is_notifications_blocked: bool | None = Field(
        default=None,
    )
    """Property `LiveInfo.is_notifications_blocked`."""


class LiveSettings(BaseModel):
    """Video live settings
    Model: `LiveSettings`
    """

    can_rewind: bool | None = Field(
        default=None,
    )
    """If user car rewind live or not."""

    is_endless: bool | None = Field(
        default=None,
    )
    """If live is endless or not."""

    max_duration: int | None = Field(
        default=None,
    )
    """Max possible time for rewind."""

    is_clips_live: bool | None = Field(
        default=None,
    )
    """If live in clips apps."""


class PlaylistPrivacyCategory(StrEnum, metaclass=BaseEnumMeta):
    ALL = "all"
    FRIENDS = "friends"
    FRIENDS_OF_FRIENDS = "friends_of_friends"
    FRIENDS_OF_FRIENDS_ONLY = "friends_of_friends_only"
    ONLY_ME = "only_me"


class SaveResult(BaseModel):
    """Model: `SaveResult`"""

    access_key: str | None = Field(
        default=None,
    )
    """Video access key."""

    description: str | None = Field(
        default=None,
    )
    """Video description."""

    owner_id: int | None = Field(
        default=None,
    )
    """Video owner ID."""

    title: str | None = Field(
        default=None,
    )
    """Video title."""

    upload_url: str | None = Field(
        default=None,
    )
    """URL for the video uploading."""

    video_id: int | None = Field(
        default=None,
    )
    """Video ID."""


class StreamInputParams(BaseModel):
    """Model: `StreamInputParams`"""

    url: str | None = Field(
        default=None,
    )
    """Property `StreamInputParams.url`."""

    key: str | None = Field(
        default=None,
    )
    """Property `StreamInputParams.key`."""

    okmp_url: str | None = Field(
        default=None,
    )
    """Property `StreamInputParams.okmp_url`."""

    webrtc_url: str | None = Field(
        default=None,
    )
    """Property `StreamInputParams.webrtc_url`."""


class VideoResponseType(StrEnum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class Video(BaseModel):
    """Model: `Video`"""
    response_type: "VideoResponseType | None" = Field(
        default=None,
    )
    """Property `Video.response_type`."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Video access key."""
    adding_date: 'datetime.datetime | None' = Field(
        default=None,
    )
    """Date when the video has been added in Unixtime."""
    can_comment: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can comment the video."""
    can_edit: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can edit the video."""
    can_delete: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can delete the video."""
    can_like: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can like the video."""
    can_repost: 'int | None' = Field(
        default=None,
    )
    """Information whether current user can repost the video."""
    can_subscribe: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can subscribe to author of the video."""
    can_be_promoted: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can promote the video."""
    can_add_to_faves: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can add the video to favourites."""
    can_add: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can add the video."""
    can_attach_link: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can attach action button to the video."""
    can_edit_privacy: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can edit the video privacy."""
    is_private: 'bool | None' = Field(
        default=None,
    )
    """1 if video is private."""
    comments: 'int | None' = Field(
        default=None,
    )
    """Number of comments."""
    date: 'datetime.datetime | None' = Field(
        default=None,
    )
    """Date when video has been uploaded in Unixtime."""
    description: 'str | None' = Field(
        default=None,
    )
    """Video description."""
    duration: 'int | None' = Field(
        default=None,
    )
    """Video duration in seconds."""
    image: 'list["VideoImage"] | None' = Field(
        default=None,
    )
    """Property `Video.image`."""
    first_frame: 'list["VideoImage"] | None' = Field(
        default=None,
    )
    """Property `Video.first_frame`."""
    width: 'int | None' = Field(
        default=None,
    )
    """Video width."""
    height: 'int | None' = Field(
        default=None,
    )
    """Video height."""
    id: 'int | None' = Field(
        default=None,
    )
    """Video ID."""
    owner_id: 'int | None' = Field(
        default=None,
    )
    """Video owner ID."""
    user_id: 'int | None' = Field(
        default=None,
    )
    """Id of the user who uploaded the video if it was uploaded to a group by member."""
    title: 'str | None' = Field(
        default=None,
    )
    """Video title."""
    is_favorite: 'bool | None' = Field(
        default=None,
    )
    """Whether video is added to bookmarks."""
    player: 'str | None' = Field(
        default=None,
    )
    """Video embed URL."""
    processing: "PropertyExists | None" = Field(
        default=None,
    )
    """Returns if the video is processing."""
    converting: 'bool | None' = Field(
        default=None,
    )
    """1 if  video is being converted."""
    added: 'bool | None' = Field(
        default=None,
    )
    """1 if video is added to user\'s albums."""
    is_subscribed: 'bool | None' = Field(
        default=None,
    )
    """1 if user is subscribed to author of the video."""
    track_code: 'str | None' = Field(
        default=None,
    )
    """Property `Video.track_code`."""
    repeat: "PropertyExists | None" = Field(
        default=None,
    )
    """Information whether the video is repeated."""
    views: 'int | None' = Field(
        default=None,
    )
    """Number of views."""
    local_views: 'int | None' = Field(
        default=None,
    )
    """If video is external, number of views on vk."""
    content_restricted: 'int | None' = Field(
        default=None,
    )
    """Restriction code."""
    content_restricted_message: 'str | None' = Field(
        default=None,
    )
    """Restriction text."""
    balance: 'int | None' = Field(
        default=None,
    )
    """Live donations balance."""
    live: "PropertyExists | None" = Field(
        default=None,
    )
    """1 if the video is a live stream."""
    upcoming: "PropertyExists | None" = Field(
        default=None,
    )
    """1 if the video is an upcoming stream."""
    live_start_time: 'int | None' = Field(
        default=None,
    )
    """Date in Unixtime when the live stream is scheduled to start by the author."""
    live_notify: 'bool | None' = Field(
        default=None,
    )
    """Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)."""
    spectators: 'int | None' = Field(
        default=None,
    )
    """Number of spectators of the stream."""
    platform: 'str | None' = Field(
        default=None,
    )
    """External platform."""
    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `Video.likes`."""
    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `Video.reposts`."""
    type: 'VideoType | None' = None


class VideoAlbumResponseType(StrEnum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class VideoAlbum(BaseModel):
    """Model: `VideoAlbum`"""

    id: int = Field()
    """Album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    title: str = Field()
    """Album title."""

    track_code: str | None = Field(
        default=None,
    )
    """Album trackcode."""

    response_type: "VideoAlbumResponseType | None" = Field(
        default=None,
    )
    """Property `VideoAlbum.response_type`."""


class VideoFiles(BaseModel):
    """Model: `VideoFiles`"""

    external: str | None = Field(
        default=None,
    )
    """URL of the external player."""

    mp4_144: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 144p quality."""

    mp4_240: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 240p quality."""

    mp4_360: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 360p quality."""

    mp4_480: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 480p quality."""

    mp4_720: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 720p quality."""

    mp4_1080: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 1080p quality."""

    mp4_1440: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 2K quality."""

    mp4_2160: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 4K quality."""

    flv_320: str | None = Field(
        default=None,
    )
    """URL of the flv file with 320p quality."""


class AppPost(BaseModel):
    """Model: `AppPost`"""

    id: int | None = Field(
        default=None,
    )
    """Application ID."""

    name: str | None = Field(
        default=None,
    )
    """Application name."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class AttachedNote(BaseModel):
    """Model: `AttachedNote`"""

    comments: int = Field()
    """Comments number."""

    date: datetime.datetime = Field()
    """Date when the note has been created in Unixtime."""

    id: int = Field()
    """Note ID."""

    owner_id: int = Field()
    """Note owner\'s ID."""

    read_comments: int = Field()
    """Read comments number."""

    title: str = Field()
    """Note title."""

    view_url: str = Field()
    """URL of the page with note preview."""

    text: str | None = Field(
        default=None,
    )
    """Note text."""

    privacy_view: list[str] | None = Field(
        default=None,
    )
    """Property `AttachedNote.privacy_view`."""

    privacy_comment: list[str] | None = Field(
        default=None,
    )
    """Property `AttachedNote.privacy_comment`."""

    can_comment: int | None = Field(
        default=None,
    )
    """Property `AttachedNote.can_comment`."""

    text_wiki: str | None = Field(
        default=None,
    )
    """Note wiki text."""


class CarouselBase(BaseModel):
    """Model: `CarouselBase`"""

    carousel_offset: int | None = Field(
        default=None,
    )
    """Index of current carousel element."""


class CommentAttachment(BaseModel):
    """Model: `CommentAttachment`"""
    type: "CommentAttachmentType" = Field()
    """Property `CommentAttachment.type`."""
    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.audio`."""
    doc: "Doc | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.doc`."""
    link: "Link | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.link`."""
    market: "MarketItem | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.market`."""
    market_market_album: "MarketAlbum | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.market_market_album`."""
    note: "AttachedNote | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.note`."""
    page: "WikipageFull | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.page`."""
    sticker: "Sticker | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.sticker`."""
    video: "Video | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.video`."""
    graffiti: "WallGraffiti | None" = Field(
        default=None,
    )
    """Property `CommentAttachment.graffiti`."""
    photo: 'Photo | None' = None


class CommentAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"
    GRAFFITI = "graffiti"


class GeoType(StrEnum, metaclass=BaseEnumMeta):
    PLACE = "place"
    POINT = "point"


class Geo(BaseModel):
    """Model: `Geo`"""

    coordinates: str | None = Field(
        default=None,
    )
    """Coordinates as string. <latitude> <longtitude>."""

    showmap: int | None = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: "GeoType | None" = Field(
        default=None,
    )
    """Place type."""


class GetFilter(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


class WallGraffiti(BaseModel):
    """Model: `WallGraffiti`"""

    id: int | None = Field(
        default=None,
    )
    """Graffiti ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Graffiti owner\'s ID."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_586: str | None = Field(
        default=None,
    )
    """URL of the preview image with 586 px in width."""

    height: int | None = Field(
        default=None,
    )
    """Graffiti height."""

    url: str | None = Field(
        default=None,
    )
    """Graffiti URL."""

    width: int | None = Field(
        default=None,
    )
    """Graffiti width."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for graffiti."""


class PostCopyright(BaseModel):
    """Model: `PostCopyright`"""

    link: str = Field()
    """Property `PostCopyright.link`."""

    name: str = Field()
    """Property `PostCopyright.name`."""

    type: str = Field()
    """Property `PostCopyright.type`."""

    id: int | None = Field(
        default=None,
    )
    """Property `PostCopyright.id`."""


class PostSource(BaseModel):
    """Model: `PostSource`"""

    data: str | None = Field(
        default=None,
    )
    """Additional data."""

    platform: str | None = Field(
        default=None,
    )
    """Platform name."""

    type: "PostSourceType | None" = Field(
        default=None,
    )
    """Property `PostSource.type`."""

    url: str | None = Field(
        default=None,
    )
    """URL to an external site used to publish the post."""

    link: "Link | None" = Field(
        default=None,
    )
    """Property `PostSource.link`."""


class PostSourceType(StrEnum, metaclass=BaseEnumMeta):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class PostType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    POST_ADS = "post_ads"
    PHOTO = "photo"
    VIDEO = "video"
    CLIP = "clip"


class PostedPhoto(BaseModel):
    """Model: `PostedPhoto`"""

    id: int | None = Field(
        default=None,
    )
    """Photo ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Photo owner\'s ID."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class WallViews(BaseModel):
    """Model: `WallViews`"""

    count: int | None = Field(
        default=None,
    )
    """Count."""


class WallComment(BaseModel):
    """Model: `WallComment`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `WallComment.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `WallComment.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `WallComment.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `WallComment.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `WallComment.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `WallComment.video_id`."""

    attachments: list["WallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `WallComment.attachments`."""

    donut: "WallCommentDonut | None" = Field(
        default=None,
    )
    """Property `WallComment.donut`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `WallComment.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `WallComment.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `WallComment.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class WallCommentDonut(BaseModel):
    """Model: `WallCommentDonut`"""

    is_don: bool | None = Field(
        default=None,
    )
    """Means commentator is donator."""

    placeholder: "WallCommentDonutPlaceholder | None" = Field(
        default=None,
    )
    """Property `WallCommentDonut.placeholder`."""


class WallCommentDonutPlaceholder(BaseModel):
    """Model: `WallCommentDonutPlaceholder`"""

    text: str = Field()
    """Property `WallCommentDonutPlaceholder.text`."""


class WallItem(BaseModel):
    """Model: `WallItem`"""

    copy_history: list["WallpostFull"] | None = Field(
        default=None,
    )
    """Property `WallItem.copy_history`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the post."""

    created_by: int | None = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the post."""

    can_pin: bool | None = Field(
        default=None,
    )
    """Information whether current user can pin the post."""

    donut: "WallpostDonut | None" = Field(
        default=None,
    )
    """Property `WallItem.donut`."""

    is_pinned: bool | None = Field(
        default=None,
    )
    """Information whether the post is pinned."""

    comments: "CommentsInfo | None" = Field(
        default=None,
    )
    """Property `WallItem.comments`."""

    marked_as_ads: bool | None = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""

    topic_id: int | None = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""

    hash: str | None = Field(
        default=None,
    )
    """Hash for sharing."""

    type: "PostType | None" = Field(
        default=None,
    )
    """Property `WallItem.type`."""

    feedback: "ItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `WallItem.feedback`."""

    to_id: int | None = Field(
        default=None,
    )
    """Property `WallItem.to_id`."""


class WallpostInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class Wallpost(BaseModel):
    """Model: `Wallpost`"""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Access key to private object."""
    is_deleted: 'bool | None' = Field(
        default=None,
    )
    """Property `Wallpost.is_deleted`."""
    deleted_reason: 'str | None' = Field(
        default=None,
    )
    """Property `Wallpost.deleted_reason`."""
    deleted_details: 'str | None' = Field(
        default=None,
    )
    """Property `Wallpost.deleted_details`."""
    donut_miniapp_url: 'str | None' = Field(
        default=None,
    )
    """Property `Wallpost.donut_miniapp_url`."""
    attachments: 'list["WallpostAttachment"] | None' = Field(
        default=None,
    )
    """Property `Wallpost.attachments`."""
    copyright: "PostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""
    date: 'datetime.datetime | None' = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""
    edited: 'int | None' = Field(
        default=None,
    )
    """Date of editing in Unixtime."""
    from_id: 'int | None' = Field(
        default=None,
    )
    """Post author ID."""
    geo: "Geo | None" = Field(
        default=None,
    )
    """Property `Wallpost.geo`."""
    id: 'int | None' = Field(
        default=None,
    )
    """Post ID."""
    is_archived: 'bool | None' = Field(
        default=None,
    )
    """Is post archived, only for post owners."""
    is_favorite: 'bool | None' = Field(
        default=None,
    )
    """Information whether the post in favorites list."""
    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""
    owner_id: 'int | None' = Field(
        default=None,
    )
    """Wall owner\'s ID."""
    post_id: 'int | None' = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""
    parents_stack: 'list[int] | None' = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""
    post_source: "PostSource | None" = Field(
        default=None,
    )
    """Property `Wallpost.post_source`."""
    post_type: "PostType | None" = Field(
        default=None,
    )
    """Property `Wallpost.post_type`."""
    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `Wallpost.reposts`."""
    signer_id: 'int | None' = Field(
        default=None,
    )
    """Post signer ID."""
    text: 'str | None' = Field(
        default=None,
    )
    """Post text."""
    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""
    inner_type: 'WallpostInnerType | None' = None


class WallpostAttachment(BaseModel):
    """Model: `WallpostAttachment`"""
    type: "WallpostAttachmentType" = Field()
    """Property `WallpostAttachment.type`."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Access key for the audio."""
    album: "PhotoAlbum | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.album`."""
    app: "AppPost | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.app`."""
    audio: "Audio | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.audio`."""
    doc: "Doc | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.doc`."""
    event: "EventsEventAttach | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.event`."""
    group: "GroupAttach | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.group`."""
    graffiti: "WallGraffiti | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.graffiti`."""
    link: "Link | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.link`."""
    market: "MarketItem | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.market`."""
    market_album: "MarketAlbum | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.market_album`."""
    note: "Note | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.note`."""
    page: "WikipageFull | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.page`."""
    posted_photo: "PostedPhoto | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.posted_photo`."""
    video: "VideoFull | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.video`."""
    clip: "VideoFull | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.clip`."""
    video_playlist: "VideoAlbumFull | None" = Field(
        default=None,
    )
    """Property `WallpostAttachment.video_playlist`."""
    photo: 'Photo | None' = None
    mini_app: 'App | None' = None
    pretty_cards: 'PrettyCardsList | None' = None
    poll: 'Poll | None' = None


class WallpostCommentsDonut(BaseModel):
    """Model: `WallpostCommentsDonut`"""

    placeholder: "WallpostCommentsDonutPlaceholder | None" = Field(
        default=None,
    )
    """Property `WallpostCommentsDonut.placeholder`."""


class WallpostCommentsDonutPlaceholder(BaseModel):
    """Info about paid comments feature
    Model: `WallpostCommentsDonutPlaceholder`
    """

    text: str = Field()
    """Property `WallpostCommentsDonutPlaceholder.text`."""


class WallpostDonutEditMode(StrEnum, metaclass=BaseEnumMeta):
    ALL = "all"
    DURATION = "duration"


class WallpostDonut(BaseModel):
    """Info about paid wall post
    Model: `WallpostDonut`
    """

    is_donut: bool = Field()
    """Post only for dons."""

    paid_duration: int | None = Field(
        default=None,
    )
    """Value of this field need to pass in wall.post/edit in donut_paid_duration."""

    placeholder: "WallpostDonutPlaceholder | None" = Field(
        default=None,
    )
    """If placeholder was respond, text and all attachments will be hidden."""

    can_publish_free_copy: bool | None = Field(
        default=None,
    )
    """Says whether group admin can post free copy of this donut post."""

    edit_mode: "WallpostDonutEditMode | None" = Field(
        default=None,
    )
    """Says what user can edit in post about donut properties."""


class WallpostDonutPlaceholder(BaseModel):
    """Model: `WallpostDonutPlaceholder`"""

    text: str = Field()
    """Property `WallpostDonutPlaceholder.text`."""


class CommentsFilters(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class CommentsItem(BaseModel):
    """Model: `CommentsItem`"""


class CommentsItemBase(BaseModel):
    """Model: `CommentsItemBase`"""

    type: "NewsfeedItemType" = Field()
    """Property `CommentsItemBase.type`."""

    source_id: int | None = Field(
        default=None,
    )
    """Property `CommentsItemBase.source_id`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Property `CommentsItemBase.date`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CommentsItemBase.post_id`."""


class IgnoreItemType(StrEnum, metaclass=BaseEnumMeta):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class ItemAudioAudio(BaseModel):
    """Model: `ItemAudioAudio`"""

    count: int | None = Field(
        default=None,
    )
    """Audios number."""

    items: list["Audio"] | None = Field(
        default=None,
    )
    """Property `ItemAudioAudio.items`."""


class ItemBase(BaseModel):
    """Model: `ItemBase`"""

    type: "NewsfeedItemType" = Field()
    """Property `ItemBase.type`."""

    source_id: int = Field()
    """Item source ID."""

    date: datetime.datetime = Field()
    """Date when item has been added in Unixtime."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""

    feedback: "ItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `ItemBase.feedback`."""


class ItemDigestButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"


class ItemDigestButton(BaseModel):
    """Model: `ItemDigestButton`"""

    title: str = Field()
    """Property `ItemDigestButton.title`."""

    style: "ItemDigestButtonStyle | None" = Field(
        default=None,
    )
    """Property `ItemDigestButton.style`."""


class ItemDigestFooterStyle(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    BUTTON = "button"


class ItemDigestFooter(BaseModel):
    """Model: `ItemDigestFooter`"""

    style: "ItemDigestFooterStyle" = Field()
    """Property `ItemDigestFooter.style`."""

    text: str = Field()
    """text for invite to enable smart feed."""

    button: "ItemDigestButton | None" = Field(
        default=None,
    )
    """Property `ItemDigestFooter.button`."""

    feed_id: str | None = Field(
        default=None,
    )
    """Property `ItemDigestFooter.feed_id`."""


class ItemDigestHeaderStyle(StrEnum, metaclass=BaseEnumMeta):
    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class ItemDigestHeader(BaseModel):
    """Model: `ItemDigestHeader`"""

    title: str = Field()
    """Title of the header."""

    style: "ItemDigestHeaderStyle" = Field()
    """Property `ItemDigestHeader.style`."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the header, when title have two strings."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional field for red badge in Trends feed blocks."""

    button: "ItemDigestButton | None" = Field(
        default=None,
    )
    """Property `ItemDigestHeader.button`."""


class ItemDigestItem(BaseModel):
    """Model: `ItemDigestItem`"""

    inner_type: str = Field()
    """Property `ItemDigestItem.inner_type`."""

    post: "ItemWallpost" = Field()
    """Property `ItemDigestItem.post`."""

    text: str | None = Field(
        default=None,
    )
    """Property `ItemDigestItem.text`."""

    source_name: str | None = Field(
        default=None,
    )
    """Property `ItemDigestItem.source_name`."""

    attachment_index: int | None = Field(
        default=None,
    )
    """Property `ItemDigestItem.attachment_index`."""

    attachment: "WallpostAttachment | None" = Field(
        default=None,
    )
    """Property `ItemDigestItem.attachment`."""

    style: str | None = Field(
        default=None,
    )
    """Property `ItemDigestItem.style`."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class ItemFriendFriends(BaseModel):
    """Model: `ItemFriendFriends`"""

    count: int | None = Field(
        default=None,
    )
    """Number of friends has been added."""

    items: list["UserId"] | None = Field(
        default=None,
    )
    """Property `ItemFriendFriends.items`."""


class ItemHolidayRecommendationsBlockHeader(BaseModel):
    """Model: `ItemHolidayRecommendationsBlockHeader`"""

    title: str | None = Field(
        default=None,
    )
    """Title of the header."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the header."""

    image: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `ItemHolidayRecommendationsBlockHeader.image`."""

    action: "LinkButtonAction | None" = Field(
        default=None,
    )
    """Property `ItemHolidayRecommendationsBlockHeader.action`."""


class ItemPhotoPhotos(BaseModel):
    """Model: `ItemPhotoPhotos`"""
    count: 'int | None' = Field(
        default=None,
    )
    """Photos number."""
    items: 'list[Photo] | None' = None


class ItemPhotoTagPhotoTags(BaseModel):
    """Model: `ItemPhotoTagPhotoTags`"""
    count: 'int | None' = Field(
        default=None,
    )
    """Tags number."""
    items: 'list[Photo] | None' = None


class ItemPromoButtonAction(BaseModel):
    """Model: `ItemPromoButtonAction`"""

    url: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonAction.url`."""

    type: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonAction.type`."""

    target: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonAction.target`."""


class ItemPromoButtonImage(BaseModel):
    """Model: `ItemPromoButtonImage`"""

    width: int | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonImage.width`."""

    height: int | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonImage.height`."""

    url: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButtonImage.url`."""


class ItemVideoVideo(BaseModel):
    """Model: `ItemVideoVideo`"""

    count: int | None = Field(
        default=None,
    )
    """Tags number."""

    items: list["VideoFull"] | None = Field(
        default=None,
    )
    """Property `ItemVideoVideo.items`."""


class ItemWallpostFeedback(BaseModel):
    """Model: `ItemWallpostFeedback`"""

    type: "ItemWallpostFeedbackType" = Field()
    """Property `ItemWallpostFeedback.type`."""

    question: str = Field()
    """Property `ItemWallpostFeedback.question`."""

    answers: list["ItemWallpostFeedbackAnswer"] | None = Field(
        default=None,
    )
    """Property `ItemWallpostFeedback.answers`."""

    stars_count: int | None = Field(
        default=None,
    )
    """Property `ItemWallpostFeedback.stars_count`."""

    descriptions: list[str] | None = Field(
        default=None,
    )
    """Property `ItemWallpostFeedback.descriptions`."""

    gratitude: str | None = Field(
        default=None,
    )
    """Property `ItemWallpostFeedback.gratitude`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `ItemWallpostFeedback.track_code`."""


class ItemWallpostFeedbackAnswer(BaseModel):
    """Model: `ItemWallpostFeedbackAnswer`"""

    title: str = Field()
    """Property `ItemWallpostFeedbackAnswer.title`."""

    id: str = Field()
    """Property `ItemWallpostFeedbackAnswer.id`."""


class ItemWallpostFeedbackType(StrEnum, metaclass=BaseEnumMeta):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedList(BaseModel):
    """Model: `NewsfeedList`"""

    id: int = Field()
    """List ID."""

    title: str = Field()
    """List title."""


class NewsfeedItem(BaseModel):
    """Model: `NewsfeedItem`"""


class NewsfeedItemType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    NOTE = "note"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"
    CLIPS_RETENTION = "clips_retention"


class CommentMedia(BaseModel):
    """Model: `CommentMedia`"""

    item_id: int | None = Field(
        default=None,
    )
    """Media item ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Media owner\'s ID."""

    thumb_src: str | None = Field(
        default=None,
    )
    """URL of the preview image (type=photo only)."""

    type: "CommentMediaType | None" = Field(
        default=None,
    )
    """Property `CommentMedia.type`."""


class CommentMediaType(StrEnum, metaclass=BaseEnumMeta):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class CommentReplies(BaseModel):
    """Model: `CommentReplies`"""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    count: int | None = Field(
        default=None,
    )
    """Comments number."""

    replies: list["CommentRepliesItem"] | None = Field(
        default=None,
    )
    """Property `CommentReplies.replies`."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    can_view: bool | None = Field(
        default=None,
    )
    """Information whether current user can view the comments."""


class CommentRepliesItem(BaseModel):
    """Model: `CommentRepliesItem`"""

    cid: int | None = Field(
        default=None,
    )
    """Comment ID."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the comment has been added in Unixtime."""

    likes: "WidgetLikes | None" = Field(
        default=None,
    )
    """Property `CommentRepliesItem.likes`."""

    text: str | None = Field(
        default=None,
    )
    """Comment text."""

    uid: int | None = Field(
        default=None,
    )
    """User ID."""

    user: "UserFull | None" = Field(
        default=None,
    )
    """Property `CommentRepliesItem.user`."""


class WidgetComment(BaseModel):
    """Model: `WidgetComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Comment author ID."""

    id: int = Field()
    """Comment ID."""

    post_type: str = Field()
    """Post type."""

    text: str = Field()
    """Comment text."""

    to_id: int = Field()
    """Wall owner."""

    attachments: list["CommentAttachment"] | None = Field(
        default=None,
    )
    """Property `WidgetComment.attachments`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the comment."""

    comments: "CommentReplies | None" = Field(
        default=None,
    )
    """Property `WidgetComment.comments`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `WidgetComment.likes`."""

    media: "CommentMedia | None" = Field(
        default=None,
    )
    """Property `WidgetComment.media`."""

    post_source: "PostSource | None" = Field(
        default=None,
    )
    """Property `WidgetComment.post_source`."""

    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `WidgetComment.reposts`."""

    user: "UserFull | None" = Field(
        default=None,
    )
    """Property `WidgetComment.user`."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""


class WidgetLikes(BaseModel):
    """Model: `WidgetLikes`"""

    count: int | None = Field(
        default=None,
    )
    """Likes number."""


class WidgetPage(BaseModel):
    """Model: `WidgetPage`"""

    comments: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `WidgetPage.comments`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when widgets on the page has been initialized firstly in Unixtime."""

    description: str | None = Field(
        default=None,
    )
    """Page description."""

    id: int | None = Field(
        default=None,
    )
    """Page ID."""

    likes: "ObjectCount | None" = Field(
        default=None,
    )
    """Property `WidgetPage.likes`."""

    page_id: str | None = Field(
        default=None,
    )
    """page_id parameter value."""

    photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    title: str | None = Field(
        default=None,
    )
    """Page title."""

    url: str | None = Field(
        default=None,
    )
    """Page absolute URL."""


class Link(LinkNoProduct):
    """Model: `Link`"""

    text: str | None = Field(
        default=None,
    )
    """Property `Link.text`."""

    product: "LinkProduct | None" = Field(
        default=None,
    )
    """Property `Link.product`."""


class User(UserMin):
    """Model: `User`"""

    sex: "Sex | None" = Field(
        default=None,
    )
    """User sex."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 50 pixels in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 100 pixels in width."""

    online_info: "OnlineInfo | None" = Field(
        default=None,
    )
    """Property `User.online_info`."""

    online: bool | None = Field(
        default=None,
    )
    """Information whether the user is online."""

    online_mobile: bool | None = Field(
        default=None,
    )
    """Information whether the user is online in mobile site or application."""

    online_app: int | None = Field(
        default=None,
    )
    """Application ID."""

    verified: bool | None = Field(
        default=None,
    )
    """Information whether the user is verified."""

    trending: bool | None = Field(
        default=None,
    )
    """Information whether the user has a \"fire\" pictogram.."""

    friend_status: "FriendStatusStatus | None" = Field(
        default=None,
    )
    """Property `User.friend_status`."""

    mutual: "RequestsMutual | None" = Field(
        default=None,
    )
    """Property `User.mutual`."""


class UserFull(User):
    """Model: `UserFull`"""
    first_name_nom: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in nominative case."""
    first_name_gen: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in genitive case."""
    first_name_dat: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in dative case."""
    first_name_acc: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in accusative case."""
    first_name_ins: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in instrumental case."""
    first_name_abl: 'str | None' = Field(
        default=None,
    )
    """User\'s first name in prepositional case."""
    last_name_nom: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in nominative case."""
    last_name_gen: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in genitive case."""
    last_name_dat: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in dative case."""
    last_name_acc: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in accusative case."""
    last_name_ins: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in instrumental case."""
    last_name_abl: 'str | None' = Field(
        default=None,
    )
    """User\'s last name in prepositional case."""
    nickname: 'str | None' = Field(
        default=None,
    )
    """User nickname."""
    maiden_name: 'str | None' = Field(
        default=None,
    )
    """User maiden name."""
    contact_name: 'str | None' = Field(
        default=None,
    )
    """User contact name."""
    domain: 'str | None' = Field(
        default=None,
    )
    """Domain name of the user\'s page."""
    bdate: 'str | None' = Field(
        default=None,
    )
    """User\'s date of birth."""
    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `UserFull.city`."""
    timezone: 'float | None' = Field(
        default=None,
    )
    """User\'s timezone."""
    owner_state: "OwnerState | None" = Field(
        default=None,
    )
    """Property `UserFull.owner_state`."""
    photo_200: 'str | None' = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""
    photo_max: 'str | None' = Field(
        default=None,
    )
    """URL of square photo of the user with maximum width."""
    photo_200_orig: 'str | None' = Field(
        default=None,
    )
    """URL of user\'s photo with 200 pixels in width."""
    photo_400_orig: 'str | None' = Field(
        default=None,
    )
    """URL of user\'s photo with 400 pixels in width."""
    photo_max_orig: 'str | None' = Field(
        default=None,
    )
    """URL of user\'s photo of maximum size."""
    photo_id: 'str | None' = Field(
        default=None,
    )
    """ID of the user\'s main photo."""
    has_photo: 'bool | None' = Field(
        default=None,
    )
    """Information whether the user has main photo."""
    has_mobile: 'bool | None' = Field(
        default=None,
    )
    """Information whether the user specified his phone number."""
    is_friend: 'bool | None' = Field(
        default=None,
    )
    """Information whether the user is a friend of current user."""
    is_best_friend: 'bool | None' = Field(
        default=None,
    )
    """Information whether the user is a best friend of current user."""
    wall_comments: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can comment wall posts."""
    can_post: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can post on the user\'s wall."""
    can_see_all_posts: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can see other users\' audio on the wall."""
    can_see_audio: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can see the user\'s audio."""
    type: "UserType | None" = Field(
        default=None,
    )
    """Property `UserFull.type`."""
    email: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.email`."""
    skype: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.skype`."""
    facebook: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.facebook`."""
    facebook_name: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.facebook_name`."""
    twitter: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.twitter`."""
    livejournal: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.livejournal`."""
    instagram: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.instagram`."""
    test: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.test`."""
    video_live: "LiveInfo | None" = Field(
        default=None,
    )
    """Property `UserFull.video_live`."""
    is_video_live_notifications_blocked: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.is_video_live_notifications_blocked`."""
    is_service: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.is_service`."""
    service_description: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.service_description`."""
    photo_rec: 'str | bool | None' = Field(
        default=None,
    )
    """Property `UserFull.photo_rec`."""
    photo_medium: 'str | bool | None' = Field(
        default=None,
    )
    """Property `UserFull.photo_medium`."""
    photo_medium_rec: 'str | bool | None' = Field(
        default=None,
    )
    """Property `UserFull.photo_medium_rec`."""
    photo: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.photo`."""
    photo_big: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.photo_big`."""
    photo_400: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.photo_400`."""
    language: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.language`."""
    stories_archive_count: 'int | None' = Field(
        default=None,
    )
    """Property `UserFull.stories_archive_count`."""
    has_unseen_stories: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.has_unseen_stories`."""
    wall_default: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.wall_default`."""
    can_call: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can call."""
    can_call_from_group: 'bool | None' = Field(
        default=None,
    )
    """Information whether group can call user."""
    can_invite_as_voicerooms_speaker: 'bool | None' = Field(
        default=None,
    )
    """Information whether user/group can invite user as voicerooms speakr."""
    can_see_wishes: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can see the user\'s wishes."""
    can_see_gifts: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can see the user\'s gifts."""
    interests: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.interests`."""
    books: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.books`."""
    tv: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.tv`."""
    quotes: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.quotes`."""
    about: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.about`."""
    games: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.games`."""
    movies: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.movies`."""
    activities: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.activities`."""
    music: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.music`."""
    can_write_private_message: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can write private message."""
    can_send_friend_request: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can send a friend request."""
    can_be_invited_group: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can be invited to the community."""
    mobile_phone: 'str | None' = Field(
        default=None,
    )
    """User\'s mobile phone number."""
    home_phone: 'str | None' = Field(
        default=None,
    )
    """User\'s additional phone number."""
    site: 'str | None' = Field(
        default=None,
    )
    """User\'s website."""
    status_audio: "Audio | None" = Field(
        default=None,
    )
    """Property `UserFull.status_audio`."""
    status: 'str | None' = Field(
        default=None,
    )
    """User\'s status."""
    activity: 'str | None' = Field(
        default=None,
    )
    """User\'s status."""
    status_app: "AppMin | None" = Field(
        default=None,
    )
    """Property `UserFull.status_app`."""
    last_seen: "LastSeen | None" = Field(
        default=None,
    )
    """Property `UserFull.last_seen`."""
    exports: "Exports | None" = Field(
        default=None,
    )
    """Property `UserFull.exports`."""
    crop_photo: "CropPhoto | None" = Field(
        default=None,
    )
    """Property `UserFull.crop_photo`."""
    followers_count: 'int | None' = Field(
        default=None,
    )
    """Number of user\'s followers and friends."""
    video_live_level: 'int | None' = Field(
        default=None,
    )
    """User level in live streams achievements."""
    video_live_count: 'int | None' = Field(
        default=None,
    )
    """Number of user\'s live streams."""
    clips_count: 'int | None' = Field(
        default=None,
    )
    """Number of user\'s clips."""
    blacklisted: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user is in the requested user\'s blacklist.."""
    blacklisted_by_me: 'bool | None' = Field(
        default=None,
    )
    """Information whether the requested user is in current user\'s blacklist."""
    is_favorite: 'bool | None' = Field(
        default=None,
    )
    """Information whether the requested user is in faves of current user."""
    is_hidden_from_feed: 'bool | None' = Field(
        default=None,
    )
    """Information whether the requested user is hidden from current user\'s newsfeed."""
    common_count: 'int | None' = Field(
        default=None,
    )
    """Number of common friends with current user."""
    occupation: "Occupation | None" = Field(
        default=None,
    )
    """Property `UserFull.occupation`."""
    career: 'list["Career"] | None' = Field(
        default=None,
    )
    """Property `UserFull.career`."""
    military: 'list["Military"] | None' = Field(
        default=None,
    )
    """Property `UserFull.military`."""
    university: 'int | None' = Field(
        default=None,
    )
    """University ID."""
    university_name: 'str | None' = Field(
        default=None,
    )
    """University name."""
    university_group_id: 'int | None' = Field(
        default=None,
    )
    """Property `UserFull.university_group_id`."""
    faculty: 'int | None' = Field(
        default=None,
    )
    """Faculty ID."""
    faculty_name: 'str | None' = Field(
        default=None,
    )
    """Faculty name."""
    graduation: 'int | None' = Field(
        default=None,
    )
    """Graduation year."""
    education_form: 'str | None' = Field(
        default=None,
    )
    """Education form."""
    education_status: 'str | None' = Field(
        default=None,
    )
    """User\'s education status."""
    home_town: 'str | None' = Field(
        default=None,
    )
    """User hometown."""
    relation: "UserRelation | None" = Field(
        default=None,
    )
    """User relationship status."""
    relation_partner: "UserMin | None" = Field(
        default=None,
    )
    """Property `UserFull.relation_partner`."""
    personal: "Personal | None" = Field(
        default=None,
    )
    """Property `UserFull.personal`."""
    universities: 'list["UsersUniversity"] | None' = Field(
        default=None,
    )
    """Property `UserFull.universities`."""
    schools: 'list["UsersSchool"] | None' = Field(
        default=None,
    )
    """Property `UserFull.schools`."""
    relatives: 'list["Relative"] | None' = Field(
        default=None,
    )
    """Property `UserFull.relatives`."""
    is_subscribed_podcasts: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""
    can_subscribe_podcasts: 'bool | None' = Field(
        default=None,
    )
    """Owner in whitelist or not."""
    can_subscribe_posts: 'bool | None' = Field(
        default=None,
    )
    """Can subscribe to wall."""
    counters: "UserCounters | None" = Field(
        default=None,
    )
    """Property `UserFull.counters`."""
    access_key: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.access_key`."""
    can_upload_doc: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.can_upload_doc`."""
    can_ban: 'bool | None' = Field(
        default=None,
    )
    """Information whether the user can be baned (added to black list) by me."""
    hash: 'str | None' = Field(
        default=None,
    )
    """Property `UserFull.hash`."""
    is_no_index: 'bool | None' = Field(
        default=None,
    )
    """Access to user profile is restricted for search engines."""
    contact_id: 'int | None' = Field(
        default=None,
    )
    """Contact person ID."""
    is_message_request: 'bool | None' = Field(
        default=None,
    )
    """Property `UserFull.is_message_request`."""
    descriptions: 'list[str] | None' = Field(
        default=None,
    )
    """Property `UserFull.descriptions`."""
    lists: 'list[int] | None' = Field(
        default=None,
    )
    """Property `UserFull.lists`."""
    photo_max_size: 'Photo | None' = None


class UserXtrType(UserFull):
    """Model: `UserXtrType`"""

    type: "UserType | None" = Field(
        default=None,
    )
    """Property `UserXtrType.type`."""


class UserXtrInvitedBy(UserXtrType):
    """Model: `UserXtrInvitedBy`"""

    invited_by: int | None = Field(
        default=None,
    )
    """ID of the inviter."""

    name: str | None = Field(
        default=None,
    )
    """Name of group."""

    type: "UserTypeForXtrInvitedBy | None" = Field(
        default=None,
    )
    """Property `UserXtrInvitedBy.type`."""


class GetConversationByIdExtended(GetConversationById):
    """Model: `GetConversationByIdExtended`"""

    profiles: list["UserFull"] | None = Field(
        default=None,
    )
    """Property `GetConversationByIdExtended.profiles`."""

    groups: list["GroupFull"] | None = Field(
        default=None,
    )
    """Property `GetConversationByIdExtended.groups`."""


class Message(BaseMessage):
    """Model: `Message`"""
    important: 'bool | None' = Field(
        default=None,
    )
    """Is it an important message."""
    is_hidden: 'bool | None' = Field(
        default=None,
    )
    """Property `Message.is_hidden`."""
    members_count: 'int | None' = Field(
        default=None,
    )
    """Members number."""
    reaction_id: 'int | None' = Field(
        default=None,
    )
    """Reaction id set on message."""
    reactions: 'list["ReactionCounterResponseItem"] | None' = Field(
        default=None,
    )
    """Actual reactions counters on this message."""
    last_reaction_id: 'int | None' = Field(
        default=None,
    )
    """Last reaction id set on this message."""
    is_pinned: 'bool | None' = Field(
        default=None,
    )
    """Is message pinned in its conversation."""
    was_listened: 'bool | None' = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""
    pinned_at: 'int | None' = Field(
        default=None,
    )
    """Date when the message has been pinned in Unixtime."""
    attachments: 'list[MessageAttachment] | None' = None
    reply_message: 'ForeignMessage | None' = None
    fwd_messages: 'list[ForeignMessage] | None' = None


class UserSettings(UserMin, UserSettingsXtr):
    """Model: `UserSettings`"""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""

    is_service_account: bool | None = Field(
        default=None,
    )
    """flag about service account."""


class StatsAge(DemographicStatsPeriodItemBase):
    """Model: `StatsAge`"""

    value: str | None = Field(
        default=None,
    )
    """Age interval."""


class StatsCities(DemographicStatsPeriodItemBase):
    """Model: `StatsCities`"""

    name: str | None = Field(
        default=None,
    )
    """City name."""

    value: int | str | None = Field(
        default=None,
    )
    """City ID."""


class StatsSex(DemographicStatsPeriodItemBase):
    """Model: `StatsSex`"""

    value: "StatsSexValue | None" = Field(
        default=None,
    )
    """Property `StatsSex.value`."""


class AdsStatsSexAge(DemographicStatsPeriodItemBase):
    """Model: `AdsStatsSexAge`"""

    value: str | None = Field(
        default=None,
    )
    """Sex and age interval."""


class TargSettings(Criteria):
    """Model: `TargSettings`"""

    id: str | None = Field(
        default=None,
    )
    """Ad ID."""

    campaign_id: str | None = Field(
        default=None,
    )
    """Campaign ID."""


class App(AppMin):
    """Model: `App`"""
    author_url: 'str | None' = Field(
        default=None,
    )
    """Application author\'s URL."""
    banner_1120: 'str | None' = Field(
        default=None,
    )
    """URL of the app banner with 1120 px in width."""
    banner_560: 'str | None' = Field(
        default=None,
    )
    """URL of the app banner with 560 px in width."""
    icon_16: 'str | None' = Field(
        default=None,
    )
    """URL of the app icon with 16 px in width."""
    is_new: 'bool | None' = Field(
        default=None,
    )
    """Is new flag."""
    push_enabled: 'bool | None' = Field(
        default=None,
    )
    """Is push enabled."""
    friends: 'list[int] | None' = Field(
        default=None,
    )
    """Property `App.friends`."""
    catalog_position: 'int | None' = Field(
        default=None,
    )
    """Catalog position."""
    description: 'str | None' = Field(
        default=None,
    )
    """Application description."""
    genre: 'str | None' = Field(
        default=None,
    )
    """Genre name."""
    genre_id: 'int | None' = Field(
        default=None,
    )
    """Genre ID."""
    international: 'bool | None' = Field(
        default=None,
    )
    """Information whether the application is multilanguage."""
    is_in_catalog: 'int | None' = Field(
        default=None,
    )
    """Information whether application is in mobile catalog."""
    leaderboard_type: "AppLeaderboardType | None" = Field(
        default=None,
    )
    """Property `App.leaderboard_type`."""
    members_count: 'int | None' = Field(
        default=None,
    )
    """Members number."""
    platform_id: 'str | None' = Field(
        default=None,
    )
    """Application ID in store."""
    published_date: 'datetime.datetime | None' = Field(
        default=None,
    )
    """Date when the application has been published in Unixtime."""
    screen_name: 'str | None' = Field(
        default=None,
    )
    """Screen name."""
    section: 'str | None' = Field(
        default=None,
    )
    """Application section name."""
    id: 'int | None' = None
    type: 'str | None' = None


class CallbackForeignMessage(ForeignMessage):
    """Model: `CallbackForeignMessage`"""

    is_cropped: bool | None = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.is_cropped`."""

    fwd_messages: list["CallbackForeignMessage"] | None = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.fwd_messages`."""

    reply_message: "CallbackForeignMessage | None" = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.reply_message`."""


class CallbackMessage(Message):
    """Model: `CallbackMessage`"""

    influence_score: float | None = Field(
        default=None,
    )
    """Property `CallbackMessage.influence_score`."""

    reply_message: "CallbackForeignMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessage.reply_message`."""

    fwd_messages: "CallbackFwdMessages | None" = Field(
        default=None,
    )
    """Property `CallbackMessage.fwd_messages`."""


class PhotoComment(WallComment):
    """Model: `PhotoComment`"""

    photo_owner_id: int = Field()
    """Property `PhotoComment.photo_owner_id`."""


class VideoComment(WallComment):
    """Model: `VideoComment`"""

    video_owner_id: int | None = Field(
        default=None,
    )
    """Property `VideoComment.video_owner_id`."""


class Confirmation(Base):
    """Model: `Confirmation`"""

    type: str | None = Field(
        default=None,
    )
    """Property `Confirmation.type`."""


class DatabaseCity(BaseObject):
    """Model: `DatabaseCity`"""

    area: str | None = Field(
        default=None,
    )
    """Area title."""

    region: str | None = Field(
        default=None,
    )
    """Region title."""

    important: bool | None = Field(
        default=None,
    )
    """Information whether the city is included in important cities list."""


class GroupFull(Group, MarketProperties):
    """Model: `GroupFull`"""

    member_status: "GroupFullMemberStatus | None" = Field(
        default=None,
    )
    """Current user\'s member status."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Information whether community is adult."""

    is_hidden_from_feed: bool | None = Field(
        default=None,
    )
    """Information whether community is hidden from current user\'s newsfeed."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether community is in faves."""

    is_subscribed: bool | None = Field(
        default=None,
    )
    """Information whether current user is subscribed."""

    city: "BaseObject | None" = Field(
        default=None,
    )
    """Property `GroupFull.city`."""

    description: str | None = Field(
        default=None,
    )
    """Community description."""

    wiki_page: str | None = Field(
        default=None,
    )
    """Community\'s main wiki page title."""

    members_count: int | None = Field(
        default=None,
    )
    """Community members number."""

    members_count_text: str | None = Field(
        default=None,
    )
    """Info about number of users in group."""

    requests_count: int | None = Field(
        default=None,
    )
    """The number of incoming requests to the community."""

    video_live_level: int | None = Field(
        default=None,
    )
    """Community level live streams achievements."""

    video_live_count: int | None = Field(
        default=None,
    )
    """Number of community\'s live streams."""

    clips_count: int | None = Field(
        default=None,
    )
    """Number of community\'s clips."""

    counters: "CountersGroup | None" = Field(
        default=None,
    )
    """Property `GroupFull.counters`."""

    textlives_count: int | None = Field(
        default=None,
    )
    """Textlives number."""

    cover: "OwnerCover | None" = Field(
        default=None,
    )
    """Property `GroupFull.cover`."""

    video_cover: "OwnerCover | None" = Field(
        default=None,
    )
    """Property `GroupFull.video_cover`."""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can post on community\'s wall."""

    can_suggest: bool | None = Field(
        default=None,
    )
    """Property `GroupFull.can_suggest`."""

    can_upload_story: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload story."""

    can_call_to_community: bool | None = Field(
        default=None,
    )
    """Information whether current user can call to community."""

    can_upload_doc: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload doc."""

    can_upload_video: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload video."""

    can_upload_clip: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload clip."""

    can_see_all_posts: bool | None = Field(
        default=None,
    )
    """Information whether current user can see all posts on community\'s wall."""

    can_create_topic: bool | None = Field(
        default=None,
    )
    """Information whether current user can create topic."""

    activity: str | None = Field(
        default=None,
    )
    """Type of group, start date of event or category of public page."""

    fixed_post: int | None = Field(
        default=None,
    )
    """Fixed post ID."""

    has_photo: bool | None = Field(
        default=None,
    )
    """Information whether community has photo."""

    crop_photo: "CropPhoto | None" = Field(
        default=None,
    )
    """Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества."""

    status: str | None = Field(
        default=None,
    )
    """Community status."""

    status_audio: "Audio | None" = Field(
        default=None,
    )
    """Property `GroupFull.status_audio`."""

    main_album_id: int | None = Field(
        default=None,
    )
    """Community\'s main photo album ID."""

    links: list["LinksItem"] | None = Field(
        default=None,
    )
    """Property `GroupFull.links`."""

    contacts: list["ContactsItem"] | None = Field(
        default=None,
    )
    """Property `GroupFull.contacts`."""

    wall: int | None = Field(
        default=None,
    )
    """Information about wall status in community."""

    site: str | None = Field(
        default=None,
    )
    """Community\'s website."""

    main_section: "GroupFullSection | None" = Field(
        default=None,
    )
    """Property `GroupFull.main_section`."""

    secondary_section: "GroupFullSection | None" = Field(
        default=None,
    )
    """Property `GroupFull.secondary_section`."""

    trending: bool | None = Field(
        default=None,
    )
    """Information whether the community has a \"fire\" pictogram.."""

    can_message: bool | None = Field(
        default=None,
    )
    """Information whether current user can send a message to community."""

    is_messages_blocked: bool | None = Field(
        default=None,
    )
    """Information whether community can send a message to current user."""

    can_send_notify: bool | None = Field(
        default=None,
    )
    """Information whether community can send notifications by phone number to current user."""

    online_status: "OnlineStatus | None" = Field(
        default=None,
    )
    """Status of replies in community messages."""

    invited_by: int | None = Field(
        default=None,
    )
    """Inviter ID."""

    age_limits: "GroupFullAgeLimits | None" = Field(
        default=None,
    )
    """Information whether age limit."""

    ban_info: "GroupBanInfo | None" = Field(
        default=None,
    )
    """User ban info."""

    has_group_channel: bool | None = Field(
        default=None,
    )
    """Property `GroupFull.has_group_channel`."""

    addresses: "AddressesInfo | None" = Field(
        default=None,
    )
    """Info about addresses in groups."""

    is_subscribed_podcasts: bool | None = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""

    can_subscribe_podcasts: bool | None = Field(
        default=None,
    )
    """Owner in whitelist or not."""

    can_subscribe_posts: bool | None = Field(
        default=None,
    )
    """Can subscribe to wall."""

    live_covers: "LiveCovers | None" = Field(
        default=None,
    )
    """Live covers state."""

    stories_archive_count: int | None = Field(
        default=None,
    )
    """Property `GroupFull.stories_archive_count`."""

    has_unseen_stories: bool | None = Field(
        default=None,
    )
    """Property `GroupFull.has_unseen_stories`."""

    video_notifications_status: str | None = Field(
        default=None,
    )
    """Information about the status of video notifications for the current user.."""

    videos_count: int | None = Field(
        default=None,
    )
    """Community videos number."""


class MarketItemBasicWithGroup(MarketItemBasic):
    """Model: `MarketItemBasicWithGroup`"""

    is_group_verified: bool | None = Field(
        default=None,
    )
    """Property `MarketItemBasicWithGroup.is_group_verified`."""

    group_name: str | None = Field(
        default=None,
    )
    """Property `MarketItemBasicWithGroup.group_name`."""

    group_link: str | None = Field(
        default=None,
    )
    """Property `MarketItemBasicWithGroup.group_link`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `MarketItemBasicWithGroup.is_owner`."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Property `MarketItemBasicWithGroup.is_adult`."""


class MarketItemFull(MarketItem):
    """Model: `MarketItemFull`"""
    albums_ids: 'list[int] | None' = Field(
        default=None,
    )
    """Property `MarketItemFull.albums_ids`."""
    can_comment: 'bool | None' = Field(
        default=None,
    )
    """Information whether current use can comment the item."""
    show_comments: 'bool | None' = Field(
        default=None,
    )
    """Information about whether to show the comments tab."""
    can_repost: 'bool | None' = Field(
        default=None,
    )
    """Information whether current use can repost the item."""
    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `MarketItemFull.likes`."""
    reposts: "RepostsInfo | None" = Field(
        default=None,
    )
    """Property `MarketItemFull.reposts`."""
    views_count: 'int | None' = Field(
        default=None,
    )
    """Views number."""
    wishlist_item_id: 'int | None' = Field(
        default=None,
    )
    """Object identifier in wishlist of viewer."""
    rating: 'float | None' = Field(
        default=None,
    )
    """Rating of product."""
    orders_count: 'int | None' = Field(
        default=None,
    )
    """Count of product orders."""
    cancel_info: "Link | None" = Field(
        default=None,
    )
    """Information for cancel and revert order."""
    user_agreement_info: 'str | None' = Field(
        default=None,
    )
    """User agreement info."""
    ad_id: 'int | None' = Field(
        default=None,
    )
    """Contains ad ID if it has."""
    owner_info: "ItemOwnerInfo | None" = Field(
        default=None,
    )
    """Information about the group where the item is placed."""
    can_edit: 'bool | None' = Field(
        default=None,
    )
    """Can the item be updated by current user?."""
    can_delete: 'bool | None' = Field(
        default=None,
    )
    """Can item be deleted by current user?."""
    can_recover: 'bool | None' = Field(
        default=None,
    )
    """Can item be restored by current user?."""
    can_show_convert_to_service: 'bool | None' = Field(
        default=None,
    )
    """Can the item be converted from a product into a service?."""
    promotion: "ItemPromotionInfo | None" = Field(
        default=None,
    )
    """Information about promotion of the item."""
    vk_pay_discount: 'int | None' = Field(
        default=None,
    )
    """The amount of the discount if VK Pay is used for payment."""
    photos: 'Photo | None' = None


class RequestsXtrMutual(UserFull):
    """Model: `RequestsXtrMutual`"""

    user_id: int = Field()
    """User ID."""

    id: int | None = Field(
        default=None,
    )
    """User ID."""

    from_: str | None = Field(
        default=None,
        alias="from",
    )
    """ID of the user by whom friend has been suggested."""

    mutual: "RequestsMutual | None" = Field(
        default=None,
    )
    """Property `RequestsXtrMutual.mutual`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `RequestsXtrMutual.track_code`."""

    message: str | None = Field(
        default=None,
    )
    """Message sent with a request."""

    timestamp: int | None = Field(
        default=None,
    )
    """Request timestamp."""

    descriptions: list[str] | None = Field(
        default=None,
    )
    """Property `RequestsXtrMutual.descriptions`."""


class FriendExtendedStatus(FriendStatus):
    """Model: `FriendExtendedStatus`"""

    is_request_unread: bool | None = Field(
        default=None,
    )
    """Is friend request from other user unread."""


class RequestsXtrMessage(RequestsXtrMutual):
    """Model: `RequestsXtrMessage`"""

    message: str | None = Field(
        default=None,
    )
    """Message sent with a request."""


class VideoImage(BaseImage):
    """Model: `VideoImage`"""

    with_padding: "PropertyExists | None" = Field(
        default=None,
    )
    """Property `VideoImage.with_padding`."""

    size: str | None = Field(
        default=None,
    )
    """Property `VideoImage.size`."""


class VideoAlbumFull(VideoAlbum):
    """Model: `VideoAlbumFull`"""

    count: int = Field()
    """Total number of videos in album."""

    updated_time: int = Field()
    """Date when the album has been updated last time in Unixtime."""

    image: list["VideoImage"] | None = Field(
        default=None,
    )
    """Album cover image in different sizes."""

    image_blur: "PropertyExists | None" = Field(
        default=None,
    )
    """Need blur album thumb or not."""

    is_system: "PropertyExists | None" = Field(
        default=None,
    )
    """Information whether album is system."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Is user can edit playlist."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Is user can delete playlist."""

    can_upload: bool | None = Field(
        default=None,
    )
    """Is user can upload video to playlist."""


class VideoFull(Video):
    """Model: `VideoFull`"""
    files: "VideoFiles | None" = Field(
        default=None,
    )
    """Property `VideoFull.files`."""
    trailer: "VideoFiles | None" = Field(
        default=None,
    )
    """Property `VideoFull.trailer`."""
    episodes: 'list["Episode"] | None' = Field(
        default=None,
    )
    """List of video episodes with timecodes."""
    live_settings: "LiveSettings | None" = Field(
        default=None,
    )
    """Settings for live stream."""
    type: 'VideoType | None' = None


class WallpostFull(CarouselBase, Wallpost):
    """Model: `WallpostFull`"""
    copy_history: 'list["WallpostFull"] | None' = Field(
        default=None,
    )
    """Property `WallpostFull.copy_history`."""
    can_edit: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can edit the post."""
    created_by: 'int | None' = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""
    can_delete: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can delete the post."""
    can_pin: 'bool | None' = Field(
        default=None,
    )
    """Information whether current user can pin the post."""
    donut: "WallpostDonut | None" = Field(
        default=None,
    )
    """Property `WallpostFull.donut`."""
    is_pinned: 'bool | None' = Field(
        default=None,
    )
    """Information whether the post is pinned."""
    comments: "CommentsInfo | None" = Field(
        default=None,
    )
    """Property `WallpostFull.comments`."""
    marked_as_ads: 'bool | None' = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""
    topic_id: 'int | None' = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""
    short_text_rate: 'float | None' = Field(
        default=None,
    )
    """Preview length control parameter."""
    hash: 'str | None' = Field(
        default=None,
    )
    """Hash for sharing."""
    type: "PostType | None" = Field(
        default=None,
    )
    """Property `WallpostFull.type`."""
    feedback: "ItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `WallpostFull.feedback`."""
    to_id: 'int | None' = Field(
        default=None,
    )
    """Property `WallpostFull.to_id`."""
    inner_type: 'WallpostInnerType | None' = None


class CommentsBase(CommentsInfo):
    """Model: `CommentsBase`"""

    list_: list["WallComment"] | None = Field(
        default=None,
        alias="list",
    )
    """Property `CommentsBase.list`."""


class CommentsItemTypeMarket(MarketItem, CommentsItemBase):
    """Model: `CommentsItemTypeMarket`"""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeMarket.comments`."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeMarket.likes`."""


class CommentsItemTypeNotes(CommentsItemBase):
    """Model: `CommentsItemTypeNotes`"""

    text: str | None = Field(
        default=None,
    )
    """Property `CommentsItemTypeNotes.text`."""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeNotes.comments`."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeNotes.likes`."""


class CommentsItemTypePhoto(Photo, CommentsItemBase):
    """Model: `CommentsItemTypePhoto`"""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypePhoto.comments`."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypePhoto.likes`."""


class CommentsItemTypePost(WallpostFull, CommentsItemBase):
    """Model: `CommentsItemTypePost`"""

    from_id: int | None = Field(
        default=None,
    )
    """Property `CommentsItemTypePost.from_id`."""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypePost.comments`."""


class CommentsItemTypeTopic(CommentsItemBase):
    """Model: `CommentsItemTypeTopic`"""

    text: str | None = Field(
        default=None,
    )
    """Property `CommentsItemTypeTopic.text`."""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeTopic.comments`."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeTopic.likes`."""


class CommentsItemTypeVideo(Video, CommentsItemBase):
    """Model: `CommentsItemTypeVideo`"""

    text: str | None = Field(
        default=None,
    )
    """Property `CommentsItemTypeVideo.text`."""

    comments: "CommentsBase | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeVideo.comments`."""

    likes: "Likes | None" = Field(
        default=None,
    )
    """Property `CommentsItemTypeVideo.likes`."""

    type: str | None = Field(
        default=None,
    )
    """Property `CommentsItemTypeVideo.type`."""


class ItemAudio(ItemBase):
    """Model: `ItemAudio`"""

    audio: "ItemAudioAudio | None" = Field(
        default=None,
    )
    """Property `ItemAudio.audio`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class ItemDigest(ItemBase):
    """Model: `ItemDigest`"""

    feed_id: str | None = Field(
        default=None,
    )
    """id of feed in digest."""

    items: list["ItemDigestItem"] | None = Field(
        default=None,
    )
    """Property `ItemDigest.items`."""

    main_post_ids: list[str] | None = Field(
        default=None,
    )
    """Property `ItemDigest.main_post_ids`."""

    template: str | None = Field(
        default=None,
    )
    """type of digest."""

    header: "ItemDigestHeader | None" = Field(
        default=None,
    )
    """Property `ItemDigest.header`."""

    footer: "ItemDigestFooter | None" = Field(
        default=None,
    )
    """Property `ItemDigest.footer`."""


class ItemDigestFullItem(ItemBase):
    """Model: `ItemDigestFullItem`"""

    inner_type: str = Field()
    """Property `ItemDigestFullItem.inner_type`."""

    post: "ItemWallpost" = Field()
    """Property `ItemDigestFullItem.post`."""

    text: str | None = Field(
        default=None,
    )
    """Property `ItemDigestFullItem.text`."""

    source_name: str | None = Field(
        default=None,
    )
    """Property `ItemDigestFullItem.source_name`."""

    attachment_index: int | None = Field(
        default=None,
    )
    """Property `ItemDigestFullItem.attachment_index`."""

    attachment: "WallpostAttachment | None" = Field(
        default=None,
    )
    """Property `ItemDigestFullItem.attachment`."""

    style: str | None = Field(
        default=None,
    )
    """Property `ItemDigestFullItem.style`."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class ItemFriend(ItemBase):
    """Model: `ItemFriend`"""

    friends: "ItemFriendFriends | None" = Field(
        default=None,
    )
    """Property `ItemFriend.friends`."""


class ItemPhoto(CarouselBase, ItemBase):
    """Model: `ItemPhoto`"""

    photos: "ItemPhotoPhotos | None" = Field(
        default=None,
    )
    """Property `ItemPhoto.photos`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class ItemPhotoTag(CarouselBase, ItemBase):
    """Model: `ItemPhotoTag`"""

    photo_tags: "ItemPhotoTagPhotoTags | None" = Field(
        default=None,
    )
    """Property `ItemPhotoTag.photo_tags`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class ItemPromoButton(ItemBase):
    """Model: `ItemPromoButton`"""

    text: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButton.text`."""

    title: str | None = Field(
        default=None,
    )
    """Property `ItemPromoButton.title`."""

    action: "ItemPromoButtonAction | None" = Field(
        default=None,
    )
    """Property `ItemPromoButton.action`."""

    images: list["ItemPromoButtonImage"] | None = Field(
        default=None,
    )
    """Property `ItemPromoButton.images`."""


class ItemTopic(ItemBase):
    """Model: `ItemTopic`"""

    post_id: int = Field()
    """Topic post ID."""

    text: str = Field()
    """Post text."""

    comments: "CommentsInfo | None" = Field(
        default=None,
    )
    """Property `ItemTopic.comments`."""

    likes: "LikesInfo | None" = Field(
        default=None,
    )
    """Property `ItemTopic.likes`."""


class ItemVideo(CarouselBase, ItemBase):
    """Model: `ItemVideo`"""

    video: "ItemVideoVideo | None" = Field(
        default=None,
    )
    """Property `ItemVideo.video`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class ItemWallpost(ItemBase, WallpostFull):
    """Model: `ItemWallpost`"""


class ListFull(NewsfeedList):
    """Model: `ListFull`"""

    no_reposts: bool | None = Field(
        default=None,
    )
    """Information whether reposts hiding is enabled."""

    source_ids: list[int] | None = Field(
        default=None,
    )
    """Property `ListFull.source_ids`."""


__all__ = (
    "AccessRole",
    "AccessRolePublic",
    "Accesses",
    "Account",
    "AccountCounters",
    "AccountInfo",
    "AccountPushSettings",
    "AccountType",
    "ActionOneOf",
    "Activity",
    "Ad",
    "AdApproved",
    "AdCostType",
    "AdLayout",
    "AdStatus",
    "AddCompanyGroupsMembersError",
    "Address",
    "AddressFields",
    "AddressTimetable",
    "AddressTimetableDay",
    "AddressWorkInfoStatus",
    "AddressesInfo",
    "AdsCategory",
    "AdsStats",
    "AdsStatsSexAge",
    "Amount",
    "AmountItem",
    "Answer",
    "AnswerItem",
    "AnswerOneOf",
    "App",
    "AppFields",
    "AppLeaderboardType",
    "AppMin",
    "AppPost",
    "AppType",
    "AppWidgetsPhoto",
    "AttachedNote",
    "Attachment",
    "AttachmentType",
    "Audio",
    "AudioMessage",
    "Background",
    "BackgroundType",
    "BanInfo",
    "BanInfoReason",
    "Base",
    "BaseCity",
    "BaseCountry",
    "BaseGeo",
    "BaseImage",
    "BaseMessage",
    "BaseObject",
    "Bookmark",
    "BookmarkType",
    "BoolInt",
    "Bugreport",
    "BugreportSubscribeState",
    "Button",
    "ButtonAction",
    "ButtonOneOf",
    "ButtonPayload",
    "CallbackAppPayload",
    "CallbackAudioNew",
    "CallbackBoardPostDelete",
    "CallbackBoardPostEdit",
    "CallbackBoardPostNew",
    "CallbackBoardPostRestore",
    "CallbackDonutMoneyWithdraw",
    "CallbackDonutMoneyWithdrawError",
    "CallbackDonutSubscriptionCancelled",
    "CallbackDonutSubscriptionCreate",
    "CallbackDonutSubscriptionExpired",
    "CallbackDonutSubscriptionPriceChanged",
    "CallbackDonutSubscriptionProlonged",
    "CallbackForeignMessage",
    "CallbackFwdMessages",
    "CallbackGroupChangePhoto",
    "CallbackGroupChangeSettings",
    "CallbackGroupJoin",
    "CallbackGroupLeave",
    "CallbackGroupOfficersEdit",
    "CallbackMarketCommentDelete",
    "CallbackMessage",
    "CallbackMessageAllow",
    "CallbackMessageDeny",
    "CallbackMessageEvent",
    "CallbackMessageNew",
    "CallbackMessageObject",
    "CallbackMessageReactionEvent",
    "CallbackMessageRead",
    "CallbackMessageTypingState",
    "CallbackPhotoCommentDelete",
    "CallbackPhotoNew",
    "CallbackPollVoteNew",
    "CallbackServer",
    "CallbackServerStatus",
    "CallbackSettings",
    "CallbackType",
    "CallbackUserBlock",
    "CallbackUserUnblock",
    "CallbackVideoCommentDelete",
    "CallbackVideoNew",
    "CallbackVkpayTransaction",
    "CallbackWallPostNew",
    "CallbackWallReplyEdit",
    "CallbackWallReplyNew",
    "CallbackWallReplyRestore",
    "CallbackWallRepost",
    "CallsCall",
    "Campaign",
    "CampaignStatus",
    "CampaignType",
    "Career",
    "CarouselBase",
    "CatalogList",
    "Chat",
    "ChatFull",
    "ChatPreview",
    "ChatPushSettings",
    "ChatRestrictions",
    "ChatSettings",
    "ChatSettingsAcl",
    "ChatSettingsPermissions",
    "ChatSettingsPermissionsCall",
    "ChatSettingsPermissionsChangeAdmins",
    "ChatSettingsPermissionsChangeInfo",
    "ChatSettingsPermissionsChangePin",
    "ChatSettingsPermissionsInvite",
    "ChatSettingsPermissionsSeeInviteLink",
    "ChatSettingsPermissionsUseMassMentions",
    "ChatSettingsPhoto",
    "ChatSettingsState",
    "CityById",
    "ClickableArea",
    "ClickableSticker",
    "ClickableStickerStyle",
    "ClickableStickerSubtype",
    "ClickableStickerType",
    "ClickableStickers",
    "Client",
    "ClipItem",
    "ClipItemLink",
    "Comment",
    "CommentAttachment",
    "CommentAttachmentType",
    "CommentAuthor",
    "CommentMedia",
    "CommentMediaType",
    "CommentReplies",
    "CommentRepliesItem",
    "CommentThread",
    "CommentsBase",
    "CommentsFilters",
    "CommentsInfo",
    "CommentsItem",
    "CommentsItemBase",
    "CommentsItemTypeMarket",
    "CommentsItemTypeNotes",
    "CommentsItemTypePhoto",
    "CommentsItemTypePost",
    "CommentsItemTypeTopic",
    "CommentsItemTypeVideo",
    "CompanyMember",
    "CompanyMemberProduct",
    "Confirmation",
    "ContactsItem",
    "Conversation",
    "ConversationCanWrite",
    "ConversationMember",
    "ConversationPeer",
    "ConversationPeerType",
    "ConversationSortId",
    "ConversationSpecialServiceType",
    "ConversationWithMessage",
    "CountersFilter",
    "CountersGroup",
    "Country",
    "CreateAdStatus",
    "CreateCampaignStatus",
    "CreateClientsStatus",
    "Criteria",
    "CriteriaSex",
    "CropPhoto",
    "CropPhotoCrop",
    "CropPhotoRect",
    "Currency",
    "CustomSnippet",
    "CustomSnippetButton",
    "DatabaseCitiesFields",
    "DatabaseCity",
    "DatabaseSchool",
    "DatabaseUniversity",
    "DefaultOrder",
    "DeleteFullResponseItem",
    "DemoStats",
    "DemographicStatsPeriodItemBase",
    "DemostatsFormat",
    "Doc",
    "DocAttachmentType",
    "DocPreview",
    "DocPreviewAudioMsg",
    "DocPreviewGraffiti",
    "DocPreviewPhoto",
    "DocPreviewPhotoSizes",
    "DocPreviewVideo",
    "DocTypes",
    "DomainResolved",
    "DomainResolvedType",
    "DonatorSubscriptionInfo",
    "DonatorSubscriptionInfoStatus",
    "EndState",
    "Episode",
    "Error",
    "ErrorInnerType",
    "EventsEventAttach",
    "EventsRetargetingGroup",
    "Exports",
    "Faculty",
    "FeedItem",
    "FeedItemType",
    "Feedback",
    "FieldsVoters",
    "Filter",
    "FloodStats",
    "FloodStatsByUserItem",
    "ForeignMessage",
    "Form",
    "Forward",
    "Friend",
    "FriendExtendedStatus",
    "FriendStatus",
    "FriendStatusStatus",
    "FriendsList",
    "Geo",
    "GeoCoordinates",
    "GeoType",
    "GetConversationById",
    "GetConversationByIdExtended",
    "GetConversationMembers",
    "GetFilter",
    "GetInviteLinkByOwnerResponseItem",
    "Gift",
    "GiftPrivacy",
    "GiveEventStickerItem",
    "GlobalSearchFilters",
    "GradientPoint",
    "Group",
    "GroupAccess",
    "GroupAdminLevel",
    "GroupAgeLimits",
    "GroupAttach",
    "GroupAudio",
    "GroupBanInfo",
    "GroupCategory",
    "GroupCategoryFull",
    "GroupCategoryType",
    "GroupDocs",
    "GroupFull",
    "GroupFullAgeLimits",
    "GroupFullMemberStatus",
    "GroupFullSection",
    "GroupIsClosed",
    "GroupJoinType",
    "GroupMarket",
    "GroupMarketCurrency",
    "GroupOfficerRole",
    "GroupPhotos",
    "GroupPublicCategoryList",
    "GroupRole",
    "GroupSettingsChanges",
    "GroupSettingsChangesIntegerValues",
    "GroupSettingsChangesStringValues",
    "GroupSubcategory",
    "GroupSubject",
    "GroupSuggestedPrivacy",
    "GroupTag",
    "GroupTagColor",
    "GroupTopics",
    "GroupType",
    "GroupVideo",
    "GroupWall",
    "GroupWiki",
    "GroupsArray",
    "GroupsFields",
    "Hint",
    "HintSection",
    "HintType",
    "HistoryAttachment",
    "HistoryMessageAttachment",
    "HistoryMessageAttachmentType",
    "IgnoreItemType",
    "Image",
    "ImageTheme",
    "ImageType",
    "InfoForBots",
    "ItemAudio",
    "ItemAudioAudio",
    "ItemBase",
    "ItemDigest",
    "ItemDigestButton",
    "ItemDigestButtonStyle",
    "ItemDigestFooter",
    "ItemDigestFooterStyle",
    "ItemDigestFullItem",
    "ItemDigestHeader",
    "ItemDigestHeaderStyle",
    "ItemDigestItem",
    "ItemFriend",
    "ItemFriendFriends",
    "ItemHolidayRecommendationsBlockHeader",
    "ItemOwnerInfo",
    "ItemPhoto",
    "ItemPhotoPhotos",
    "ItemPhotoTag",
    "ItemPhotoTagPhotoTags",
    "ItemPromoButton",
    "ItemPromoButtonAction",
    "ItemPromoButtonImage",
    "ItemPromotionInfo",
    "ItemTopic",
    "ItemVideo",
    "ItemVideoVideo",
    "ItemWallpost",
    "ItemWallpostFeedback",
    "ItemWallpostFeedbackAnswer",
    "ItemWallpostFeedbackType",
    "Keyboard",
    "KeyboardButton",
    "KeyboardButtonActionCallback",
    "KeyboardButtonActionCallbackType",
    "KeyboardButtonActionLocation",
    "KeyboardButtonActionLocationType",
    "KeyboardButtonActionOpenApp",
    "KeyboardButtonActionOpenAppType",
    "KeyboardButtonActionOpenLink",
    "KeyboardButtonActionOpenLinkType",
    "KeyboardButtonActionOpenPhoto",
    "KeyboardButtonActionOpenPhotoType",
    "KeyboardButtonActionText",
    "KeyboardButtonActionTextType",
    "KeyboardButtonActionVkpay",
    "KeyboardButtonActionVkpayType",
    "KeyboardButtonColor",
    "KeyboardButtonPropertyAction",
    "Lang",
    "LanguageFull",
    "LastActivity",
    "LastSeen",
    "LastShortenedLink",
    "Layout",
    "Lead",
    "LeadFormsAnswer",
    "Leaderboard",
    "Level",
    "LikeAddRemove",
    "LikeAddRemoveObjectType",
    "Likes",
    "LikesInfo",
    "LikesType",
    "Link",
    "LinkApplication",
    "LinkApplicationStore",
    "LinkButton",
    "LinkButtonAction",
    "LinkButtonActionType",
    "LinkButtonStyle",
    "LinkChecked",
    "LinkCheckedStatus",
    "LinkNoProduct",
    "LinkProduct",
    "LinkProductCategory",
    "LinkProductStatus",
    "LinkProductType",
    "LinkRating",
    "LinkRatingType",
    "LinkStats",
    "LinkStatsExtended",
    "LinkStatus",
    "LinkTargetObject",
    "LinksItem",
    "ListFull",
    "LiveCategory",
    "LiveCovers",
    "LiveInfo",
    "LiveSettings",
    "LongPollEvents",
    "LongPollServer",
    "LongPollSettings",
    "LongpollMessages",
    "LongpollParams",
    "LookalikeRequest",
    "LookalikeRequestSaveAudienceLevel",
    "LookalikeRequestSourceType",
    "LookalikeRequestStatus",
    "MarketAlbum",
    "MarketCategoryInnerType",
    "MarketCategoryNested",
    "MarketCategoryNestedInnerType",
    "MarketCategoryTree",
    "MarketCategoryTreeView",
    "MarketCategoryTreeViewType",
    "MarketComment",
    "MarketInfo",
    "MarketItem",
    "MarketItemAvailability",
    "MarketItemBasic",
    "MarketItemBasicWithGroup",
    "MarketItemFull",
    "MarketMarketCategory",
    "MarketOrder",
    "MarketProperties",
    "MarketState",
    "MemberRole",
    "MemberRolePermission",
    "MemberRoleStatus",
    "MemberStatus",
    "MemberStatusFull",
    "Message",
    "MessageAction",
    "MessageActionPhoto",
    "MessageActionStatus",
    "MessageAttachment",
    "MessageAttachmentType",
    "MessageError",
    "MessageRequestData",
    "MessageTypingStateState",
    "MessagesArray",
    "MessagesFwdMessages",
    "MessagesGraffiti",
    "MessagesPushSettings",
    "Military",
    "MobileStatItem",
    "Musician",
    "MutualFriend",
    "NameCase",
    "NameRequest",
    "NameRequestStatus",
    "NewsfeedItem",
    "NewsfeedItemType",
    "NewsfeedList",
    "Note",
    "NoteComment",
    "Notification",
    "NotificationInnerType",
    "NotificationItem",
    "NotificationItemInnerType",
    "OauthError",
    "ObjectCount",
    "ObjectType",
    "ObjectWithName",
    "Occupation",
    "OccupationType",
    "Offer",
    "OfferLinkType",
    "OnlineInfo",
    "OnlineInfoStatus",
    "OnlineStatus",
    "OnlineStatusType",
    "OnlineUsers",
    "OnlineUsersWithMobile",
    "OrdClientType",
    "OrdData",
    "OrdSubagent",
    "OrderItem",
    "OrderStatus",
    "OrdersOrder",
    "OutReadBy",
    "OwnerCover",
    "OwnerCoverCropParams",
    "OwnerState",
    "OwnerType",
    "OwnerXtrBanInfo",
    "OwnerXtrBanInfoType",
    "Page",
    "PageType",
    "Participants",
    "Period",
    "Personal",
    "Photo",
    "PhotoAlbum",
    "PhotoAlbumFull",
    "PhotoComment",
    "PhotoNewVerticalAlign",
    "PhotoSize",
    "PhotoSizes",
    "PhotoSizesType",
    "PhotoTag",
    "PhotoUpload",
    "PhotoVerticalAlign",
    "PhotoXtrTagInfo",
    "Photos",
    "PinnedMessage",
    "Place",
    "PlaylistPrivacyCategory",
    "PodcastCover",
    "PodcastExternalData",
    "Poll",
    "PollExtended",
    "PollsPollAnonymous",
    "Post",
    "PostComments",
    "PostCopyright",
    "PostDonut",
    "PostEasyPromote",
    "PostLikes",
    "PostOwner",
    "PostReposts",
    "PostSource",
    "PostSourceType",
    "PostType",
    "PostViews",
    "PostedPhoto",
    "PrettyCard",
    "PrettyCardInnerType",
    "PrettyCardOrError",
    "Price",
    "PrivacySettings",
    "Product",
    "ProductIcon",
    "ProductType",
    "ProfileItem",
    "PromoBlock",
    "PromotedPostReach",
    "Property",
    "PropertyExists",
    "PropertyType",
    "PropertyVariant",
    "PushConversations",
    "PushConversationsItem",
    "PushParams",
    "PushParamsMode",
    "PushParamsOnoff",
    "PushParamsSettings",
    "QuestionItem",
    "QuestionItemOption",
    "QuestionItemType",
    "Reach",
    "ReactionAssetItem",
    "ReactionAssetItemLinks",
    "ReactionCounterResponseItem",
    "ReactionCountersResponseItem",
    "ReactionResponseItem",
    "Region",
    "RejectReason",
    "Relative",
    "RelativeType",
    "Replies",
    "Reply",
    "RepostsInfo",
    "RequestParam",
    "RequestsMutual",
    "RequestsXtrMessage",
    "RequestsXtrMutual",
    "RoleOptions",
    "Rules",
    "SaveResult",
    "SchoolClass",
    "Scope",
    "ScopeName",
    "SectionsListItem",
    "SendMessageError",
    "SendMessageItem",
    "SendUserIdsResponseItem",
    "ServicesViewType",
    "SetCounterItem",
    "SettingsTwitter",
    "SettingsTwitterStatus",
    "Sex",
    "SexAge",
    "ShortCredentials",
    "ShortLink",
    "SmsNotification",
    "Station",
    "StatisticClickAction",
    "StatisticClickActionType",
    "StatsAge",
    "StatsCities",
    "StatsCity",
    "StatsEventType",
    "StatsExtended",
    "StatsFormat",
    "StatsPeriodFromOneOf",
    "StatsPeriodToOneOf",
    "StatsPoint",
    "StatsSex",
    "StatsSexValue",
    "StatsViews",
    "StatsViewsTimes",
    "Status",
    "Sticker",
    "StickerAnimation",
    "StickerAnimationType",
    "StickerInnerType",
    "StickerNew",
    "StickerNewInnerType",
    "StickersImageSet",
    "StickersKeyword",
    "StickersKeywordSticker",
    "Stories",
    "StoriesOwner",
    "Story",
    "StoryItem",
    "StoryItemLink",
    "StoryItemStats",
    "StoryItemStatsFollow",
    "StoryItemStatsUrlView",
    "StoryLink",
    "StoryStats",
    "StoryStatsStat",
    "StoryStatsState",
    "StoryType",
    "StreamInputParams",
    "StreamingStats",
    "SubjectItem",
    "Subscription",
    "SubscriptionsItem",
    "Tag",
    "TagsSuggestionItem",
    "TagsSuggestionItemButton",
    "TagsSuggestionItemButtonAction",
    "TagsSuggestionItemButtonStyle",
    "TargSettings",
    "TargStats",
    "TargSuggestions",
    "TargSuggestionsCities",
    "TargSuggestionsRegions",
    "TargSuggestionsSchools",
    "TargSuggestionsSchoolsType",
    "TargetGroup",
    "TargetGroupTargetPixelRule",
    "TargetPixelInfo",
    "TemplateActionTypeNames",
    "TestingGroup",
    "TokenChecked",
    "TokenPermissionSetting",
    "Topic",
    "TopicComment",
    "Transaction",
    "UpdateAdsStatus",
    "UpdateClientsStatus",
    "UpdateOfficeUsersResult",
    "UploadLinkText",
    "UploadPhotoData",
    "UploadResult",
    "UploadServer",
    "User",
    "UserConnections",
    "UserCounters",
    "UserFull",
    "UserGroupFields",
    "UserId",
    "UserMin",
    "UserRelation",
    "UserSettings",
    "UserSettingsInterest",
    "UserSettingsInterests",
    "UserSettingsXtr",
    "UserSpecification",
    "UserSpecificationCutted",
    "UserType",
    "UserTypeForXtrInvitedBy",
    "UserXtrInvitedBy",
    "UserXtrRole",
    "UserXtrType",
    "Users",
    "UsersArray",
    "UsersFields",
    "UsersSchool",
    "UsersUniversity",
    "UtilsStats",
    "UtilsStatsCity",
    "UtilsStatsCountry",
    "UtilsStatsSexAge",
    "Value",
    "Video",
    "VideoAlbum",
    "VideoAlbumFull",
    "VideoAlbumResponseType",
    "VideoComment",
    "VideoFiles",
    "VideoFull",
    "VideoImage",
    "VideoResponseType",
    "VideoType",
    "ViewersItem",
    "Voters",
    "VotersFieldsUsers",
    "VotersUsers",
    "WallComment",
    "WallCommentDelete",
    "WallCommentDonut",
    "WallCommentDonutPlaceholder",
    "WallGraffiti",
    "WallItem",
    "WallPostNewInnerType",
    "WallRepostInnerType",
    "WallViews",
    "Wallpost",
    "WallpostAttachment",
    "WallpostAttachmentType",
    "WallpostCommentsDonut",
    "WallpostCommentsDonutPlaceholder",
    "WallpostDonut",
    "WallpostDonutEditMode",
    "WallpostDonutPlaceholder",
    "WallpostFull",
    "WallpostInnerType",
    "WallpostStat",
    "WidgetComment",
    "WidgetLikes",
    "WidgetPage",
    "Wikipage",
    "WikipageFull",
    "WikipageHistory",
)

import datetime
from typing import TYPE_CHECKING

from .base_model import BaseEnumMeta, BaseModel, Field, StrEnum


class MessageActionStatus(StrEnum, metaclass=BaseEnumMeta):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
    CHAT_SCREENSHOT = "chat_screenshot"
    CONVERSATION_STYLE_UPDATE = "conversation_style_update"


class MessageAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"
    STORY = "story"
    GROUP_CALL_IN_PROGRESS = "group_call_in_progress"
    MINI_APP = "mini_app"
    VIDEO_PLAYLIST = "video_playlist"
    NARRATIVE = "narrative"


class VideoType(StrEnum, metaclass=BaseEnumMeta):
    INTERACTIVE = "interactive"
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    VIDEO_MESSAGE = "video_message"
    LIVE = "live"
    SHORT_VIDEO = "short_video"
    STORY = "story"


class WallpostAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    """Attachment type"""

    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    MARKET_ALBUM = "market_album"
    MARKET = "market"
    EVENT = "event"
    DONUT_LINK = "donut_link"
    ARTICLE = "article"
    TEXTLIVE = "textlive"
    TEXTPOST = "textpost"
    TEXTPOST_PUBLISH = "textpost_publish"
    SITUATIONAL_THEME = "situational_theme"
    GROUP = "group"
    STICKER = "sticker"
    PODCAST = "podcast"
    PRETTY_CARDS = "pretty_cards"
    MINI_APP = "mini_app"
    CLIP = "clip"
    VIDEO_PLAYLIST = "video_playlist"


class LikeAddRemoveObjectType(StrEnum, metaclass=BaseEnumMeta):
    VIDEO = "video"
    PHOTO = "photo"
    POST = "post"
    COMMENT = "comment"
    NOTE = "note"
    TOPIC_COMMENT = "topic_comment"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    MARKET = "market"
    MARKET_COMMENT = "market_comment"
    CLIP = "clip"


class LinkButtonActionType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_URL = "open_url"
    JOIN_GROUP_AND_OPEN_URL = "join_group_and_open_url"
    MARKET_CLEAR_RECENT_QUERIES = "market_clear_recent_queries"
    CLOSE_WEB_APP = "close_web_app"
    ADD_PLAYLIST = "add_playlist"
    OPEN_SEARCH_TAB = "open_search_tab"
    OPEN_SEARCH_FILTERS = "open_search_filters"
    RESET_SEARCH_FILTERS = "reset_search_filters"
    IMPORT_CONTACTS = "import_contacts"
    ADD_FRIENDS = "add_friends"
    ONBOARDING = "onboarding"
    SHOW_FILTERS = "show_filters"


class PollExtended(Poll):
    pass


class UserXtrRole(UserFull, MemberRole):
    pass


class LinkPhoto(Photo):
    has_tags: bool | None = None
    date: datetime.datetime | None = None


class PrettyCardsList(BaseModel):
    cards: PrettyCard | None = None


class GroupCallInProgress(CallsCall):
    receiver_id: int | None = None
    time: int | None = None
    join_link: str | None = None
    state: EndState | None = None


class LinkAttachment(Link):
    photo: LinkPhoto | None = None


class SendUserIdsResponseItem(BaseModel):
    conversation_message_id: int | None = None
    error: MessageError | None = None
    message_id: int | None
    peer_id: int

    # NOTE: Add `narrative` field. Now, we've no docs and schema about this attachment.


class ClientInfoForBots(BaseModel):
    """Model: `ClientInfoForBots`"""

    button_actions: list[TemplateActionTypeNames] | None = Field(
        default=None,
    )
    """Property `ClientInfoForBots.button_actions`."""

    keyboard: bool | None = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: bool | None = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: bool | None = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: int | None = Field(
        default=None,
    )
    """client or user language id."""


type SubscriptionsItem = GroupFull | UserFull

if not TYPE_CHECKING:

    localns = locals().copy()
    types_namespace = dict(globals()) | localns
    alls = {"SubscriptionsItem"}

    for item_name, item in localns.items():
        if issubclass(type(item), BaseEnumMeta):
            alls.add(item_name)

        if not (isinstance(item, type) and item is not BaseModel and issubclass(item, BaseModel)):
            continue

        item.set_original_module_namespace(types_namespace)

        for parent in item.__bases__:
            if parent.__name__ == item.__name__ and issubclass(parent, BaseModel):
                parent.__pydantic_fields__.update(item.__pydantic_fields__)
                parent.set_original_module_namespace(types_namespace)
                item.__pydantic_fields__.update(
                    {name: field for name, field in parent.__pydantic_fields__.items() if name not in item.__pydantic_fields__},
                )

        alls.add(item_name)

    alls.update(__all__)

    __all__ = tuple(sorted(alls))

    del alls, localns, types_namespace, item, parent
