from typing import Any

import pydantic

from vkx.models.base_model import BaseModel

from .enums import GroupEventType
from .objects import group_event_objects


class BaseGroupEvent(BaseModel):
    object: group_event_objects.EventObject | None
    type: GroupEventType | None = None
    secret: str | None = None
    event_id: str | None = None
    group_id: int | None = None
    unprepared_ctx_api: Any | None = None

    model_config = pydantic.ConfigDict(frozen=False)

    @property
    def ctx_api(self) -> "Any":
        if self.unprepared_ctx_api is None:
            raise AssertionError
        return self.unprepared_ctx_api


class MessageNewEvent(BaseGroupEvent):
    object: group_event_objects.MessageNewObject


class MessageReplyEvent(BaseGroupEvent):
    object: group_event_objects.MessageReplyObject


class MessageEditEvent(BaseGroupEvent):
    object: group_event_objects.MessageEditObject


class MessageAllowEvent(BaseGroupEvent):
    object: group_event_objects.MessageAllowObject


class MessageDenyEvent(BaseGroupEvent):
    object: group_event_objects.MessageDenyObject


class MessageTypingStateEvent(BaseGroupEvent):
    object: group_event_objects.MessageTypingStateObject


class MessageEvent(BaseGroupEvent):
    object: group_event_objects.MessageEventObject


class PhotoNewEvent(BaseGroupEvent):
    object: group_event_objects.PhotoNewObject


class PhotoCommentNewEvent(BaseGroupEvent):
    object: group_event_objects.PhotoCommentNewObject


class PhotoCommentEditEvent(BaseGroupEvent):
    object: group_event_objects.PhotoCommentNewObject


class PhotoCommentRestoreEvent(BaseGroupEvent):
    object: group_event_objects.PhotoCommentRestoreObject


class PhotoCommentDeleteEvent(BaseGroupEvent):
    object: group_event_objects.PhotoCommentDeleteObject


class AudioNewEvent(BaseGroupEvent):
    object: group_event_objects.AudioNewObject


class VideoNewEvent(BaseGroupEvent):
    object: group_event_objects.VideoNewObject


class VideoCommentNewEvent(BaseGroupEvent):
    object: group_event_objects.VideoCommentNewObject


class VideoCommentEditEvent(BaseGroupEvent):
    object: group_event_objects.VideoCommentEditObject


class VideoCommentRestoreEvent(BaseGroupEvent):
    object: group_event_objects.VideoCommentRestoreObject


class LeadFormsNewEvent(BaseGroupEvent):
    object: group_event_objects.LeadFormsNewObject


class VideoCommentDeleteEvent(BaseGroupEvent):
    object: group_event_objects.VideoCommentDeleteObject


class WallPostNewEvent(BaseGroupEvent):
    object: group_event_objects.WallPostNewObject


class WallRepostEvent(BaseGroupEvent):
    object: group_event_objects.RepostObject


class WallReplyNewEvent(BaseGroupEvent):
    object: group_event_objects.ReplyNewObject


class WallReplyEditEvent(BaseGroupEvent):
    object: group_event_objects.ReplyRestoreObject


class WallReplyRestoreEvent(BaseGroupEvent):
    object: group_event_objects.ReplyRestoreObject


class WallReplyDeleteEvent(BaseGroupEvent):
    object: group_event_objects.ReplyDeleteObject


class LikeAddEvent(BaseGroupEvent):
    object: group_event_objects.LikeAddObject


class LikeRemoveEvent(BaseGroupEvent):
    object: group_event_objects.LikeRemoveObject


class BoardPostNewEvent(BaseGroupEvent):
    object: group_event_objects.BoardPostNewObject


class BoardPostEditEvent(BaseGroupEvent):
    object: group_event_objects.PostEditObject


class BoardPostRestoreEvent(BaseGroupEvent):
    object: group_event_objects.PostRestoreObject


class BoardPostDeleteEvent(BaseGroupEvent):
    object: group_event_objects.PostDeleteObject


class MarketCommentNewEvent(BaseGroupEvent):
    object: group_event_objects.MarketCommentNewObject


class MarketCommentEditEvent(BaseGroupEvent):
    object: group_event_objects.MarketCommentEditObject


class MarketCommentRestoreEvent(BaseGroupEvent):
    object: group_event_objects.MarketCommentRestoreObject


class MarketCommentDeleteEvent(BaseGroupEvent):
    object: group_event_objects.MarketCommentDeleteObject


class MarketOrderNewEvent(BaseGroupEvent):
    object: group_event_objects.OrderNewObject


class MarketOrderEditEvent(BaseGroupEvent):
    object: group_event_objects.OrderEditObject


class GroupLeaveEvent(BaseGroupEvent):
    object: group_event_objects.GroupLeaveObject


class GroupJoinEvent(BaseGroupEvent):
    object: group_event_objects.GroupJoinObject


class UserBlockEvent(BaseGroupEvent):
    object: group_event_objects.UserBlockObject


class UserUnblockEvent(BaseGroupEvent):
    object: group_event_objects.UserUnblockObject


class PollVoteNewEvent(BaseGroupEvent):
    object: group_event_objects.PollVoteNewObject


class GroupOfficersEditEvent(BaseGroupEvent):
    object: group_event_objects.GroupOfficersEditObject


class GroupChangeSettingsEvent(BaseGroupEvent):
    object: group_event_objects.GroupChangeSettingsObject


class GroupChangePhotoEvent(BaseGroupEvent):
    object: group_event_objects.GroupChangePhotoObject


class VkpayTransactionEvent(BaseGroupEvent):
    object: group_event_objects.VkpayTransactionObject


class AppPayloadEvent(BaseGroupEvent):
    object: group_event_objects.AppPayloadObject


class DonutSubscriptionCreateEvent(BaseGroupEvent):
    object: group_event_objects.SubscriptionCreateObject


class DonutSubscriptionProlongedEvent(BaseGroupEvent):
    object: group_event_objects.SubscriptionProlongedObject


class DonutSubscriptionExpiredEvent(BaseGroupEvent):
    object: group_event_objects.SubscriptionExpiredObject


class DonutSubscriptionCancelledEvent(BaseGroupEvent):
    object: group_event_objects.SubscriptionCancelledObject


class DonutSubscriptionPriceChangedEvent(BaseGroupEvent):
    object: group_event_objects.SubscriptionPriceChangedObject


class DonutMoneyWithdrawEvent(BaseGroupEvent):
    object: group_event_objects.MoneyWithdrawObject


class DonutMoneyWithdrawErrorEvent(BaseGroupEvent):
    object: group_event_objects.MoneyWithdrawErrorObject


class MessageReactionEvent(BaseGroupEvent):
    object: group_event_objects.MessageReactionEventObject


class MessageReadEvent(BaseGroupEvent):
    object: group_event_objects.MessageReadObject


localns = locals().copy()
for item in localns.values():
    if isinstance(item, type) and item is not BaseGroupEvent and issubclass(item, BaseGroupEvent):
        item.set_original_module_namespace(localns)

del localns


__all__ = (
    "AppPayloadEvent",
    "AudioNewEvent",
    "BaseGroupEvent",
    "BoardPostDeleteEvent",
    "BoardPostEditEvent",
    "BoardPostNewEvent",
    "BoardPostRestoreEvent",
    "DonutMoneyWithdrawErrorEvent",
    "DonutMoneyWithdrawEvent",
    "DonutSubscriptionCancelledEvent",
    "DonutSubscriptionCreateEvent",
    "DonutSubscriptionExpiredEvent",
    "DonutSubscriptionPriceChangedEvent",
    "DonutSubscriptionProlongedEvent",
    "GroupChangePhotoEvent",
    "GroupChangeSettingsEvent",
    "GroupJoinEvent",
    "GroupLeaveEvent",
    "GroupOfficersEditEvent",
    "LeadFormsNewEvent",
    "LikeAddEvent",
    "LikeRemoveEvent",
    "MarketCommentDeleteEvent",
    "MarketCommentEditEvent",
    "MarketCommentNewEvent",
    "MarketCommentRestoreEvent",
    "MarketOrderEditEvent",
    "MarketOrderNewEvent",
    "MessageAllowEvent",
    "MessageDenyEvent",
    "MessageEditEvent",
    "MessageEvent",
    "MessageNewEvent",
    "MessageReactionEvent",
    "MessageReadEvent",
    "MessageReplyEvent",
    "MessageTypingStateEvent",
    "PhotoCommentDeleteEvent",
    "PhotoCommentEditEvent",
    "PhotoCommentNewEvent",
    "PhotoCommentRestoreEvent",
    "PhotoNewEvent",
    "PollVoteNewEvent",
    "UserBlockEvent",
    "UserUnblockEvent",
    "VideoCommentDeleteEvent",
    "VideoCommentEditEvent",
    "VideoCommentNewEvent",
    "VideoCommentRestoreEvent",
    "VideoNewEvent",
    "VkpayTransactionEvent",
    "WallPostNewEvent",
    "WallReplyDeleteEvent",
    "WallReplyEditEvent",
    "WallReplyNewEvent",
    "WallReplyRestoreEvent",
    "WallRepostEvent",
)
