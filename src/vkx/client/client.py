"""VKClient: выбор токена по правам (scope), привязка к владельцу и батчинг через execute.

Клиент жёстко привязан к владельцу: user_id > 0 — пользователь, user_id < 0 —
сообщество. Владелец и тип токена определяются при probe: users.get пуст ->
groups.getById (токен группы). Владельцем становится первый успешно опрошенный
источник; остальные источники с чужим user_id отбрасываются.

    vk = VKClient(tokens=["tok_a"], cookies=[{"p": ..., "remixsid": ...}])
    await vk.probe()
    vk.permissions  # ['Сообщения', 'Друзья', ...]
    await vk.call("messages.send", peer_id=1, message="hi")

Источники токенов задаются тремя необязательными полями: tokens (строки или
TokenSource), cookies (словари с p и remixsid) и sources (готовые TokenSource).
Из tokens/cookies источники создаются автоматически; можно передавать один
элемент или iterable. Все полученные источники опрашиваются при probe: нерабочие
отбрасываются с логированием причины, а источники с чужим владельцем — по id
первого рабочего.

HTTP: клиент работает с протоколом HttpClient (асинхронные get/post); httpx —
опциональная зависимость, создаётся лениво, если свой клиент не передан.
http_client / base_api_url / v задаются у клиента и могут быть переопределены
для отдельного запроса (call); у клиента по умолчанию base_api_url=API_HOST,
v=API_VERSION.

Очередь и батчинг: call() фиксирует маршрут запроса (_Queued: кандидаты, HTTP-
настройки и текущий источник) и кладёт его в очередь; PendingApiCall ждёт
событие с результатом. Раз в interval (DEFAULT_USER_INTERVAL для пользователя,
DEFAULT_GROUP_INTERVAL для сообщества; переопределяется при инициализации
клиента) клиент забирает все запросы из очереди и отправляет батчами через
execute (_call_batch):
VKScript собирает _vkscript_call: не более EXECUTE_BATCH_LIMIT вызовов и не
длиннее EXECUTE_CODE_BYTES_LIMIT байт кода на батч (остаток уходит следующим).
Ошибки внутри execute (execute_errors) раздаются конкретным запросам;
авторизационные ошибки (5/27/28) -> duck-refresh источника либо следующий
кандидат. Снаружи ничего не меняется: await vk.call(...) возвращает результат
одиночного метода.
"""

from __future__ import annotations

import asyncio
import contextlib
import contextvars
import inspect
import json
import logging
import time
from collections import deque
from collections.abc import AsyncIterator, Awaitable, Callable, Iterable, Mapping
from dataclasses import dataclass
from typing import Any, Self

from ..models.categories import APICategories
from . import pagination
from .errors import VKError, VKTimeoutError, VKTransportError, build_error
from .http import API_HOST, API_VERSION, HttpClient, create_http_client
from .storage import Store
from .tokens import (
    ALL_SCOPES,
    StaticTokenSource,
    TokenSource,
    TokenSourceError,
    WebCookieSource,
    method_scope,
    scope_titles,
    validate_web_cookies,
)
from .upload import UploadNamespace

EXECUTE_BATCH_LIMIT = 25
EXECUTE_CODE_BYTES_LIMIT = 260_000
DEFAULT_USER_INTERVAL = 0.5
DEFAULT_GROUP_INTERVAL = 0.1
MAX_BATCH_RETRIES = 2
DEFAULT_MAX_RETRIES = 2
DEFAULT_RETRY_BACKOFF = 0.5
MAX_ADAPTIVE_BACKOFF = 30.0

CookieMap = Mapping[str, str]
TokenInput = str | TokenSource
TokensInput = TokenInput | Iterable[TokenInput] | None
CookiesInput = CookieMap | Iterable[CookieMap] | None
SourcesInput = TokenSource | Iterable[TokenSource] | None
CaptchaHandler = Callable[[VKError], "Awaitable[Mapping[str, str] | None] | Mapping[str, str] | None"]
"""Обработчик капчи: получает VKCaptchaError, возвращает лишние параметры запроса."""


@dataclass(frozen=True, slots=True)
class _Overrides:
    """Переопределения уровня запроса: ``None`` — взять значение клиента."""

    batching: bool | None = None
    pagination: bool | None = None


_overrides: contextvars.ContextVar[_Overrides] = contextvars.ContextVar(
    "vkx_overrides",
    default=_Overrides(),  # noqa: B039 — _Overrides заморожен (frozen), не мутируется
)
"""Активные переопределения (``vk.overrides(...)``); по умолчанию — значения клиента."""


def _is_transient_exception(exc: BaseException) -> bool:
    """True для сетевых сбоев, которые имеет смысл повторить (без импорта httpx)."""
    if isinstance(exc, (TimeoutError, ConnectionError)):
        return True
    return type(exc).__name__ in {
        "TimeoutException",
        "TransportError",
        "ConnectError",
        "ConnectTimeout",
        "ReadTimeout",
        "WriteTimeout",
        "PoolTimeout",
        "ReadError",
        "WriteError",
        "RemoteProtocolError",
    }


def _retry_after_header(response: Any) -> float | None:
    """Retry-After из заголовков ответа, если HTTP-клиент их отдаёт."""
    headers = getattr(response, "headers", None)
    if headers is None:
        return None
    try:
        value = headers.get("Retry-After") or headers.get("retry-after")
    except AttributeError:
        return None
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _stringify(value: Any) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (list, tuple, set)):
        return ",".join(_stringify(item) for item in value)
    return str(value)


def _vkscript_call(method: str, params: dict[str, Any]) -> str:
    """method, params -> строка VKScript: 'API.messages.send({...})'."""
    clean: dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            value = int(value)
        clean[key] = value
    return f"API.{method}({json.dumps(clean, ensure_ascii=False, separators=(',', ':'))})"


_BATCH_CODE_EMPTY = "return [];"


def _split_execute_batches(regular: list[_Queued]) -> list[list[_Queued]]:
    """Режет вызовы на батчи по количеству и по накопленной длине VKScript (UTF-8 байты).

    Кусочки добавляются по порядку, пока не упрёмся в EXECUTE_BATCH_LIMIT вызовов
    или в EXECUTE_CODE_BYTES_LIMIT байт кода: тогда батч отправляется без
    очередного кусочка, а тот начинает следующий. Один слишком длинный вызов
    уходит отдельным батчем (дробить его нечем).
    """
    batches: list[list[_Queued]] = []
    current: list[_Queued] = []
    current_bytes = len(_BATCH_CODE_EMPTY)
    for item in regular:
        chunk_bytes = len(
            _vkscript_call(item.request.method, item.request.params).encode("utf-8")
        )
        extra = chunk_bytes + (1 if current else 0)  # 1 — разделитель-запятая
        if current and (
            len(current) >= EXECUTE_BATCH_LIMIT
            or current_bytes + extra > EXECUTE_CODE_BYTES_LIMIT
        ):
            batches.append(current)
            current = []
            current_bytes = len(_BATCH_CODE_EMPTY)
            extra = chunk_bytes
        current.append(item)
        current_bytes += extra
    if current:
        batches.append(current)
    return batches


def _as_list(value: Any) -> list[Any]:
    """Один элемент или iterable -> список (строки/TokenSource не разбираются посимвольно)."""
    if value is None:
        return []
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        return [value]
    return list(value)


def _iter_cookie_dicts(cookies: CookiesInput) -> list[dict[str, str]]:
    """Нормализует cookies (один словарь или iterable) и проверяет p + remixsid."""
    if cookies is None:
        return []
    items = [cookies] if isinstance(cookies, Mapping) else list(cookies)
    result: list[dict[str, str]] = []
    for item in items:
        if not isinstance(item, Mapping):
            raise TypeError(f"cookies: ожидался словарь, получено {item!r}")
        value = {str(key): str(val) for key, val in item.items()}
        validate_web_cookies(value)
        result.append(value)
    return result


def _token_sources(tokens: TokensInput, *, store: Store | None = None) -> list[TokenSource]:
    """Строки -> StaticTokenSource; готовые TokenSource используются как есть.

    store прокидывается в автоматически созданные источники (свой store готового
    источника не переопределяется).
    """
    result: list[TokenSource] = []
    for index, item in enumerate(_as_list(tokens)):
        if isinstance(item, str):
            result.append(StaticTokenSource(item, store=store, source=f"static{index}"))
        elif isinstance(item, TokenSource):
            result.append(item)
        else:
            raise TypeError(f"токен {item!r} должен быть строкой или TokenSource")
    return result


def _source_objects(sources: SourcesInput) -> list[TokenSource]:
    """Готовые источники, реализующие TokenSource."""
    result: list[TokenSource] = []
    for item in _as_list(sources):
        if not isinstance(item, TokenSource):
            raise TypeError(f"источник {item!r} не реализует TokenSource.token()")
        result.append(item)
    return result


def _is_invalid_token_error(exc: BaseException) -> bool:
    """True, если в цепочке причин есть VKError с кодом инвалидации токена (5)."""
    seen: set[int] = set()
    while exc is not None and id(exc) not in seen:
        seen.add(id(exc))
        if isinstance(exc, VKError) and exc.is_invalid_token:
            return True
        exc = exc.__cause__  # type: ignore[assignment]
    return False


@dataclass(eq=False)
class TokenSourceEntry:
    """Источник токена + результат probe."""

    source: TokenSource
    user_id: int | None = None  # >0 — пользователь, <0 — сообщество
    kind: str | None = None  # "user" | "group"
    name: str | None = None
    permissions: int | None = None  # None — права неизвестны, считаем полным доступом

    @property
    def group_id(self) -> int | None:
        """id сообщества (>0) для группового токена, иначе None."""
        if self.user_id is not None and self.user_id < 0:
            return -self.user_id
        return None


class PendingApiCall:
    """Запись одного запроса: метод, параметры, требуемый scope + событие ожидания.

    Никакой маршрутизации: каким токеном поедет запрос — решает клиент
    (см. _Queued — его запись в очереди). ``timeout`` ограничивает ожидание
    ответа; по истечении запрос помечается ``cancelled``, а ожидающий получает
    ``VKTimeoutError``.
    """

    __slots__ = (
        "cancelled",
        "client",
        "error",
        "event",
        "method",
        "params",
        "result",
        "scope",
        "timeout",
    )

    def __init__(
        self,
        method: str,
        params: dict[str, Any],
        *,
        client: VKClient | None = None,
        timeout: float | None = None,
    ) -> None:
        self.method = method
        self.params = params
        self.scope = method_scope(method)
        self.event = asyncio.Event()
        self.result: Any = None
        self.error: VKError | None = None
        self.client = client
        self.timeout = timeout
        self.cancelled = False

    def set_result(self, value: Any) -> None:
        if self.cancelled:
            return
        self.result = value
        self.event.set()

    def set_error(self, error: VKError) -> None:
        if self.cancelled:
            return
        self.error = error.bind(self)
        self.event.set()

    async def wait(self) -> Any:
        if self.timeout is None:
            await self.event.wait()
        else:
            try:
                await asyncio.wait_for(self.event.wait(), self.timeout)
            except TimeoutError:
                self.cancelled = True
                raise VKTimeoutError(
                    f"{self.method}: таймаут ожидания ответа ({self.timeout} с)",
                    client=self.client,
                    call=self,
                ) from None
        if self.error is not None:
            raise self.error
        return self.result


@dataclass
class _Queued:
    """Маршрут запроса, фиксированный клиентом: кандидаты и HTTP-настройки запроса."""

    request: PendingApiCall
    candidates: list[TokenSourceEntry]  # источники, чьи права покрывают scope метода
    http_client: HttpClient  # разрешённый для запроса HTTP-клиент
    base_api_url: str  # разрешённый базовый URL API
    v: str  # разрешённая версия API
    batch: bool = True  # участвовать ли в execute-батче (False — прямой вызов)
    index: int = 0  # текущий кандидат
    refreshes: int = 0  # duck-refresh попытки на текущем кандидате
    retries: int = 0  # повторы из-за временных ошибок VK
    captchas: int = 0  # повторы после обработки капчи
    not_before: float = 0.0  # monotonic-время, раньше которого запрос не отправляем

    @property
    def entry(self) -> TokenSourceEntry:
        return self.candidates[self.index]


class _CategoryApi:
    """Мост между сгенерированными категориями и VKClient.

    Категории ждут ``await api.request(method, params)`` -> envelope ``{"response": ...}``,
    поэтому оборачиваем результат ``VKClient.call``.
    """

    __slots__ = ("_client",)

    def __init__(self, client: VKClient) -> None:
        self._client = client

    async def request(self, method: str, params: dict[str, Any]) -> Any:
        if method == "execute":
            return await self._client.call(method, **params)
        result = await self._request_paginated(method, params)
        return {"response": result}

    async def _request_paginated(self, method: str, params: dict[str, Any]) -> Any:
        """Вызов метода с автопагинацией: зажать count, добрать страницы, слить."""
        if not self._client._effective_pagination():
            # Автопагинация выключена: одна страница, тело ответа как есть.
            return await self._client.call(method, **params)
        original = params.get("count")
        requested = int(original) if original is not None else None
        call_params = params
        limit = pagination.limit_for(method)
        if limit is not None:
            page_count = limit if requested is None else min(requested, limit)
            call_params = {**params, "count": page_count}
        try:
            result = await self._client.call(method, **call_params)
        except VKError as exc:
            learned = pagination.parse_count_limit(exc)
            if learned is None or "count" not in call_params:
                raise
            pagination.remember_limit(method, learned)
            call_params = {
                **call_params,
                "count": min(int(call_params["count"]), learned),
            }
            result = await self._client.call(method, **call_params)
        return await pagination.paginate(
            lambda page: self._client.call(method, **page),
            method,
            call_params,
            result,
            requested,
        )


class VKClient(APICategories):
    """Клиент VK API: источники токенов одного владельца, очередь и батчинг execute.

    Источники задаются необязательными tokens (строки/TokenSource), cookies
    (словари с p и remixsid; проверяются сразу) и sources (готовые TokenSource);
    tokens/cookies превращаются в источники автоматически, можно смешивать.
    Конструктор не обращается к сети. probe() (автоматически при первом call())
    опрашивает все источники: нерабочие отбрасываются с логированием причины,
    клиент привязывается к владельцу первого валидного токена (user_id
    пользователя >0 или -id сообщества <0), источники с чужим владельцем
    отбрасываются.
    """

    def __init__(
        self,
        tokens: TokensInput = None,
        cookies: CookiesInput = None,
        sources: SourcesInput = None,
        *,
        logger: logging.Logger | None = None,
        http_client: HttpClient | None = None,
        base_api_url: str = API_HOST,
        v: str = API_VERSION,
        lang: int = 0,
        store: Store | None = None,
        interval: float | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_backoff: float = DEFAULT_RETRY_BACKOFF,
        timeout: float | None = None,
        captcha_handler: CaptchaHandler | None = None,
        batching: bool = True,
        pagination: bool = True,
    ) -> None:
        if interval is not None and interval < 0:
            raise ValueError("interval: пауза между запросами не может быть отрицательной")
        if max_retries < 0:
            raise ValueError("max_retries: число повторов не может быть отрицательным")
        if retry_backoff < 0:
            raise ValueError("retry_backoff: базовая пауза не может быть отрицательной")
        if timeout is not None and timeout <= 0:
            raise ValueError("timeout: ожидание ответа должно быть положительным")
        cookie_dicts = _iter_cookie_dicts(cookies)
        token_sources = _token_sources(tokens, store=store)
        explicit_sources = _source_objects(sources)
        self._own_http = http_client is None
        self._http: HttpClient = http_client or create_http_client()
        self._base_api_url = base_api_url.rstrip("/")
        built: list[TokenSource] = [
            *token_sources,
            *(
                WebCookieSource(item, http=self._http, store=store, source=f"web{index}")
                for index, item in enumerate(cookie_dicts)
            ),
            *explicit_sources,
        ]
        self._entries = [TokenSourceEntry(s) for s in built]
        self._user_id: int | None = None
        self._logger = logger or logging.getLogger(__name__)
        self._store = store
        self._v = v
        self._lang = lang
        self._interval = interval
        self._max_retries = max_retries
        self._retry_backoff = retry_backoff
        self._timeout = timeout
        self._adaptive_backoff = retry_backoff
        self._cooldown_until = 0.0
        self._captcha_handler = captcha_handler
        self._batching = batching
        self._pagination = pagination
        self._probed = False
        self._probe_lock = asyncio.Lock()
        self._queue: deque[_Queued] = deque()
        self._flush_task: asyncio.Task | None = None
        self._drain_lock = asyncio.Lock()
        self._closed = False

    @property
    def api_instance(self) -> _CategoryApi:
        """Хост для сгенерированных категорий (``vk.board``, ``vk.messages``, ...)."""
        return _CategoryApi(self)

    def _effective_batching(self) -> bool:
        """Батчинг с учётом активного переопределения (``vk.overrides``)."""
        override = _overrides.get().batching
        return self._batching if override is None else override

    def _effective_pagination(self) -> bool:
        """Автопагинация с учётом активного переопределения (``vk.overrides``)."""
        override = _overrides.get().pagination
        return self._pagination if override is None else override

    @contextlib.asynccontextmanager
    async def overrides(
        self,
        *,
        batching: bool | None = None,
        pagination: bool | None = None,
    ) -> AsyncIterator[VKClient]:
        """Временно переопределить батчинг/пагинацию (оба включены по умолчанию).

        Действует на все запросы внутри блока; ``None`` оставляет текущее
        значение. Пример: ``async with vk.overrides(pagination=False): ...``.
        """
        current = _overrides.get()
        token = _overrides.set(
            _Overrides(
                batching=current.batching if batching is None else batching,
                pagination=current.pagination if pagination is None else pagination,
            )
        )
        try:
            yield self
        finally:
            _overrides.reset(token)

    @property
    def upload(self) -> UploadNamespace:
        """Хелперы загрузки файлов: ``vk.upload.photo_to_wall(data, ...)``."""
        return UploadNamespace(self)

    def __repr__(self) -> str:
        name = self._entries[0].name if self._entries else None
        owner = self._user_id if self._user_id is not None else "?"
        return f"VKClient({name or '<не опрошен>'}, owner={owner}, источников: {len(self._entries)})"

    # ---------- probe ----------

    async def probe(self) -> VKClient:
        """Опрашивает источники и привязывает клиент к владельцу первого токена."""
        async with self._probe_lock:
            if self._probed:
                return self
            if not self._entries:
                raise VKError("клиент без источников токенов", client=self)
            owner: int | None = None
            valid: list[TokenSourceEntry] = []
            last_error: Exception | None = None
            for entry in self._entries:
                try:
                    await self._probe(entry)
                except (TokenSourceError, VKError) as exc:
                    last_error = exc
                    if _is_invalid_token_error(exc):
                        await self._invalidate(entry.source)
                    self._logger.warning(
                        "проверка токена не удалась для %r: %s", entry.source, exc
                    )
                    continue
                if owner is None:
                    owner = entry.user_id
                    self._logger.info("владелец клиента: user_id=%s (%s)", owner, entry.kind)
                if entry.user_id != owner:
                    self._logger.warning(
                        "источник %r принадлежит user_id=%s, а не %s — отбрасываю",
                        entry.source,
                        entry.user_id,
                        owner,
                    )
                    continue
                valid.append(entry)
            if not valid:
                if isinstance(last_error, TokenSourceError):
                    raise last_error
                if isinstance(last_error, VKError):
                    # Транзиентный сбой (6/9/10/…): не маскируем его общим текстом,
                    # чтобы вызывающий видел код и мог повторить probe.
                    raise last_error
                raise VKError("не удалось определить владельца токенов", client=self) from last_error
            self._entries = valid
            self._user_id = owner
            for entry in valid:
                source = entry.source
                if hasattr(source, "user_id"):
                    setattr(source, "user_id", entry.user_id)  # noqa: B010
                if hasattr(source, "group_id"):
                    setattr(source, "group_id", entry.group_id)  # noqa: B010
                commit = getattr(source, "commit_state", None)
                if commit is not None:
                    await commit()
            self._probed = True
            self._logger.info("probe завершён: user_id=%s, источников=%d", owner, len(valid))
        return self

    async def _probe(self, entry: TokenSourceEntry) -> None:
        """Владелец и права одного токена: users.get -> groups.getById для групп."""
        if entry.user_id is not None:
            return
        token = await entry.source.token(None)
        if token is None:
            raise TokenSourceError(f"{entry.source!r}: источник не выдал токен")
        self._logger.debug("проверка токена %r: users.get", entry.source)
        users: list[Any] = []
        probe_error: VKError | None = None
        try:
            payload = await self._api("users.get", {}, entry=entry)
            users = payload.get("response") or []
        except VKError as exc:
            if exc.is_retryable:
                # Транзиентный сбой (6/9/10/…): это не значит «токен группы» —
                # отдаём ошибку наверх, чтобы probe/вызывающий повторил позже.
                raise
            probe_error = exc
        if users:
            user = users[0]
            entry.user_id = int(user["id"])
            entry.kind = "user"
            entry.name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
            self._logger.debug("токен %r: пользователь id=%s", entry.source, entry.user_id)
            payload = await self._api("account.getAppPermissions", {}, entry=entry)
            response = payload.get("response")
            raw = response.get("permissions") if isinstance(response, dict) else response
            if raw is None:
                raise VKError(
                    "account.getAppPermissions: не удалось получить permissions",
                    client=self,
                    raw=payload,
                )
            entry.permissions = int(raw)
            self._logger.debug("токен %r: permissions=%s", entry.source, entry.permissions)
            return
        self._logger.debug("токен %r: пользователь не найден, groups.getById", entry.source)
        try:
            payload = await self._api("groups.getById", {}, entry=entry)
        except VKError as exc:
            raise TokenSourceError(
                f"{entry.source!r}: не удалось определить владельца токена "
                f"(ни пользователь, ни сообщество)"
            ) from (probe_error or exc)
        groups = payload.get("response")
        if isinstance(groups, dict):
            groups = groups.get("groups") or []
        if not groups:
            raise TokenSourceError(
                f"{entry.source!r}: не удалось определить владельца токена"
            ) from probe_error
        group = groups[0]
        entry.user_id = -int(group["id"])
        entry.kind = "group"
        entry.name = group.get("name")
        entry.permissions = None  # права сообщества VK не отдаёт — считаем полным доступом
        self._logger.debug("токен %r: сообщество id=%s", entry.source, entry.user_id)

    async def _invalidate(self, source: TokenSource) -> None:
        """Инвалидированный токен: забыть в источнике и удалить запись из store."""
        invalidate = getattr(source, "invalidate", None)
        if invalidate is None:
            return
        try:
            await invalidate()
            self._logger.info("недействительный токен источника %r удалён", source)
        except Exception as exc:  # noqa: BLE001 — сбой очистки не должен ронять клиента
            self._logger.warning("не удалось удалить токен источника %r: %r", source, exc)

    async def _ensure_probed(self) -> None:
        if not self._probed:
            await self.probe()

    def _require_probed(self) -> None:
        if not self._probed:
            raise VKError("клиент не опрошен: await vk.probe()", client=self)

    # ---------- низкоуровневый вызов API ----------

    def _retry_delay(self, attempt: int, retry_after: float | None = None) -> float:
        """Пауза перед повтором: retry_after от VK либо адаптивный backoff."""
        if retry_after is not None and retry_after > 0:
            return retry_after
        delay = self._adaptive_backoff * (2 ** max(attempt - 1, 0))
        return min(delay, MAX_ADAPTIVE_BACKOFF)

    def _note_rate_limit(self, retry_after: float | None = None) -> float:
        """VK просит сбавить темп: растёт общий backoff и cooldown для всех запросов.

        Возвращает паузу, на которую выставлен cooldown.
        """
        self._adaptive_backoff = min(self._adaptive_backoff * 2, MAX_ADAPTIVE_BACKOFF)
        delay = retry_after if retry_after is not None and retry_after > 0 else self._adaptive_backoff
        self._cooldown_until = max(self._cooldown_until, time.monotonic() + delay)
        return delay

    def _note_success(self) -> None:
        """Успешный ответ: постепенно сбрасываем адаптивный backoff."""
        if self._adaptive_backoff > self._retry_backoff:
            self._adaptive_backoff = self._retry_backoff

    async def _respect_cooldown(self) -> None:
        """Ждёт окончания общего cooldown, выставленного троттлингом VK."""
        delay = self._cooldown_until - time.monotonic()
        if delay > 0:
            await asyncio.sleep(delay)

    async def _call_captcha_handler(self, error: VKError) -> Mapping[str, str] | None:
        """Спрашивает у captcha_handler параметры для повтора (captcha_key и т.п.)."""
        handler = self._captcha_handler
        if handler is None:
            return None
        try:
            result: Any = handler(error)
            if inspect.isawaitable(result):
                result = await result
        except Exception as exc:  # noqa: BLE001 — сбой обработчика не должен ронять клиента
            self._logger.warning("captcha_handler упал: %r", exc)
            return None
        return dict(result) if result else None

    async def _api(
        self,
        method: str,
        params: dict[str, Any],
        *,
        entry: TokenSourceEntry | None = None,
        http_client: HttpClient | None = None,
        base_api_url: str | None = None,
        v: str | None = None,
    ) -> dict[str, Any]:
        """Сырой вызов VK API (без очереди и батчинга). Возвращает полный payload.

        http_client / base_api_url / v переопределяют настройки клиента для этого
        вызова; None означает «взять из клиента». Транзиентные сбои (сеть, HTTP
        5xx/429 и коды 1/6/9/10/29) повторяются до max_retries раз с паузой
        retry_backoff (или retry_after из ответа VK).
        """
        if entry is None:
            if not self._entries:
                raise VKError("клиент без источников токенов", client=self)
            entry = self._entries[0]
        token = await entry.source.token(method)
        if token is None:
            self._logger.warning("источник %r не выдал токен для %s", entry.source, method)
            raise VKError(f"{method}: источник {entry.source!r} не выдал токен", client=self)
        self._logger.debug("VK API %s через %r", method, entry.source)
        data = {
            "v": v if v is not None else self._v,
            "lang": str(self._lang),
            "access_token": token,
        }
        for key, value in params.items():
            if value is None:
                continue
            data[key] = _stringify(value)
        base = (base_api_url or self._base_api_url).rstrip("/")
        http = http_client or self._http
        url = f"{base}/method/{method}"
        attempt = 0
        while True:
            await self._respect_cooldown()
            try:
                response = await http.post(url, data=data)
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # noqa: BLE001 — решение о повторе ниже
                if _is_transient_exception(exc) and attempt < self._max_retries:
                    attempt += 1
                    delay = self._retry_delay(attempt)
                    self._logger.warning(
                        "VK API %s: сетевой сбой (%r), повтор #%d через %.2f с",
                        method,
                        exc,
                        attempt,
                        delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                raise VKTransportError(f"{method}: {exc!r}", client=self) from exc
            status = getattr(response, "status_code", 200)
            if status == 429 or status >= 500:
                if attempt < self._max_retries:
                    attempt += 1
                    delay = self._retry_delay(attempt, _retry_after_header(response))
                    if status == 429:
                        self._cooldown_until = max(
                            self._cooldown_until, time.monotonic() + delay
                        )
                    self._logger.warning(
                        "VK API %s: HTTP %s, повтор #%d через %.2f с",
                        method,
                        status,
                        attempt,
                        delay,
                    )
                    await asyncio.sleep(delay)
                    continue
                raise VKTransportError(
                    f"{method}: HTTP {status}", client=self, raw=response.text[:300]
                )
            try:
                payload: dict[str, Any] = response.json()
            except ValueError as exc:
                raise VKError(
                    f"{method}: некорректный ответ (HTTP {status})",
                    client=self,
                    raw=response.text[:300],
                ) from exc
            error = payload.get("error") if isinstance(payload, dict) else None
            if not error:
                self._note_success()
                return payload
            code = int(error.get("error_code") or 0)
            message = str(error.get("error_msg") or f"VK API error {code}")
            api_error = build_error(message, client=self, code=code, raw=payload)
            if api_error.is_rate_limit:
                self._note_rate_limit(api_error.retry_after)
            if api_error.is_retryable and attempt < self._max_retries:
                attempt += 1
                delay = self._retry_delay(attempt, api_error.retry_after)
                self._logger.warning(
                    "VK API %s: ошибка %s — %s, повтор #%d через %.2f с",
                    method,
                    code,
                    message,
                    attempt,
                    delay,
                )
                await asyncio.sleep(delay)
                continue
            self._logger.warning("VK API %s: ошибка %s — %s", method, code, message)
            raise api_error

    # ---------- свойства ----------

    @property
    def user_id(self) -> int | None:
        """Владелец: id пользователя (>0) или -id сообщества (<0)."""
        return self._user_id

    @property
    def is_group(self) -> bool:
        return self._user_id is not None and self._user_id < 0

    @property
    def kind(self) -> str:
        return "group" if self.is_group else "user"

    @property
    def group_id(self) -> int | None:
        if self._user_id is None or self._user_id >= 0:
            return None
        return -self._user_id

    @property
    def http_client(self) -> HttpClient:
        """HTTP-клиент клиента — для запросов вне VK API (LongPoll, загрузки и т.п.)."""
        return self._http

    @property
    def interval(self) -> float:
        """Пауза между батчами: DEFAULT_USER_INTERVAL или DEFAULT_GROUP_INTERVAL.

        Если interval задан при инициализации клиента — берётся он (запрос
        переопределить интервал не может).
        """
        if self._interval is not None:
            return self._interval
        return DEFAULT_GROUP_INTERVAL if self.is_group else DEFAULT_USER_INTERVAL

    @property
    def scope(self) -> int:
        """Объединённые права всех источников (неизвестные считаются полными)."""
        self._require_probed()
        mask = 0
        for entry in self._entries:
            mask |= entry.permissions if entry.permissions is not None else ALL_SCOPES
        return mask

    @property
    def permissions(self) -> list[str]:
        """Человекочитаемый список категорий методов, доступных клиенту."""
        return scope_titles(self.scope)

    # ---------- очередь и батчинг ----------

    def _ensure_flush_task(self) -> None:
        if self._closed:
            raise VKError("клиент закрыт", client=self)
        if self._flush_task is None or self._flush_task.done():
            self._flush_task = asyncio.get_running_loop().create_task(self._flush_loop())

    async def _flush_loop(self) -> None:
        while True:
            await asyncio.sleep(self.interval)
            if not self._queue:
                continue
            try:
                async with self._drain_lock:
                    await self._drain()
            except Exception:  # noqa: BLE001, S112 — цикл обязан выжить
                continue

    async def _drain(self) -> None:
        """Запросы, чей not_before наступил, -> батчи (по 25) по источнику/HTTP-настройкам."""
        now = time.monotonic()
        cooling = self._cooldown_until > now
        pending: list[_Queued] = []
        deferred: list[_Queued] = []
        while self._queue:
            item = self._queue.popleft()
            if item.request.cancelled:
                continue
            (deferred if cooling or item.not_before > now else pending).append(item)
        if deferred:
            self._queue.extend(deferred)
        if not pending:
            return
        by_route: dict[tuple[Any, ...], list[_Queued]] = {}
        singles: list[_Queued] = []
        for item in pending:
            if not item.batch:  # батчинг отключён для этого запроса — прямой вызов
                singles.append(item)
                continue
            key = (item.entry, id(item.http_client), item.base_api_url, item.v)
            by_route.setdefault(key, []).append(item)
        batches: list[list[_Queued]] = []
        for items in by_route.values():
            regular = [item for item in items if item.request.method != "execute"]
            executes = [item for item in items if item.request.method == "execute"]
            batches.extend(_split_execute_batches(regular))
            for item in executes:
                batches.append([item])
        tasks = [self._call_batch(chunk) for chunk in batches]
        tasks.extend(self._call_single(item) for item in singles)
        if tasks:
            await asyncio.gather(*tasks)

    async def _call_batch(self, items: list[_Queued]) -> None:
        """Обёртка батча: VKScript -> execute -> раздача результатов запросам."""
        entry = items[0].entry
        code = (
            "return ["
            + ",".join(_vkscript_call(item.request.method, item.request.params) for item in items)
            + "];"
        )
        requests = [item.request for item in items]
        if len(items) == 1 and requests[0].method == "execute":
            await self._call_single_execute(items[0])
            return
        try:
            payload = await self._api(
                "execute",
                {"code": code},
                entry=entry,
                http_client=items[0].http_client,
                base_api_url=items[0].base_api_url,
                v=items[0].v,
            )
        except VKError as exc:
            await self._handle_batch_failure(entry, items, exc)
            return
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001 — сеть/клиент: ошибка на весь батч
            self._logger.error("execute-батч упал: %r", exc)
            self._fail_batch(requests, VKError(f"execute: {exc!r}", client=self))
            return
        try:
            await self._distribute_batch(items, payload)
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001
            self._logger.error("раздача execute-батча упала: %r", exc)
            self._fail_batch(requests, VKError(f"execute: {exc!r}", client=self))

    async def _distribute_batch(self, items: list[_Queued], payload: Any) -> None:
        requests = [item.request for item in items]
        if not isinstance(payload, dict):
            self._logger.error("execute: неожиданный ответ %r", payload)
            self._fail_batch(
                requests, VKError(f"execute: неожиданный ответ {payload!r}", client=self)
            )
            return
        response = payload.get("response")
        execute_errors = payload.get("execute_errors") or []
        if not isinstance(response, list):
            self._logger.error("execute: в ответе нет массива response")
            self._fail_batch(
                requests,
                VKError("execute: в ответе нет массива response", client=self, raw=payload),
            )
            return
        remaining_errors = list(range(len(execute_errors)))  # индексы непотреблённых ошибок

        def take_error(method: str) -> dict[str, Any] | None:
            """execute_errors с подходящим именем метода (порядок сохраняется)."""
            for index in remaining_errors:
                if execute_errors[index].get("method") == method:
                    remaining_errors.remove(index)
                    return execute_errors[index]
            return None

        def take_any_error() -> dict[str, Any] | None:
            if remaining_errors:
                return execute_errors[remaining_errors.pop(0)]
            return None

        for position, item in enumerate(items):
            request = item.request
            if request.cancelled:
                continue
            value = response[position] if position < len(response) else None
            # VK помечает упавший вызов в execute значением false (или null)
            if value is not None and value is not False:
                request.set_result(value)
                continue
            raw_error = take_error(request.method)
            if raw_error is None and value is None:
                raw_error = take_any_error()
            if raw_error is None:
                if value is None:
                    self._logger.warning("%s: нет результата в execute", request.method)
                    request.set_error(
                        VKError(
                            f"{request.method}: нет результата в execute",
                            client=self,
                            call=request,
                        )
                    )
                else:
                    request.set_result(False)  # легитимный false-ответ метода
                continue
            code = int(raw_error.get("error_code") or 0)
            message = str(raw_error.get("error_msg") or "ошибка внутри execute")
            error = build_error(message, client=self, call=request, code=code, raw=raw_error)
            if error.is_captcha and self._captcha_handler is not None and item.captchas < 1:
                extra = await self._call_captcha_handler(error)
                if extra:
                    request.params.update(extra)
                    item.captchas += 1
                    self._queue.append(item)
                    self._logger.warning(
                        "%s: требуется капча, повтор с %s", request.method, sorted(extra)
                    )
                    continue
            if error.is_retryable and item.retries < self._max_retries:
                item.retries += 1
                item.not_before = time.monotonic() + self._retry_delay(
                    item.retries, error.retry_after
                )
                self._queue.append(item)
                self._logger.warning(
                    "VK API %s (execute): временная ошибка %s — %s, повтор #%d",
                    request.method,
                    code,
                    message,
                    item.retries,
                )
                continue
            self._logger.warning(
                "VK API %s (execute): ошибка %s — %s", request.method, code, message
            )
            request.set_error(error)

    async def _handle_batch_failure(
        self, entry: TokenSourceEntry, items: list[_Queued], exc: VKError
    ) -> None:
        """Авторизационная ошибка: duck-refresh источника либо следующий кандидат."""
        if not exc.is_auth:
            self._logger.warning("execute-батч: ошибка %s — %s", exc.code, exc)
            self._fail_batch([item.request for item in items], exc)
            return
        self._logger.warning(
            "авторизационная ошибка %s на источнике %r", exc.code, entry.source
        )
        if exc.is_invalid_token:
            await self._invalidate(entry.source)
        refresh = getattr(entry.source, "refresh", None)
        if refresh is not None:
            try:
                await refresh()
                self._logger.info("токен источника %r обновлён", entry.source)
            except Exception as refresh_error:  # noqa: BLE001 — refresh не должен ронять батч
                self._logger.warning(
                    "refresh источника %r не удался: %r", entry.source, refresh_error
                )
        requeue: list[_Queued] = []
        for item in items:
            if item.request.cancelled:
                continue
            if refresh is not None:
                if item.refreshes >= MAX_BATCH_RETRIES:
                    item.request.set_error(exc)
                    continue
                item.refreshes += 1  # токен обновлён — повторяем того же кандидата
            else:
                item.index += 1  # статичный источник не оживёт — следующий кандидат
                if item.index >= len(item.candidates):
                    item.request.set_error(exc)
                    continue
            requeue.append(item)
        self._queue.extend(requeue)

    @staticmethod
    def _fail_batch(requests: list[PendingApiCall], error: VKError) -> None:
        for request in requests:
            request.set_error(error)

    # ---------- публичные вызовы ----------

    async def call(
        self,
        method: str,
        *,
        http_client: HttpClient | None = None,
        base_api_url: str | None = None,
        v: str | None = None,
        timeout: float | None = None,
        batching: bool | None = None,
        **params: Any,
    ) -> Any:
        """Вызов VK API: запрос встаёт в очередь, ответ приходит очередным батчем.

        http_client / base_api_url / v переопределяют настройки клиента для этого
        запроса; если не заданы — берутся настройки клиента (по умолчанию API_HOST
        и API_VERSION). Запросы с разными http_client/base_api_url/v не батчатся
        вместе. ``timeout`` (или значение клиента) ограничивает ожидание ответа:
        по истечении поднимается ``VKTimeoutError``.

        ``batching=False`` выключает батчинг для одного этого запроса: он уйдёт
        прямым вызовом метода, а не через ``execute`` (по умолчанию — значение
        клиента, см. ``vk.overrides``).
        """
        if timeout is not None and timeout <= 0:
            raise ValueError("timeout: ожидание ответа должно быть положительным")
        if self._closed:
            self._logger.warning("вызов %s после закрытия клиента", method)
            raise VKError("клиент закрыт", client=self)
        await self._ensure_probed()
        required = method_scope(method)
        candidates = [
            entry
            for entry in self._entries
            if entry.permissions is None or (entry.permissions & required) == required
        ]
        if not candidates:
            self._logger.warning(
                "нет прав на %s: требуется %s", method, scope_titles(required)
            )
            raise VKError(
                f"{method}: ни у одного источника нет прав {scope_titles(required)} "
                f"(доступно: {scope_titles(self.scope)})",
                client=self,
            )
        request = PendingApiCall(
            method,
            params,
            client=self,
            timeout=timeout if timeout is not None else self._timeout,
        )
        self._queue.append(
            _Queued(
                request,
                candidates,
                http_client or self._http,
                (base_api_url or self._base_api_url).rstrip("/"),
                v if v is not None else self._v,
                batch=self._effective_batching() if batching is None else batching,
            )
        )
        self._ensure_flush_task()
        self._logger.debug("в очередь: %s", method)
        return await request.wait()

    api = call

    async def _call_single(self, item: _Queued) -> None:
        """Прямой вызов метода без ``execute`` (для запросов с выключенным батчингом)."""
        request = item.request
        try:
            payload = await self._api(
                request.method,
                request.params,
                entry=item.entry,
                http_client=item.http_client,
                base_api_url=item.base_api_url,
                v=item.v,
            )
        except VKError as exc:
            if exc.is_captcha and self._captcha_handler is not None and item.captchas < 1:
                extra = await self._call_captcha_handler(exc)
                if extra:
                    request.params.update(extra)
                    item.captchas += 1
                    self._queue.append(item)
                    self._logger.warning(
                        "%s: требуется капча, повтор с %s", request.method, sorted(extra)
                    )
                    return
            await self._handle_batch_failure(item.entry, [item], exc)
            return
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001 — сеть/клиент: ошибка одного запроса
            self._logger.error("%s: прямой вызов упал: %r", request.method, exc)
            request.set_error(VKError(f"{request.method}: {exc!r}", client=self))
            return
        request.set_result(payload.get("response") if isinstance(payload, dict) else payload)

    async def _call_single_execute(self, item: _Queued) -> None:
        """Одиночный execute из очереди: код отправляется как есть, без обёртки в батч."""
        request = item.request
        try:
            payload = await self._api(
                "execute",
                request.params,
                entry=item.entry,
                http_client=item.http_client,
                base_api_url=item.base_api_url,
                v=item.v,
            )
        except VKError as exc:
            await self._handle_batch_failure(item.entry, [item], exc)
            return
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001
            self._logger.error("одиночный execute упал: %r", exc)
            request.set_error(VKError(f"execute: {exc!r}", client=self))
            return
        request.set_result(payload.get("response"))

    # ---------- завершение ----------

    async def drain(self, *, timeout: float | None = None) -> None:
        """Немедленно отправить всё, что в очереди, не дожидаясь ``interval``.

        Повторяет отправку, пока очередь не опустеет или не истечёт ``timeout``
        (тогда ``VKTimeoutError``). Ждёт в том числе повторов после троттлинга,
        капчи и авторизационных ошибок.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        while True:
            async with self._drain_lock:
                await self._drain()
            if not self._queue:
                return
            if deadline is not None and time.monotonic() >= deadline:
                raise VKTimeoutError(
                    "очередь клиента не опустела за отведённое время", client=self
                )
            await asyncio.sleep(0.05)

    async def aclose(self, *, drain: bool = False, timeout: float | None = None) -> None:
        """Закрыть клиент; при ``drain=True`` сначала дождаться отправки очереди."""
        if self._closed:
            return
        if drain:
            try:
                await self.drain(timeout=timeout)
            except VKError as exc:
                self._logger.warning("очередь не опустела при закрытии: %s", exc)
        self._closed = True
        self._logger.debug("закрытие клиента")
        if self._flush_task is not None:
            self._flush_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._flush_task
            self._flush_task = None
        error = VKError("клиент закрыт", client=self)
        while self._queue:
            self._queue.popleft().request.set_error(error)
        if self._own_http:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()
