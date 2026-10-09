"""Типизированные ошибки VK API.

Совместимость: любая из ошибок — по-прежнему ``VKError``, поэтому
``except VKError`` ловит всё, а поле ``.code`` осталось целым числом.
"""

from __future__ import annotations

import copy
import enum
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .client import PendingApiCall, VKClient


class VKErrorCode(enum.IntEnum):
    """Коды ошибок VK API (``error_code``)."""

    UNKNOWN = 1
    APP_DISABLED = 2
    UNKNOWN_METHOD = 3
    INVALID_SIGNATURE = 4
    AUTH_FAILED = 5
    TOO_MANY_REQUESTS = 6
    PERMISSION_DENIED = 7
    INVALID_REQUEST = 8
    FLOOD_CONTROL = 9
    INTERNAL_SERVER_ERROR = 10
    CAPTCHA_NEEDED = 14
    ACCESS_DENIED = 15
    VALIDATION_REQUIRED = 17
    USER_DELETED = 18
    METHOD_DISABLED = 23
    GROUP_AUTH_FAILED = 27
    APP_AUTH_FAILED = 28
    RATE_LIMIT_REACHED = 29
    PARAMETER_INVALID = 100
    ACCESS_TO_POST_DENIED = 214


# Коды, при которых имеет смысл повторить запрос (троттлинг/внутренний сбой).
TRANSIENT_ERROR_CODES = frozenset({1, 6, 9, 10, 29})
# Авторизационные коды: токен мёртв либо вот-вот протухнет — нужен refresh.
AUTH_ERROR_CODES = frozenset({5, 27, 28})
# Код полной инвалидации токена: запись удаляется из store.
INVALID_TOKEN_CODE = 5
# Код 6/29 — часто оба означают «сбрось темп».
RATE_LIMIT_ERROR_CODES = frozenset({6, 29})
# Код «требуется капча».
CAPTCHA_ERROR_CODE = 14


def _as_str(value: Any) -> str | None:
    return None if value is None else str(value)


class VKError(RuntimeError):
    """Ошибка VK API. Хранит ссылки на клиент и вызвавший её запрос (PendingApiCall)."""

    def __init__(
        self,
        message: str,
        *,
        client: VKClient | None = None,
        call: PendingApiCall | None = None,
        code: int | None = None,
        raw: Any = None,
    ) -> None:
        super().__init__(message)
        self.client = client
        self.call = call
        self.code = code
        self.raw = raw

    def __repr__(self) -> str:
        return f"{type(self).__name__}(code={self.code!r}, {str(self)!r})"

    @property
    def error_code(self) -> VKErrorCode | None:
        """Код как enum, если он известен (иначе None)."""
        if self.code is None:
            return None
        try:
            return VKErrorCode(self.code)
        except ValueError:
            return None

    @property
    def payload(self) -> Mapping[str, Any]:
        """Нормализованный объект ошибки VK (без обёртки ``{"error": ...}``)."""
        raw = self.raw
        if isinstance(raw, Mapping):
            error = raw.get("error")
            if isinstance(error, Mapping):
                return error
            return raw
        return {}

    @property
    def retry_after(self) -> float | None:
        """Рекомендованная пауза из ответа VK (``retry_after``/``ratelimit``), если есть."""
        data = self.payload
        value = data.get("retry_after")
        ratelimit = data.get("ratelimit")
        if value is None and isinstance(ratelimit, Mapping):
            value = ratelimit.get("retry_after")
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    @property
    def captcha_sid(self) -> str | None:
        return _as_str(self.payload.get("captcha_sid"))

    @property
    def captcha_img(self) -> str | None:
        return _as_str(self.payload.get("captcha_img"))

    @property
    def redirect_uri(self) -> str | None:
        return _as_str(self.payload.get("redirect_uri"))

    @property
    def is_auth(self) -> bool:
        """Нужен refresh/смена токена (5/27/28)."""
        return self.code in AUTH_ERROR_CODES

    @property
    def is_invalid_token(self) -> bool:
        """Токен недействителен безвозвратно (5)."""
        return self.code == INVALID_TOKEN_CODE

    @property
    def is_rate_limit(self) -> bool:
        """Троттлинг VK (6/29)."""
        return self.code in RATE_LIMIT_ERROR_CODES

    @property
    def is_captcha(self) -> bool:
        """VK просит капчу (14)."""
        return self.code == CAPTCHA_ERROR_CODE

    @property
    def is_retryable(self) -> bool:
        """Ошибку имеет смысл повторить (троттлинг, внутренний сбой, транспорт)."""
        return isinstance(self, VKTransportError) or self.code in TRANSIENT_ERROR_CODES

    def bind(self, call: PendingApiCall) -> VKError:
        """Копия ошибки (того же класса), привязанная к конкретному вызову."""
        if self.call is call:
            return self
        clone = copy.copy(self)
        clone.call = call
        return clone


class VKAuthError(VKError):
    """Авторизационная ошибка (5/27/28): нужен refresh или смена токена."""


class VKInvalidTokenError(VKAuthError):
    """Токен недействителен безвозвратно (5)."""


class VKPermissionError(VKError):
    """Действие запрещено для токена/владельца (7/15)."""


class VKRequestError(VKError):
    """Некорректный запрос: неверные/отсутствующие параметры (100 и т.п.)."""


class VKRateLimitError(VKError):
    """Слишком много запросов (6/29). Пауза — в ``retry_after``."""


class VKFloodError(VKError):
    """Flood control (9). Пауза — в ``retry_after``."""


class VKServerError(VKError):
    """Внутренний сбой на стороне VK (10)."""


class VKCaptchaError(VKError):
    """VK требует капчу (14). Поля — ``captcha_sid``/``captcha_img``/``redirect_uri``."""


class VKTransportError(VKError):
    """Сбой транспорта: сеть, таймаут или HTTP 5xx/429 без тела ошибки VK."""


class VKTimeoutError(VKError):
    """Запрос не получил ответ за отведённое время (клиентский таймаут).

    Возникает, когда ``call(timeout=...)`` не дождался результата: запрос мог
    ещё выполняться на стороне VK, но ожидание прекращено.
    """


class VKValidationError(VKError):
    """Ответ VK не соответствует ожидаемой модели.

    ``validation_error`` хранит исходную ошибку Pydantic, а ``raw_response`` и
    ``raw_responses`` — текст HTTP-ответа (или страниц при автопагинации).
    """

    def __init__(
        self,
        message: str,
        *,
        validation_error: Exception,
        raw_response: str | None = None,
        raw_responses: tuple[str, ...] = (),
        **kwargs: Any,
    ) -> None:
        super().__init__(message, **kwargs)
        self.validation_error = validation_error
        self.raw_response = raw_response
        self.raw_responses = raw_responses or (
            (raw_response,) if raw_response is not None else ()
        )


_CODE_CLASSES: dict[int, type[VKError]] = {
    5: VKInvalidTokenError,
    27: VKAuthError,
    28: VKAuthError,
    6: VKRateLimitError,
    29: VKRateLimitError,
    9: VKFloodError,
    10: VKServerError,
    14: VKCaptchaError,
    7: VKPermissionError,
    15: VKPermissionError,
    100: VKRequestError,
}


def build_error(
    message: str,
    *,
    code: int | None = None,
    client: VKClient | None = None,
    call: PendingApiCall | None = None,
    raw: Any = None,
) -> VKError:
    """Создаёт ``VKError`` подходящего подкласса по коду."""
    cls = _CODE_CLASSES.get(code, VKError) if code is not None else VKError
    return cls(message, client=client, call=call, code=code, raw=raw)
