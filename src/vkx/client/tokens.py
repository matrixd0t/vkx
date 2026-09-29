"""Источники токенов: всё через протокол TokenSource.

TokenSource — Protocol с одним методом:
    async def token(self, method: str | None = None) -> str | None

Реализации:
- StaticTokenSource — статичный токен пользователя ИЛИ сообщества (разница
  определяется при probe клиента: users.get пуст -> groups.getById).
- WebCookieSource    — cookies (p + remixsid), веб-токен обновляется не чаще
  refresh_seconds (по умолчанию 5 минут) через login.vk.ru?act=web_token.

Выбор токена по правам (permissions/scope) делает VKClient, не источник.
У всех источников есть необязательный store: если он задан, токен и владелец
запоминаются в State (vkx.storage), где колонки app_id / client / source
адресуют запись, user_id — пользователь, group_id — сообщество. При
инвалидации токена (error 5) клиент вызывает invalidate и запись удаляется.
"""

from __future__ import annotations

import time
from typing import Any, Protocol, Self, runtime_checkable

from .http import HttpClient, create_http_client
from .storage import State, Store

WEB_TOKEN_URL = "https://login.vk.ru/?act=web_token"
WEB_TOKEN_APP_ID = 6287487
REQUIRED_WEB_COOKIES = ("p", "remixsid")

SCOPE_NOTIFY = 1
SCOPE_FRIENDS = 2
SCOPE_PHOTOS = 4
SCOPE_AUDIO = 8
SCOPE_VIDEO = 16
SCOPE_PAGES = 64
SCOPE_STORIES = 128
SCOPE_STATUS = 1024
SCOPE_NOTES = 2048
SCOPE_MESSAGES = 4096
SCOPE_WALL = 8192
SCOPE_ADS = 32768
SCOPE_DOCS = 131072
SCOPE_GROUPS = 262144
SCOPE_NOTIFICATIONS = 524288
SCOPE_STATS = 1048576
SCOPE_MARKET = 134217728

CATEGORY_SCOPES: dict[str, int] = {
    "notify": SCOPE_NOTIFY,
    "friends": SCOPE_FRIENDS,
    "photos": SCOPE_PHOTOS,
    "audio": SCOPE_AUDIO,
    "video": SCOPE_VIDEO,
    "pages": SCOPE_PAGES,
    "stories": SCOPE_STORIES,
    "status": SCOPE_STATUS,
    "notes": SCOPE_NOTES,
    "messages": SCOPE_MESSAGES,
    "wall": SCOPE_WALL,
    "ads": SCOPE_ADS,
    "docs": SCOPE_DOCS,
    "groups": SCOPE_GROUPS,
    "notifications": SCOPE_NOTIFICATIONS,
    "stats": SCOPE_STATS,
    "market": SCOPE_MARKET,
}

SCOPE_TITLES: dict[int, str] = {
    SCOPE_NOTIFY: "Уведомления",
    SCOPE_FRIENDS: "Друзья",
    SCOPE_PHOTOS: "Фотографии",
    SCOPE_AUDIO: "Аудиозаписи",
    SCOPE_VIDEO: "Видео",
    SCOPE_PAGES: "Wiki-страницы",
    SCOPE_STORIES: "Истории",
    SCOPE_STATUS: "Статус",
    SCOPE_NOTES: "Заметки",
    SCOPE_MESSAGES: "Сообщения",
    SCOPE_WALL: "Стена на стене",
    SCOPE_ADS: "Реклама",
    SCOPE_DOCS: "Документы",
    SCOPE_GROUPS: "Сообщества",
    SCOPE_NOTIFICATIONS: "Ответы и упоминания",
    SCOPE_STATS: "Статистика",
    SCOPE_MARKET: "Товары",
}

ALL_SCOPES = sum(CATEGORY_SCOPES.values())


def method_scope(method: str) -> int:
    """Требуемый бит scope для метода: префикс категории -> бит scope."""
    category = method.split(".", 1)[0].lower()
    return CATEGORY_SCOPES.get(category, 0)


def scope_titles(mask: int) -> list[str]:
    """Человекочитаемые названия категорий по битовой маске."""
    return [title for bit, title in SCOPE_TITLES.items() if mask & bit]


def scope_keys(mask: int) -> list[str]:
    """Английские имена категорий (notify, friends, ...) по битовой маске."""
    return [key for key, bit in CATEGORY_SCOPES.items() if mask & bit]


class TokenSourceError(RuntimeError):
    def __init__(self, message: str, *, code: str | int | None = None, raw: Any = None) -> None:
        super().__init__(message)
        self.code = code
        self.raw = raw


@runtime_checkable
class TokenSource(Protocol):
    """Поставщик токена.

    Возвращает токен, пригодный для method, либо None, если пригодного нет.
    """

    async def token(self, method: str | None = None) -> str | None: ...


class _StatefulSource:
    """Общая персистентность State: адрес (app_id, client, source) + необязательный store.

    Если store задан, состояние источника (токен, владелец, cookies) сохраняется
    и восстанавливается. Владелец-сообщество хранится в колонке group_id, а не в
    user_id (user_id — только для пользователя).
    """

    user_id: int | None = None
    group_id: int | None = None

    _app_id: int
    _client_label: str
    _source_label: str
    _store: Store | None

    @property
    def identity(self) -> tuple[int, str, str]:
        """Адрес состояния: (app_id, client, source)."""
        return self._app_id, self._client_label, self._source_label

    async def load_state(self) -> State | None:
        if self._store is None:
            return None
        return await self._store.load(*self.identity)

    async def save_state(self, state: State) -> None:
        if self._store is not None:
            await self._store.save(state)

    async def delete_state(self) -> None:
        """Удалить состояние источника из store (например, при инвалидации токена)."""
        if self._store is not None:
            await self._store.delete(*self.identity)

    def owner_columns(self) -> tuple[int | None, int | None]:
        """(user_id, group_id) для State: у сообщества user_id пуст, id — в group_id."""
        user_id, group_id = self.user_id, self.group_id
        if user_id is not None and user_id < 0:
            if group_id is None:
                group_id = -user_id
            user_id = None
        return user_id, group_id

    async def commit_state(self) -> None:
        """Сохранить текущее состояние (клиент вызывает после probe)."""
        await self._save()

    async def _save(self) -> None:
        if self._store is None:
            return
        try:
            await self.save_state(self.state())
        except Exception:  # noqa: BLE001, S110 — сбой персистентности не ломает авторизацию
            pass

    def state(self) -> State:
        raise NotImplementedError


class StaticTokenSource(_StatefulSource):
    """Статичный токен (пользователя или сообщества) без обновления.

    С store токен и его владелец запоминаются при probe: источник можно создать
    без токена и восстановить его из базы. При инвалидации (error 5) запись
    удаляется, а токен забывается.
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        label: str | None = None,
        app_id: int = WEB_TOKEN_APP_ID,
        client: str = "default",
        source: str = "static",
        store: Store | None = None,
    ) -> None:
        self._token = str(token) if token is not None else None
        self.label = label
        self._app_id = app_id
        self._client_label = client
        self._source_label = source
        self._store = store
        self.user_id: int | None = None
        self.group_id: int | None = None
        self._loaded = False

    def __repr__(self) -> str:
        if self.label:
            name = self.label
        elif self._token:
            name = self._token[:8] + "..."
        else:
            name = "<из store>"
        return f"StaticTokenSource({name})"

    async def token(self, method: str | None = None) -> str | None:
        if self._token is None and not self._loaded:
            await self._restore()
        return self._token

    async def invalidate(self) -> None:
        """Токен недействителен: забыть его и удалить запись из store."""
        self._token = None
        self._loaded = True
        try:
            await self.delete_state()
        except Exception:  # noqa: BLE001, S110
            pass

    def state(self) -> State:
        user_id, group_id = self.owner_columns()
        return State(
            app_id=self._app_id,
            client=self._client_label,
            source=self._source_label,
            user_id=user_id,
            group_id=group_id,
            token=self._token,
            updated_at=time.time(),
        )

    @classmethod
    def from_env(cls, name: str, **kwargs: Any) -> StaticTokenSource:
        import os

        value = os.environ.get(name)
        if not value:
            raise TokenSourceError(f"переменная окружения {name} не задана")
        return cls(value, label=name, **kwargs)

    async def _restore(self) -> None:
        self._loaded = True
        state = await self.load_state()
        if state is None:
            return
        if state.token:
            self._token = state.token
        if state.group_id is not None:
            self.group_id = state.group_id
            self.user_id = -state.group_id
        elif state.user_id is not None:
            self.user_id = state.user_id


def validate_web_cookies(cookies: dict[str, str]) -> None:
    """Проверяет обязательные cookies веб-сессии (p и remixsid)."""
    missing = [name for name in REQUIRED_WEB_COOKIES if not cookies.get(name)]
    if missing:
        raise TokenSourceError(
            "WebCookieSource: cookies должны содержать " + " и ".join(missing)
        )


class WebCookieSource(_StatefulSource):
    """Cookies (p + remixsid) -> веб-токен, обновляемый не чаще refresh_seconds.

    refresh_seconds=300 — токен живёт максимум 5 минут, затем обновляется.
    Если VK вернул свой expires — берётся минимальный срок. Cookies и токен
    переживают перезапуск через Store (по умолчанию SQLite CWD/.vkx/vkx.sqlite);
    переопределите load_state/save_state для другого хранилища.
    """

    def __init__(
        self,
        cookies: dict[str, str] | None = None,
        *,
        app_id: int = WEB_TOKEN_APP_ID,
        client: str = "default",
        source: str = "web",
        refresh_seconds: float = 300.0,
        http: HttpClient | None = None,
        store: Store | None = None,
    ) -> None:
        self._app_id = app_id
        self._client_label = client
        self._source_label = source
        self._refresh_seconds = refresh_seconds
        self._store = store
        self._own_http = http is None
        self._http = http or create_http_client()
        self._cookies = dict(cookies) if cookies else None
        if self._cookies:
            validate_web_cookies(self._cookies)
        self._token: str | None = None
        self._token_expires = 0.0
        self._loaded = False
        self.user_id: int | None = None
        self.group_id: int | None = None

    @property
    def cookies(self) -> dict[str, str]:
        return dict(self._cookies or {})

    def __repr__(self) -> str:
        return f"WebCookieSource(app_id={self._app_id}, client={self._client_label!r})"

    async def token(self, method: str | None = None) -> str | None:
        if not self._loaded:
            await self._restore()
        if self._token is not None and time.time() < self._token_expires:
            return self._token
        await self.refresh()
        return self._token

    async def refresh(self) -> None:
        """Обновление веб-токена по cookies (не чаще, чем раз в refresh_seconds)."""
        await self._ensure_cookies()
        response = await self._http.post(
            WEB_TOKEN_URL,
            data={"version": "1", "app_id": str(self._app_id)},
            headers={
                "Origin": "https://vk.ru",
                "Referer": "https://vk.ru/",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            cookies=self._cookies,
        )
        try:
            data = response.json()["data"]
            value = str(data["access_token"])
            expires = float(data["expires"])
        except (ValueError, KeyError, TypeError) as exc:
            raise TokenSourceError(
                f"act=web_token: не удалось получить токен (HTTP {response.status_code}) "
                f"— сессия истекла, либо ошибка: {response.text[:200]}"
            ) from exc
        now = time.time()
        if expires < now:
            expires += now
        self._token = value
        self._token_expires = (
            min(now + self._refresh_seconds, expires) if self._refresh_seconds else expires
        )
        await self._save()

    # --- персистентность состояния ---

    def state(self) -> State:
        cookies = self._cookies or {}
        user_id, group_id = self.owner_columns()
        return State(
            app_id=self._app_id,
            client=self._client_label,
            source=self._source_label,
            user_id=user_id,
            group_id=group_id,
            token=self._token,
            token_expires=self._token_expires or None,
            cookie_p=cookies.get("p"),
            cookie_remixsid=cookies.get("remixsid"),
            updated_at=time.time(),
        )

    async def invalidate(self) -> None:
        """Токен недействителен: забыть его и удалить запись из store (cookies остаются)."""
        self._token = None
        self._token_expires = 0.0
        try:
            await self.delete_state()
        except Exception:  # noqa: BLE001, S110
            pass

    async def aclose(self) -> None:
        if self._own_http:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()

    # --- внутренности ---

    async def _restore(self) -> None:
        """Cookies из аргументов приоритетны; иначе cookies и токен из store (если свежий)."""
        self._loaded = True
        if self._cookies is not None:
            return
        state = await self.load_state()
        if state is None:
            return
        if state.cookie_p or state.cookie_remixsid:
            self._cookies = {}
            if state.cookie_p:
                self._cookies["p"] = state.cookie_p
            if state.cookie_remixsid:
                self._cookies["remixsid"] = state.cookie_remixsid
        if state.token and state.token_expires and time.time() < state.token_expires:
            self._token = state.token
            self._token_expires = state.token_expires
        if state.group_id is not None:
            self.group_id = state.group_id
            self.user_id = -state.group_id
        elif state.user_id is not None:
            self.user_id = state.user_id

    async def _ensure_cookies(self) -> dict[str, str]:
        if not self._loaded:
            await self._restore()
        if not self._cookies:
            raise TokenSourceError(
                "WebCookieSource: нет cookies — передайте {'p': ..., 'remixsid': ...} "
                "или укажите store с сохранённым состоянием"
            )
        return self._cookies
