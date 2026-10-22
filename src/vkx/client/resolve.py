"""Резолв упоминаний: ссылки и @упоминания в тексте -> пользователи и сообщества.

Что разбирается в тексте:

- ссылки VK: ``vk.com/durov``, ``vk.ru/id123``, ``m.vk.com/club123``,
  ``vk.com/wall123_456`` (владелец ресурса), ``vk.com/topic123_456``;
- ссылки-приглашения: ``vk.com/invite/CODE`` и ``vk.com/join/CODE`` ->
  сообщество (резолвится методом ``groups.getInviteLinkPreview``);
- упоминания в скобках: ``[id123|@Имя]``, ``[club123|@Имя]``, ``[durov|@Имя]``;
- @упоминания: ``@durov``.

Все найденные id и имена уходят в один ``execute``: ``users.get`` +
``groups.getById`` (+ по одному ``groups.getInviteLinkPreview`` на приглашение).
Если вызовов не больше ``EXECUTE_CALL_LIMIT`` (25) — это один HTTP-запрос к VK
API; больше — запросы режутся на батчи по 25.

Результат кешируется в общем на приложение кеше (``ResolveCache``): ttl и
максимальный размер задаёт клиент, сам кеш общий для всех клиентов процесса.
Хранить его в ``Store`` не нужно: ``Store`` устроен под состояние токенов
(app_id/client/source), а JSON-вариант переписывает файл целиком на каждую
запись — для кеша это лишний ввод-вывод, и кеш всё равно живёт не дольше
процесса.
"""

from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic import ValidationError

from ..models.base_model import BaseModel, Field
from ..models.objects import GroupFull, UserFull

if TYPE_CHECKING:
    from .client import VKClient

DEFAULT_RESOLVE_CACHE_TTL = 3600.0
"""TTL кеша резолва по умолчанию (секунды): час."""

DEFAULT_RESOLVE_CACHE_SIZE = 1000
"""Максимум записей в общем кеше резолва по умолчанию."""

RESOLVE_USER_FIELDS = "photo_50,photo_100,screen_name,sex,bdate,city,country,verified"
"""Поля users.get по умолчанию."""

RESOLVE_GROUP_FIELDS = "description,members_count,site,contacts"
"""Поля groups.getById по умолчанию."""

EXECUTE_CALL_LIMIT = 25
"""Сколько вызовов VK API помещается в один execute."""

RESOLVE_IDS_PER_CALL = 100
"""Сколько id/имён уходит в один users.get / groups.getById."""

RE_VK_INVITE = re.compile(
    r"(?:m\.)?[Vv]k\.(?:com|me|ru)/(?:invite|join)/([^\s.,:;()|\'\"«»/?#]+)"
)
"""Ссылка-приглашение: ``vk.com/invite/CODE`` или ``vk.com/join/CODE``."""

RE_VK_PATH = re.compile(r"(?:m\.)?[Vv]k\.(?:com|me|ru)/([^\s?#]+)")
"""Путь ссылки VK: ``vk.com/durov``, ``vk.com/id123``, ``vk.com/wall123_456``."""

RE_VK_ID = re.compile(r"(id|club|public|event)(\d+)")
"""Числовой идентификатор VK: ``id123``, ``club123``, ``public123``, ``event123``."""

RE_VK_RESOURCE = re.compile(r"(wall|album|photo|topic|page|clip)(-?\d+)_\d+")
"""Владелец ресурса: ``wall123_456``, ``topic123_456``, ``photo-123_456``."""

RE_BRACKET = re.compile(r"\[(?:#alias\|)?([^\[\]|]+)\|[^\[\]]*\]?")
"""Упоминание в скобках: ``[id123|@Имя]``, ``[durov|@Имя]``."""

RE_AT = re.compile(r"(?<![A-Za-zА-Яа-яЁё0-9@_])@([A-Za-z][A-Za-z0-9_.]*)")
"""@упоминание: ``@durov``."""

RE_URL_PREFIX = re.compile(r"^(?:https?://)?(?:m\.)?[Vv]k\.(?:com|me|ru)/")

_RESERVED_PATHS = frozenset(
    {
        "album",
        "albums",
        "apps",
        "audio",
        "clubs",
        "docs",
        "event",
        "events",
        "feed",
        "friends",
        "games",
        "gifts",
        "groups",
        "help",
        "invite",
        "join",
        "market",
        "messages",
        "notifications",
        "offers",
        "orders",
        "page",
        "people",
        "photo",
        "photos",
        "privacy",
        "public",
        "search",
        "settings",
        "store",
        "topic",
        "video",
        "videos",
        "wall",
    }
)
"""Пути VK, которые не бывают именами пользователей или сообществ."""

ModelT = TypeVar("ModelT", bound=BaseModel)


class ResolvedMention(BaseModel):
    """Упоминание, найденное в тексте."""

    raw: str = Field()
    """Фрагмент текста, в котором найдено упоминание."""

    kind: str = Field()
    """Тип упоминания: ``user`` (пользователь), ``group`` (сообщество), ``unknown``."""

    id: int | None = Field(
        default=None,
    )
    """id пользователя или сообщества, если удалось определить."""

    screen_name: str | None = Field(
        default=None,
    )
    """Краткое имя (``durov``), если объект найден по имени."""


class ResolveResult(BaseModel):
    """Результат резолва упоминаний в тексте: найденные пользователи и сообщества."""

    users: list[UserFull] = Field(
        default_factory=list,
    )
    """Пользователи, которых упоминает текст."""

    groups: list[GroupFull] = Field(
        default_factory=list,
    )
    """Сообщества, которых упоминает текст."""

    mentions: list[ResolvedMention] = Field(
        default_factory=list,
    )
    """Все найденные упоминания (в порядке появления в тексте)."""


@dataclass(frozen=True, slots=True)
class Mention:
    """Упоминание в тексте (до обращения к API)."""

    kind: str  # "user" | "group" | "screen" | "invite"
    value: str  # id (цифрами) | краткое имя | код приглашения
    raw: str  # исходный фрагмент текста


class ResolveCache:
    """Кеш резолва, общий на приложение (по умолчанию — один на процесс).

    Ключи: ``u:<id>`` — пользователь, ``g:<id>`` — сообщество, ``s:<name>`` —
    краткое имя (пара ``(kind, id)``), ``i:<code>`` — код приглашения (id
    сообщества). Значение хранится вместе с меткой времени; клиент сам решает,
    протухла ли запись (его ttl), и пополняет кеш.

    Максимальный размер задаёт клиент: при записи, если общий кеш больше лимита,
    вытесняются самые старые записи.
    """

    def __init__(self) -> None:
        self._entries: dict[str, tuple[Any, float]] = {}

    def get(self, key: str, ttl: float) -> Any | None:
        """Запись из кеша, если она свежая (ttl <= 0 — кеш выключен)."""
        if ttl <= 0:
            return None
        item = self._entries.get(key)
        if item is None:
            return None
        value, stamp = item
        if time.monotonic() - stamp > ttl:
            return None
        return value

    def set(
        self,
        key: str,
        value: Any,
        *,
        max_size: int = DEFAULT_RESOLVE_CACHE_SIZE,
    ) -> None:
        """Положить запись в кеш и ужать его до max_size (вытесняются старые)."""
        self._entries[key] = (value, time.monotonic())
        self._evict(max_size)

    def _evict(self, max_size: int) -> None:
        if max_size <= 0:
            self._entries.clear()
            return
        overflow = len(self._entries) - max_size
        if overflow <= 0:
            return
        oldest = sorted(self._entries.items(), key=lambda item: item[1][1])
        for key, _ in oldest[:overflow]:
            self._entries.pop(key, None)

    def clear(self) -> None:
        """Очистить кеш (например, при смене токена)."""
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)


RESOLVE_CACHE = ResolveCache()
"""Кеш резолва по умолчанию: общий на приложение."""


def _classify(identifier: str) -> tuple[str, str] | None:
    """Идентификатор из текста -> (``user``/``group``/``screen``, значение)."""
    ident = identifier.strip().strip(".,;:!?")
    if not ident:
        return None
    match = RE_VK_ID.fullmatch(ident)
    if match:
        prefix, digits = match.group(1), match.group(2)
        return ("user" if prefix == "id" else "group", digits)
    match = RE_VK_RESOURCE.fullmatch(ident)
    if match:
        kind, owner = match.group(1), match.group(2)
        if owner.startswith("-"):
            # фото/стена сообщества: владелец отрицательный
            return ("group", owner[1:])
        if kind == "topic":
            return ("group", owner)
        if kind == "page":
            # старая страница: владелец мог быть и пользователем, и сообществом
            return ("screen", owner)
        return ("user", owner)
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*", ident):
        if ident.lower() in _RESERVED_PATHS:
            return None
        return ("screen", ident)
    return None


def parse_mentions(text: str) -> list[Mention]:
    """Упоминания пользователей и сообществ в тексте (без обращения к API)."""
    found: list[tuple[int, Mention]] = []
    seen: set[tuple[str, str]] = set()
    bracket_spans: list[tuple[int, int]] = []

    def add(kind: str, value: str, raw: str, pos: int) -> None:
        key = (kind, value)
        if key in seen:
            return
        seen.add(key)
        found.append((pos, Mention(kind, value, raw)))

    for match in RE_VK_INVITE.finditer(text):
        add("invite", match.group(1), match.group(0), match.start())

    for match in RE_VK_PATH.finditer(text):
        head = match.group(1).split("/", 1)[0]
        if head.lower() in ("invite", "join"):
            continue  # ссылка-приглашение уже разобрана
        classified = _classify(head)
        if classified is not None:
            add(classified[0], classified[1], match.group(0), match.start())

    for match in RE_BRACKET.finditer(text):
        bracket_spans.append(match.span())
        inner = RE_URL_PREFIX.sub("", match.group(1).strip())
        classified = _classify(inner)
        if classified is not None:
            add(classified[0], classified[1], match.group(0), match.start())

    for match in RE_AT.finditer(text):
        if any(start <= match.start() < end for start, end in bracket_spans):
            continue  # отображаемое имя внутри скобок — не краткое имя
        classified = _classify(match.group(1).rstrip("."))
        if classified is not None and classified[0] == "screen":
            add("screen", classified[1], match.group(0), match.start())

    found.sort(key=lambda item: item[0])
    return [item[1] for item in found]


def _chunks(items: list[Any], size: int) -> list[list[Any]]:
    """Список -> куски по size элементов."""
    if size <= 0:
        return [items] if items else []
    return [items[index : index + size] for index in range(0, len(items), size)]


def _vkscript(method: str, params: dict[str, Any]) -> str:
    """method + params -> строка VKScript для execute."""
    clean = {key: value for key, value in params.items() if value is not None}
    return f"API.{method}({json.dumps(clean, ensure_ascii=False, separators=(',', ':'))})"


async def _execute(
    client: VKClient,
    calls: list[tuple[str, str, dict[str, Any]]],
) -> list[tuple[str, str, dict[str, Any], Any]]:
    """Выполнить вызовы VK API через execute (по 25 вызовов на запрос).

    ``calls`` — список ``(метка, метод, параметры)``; возвращается список
    ``(метка, метод, параметры, результат)`` в том же порядке.
    """
    results: list[tuple[str, str, dict[str, Any], Any]] = []
    for chunk in _chunks(calls, EXECUTE_CALL_LIMIT):
        code = (
            "return ["
            + ",".join(_vkscript(method, params) for _, method, params in chunk)
            + "];"
        )
        response, errors = await client.execute_raw(code)
        values = response if isinstance(response, list) else []
        for index, (tag, method, params) in enumerate(chunk):
            results.append((tag, method, params, values[index] if index < len(values) else None))
        for error in errors:
            client.logger.warning(
                "resolve: %s — %s",
                error.get("method"),
                error.get("error_msg"),
            )
    return results


def _validate[modelT: BaseModel](model: type[modelT], item: Any, logger: logging.Logger) -> modelT | None:
    """Проверить ответ VK в модель; негодные элементы пропускаются."""
    try:
        return model.model_validate(item)
    except ValidationError as exc:
        logger.warning("resolve: не удалось разобрать ответ VK (%s): %s", model.__name__, exc)
        return None


def _read_users(value: Any, logger: logging.Logger) -> dict[int, UserFull]:
    """Ответ users.get -> пользователи по id."""
    result: dict[int, UserFull] = {}
    for item in value or []:
        user = _validate(UserFull, item, logger)
        if user is not None:
            result[user.id] = user
    return result


def _read_groups(value: Any, logger: logging.Logger) -> dict[int, GroupFull]:
    """Ответ groups.getById -> сообщества по id (пустое имя — заглушка VK)."""
    result: dict[int, GroupFull] = {}
    groups = value.get("groups") if isinstance(value, dict) else None
    for item in groups or []:
        group = _validate(GroupFull, item, logger)
        if group is not None and group.name:
            result[group.id] = group
    return result


def _read_profiles(value: Any, logger: logging.Logger) -> dict[int, UserFull]:
    """Ответ groups.getById -> профили (пользователи) по id."""
    result: dict[int, UserFull] = {}
    profiles = value.get("profiles") if isinstance(value, dict) else None
    for item in profiles or []:
        user = _validate(UserFull, item, logger)
        if user is not None:
            result[user.id] = user
    return result


async def resolve_texts(
    client: VKClient,
    texts: list[str],
    *,
    ttl: float = DEFAULT_RESOLVE_CACHE_TTL,
    max_size: int = DEFAULT_RESOLVE_CACHE_SIZE,
    user_fields: str = RESOLVE_USER_FIELDS,
    group_fields: str = RESOLVE_GROUP_FIELDS,
) -> list[ResolveResult]:
    """Резолвить упоминания во всех текстах (запросы VK API батчатся вместе)."""
    mentions = [parse_mentions(text) for text in texts]
    cache = RESOLVE_CACHE
    logger = client.logger

    # --- что искать ---
    want_users: set[int] = set()
    want_groups: set[int] = set()
    want_screens: set[str] = set()
    want_invites: set[str] = set()
    for items in mentions:
        for item in items:
            if item.kind == "user":
                want_users.add(int(item.value))
            elif item.kind == "group":
                want_groups.add(int(item.value))
            elif item.kind == "screen":
                want_screens.add(item.value.lower())
            elif item.kind == "invite":
                want_invites.add(item.value)

    # --- что уже есть в кеше ---
    screens: dict[str, tuple[str, int]] = {}
    pending_screens: set[str] = set()
    for name in want_screens:
        cached = cache.get(f"s:{name}", ttl)
        if isinstance(cached, tuple) and len(cached) == 2:
            screens[name] = (str(cached[0]), int(cached[1]))
        else:
            pending_screens.add(name)

    invites: dict[str, int] = {}
    pending_invites: set[str] = set()
    for code in want_invites:
        cached = cache.get(f"i:{code}", ttl)
        if isinstance(cached, int):
            invites[code] = cached
        else:
            pending_invites.add(code)

    for kind, oid in screens.values():
        (want_users if kind == "user" else want_groups).add(oid)

    need_users = {uid for uid in want_users if cache.get(f"u:{uid}", ttl) is None}
    need_groups = {gid for gid in want_groups if cache.get(f"g:{gid}", ttl) is None}

    # --- один execute: пользователи, сообщества, приглашения ---
    calls: list[tuple[str, str, dict[str, Any]]] = []
    user_ids = sorted(need_users) + sorted(pending_screens)
    group_ids = sorted(need_groups) + sorted(pending_screens)
    for chunk in _chunks(user_ids, RESOLVE_IDS_PER_CALL):
        calls.append(
            (
                "users",
                "users.get",
                {"user_ids": ",".join(str(value) for value in chunk), "fields": user_fields},
            )
        )
    for chunk in _chunks(group_ids, RESOLVE_IDS_PER_CALL):
        calls.append(
            (
                "groups",
                "groups.getById",
                {"group_ids": ",".join(str(value) for value in chunk), "fields": group_fields},
            )
        )
    for code in sorted(pending_invites):
        calls.append(("invite", "groups.getInviteLinkPreview", {"link": code}))

    fetched_users: dict[int, UserFull] = {}
    fetched_groups: dict[int, GroupFull] = {}
    if calls:
        for tag, _method, params, value in await _execute(client, calls):
            if tag == "users":
                fetched_users.update(_read_users(value, logger))
            elif tag == "groups":
                fetched_groups.update(_read_groups(value, logger))
                fetched_users.update(_read_profiles(value, logger))
            elif tag == "invite":
                link = value.get("invite_link") if isinstance(value, dict) else None
                group_id = link.get("group_id") if isinstance(link, dict) else None
                if isinstance(group_id, int):
                    invites[str(params.get("link"))] = group_id

    # --- приглашения дали id сообществ: их тоже нужно догрузить ---
    missing_groups = sorted(
        gid
        for gid in set(invites.values())
        if gid not in fetched_groups and cache.get(f"g:{gid}", ttl) is None
    )
    if missing_groups:
        calls = []
        for chunk in _chunks(missing_groups, RESOLVE_IDS_PER_CALL):
            calls.append(
                (
                    "groups",
                    "groups.getById",
                    {"group_ids": ",".join(str(value) for value in chunk), "fields": group_fields},
                )
            )
        for tag, _method, _params, value in await _execute(client, calls):
            if tag == "groups":
                fetched_groups.update(_read_groups(value, logger))

    # --- краткие имена, которые нашлись в ответе ---
    for user in fetched_users.values():
        if user.screen_name:
            screens.setdefault(user.screen_name.lower(), ("user", user.id))
    for group in fetched_groups.values():
        if group.screen_name:
            screens.setdefault(group.screen_name.lower(), ("group", group.id))

    # --- кеш ---
    if ttl > 0:
        for uid, user in fetched_users.items():
            cache.set(f"u:{uid}", user, max_size=max_size)
        for gid, group in fetched_groups.items():
            cache.set(f"g:{gid}", group, max_size=max_size)
        for name, (kind, oid) in screens.items():
            cache.set(f"s:{name}", (kind, oid), max_size=max_size)
        for code, gid in invites.items():
            cache.set(f"i:{code}", gid, max_size=max_size)

    # --- результат по каждому тексту ---
    results: list[ResolveResult] = []
    for items in mentions:
        users: list[UserFull] = []
        groups: list[GroupFull] = []
        found_mentions: list[ResolvedMention] = []
        seen_users: set[int] = set()
        seen_groups: set[int] = set()
        for item in items:
            kind = "unknown"
            oid: int | None = None
            screen_name: str | None = None
            if item.kind == "user":
                kind, oid = "user", int(item.value)
            elif item.kind == "group":
                kind, oid = "group", int(item.value)
            elif item.kind == "screen":
                resolved = screens.get(item.value.lower())
                if resolved is not None:
                    kind, oid = resolved
                    screen_name = item.value
            elif item.kind == "invite":
                gid = invites.get(item.value)
                if gid is not None:
                    kind, oid = "group", gid

            if kind == "user" and oid is not None:
                user = fetched_users.get(oid)
                if user is None:
                    user = cache.get(f"u:{oid}", ttl)
                if user is not None:
                    if oid not in seen_users:
                        seen_users.add(oid)
                        users.append(user)
                    screen_name = screen_name or user.screen_name
            elif kind == "group" and oid is not None:
                group = fetched_groups.get(oid)
                if group is None:
                    group = cache.get(f"g:{oid}", ttl)
                if group is not None:
                    if oid not in seen_groups:
                        seen_groups.add(oid)
                        groups.append(group)
                    screen_name = screen_name or group.screen_name

            found_mentions.append(
                ResolvedMention(
                    raw=item.raw,
                    kind=kind,
                    id=oid,
                    screen_name=screen_name,
                )
            )
        results.append(ResolveResult(users=users, groups=groups, mentions=found_mentions))
    return results


__all__ = (
    "DEFAULT_RESOLVE_CACHE_SIZE",
    "DEFAULT_RESOLVE_CACHE_TTL",
    "EXECUTE_CALL_LIMIT",
    "RESOLVE_CACHE",
    "RESOLVE_GROUP_FIELDS",
    "RESOLVE_IDS_PER_CALL",
    "RESOLVE_USER_FIELDS",
    "Mention",
    "ResolveCache",
    "ResolveResult",
    "ResolvedMention",
    "parse_mentions",
    "resolve_texts",
)
