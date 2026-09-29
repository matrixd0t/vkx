from ...base_model import BaseEnumMeta, StrEnum


class CallbackEventType(StrEnum, metaclass=BaseEnumMeta):
    # Сообщения
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_EVENT = "message_event"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGE_READ = "message_read"
    MESSAGE_REACTION_EVENT = "message_reaction_event"

    # Фотографии
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"

    # Аудиозаписи
    AUDIO_NEW = "audio_new"

    # Видеозаписи
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    VIDEO_COMMENT_DELETE = "video_comment_delete"

    # Записи на стене
    WALL_POST_NEW = "wall_post_new"
    WALL_REPOST = "wall_repost"
    WALL_SCHEDULE_POST_NEW = "wall_schedule_post_new"
    WALL_SCHEDULE_POST_DELETE = "wall_schedule_post_delete"

    # Комментарии на стене
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"

    # Отметки «Нравится»
    LIKE_ADD = "like_add"
    LIKE_REMOVE = "like_remove"

    # Обсуждения
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"

    # Товары
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_ORDER_NEW = "market_order_new"
    MARKET_ORDER_EDIT = "market_order_edit"

    # Пользователи
    GROUP_JOIN = "group_join"
    GROUP_LEAVE = "group_leave"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"

    # Платные подписки VK Donut
    DONUT_SUBSCRIPTION_CREATE = "donut_subscription_create"
    DONUT_SUBSCRIPTION_PROLONGED = "donut_subscription_prolonged"
    DONUT_SUBSCRIPTION_EXPIRED = "donut_subscription_expired"
    DONUT_SUBSCRIPTION_CANCELLED = "donut_subscription_cancelled"
    DONUT_SUBSCRIPTION_PRICE_CHANGED = "donut_subscription_price_changed"
    DONUT_MONEY_WITHDRAW = "donut_money_withdraw"
    DONUT_MONEY_WITHDRAW_ERROR = "donut_money_withdraw_error"

    # Прочее
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    POLL_VOTE_NEW = "poll_vote_new"
    LEAD_FORMS_NEW = "lead_forms_new"
    VKPAY_TRANSACTION = "vkpay_transaction"
    APP_PAYLOAD = "app_payload"

    # Служебное
    CONFIRMATION = "confirmation"


__all__ = ("CallbackEventType",)
