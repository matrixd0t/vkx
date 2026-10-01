from typing import Any

import pydantic

from ...base_model import BaseModel
from ...objects import *


class EventObject(BaseModel):
    model_config = pydantic.ConfigDict(frozen=False)


class MessageNewObject(EventObject):
    client_info: ClientInfoForBots | None = None
    message: Message | None = None


class MessageReplyObject(EventObject, Message):
    pass


class MessageEditObject(EventObject, Message):
    pass


class MessageAllowObject(EventObject):
    key: str
    user_id: int


class MessageDenyObject(EventObject):
    user_id: int


class MessageTypingStateObject(EventObject):
    state: str | None = None
    from_id: int | None = None
    to_id: int | None = None


class MessageEventObject(EventObject):
    user_id: int
    peer_id: int
    event_id: str
    payload: dict[str, Any] | str | None = None
    conversation_message_id: int | None = None


class PhotoNewObject(EventObject, Photo):
    pass


class PhotoCommentNewObject(EventObject, WallComment):
    photo_id: int  # type: ignore
    photo_owner_id: int


class PhotoCommentEditObject(PhotoCommentNewObject):
    pass


class PhotoCommentRestoreObject(PhotoCommentNewObject):
    pass


class PhotoCommentDeleteObject(EventObject):
    id: int
    owner_id: int
    photo_id: int
    user_id: int


class AudioNewObject(EventObject, Audio):
    pass


class VideoNewObject(EventObject, Video):
    pass


class VideoCommentNewObject(EventObject, WallComment):
    video_id: int  # type: ignore
    video_owner_id: int


class VideoCommentEditObject(VideoCommentNewObject):
    pass


class VideoCommentRestoreObject(VideoCommentNewObject):
    pass


class VideoCommentDeleteObject(EventObject):
    id: int
    deleter_id: int
    owner_id: int
    user_id: int
    video_id: int


class WallPostNewObject(EventObject, WallpostFull):
    postponed_id: int | None = None


class RepostObject(WallPostNewObject):
    pass


class WallSchedulePostObject(EventObject):
    schedule_time: int
    id: int


class ReplyNewObject(EventObject, WallComment):
    post_id: int | None = None
    post_owner_id: int | None = None


class ReplyEditObject(ReplyNewObject):
    pass


class ReplyRestoreObject(ReplyNewObject):
    pass


class ReplyDeleteObject(EventObject):
    owner_id: int | None = None
    id: int | None = None
    deleter_id: int | None = None
    post_id: int | None = None


class LikeAddObject(EventObject):
    liker_id: int
    object_id: int
    object_owner_id: int
    object_type: LikeAddRemoveObjectType | None = None
    post_id: int
    thread_reply_id: int | None = None


class LikeRemoveObject(LikeAddObject):
    pass


class LeadFormAnswerModel(BaseModel):
    key: str
    question: str
    answer: str | None = None


class LeadFormsNewObject(EventObject):
    lead_id: int
    group_id: int
    form_id: int
    user_id: int
    form_name: str
    answers: list[LeadFormAnswerModel] | None = None


class BoardPostNewObject(EventObject, TopicComment):
    topic_id: int | None = None
    topic_owner_id: int | None = None


class PostEditObject(BoardPostNewObject):
    pass


class PostRestoreObject(BoardPostNewObject):
    pass


class PostDeleteObject(EventObject):
    id: int
    topic_id: int
    topic_owner_id: int


class MarketCommentNewObject(EventObject):
    date: int
    from_id: int
    id: int
    market_owner_id: int | None = None
    photo_id: int | None = None
    text: str | None = None


class MarketCommentEditObject(MarketCommentNewObject):
    pass


class MarketCommentRestoreObject(MarketCommentNewObject):
    pass


class MarketCommentDeleteObject(EventObject):
    id: int
    item_id: int
    owner_id: int
    user_id: int


class OrderNewObject(EventObject, MarketOrder):
    pass


class OrderEditObject(OrderNewObject):
    pass


class GroupLeaveObject(EventObject):
    self: bool | None = None
    user_id: int | None = None


class GroupJoinObject(EventObject):
    join_type: GroupJoinType
    user_id: int


class UserBlockObject(EventObject):
    admin_id: int
    comment: str | None = None
    reason: int
    unblock_date: int
    user_id: int


class UserUnblockObject(EventObject):
    admin_id: int
    by_end_date: int
    user_id: int


class PollVoteNewObject(EventObject):
    option_id: int
    owner_id: int
    poll_id: int
    user_id: int


class GroupOfficersEditObject(EventObject):
    admin_id: int
    level_new: GroupOfficerRole
    level_old: GroupOfficerRole
    user_id: int


class GroupSettingsChangesObject(EventObject):
    access: GroupIsClosed | None = None
    age_limits: GroupFullAgeLimits | None = None
    description: str | None = None
    enable_audio: GroupAudio | None = None
    enable_market: GroupMarket | None = None
    enable_photo: GroupPhotos | None = None
    enable_status_default: GroupWall | None = None
    enable_video: GroupVideo | None = None
    public_category: int | None = None
    public_subcategory: int | None = None
    screen_name: str | None = None
    title: str | None = None
    website: str | None = None
    old_value: Any
    new_value: Any


class GroupChangeSettingsObject(EventObject):
    changes: GroupSettingsChangesObject | None = None
    user_id: int


class GroupChangePhotoObject(EventObject):
    photo: Photo
    user_id: int


class VkpayTransactionObject(EventObject):
    amount: int | None = None
    date: int | None = None
    description: str | None = None
    from_id: int | None = None


class AppPayloadObject(EventObject):
    user_id: int | None = None
    app_id: int | None = None
    payload: str | None = None
    group_id: int | None = None


class SubscriptionCreateObject(EventObject):
    amount: int
    amount_without_fee: float
    user_id: int | None = None


class SubscriptionProlongedObject(EventObject):
    amount: int
    amount_without_fee: float
    user_id: int | None = None


class SubscriptionExpiredObject(EventObject):
    user_id: int | None = None


class SubscriptionCancelledObject(EventObject):
    user_id: int | None = None


class SubscriptionPriceChangedObject(EventObject):
    amount_diff: float | None = None
    amount_diff_without_fee: float | None = None
    amount_new: int
    amount_old: int
    user_id: int | None = None


class MoneyWithdrawObject(EventObject):
    amount: float
    amount_without_fee: float


class MoneyWithdrawErrorObject(EventObject):
    reason: str


class MessageReactionEventObject(EventObject):
    reacted_id: int
    peer_id: int
    cmid: int
    reaction_id: int | None = None


class MessageReadObject(EventObject):
    from_id: int
    peer_id: int
    read_message_id: int
    conversation_message_id: int


__all__ = (
    "AppPayloadObject",
    "AudioNewObject",
    "BoardPostNewObject",
    "ClientInfoForBots",
    "GroupChangePhotoObject",
    "GroupChangeSettingsObject",
    "GroupLeaveObject",
    "GroupOfficersEditObject",
    "GroupSettingsChangesObject",
    "LeadFormsNewObject",
    "LikeAddObject",
    "LikeRemoveObject",
    "MarketCommentDeleteObject",
    "MarketCommentEditObject",
    "MarketCommentNewObject",
    "MarketCommentRestoreObject",
    "MessageAllowObject",
    "MessageDenyObject",
    "MessageEditObject",
    "MessageEventObject",
    "MessageNewObject",
    "MessageReactionEventObject",
    "MessageReadObject",
    "MessageReplyObject",
    "MessageTypingStateObject",
    "MoneyWithdrawErrorObject",
    "MoneyWithdrawObject",
    "OrderEditObject",
    "OrderNewObject",
    "PhotoCommentDeleteObject",
    "PhotoCommentEditObject",
    "PhotoCommentNewObject",
    "PhotoCommentRestoreObject",
    "PhotoNewObject",
    "PollVoteNewObject",
    "PostDeleteObject",
    "PostEditObject",
    "PostRestoreObject",
    "ReplyDeleteObject",
    "ReplyEditObject",
    "ReplyNewObject",
    "ReplyRestoreObject",
    "RepostObject",
    "SubscriptionCancelledObject",
    "SubscriptionCreateObject",
    "SubscriptionExpiredObject",
    "SubscriptionPriceChangedObject",
    "SubscriptionProlongedObject",
    "UserBlockObject",
    "UserUnblockObject",
    "VideoCommentDeleteObject",
    "VideoCommentEditObject",
    "VideoCommentNewObject",
    "VideoCommentRestoreObject",
    "VideoNewObject",
    "WallPostNewObject",
    "WallSchedulePostObject",
)
