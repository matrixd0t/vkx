from typing import Any, Literal

import pydantic

from vkx.models.base_model import BaseModel

from .enums import CallbackEventType
from .objects import group_event_objects as go


class BaseCallbackEvent(BaseModel):
    """Уведомление Callback API.

    Конверт уведомления: ``type``, ``object``, ``group_id``, ``event_id``,
    ``v``, ``secret``. Для неизвестного ``type`` возвращается именно этот
    класс, а поле ``object`` остаётся сырым словарём.
    """

    type: CallbackEventType
    object: Any | None = None
    group_id: int | None = None
    event_id: str | int | None = None
    v: str | None = None
    secret: str | None = None

    model_config = pydantic.ConfigDict(frozen=False)


class ConfirmationCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.CONFIRMATION]
    object: None = None


# Сообщения
class MessageNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_NEW]
    object: go.MessageNewObject


class MessageReplyCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_REPLY]
    object: go.MessageReplyObject


class MessageEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_EDIT]
    object: go.MessageEditObject


class MessageEventCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_EVENT]
    object: go.MessageEventObject


class MessageAllowCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_ALLOW]
    object: go.MessageAllowObject


class MessageDenyCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_DENY]
    object: go.MessageDenyObject


class MessageTypingStateCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_TYPING_STATE]
    object: go.MessageTypingStateObject


class MessageReadCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_READ]
    object: go.MessageReadObject


class MessageReactionCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MESSAGE_REACTION_EVENT]
    object: go.MessageReactionEventObject


# Фотографии
class PhotoNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.PHOTO_NEW]
    object: go.PhotoNewObject


class PhotoCommentNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.PHOTO_COMMENT_NEW]
    object: go.PhotoCommentNewObject


class PhotoCommentEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.PHOTO_COMMENT_EDIT]
    object: go.PhotoCommentEditObject


class PhotoCommentRestoreCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.PHOTO_COMMENT_RESTORE]
    object: go.PhotoCommentRestoreObject


class PhotoCommentDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.PHOTO_COMMENT_DELETE]
    object: go.PhotoCommentDeleteObject


# Аудиозаписи
class AudioNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.AUDIO_NEW]
    object: go.AudioNewObject


# Видеозаписи
class VideoNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VIDEO_NEW]
    object: go.VideoNewObject


class VideoCommentNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VIDEO_COMMENT_NEW]
    object: go.VideoCommentNewObject


class VideoCommentEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VIDEO_COMMENT_EDIT]
    object: go.VideoCommentEditObject


class VideoCommentRestoreCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VIDEO_COMMENT_RESTORE]
    object: go.VideoCommentRestoreObject


class VideoCommentDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VIDEO_COMMENT_DELETE]
    object: go.VideoCommentDeleteObject


# Записи на стене
class WallPostNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_POST_NEW]
    object: go.WallPostNewObject


class WallRepostCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_REPOST]
    object: go.RepostObject


class WallSchedulePostNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_SCHEDULE_POST_NEW]
    object: go.WallSchedulePostObject


class WallSchedulePostDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_SCHEDULE_POST_DELETE]
    object: go.WallSchedulePostObject


# Комментарии на стене
class WallReplyNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_REPLY_NEW]
    object: go.ReplyNewObject


class WallReplyEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_REPLY_EDIT]
    object: go.ReplyEditObject


class WallReplyRestoreCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_REPLY_RESTORE]
    object: go.ReplyRestoreObject


class WallReplyDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.WALL_REPLY_DELETE]
    object: go.ReplyDeleteObject


# Отметки «Нравится»
class LikeAddCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.LIKE_ADD]
    object: go.LikeAddObject


class LikeRemoveCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.LIKE_REMOVE]
    object: go.LikeRemoveObject


# Обсуждения
class BoardPostNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.BOARD_POST_NEW]
    object: go.BoardPostNewObject


class BoardPostEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.BOARD_POST_EDIT]
    object: go.PostEditObject


class BoardPostRestoreCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.BOARD_POST_RESTORE]
    object: go.PostRestoreObject


class BoardPostDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.BOARD_POST_DELETE]
    object: go.PostDeleteObject


# Товары
class MarketCommentNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_COMMENT_NEW]
    object: go.MarketCommentNewObject


class MarketCommentEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_COMMENT_EDIT]
    object: go.MarketCommentEditObject


class MarketCommentRestoreCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_COMMENT_RESTORE]
    object: go.MarketCommentRestoreObject


class MarketCommentDeleteCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_COMMENT_DELETE]
    object: go.MarketCommentDeleteObject


class MarketOrderNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_ORDER_NEW]
    object: go.OrderNewObject


class MarketOrderEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.MARKET_ORDER_EDIT]
    object: go.OrderEditObject


# Пользователи
class GroupJoinCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.GROUP_JOIN]
    object: go.GroupJoinObject


class GroupLeaveCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.GROUP_LEAVE]
    object: go.GroupLeaveObject


class UserBlockCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.USER_BLOCK]
    object: go.UserBlockObject


class UserUnblockCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.USER_UNBLOCK]
    object: go.UserUnblockObject


# Платные подписки VK Donut
class DonutSubscriptionCreateCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_SUBSCRIPTION_CREATE]
    object: go.SubscriptionCreateObject


class DonutSubscriptionProlongedCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_SUBSCRIPTION_PROLONGED]
    object: go.SubscriptionProlongedObject


class DonutSubscriptionExpiredCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_SUBSCRIPTION_EXPIRED]
    object: go.SubscriptionExpiredObject


class DonutSubscriptionCancelledCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_SUBSCRIPTION_CANCELLED]
    object: go.SubscriptionCancelledObject


class DonutSubscriptionPriceChangedCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_SUBSCRIPTION_PRICE_CHANGED]
    object: go.SubscriptionPriceChangedObject


class DonutMoneyWithdrawCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_MONEY_WITHDRAW]
    object: go.MoneyWithdrawObject


class DonutMoneyWithdrawErrorCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.DONUT_MONEY_WITHDRAW_ERROR]
    object: go.MoneyWithdrawErrorObject


# Прочее
class GroupChangeSettingsCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.GROUP_CHANGE_SETTINGS]
    object: go.GroupChangeSettingsObject


class GroupChangePhotoCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.GROUP_CHANGE_PHOTO]
    object: go.GroupChangePhotoObject


class GroupOfficersEditCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.GROUP_OFFICERS_EDIT]
    object: go.GroupOfficersEditObject


class PollVoteNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.POLL_VOTE_NEW]
    object: go.PollVoteNewObject


class LeadFormsNewCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.LEAD_FORMS_NEW]
    object: go.LeadFormsNewObject


class VkpayTransactionCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.VKPAY_TRANSACTION]
    object: go.VkpayTransactionObject


class AppPayloadCallbackEvent(BaseCallbackEvent):
    type: Literal[CallbackEventType.APP_PAYLOAD]
    object: go.AppPayloadObject


type CallbackEvent = (
    BaseCallbackEvent
    | ConfirmationCallbackEvent
    | MessageNewCallbackEvent
    | MessageReplyCallbackEvent
    | MessageEditCallbackEvent
    | MessageEventCallbackEvent
    | MessageAllowCallbackEvent
    | MessageDenyCallbackEvent
    | MessageTypingStateCallbackEvent
    | MessageReadCallbackEvent
    | MessageReactionCallbackEvent
    | PhotoNewCallbackEvent
    | PhotoCommentNewCallbackEvent
    | PhotoCommentEditCallbackEvent
    | PhotoCommentRestoreCallbackEvent
    | PhotoCommentDeleteCallbackEvent
    | AudioNewCallbackEvent
    | VideoNewCallbackEvent
    | VideoCommentNewCallbackEvent
    | VideoCommentEditCallbackEvent
    | VideoCommentRestoreCallbackEvent
    | VideoCommentDeleteCallbackEvent
    | WallPostNewCallbackEvent
    | WallRepostCallbackEvent
    | WallSchedulePostNewCallbackEvent
    | WallSchedulePostDeleteCallbackEvent
    | WallReplyNewCallbackEvent
    | WallReplyEditCallbackEvent
    | WallReplyRestoreCallbackEvent
    | WallReplyDeleteCallbackEvent
    | LikeAddCallbackEvent
    | LikeRemoveCallbackEvent
    | BoardPostNewCallbackEvent
    | BoardPostEditCallbackEvent
    | BoardPostRestoreCallbackEvent
    | BoardPostDeleteCallbackEvent
    | MarketCommentNewCallbackEvent
    | MarketCommentEditCallbackEvent
    | MarketCommentRestoreCallbackEvent
    | MarketCommentDeleteCallbackEvent
    | MarketOrderNewCallbackEvent
    | MarketOrderEditCallbackEvent
    | GroupJoinCallbackEvent
    | GroupLeaveCallbackEvent
    | UserBlockCallbackEvent
    | UserUnblockCallbackEvent
    | DonutSubscriptionCreateCallbackEvent
    | DonutSubscriptionProlongedCallbackEvent
    | DonutSubscriptionExpiredCallbackEvent
    | DonutSubscriptionCancelledCallbackEvent
    | DonutSubscriptionPriceChangedCallbackEvent
    | DonutMoneyWithdrawCallbackEvent
    | DonutMoneyWithdrawErrorCallbackEvent
    | GroupChangeSettingsCallbackEvent
    | GroupChangePhotoCallbackEvent
    | GroupOfficersEditCallbackEvent
    | PollVoteNewCallbackEvent
    | LeadFormsNewCallbackEvent
    | VkpayTransactionCallbackEvent
    | AppPayloadCallbackEvent
)


CALLBACK_EVENTS: dict[CallbackEventType, type[BaseCallbackEvent]] = {
    CallbackEventType.CONFIRMATION: ConfirmationCallbackEvent,
    CallbackEventType.MESSAGE_NEW: MessageNewCallbackEvent,
    CallbackEventType.MESSAGE_REPLY: MessageReplyCallbackEvent,
    CallbackEventType.MESSAGE_EDIT: MessageEditCallbackEvent,
    CallbackEventType.MESSAGE_EVENT: MessageEventCallbackEvent,
    CallbackEventType.MESSAGE_ALLOW: MessageAllowCallbackEvent,
    CallbackEventType.MESSAGE_DENY: MessageDenyCallbackEvent,
    CallbackEventType.MESSAGE_TYPING_STATE: MessageTypingStateCallbackEvent,
    CallbackEventType.MESSAGE_READ: MessageReadCallbackEvent,
    CallbackEventType.MESSAGE_REACTION_EVENT: MessageReactionCallbackEvent,
    CallbackEventType.PHOTO_NEW: PhotoNewCallbackEvent,
    CallbackEventType.PHOTO_COMMENT_NEW: PhotoCommentNewCallbackEvent,
    CallbackEventType.PHOTO_COMMENT_EDIT: PhotoCommentEditCallbackEvent,
    CallbackEventType.PHOTO_COMMENT_RESTORE: PhotoCommentRestoreCallbackEvent,
    CallbackEventType.PHOTO_COMMENT_DELETE: PhotoCommentDeleteCallbackEvent,
    CallbackEventType.AUDIO_NEW: AudioNewCallbackEvent,
    CallbackEventType.VIDEO_NEW: VideoNewCallbackEvent,
    CallbackEventType.VIDEO_COMMENT_NEW: VideoCommentNewCallbackEvent,
    CallbackEventType.VIDEO_COMMENT_EDIT: VideoCommentEditCallbackEvent,
    CallbackEventType.VIDEO_COMMENT_RESTORE: VideoCommentRestoreCallbackEvent,
    CallbackEventType.VIDEO_COMMENT_DELETE: VideoCommentDeleteCallbackEvent,
    CallbackEventType.WALL_POST_NEW: WallPostNewCallbackEvent,
    CallbackEventType.WALL_REPOST: WallRepostCallbackEvent,
    CallbackEventType.WALL_SCHEDULE_POST_NEW: WallSchedulePostNewCallbackEvent,
    CallbackEventType.WALL_SCHEDULE_POST_DELETE: WallSchedulePostDeleteCallbackEvent,
    CallbackEventType.WALL_REPLY_NEW: WallReplyNewCallbackEvent,
    CallbackEventType.WALL_REPLY_EDIT: WallReplyEditCallbackEvent,
    CallbackEventType.WALL_REPLY_RESTORE: WallReplyRestoreCallbackEvent,
    CallbackEventType.WALL_REPLY_DELETE: WallReplyDeleteCallbackEvent,
    CallbackEventType.LIKE_ADD: LikeAddCallbackEvent,
    CallbackEventType.LIKE_REMOVE: LikeRemoveCallbackEvent,
    CallbackEventType.BOARD_POST_NEW: BoardPostNewCallbackEvent,
    CallbackEventType.BOARD_POST_EDIT: BoardPostEditCallbackEvent,
    CallbackEventType.BOARD_POST_RESTORE: BoardPostRestoreCallbackEvent,
    CallbackEventType.BOARD_POST_DELETE: BoardPostDeleteCallbackEvent,
    CallbackEventType.MARKET_COMMENT_NEW: MarketCommentNewCallbackEvent,
    CallbackEventType.MARKET_COMMENT_EDIT: MarketCommentEditCallbackEvent,
    CallbackEventType.MARKET_COMMENT_RESTORE: MarketCommentRestoreCallbackEvent,
    CallbackEventType.MARKET_COMMENT_DELETE: MarketCommentDeleteCallbackEvent,
    CallbackEventType.MARKET_ORDER_NEW: MarketOrderNewCallbackEvent,
    CallbackEventType.MARKET_ORDER_EDIT: MarketOrderEditCallbackEvent,
    CallbackEventType.GROUP_JOIN: GroupJoinCallbackEvent,
    CallbackEventType.GROUP_LEAVE: GroupLeaveCallbackEvent,
    CallbackEventType.USER_BLOCK: UserBlockCallbackEvent,
    CallbackEventType.USER_UNBLOCK: UserUnblockCallbackEvent,
    CallbackEventType.DONUT_SUBSCRIPTION_CREATE: DonutSubscriptionCreateCallbackEvent,
    CallbackEventType.DONUT_SUBSCRIPTION_PROLONGED: DonutSubscriptionProlongedCallbackEvent,
    CallbackEventType.DONUT_SUBSCRIPTION_EXPIRED: DonutSubscriptionExpiredCallbackEvent,
    CallbackEventType.DONUT_SUBSCRIPTION_CANCELLED: DonutSubscriptionCancelledCallbackEvent,
    CallbackEventType.DONUT_SUBSCRIPTION_PRICE_CHANGED: DonutSubscriptionPriceChangedCallbackEvent,
    CallbackEventType.DONUT_MONEY_WITHDRAW: DonutMoneyWithdrawCallbackEvent,
    CallbackEventType.DONUT_MONEY_WITHDRAW_ERROR: DonutMoneyWithdrawErrorCallbackEvent,
    CallbackEventType.GROUP_CHANGE_SETTINGS: GroupChangeSettingsCallbackEvent,
    CallbackEventType.GROUP_CHANGE_PHOTO: GroupChangePhotoCallbackEvent,
    CallbackEventType.GROUP_OFFICERS_EDIT: GroupOfficersEditCallbackEvent,
    CallbackEventType.POLL_VOTE_NEW: PollVoteNewCallbackEvent,
    CallbackEventType.LEAD_FORMS_NEW: LeadFormsNewCallbackEvent,
    CallbackEventType.VKPAY_TRANSACTION: VkpayTransactionCallbackEvent,
    CallbackEventType.APP_PAYLOAD: AppPayloadCallbackEvent,
}


localns = locals().copy()
for item in localns.values():
    if isinstance(item, type) and issubclass(item, BaseCallbackEvent) and item is not BaseCallbackEvent:
        item.set_original_module_namespace(localns)

del localns


__all__ = (
    "CALLBACK_EVENTS",
    "AppPayloadCallbackEvent",
    "AudioNewCallbackEvent",
    "BaseCallbackEvent",
    "BoardPostDeleteCallbackEvent",
    "BoardPostEditCallbackEvent",
    "BoardPostNewCallbackEvent",
    "BoardPostRestoreCallbackEvent",
    "CallbackEvent",
    "ConfirmationCallbackEvent",
    "DonutMoneyWithdrawCallbackEvent",
    "DonutMoneyWithdrawErrorCallbackEvent",
    "DonutSubscriptionCancelledCallbackEvent",
    "DonutSubscriptionCreateCallbackEvent",
    "DonutSubscriptionExpiredCallbackEvent",
    "DonutSubscriptionPriceChangedCallbackEvent",
    "DonutSubscriptionProlongedCallbackEvent",
    "GroupChangePhotoCallbackEvent",
    "GroupChangeSettingsCallbackEvent",
    "GroupJoinCallbackEvent",
    "GroupLeaveCallbackEvent",
    "GroupOfficersEditCallbackEvent",
    "LeadFormsNewCallbackEvent",
    "LikeAddCallbackEvent",
    "LikeRemoveCallbackEvent",
    "MarketCommentDeleteCallbackEvent",
    "MarketCommentEditCallbackEvent",
    "MarketCommentNewCallbackEvent",
    "MarketCommentRestoreCallbackEvent",
    "MarketOrderEditCallbackEvent",
    "MarketOrderNewCallbackEvent",
    "MessageAllowCallbackEvent",
    "MessageDenyCallbackEvent",
    "MessageEditCallbackEvent",
    "MessageEventCallbackEvent",
    "MessageNewCallbackEvent",
    "MessageReactionCallbackEvent",
    "MessageReadCallbackEvent",
    "MessageReplyCallbackEvent",
    "MessageTypingStateCallbackEvent",
    "PhotoCommentDeleteCallbackEvent",
    "PhotoCommentEditCallbackEvent",
    "PhotoCommentNewCallbackEvent",
    "PhotoCommentRestoreCallbackEvent",
    "PhotoNewCallbackEvent",
    "PollVoteNewCallbackEvent",
    "UserBlockCallbackEvent",
    "UserUnblockCallbackEvent",
    "VideoCommentDeleteCallbackEvent",
    "VideoCommentEditCallbackEvent",
    "VideoCommentNewCallbackEvent",
    "VideoCommentRestoreCallbackEvent",
    "VideoNewCallbackEvent",
    "VkpayTransactionCallbackEvent",
    "WallPostNewCallbackEvent",
    "WallReplyDeleteCallbackEvent",
    "WallReplyEditCallbackEvent",
    "WallReplyNewCallbackEvent",
    "WallReplyRestoreCallbackEvent",
    "WallRepostCallbackEvent",
    "WallSchedulePostDeleteCallbackEvent",
    "WallSchedulePostNewCallbackEvent",
)
