"""Источники токенов: всё через протокол TokenSource.

TokenSource — Protocol с одним методом:
    async def token(self, method: str | None = None) -> str | None

Реализации:
- StaticTokenSource — статичный токен пользователя ИЛИ сообщества (разница
  определяется при probe клиента: users.get пуст -> groups.getById).
- WebCookieSource    — cookies (p + remixsid), веб-токен обновляется не чаще
  refresh_seconds (по умолчанию 5 минут) через login.vk.ru?act=web_token.
- PasswordCookieSource — сохранённые cookies с резервным входом через VK ID
  по логину/паролю, если cookie-сессия больше не выдаёт web-токен.

Выбор токена по правам (permissions/scope) делает VKClient, не источник.
У всех источников есть необязательный store: если он задан, токен и владелец
запоминаются в State (vkx.storage), где колонки app_id / client / source
адресуют запись, user_id — пользователь, group_id — сообщество. При
инвалидации токена (error 5) клиент вызывает invalidate и запись удаляется.
"""

from __future__ import annotations

import base64
import contextlib
import hashlib
import json
import re
import secrets
import string
import time
from collections.abc import Iterable
from typing import Any, Protocol, Self, cast, runtime_checkable

from .http import API_HOST, HttpClient, create_http_client, override_user_agent
from .storage import State, Store

WEB_TOKEN_URL = "https://login.vk.ru/?act=web_token"
WEB_TOKEN_APP_ID = 6287487
REQUIRED_WEB_COOKIES = ("p", "remixsid")
WEB_AUTH_URL = "https://id.vk.ru/auth"
WEB_AUTH_APP_ID = 7913379
WEB_LOGIN_API_VERSION = "5.207"
WEB_LOGIN_METHODS = (
    "push",
    "email",
    "qr_code",
    "codegen",
    "sms",
    "callreset",
    "password",
    "reserve_code",
    "passkey",
)

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
        with contextlib.suppress(Exception):  # сбой персистентности не ломает авторизацию
            await self.save_state(self.state())

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
        with contextlib.suppress(Exception):
            await self.delete_state()

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
    переживают перезапуск через Store (по умолчанию SQLite CWD/.vkx/vkx.sqlite).
    Если ответ VK содержит новые p/remixsid в Set-Cookie, источник сохраняет
    их для следующих запросов. Это не продлевает сессию без решения сервера.
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
        """Обновить веб-токен и принять новые значения cookies, если их прислал VK."""
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
        cookies_updated = self._update_cookies(response)
        try:
            data = response.json()["data"]
            value = str(data["access_token"])
            expires = float(data["expires"])
        except (ValueError, KeyError, TypeError) as exc:
            if cookies_updated:
                await self._save()
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

    def _update_cookies(self, response: Any) -> bool:
        """Скопировать ротацию p/remixsid из Set-Cookie-ответа HTTP-клиента."""
        response_cookies = getattr(response, "cookies", None)
        items = getattr(response_cookies, "items", None)
        if not callable(items):
            return False

        cookies = self._cookies
        if cookies is None:
            return False

        updated = False
        entries = cast(Iterable[tuple[str, object]], items())
        for name, value in entries:
            if name in REQUIRED_WEB_COOKIES and cookies.get(name) != str(value):
                cookies[name] = str(value)
                updated = True
        return updated

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
        with contextlib.suppress(Exception):
            await self.delete_state()

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
        self._restore_state(state)

    def _restore_state(self, state: State) -> None:
        """Восстановить поля базового web-cookie источника из состояния."""
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


class PasswordCookieSource(WebCookieSource):
    """Cookies из store или новый вход через VK ID по логину и паролю.

    Коды подтверждения и капчи автоматически не обходятся: если VK требует их,
    источник сообщает, что вход только по логину/паролю невозможен.
    """

    def __init__(
        self,
        login: str,
        password: str | None = None,
        *,
        app_id: int = WEB_TOKEN_APP_ID,
        client: str = "default",
        source: str | None = None,
        refresh_seconds: float = 300.0,
        http: HttpClient | None = None,
        store: Store | None = None,
        user_agent: str | None = None,
    ) -> None:
        if not login or not login.strip():
            raise ValueError("login: укажите логин VK")
        if password == "":
            raise ValueError("password: пароль не может быть пустым")
        source = source or (
            "password-" + hashlib.sha256(login.strip().casefold().encode("utf-8")).hexdigest()[:16]
        )
        self._login = login
        self._password = password
        self._auth_cookies: dict[str, str] = {}
        super().__init__(
            None,
            app_id=app_id,
            client=client,
            source=source,
            refresh_seconds=refresh_seconds,
            http=http,
            store=store,
        )
        if user_agent is not None:
            override_user_agent(self._http, user_agent)

    def __repr__(self) -> str:
        return f"PasswordCookieSource(app_id={self._app_id}, client={self._client_label!r})"

    def state(self) -> State:
        state = super().state()
        state.login = self._login
        state.password = self._password
        return state

    def _restore_state(self, state: State) -> None:
        super()._restore_state(state)
        if self._login is None:
            self._login = state.login
        if self._password is None:
            self._password = state.password

    async def token(self, method: str | None = None) -> str | None:
        if not self._loaded:
            await self._restore()
            # Записываем учётные данные до сетевого входа, чтобы они не потерялись,
            # если VK запросит дополнительную проверку или процесс будет прерван.
            if self._store is not None:
                try:
                    await self.save_state(self.state())
                except Exception as exc:
                    raise TokenSourceError(
                        "не удалось сохранить учётные данные в Store"
                    ) from exc
        if self._token is not None and time.time() < self._token_expires:
            return self._token

        cookie_error: TokenSourceError | None = None
        if self._cookies:
            try:
                validate_web_cookies(self._cookies)
                await super().refresh()
                return self._token
            except TokenSourceError as exc:
                cookie_error = exc
                self._token = None
                self._token_expires = 0.0
        return await self._reauthenticate(cookie_error)

    async def invalidate(self) -> None:
        """Сбросить web-токен, сохранив пароль и cookies для следующей попытки."""
        self._token = None
        self._token_expires = 0.0
        await self._save()

    async def _reauthenticate(self, cookie_error: TokenSourceError | None) -> str | None:
        if not self._login or not self._password:
            message = (
                "невозможно авторизоваться только по логину/паролю: "
                "пароль не передан и не найден в store"
            )
            raise TokenSourceError(message, code="password_auth_failed") from cookie_error

        previous_cookies = self._cookies
        self._cookies = None
        try:
            await self._login_with_password()
            await super().refresh()
        except Exception as exc:
            if self._cookies is None:
                self._cookies = previous_cookies
            await self._save()
            reason = str(exc) or type(exc).__name__
            raise TokenSourceError(
                f"невозможно авторизоваться только по логину/паролю: {reason}",
                code="password_auth_failed",
            ) from exc
        return self._token

    async def _login_with_password(self) -> None:
        self._auth_cookies = {}
        jar = getattr(self._http, "cookies", None)
        if self._own_http:
            clear = getattr(jar, "clear", None)
            if callable(clear):
                clear()

        initial_cookies = {"remixmdevice": "1920/1080/2/!!-!!!!"}
        set_cookie = getattr(jar, "set", None)
        if callable(set_cookie):
            set_cookie("remixmdevice", initial_cookies["remixmdevice"], domain=".vk.ru", path="/")
            self._auth_cookies.update(initial_cookies)

        request_kwargs: dict[str, Any] = {
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
        }
        if not callable(set_cookie):
            request_kwargs["cookies"] = initial_cookies
        uuid = "".join(secrets.choice(string.ascii_lowercase) for _ in range(6))
        auth_action = base64.b64encode(
            json.dumps(
                {
                    "name": "qr_auth",
                    "token": "qr_auth_scanned",
                    "entry": {"source": "main", "screen": "start"},
                },
                separators=(",", ":"),
            ).encode("utf-8")
        ).decode("ascii")
        response = await self._http.get(
            WEB_AUTH_URL,
            params={
                "action": auth_action,
                "scheme": "dark",
                "is_redesigned": "1",
                "response_type": "silent_token",
                "v": "1.3.0",
                "redirect_uri": "https://vk.ru/",
                "uuid": uuid,
                "app_id": str(WEB_AUTH_APP_ID),
            },
            **request_kwargs,
        )
        self._capture_cookies(response)
        config = self._parse_login_config(response.text)
        auth = config.get("auth")
        data = config.get("data")
        if not isinstance(auth, dict) or not isinstance(data, dict):
            raise TokenSourceError("VK ID вернул страницу без параметров авторизации")
        try:
            app_id = str(auth["host_app_id"])
            auth_token = str(auth["access_token"])
            anonymous_token = str(auth["anonymous_token"])
            uuid = str(data["uuid"])
        except (KeyError, TypeError) as exc:
            raise TokenSourceError("VK ID не вернул необходимые параметры входа") from exc

        device_id = "".join(
            secrets.choice(string.digits + string.ascii_letters + "-_") for _ in range(21)
        )
        common = {
            "v": WEB_LOGIN_API_VERSION,
            "client_id": app_id,
            "sid": "",
            "device_id": device_id,
            "anonymous_token": anonymous_token,
            "access_token": "",
        }
        account = await self._api_method(
            "auth.validateAccount",
            {
                **common,
                "login": self._login,
                "auth_token": auth_token,
                "super_app_token": "",
                "supported_ways": ",".join(WEB_LOGIN_METHODS),
                "is_switcher_flow": "0",
                "is_edu_flow": "",
                "is_registration": "",
            },
        )
        if not isinstance(account, dict) or not account.get("sid"):
            raise TokenSourceError("VK ID не подтвердил учётную запись")
        sid = str(account["sid"])
        next_step = account.get("next_step")
        if isinstance(next_step, dict):
            verification_method = next_step.get("verification_method")
            if verification_method not in (None, "password"):
                password_available = False
                if next_step.get("has_another_verification_methods"):
                    methods = await self._api_method(
                        "ecosystem.getVerificationMethods",
                        {**common, "sid": sid},
                    )
                    available = methods.get("methods", []) if isinstance(methods, dict) else []
                    password_available = any(
                        isinstance(item, dict) and item.get("name") == "password"
                        for item in available
                    )
                if not password_available:
                    raise TokenSourceError(
                        "VK требует дополнительный код подтверждения; "
                        "вход только по логину/паролю невозможен"
                    )

        await self._login_action(
            "connect_authorize",
            {
                "username": self._login,
                "password": self._password,
                "auth_token": auth_token,
                "sid": sid,
                "uuid": uuid,
                "device_id": device_id,
                "app_id": app_id,
                "v": WEB_LOGIN_API_VERSION,
                "service_group": "",
                "save_user": "1",
                "version": "1",
            },
        )
        cookies = self._all_auth_cookies()
        validate_web_cookies(cookies)
        self._cookies = cookies

    async def _api_method(self, method: str, params: dict[str, Any]) -> Any:
        response = await self._http.post(
            f"{API_HOST}/method/{method}",
            data=params,
            headers={"Origin": "https://id.vk.ru", "Referer": "https://id.vk.ru/"},
        )
        self._capture_cookies(response)
        status_code = getattr(response, "status_code", 200)
        if status_code >= 400:
            raise TokenSourceError(f"{method}: VK вернул HTTP {status_code}")
        try:
            payload = response.json()
        except (ValueError, TypeError) as exc:
            raise TokenSourceError(f"{method}: VK вернул некорректный ответ") from exc
        if not isinstance(payload, dict):
            raise TokenSourceError(f"{method}: VK вернул неожиданный ответ")
        error = payload.get("error")
        if isinstance(error, dict):
            code = error.get("error_code")
            message = error.get("error_msg") or "ошибка VK API"
            raise TokenSourceError(f"{method}: {message}", code=code)
        return payload.get("response", payload)

    async def _login_action(self, action: str, params: dict[str, Any]) -> Any:
        response = await self._http.post(
            f"https://login.vk.ru/?act={action}",
            data=params,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://id.vk.ru",
                "Referer": "https://id.vk.ru/",
            },
        )
        self._capture_cookies(response)
        status_code = getattr(response, "status_code", 200)
        if status_code >= 400:
            raise TokenSourceError(f"{action}: VK вернул HTTP {status_code}")
        try:
            payload = response.json()
        except (ValueError, TypeError) as exc:
            raise TokenSourceError(f"{action}: VK вернул некорректный ответ") from exc
        if not isinstance(payload, dict):
            raise TokenSourceError(f"{action}: VK вернул неожиданный ответ")
        if payload.get("type") == "captcha":
            raise TokenSourceError("VK запросил капчу; автоматический вход только по паролю невозможен")
        if payload.get("type") != "okay":
            code = payload.get("error_code")
            if code == "incorrect_password":
                message = "VK отклонил логин или пароль"
            else:
                message = payload.get("error_info") or "VK отклонил вход"
            raise TokenSourceError(str(message), code=code)
        result = payload.get("data", payload)
        if isinstance(result, dict) and result.get("is_user_banned"):
            raise TokenSourceError("учётная запись VK заблокирована")
        return result

    @staticmethod
    def _parse_login_config(text: str) -> dict[str, Any]:
        match = re.search(r"window\.init\s*=", text)
        if match is None:
            raise TokenSourceError("не удалось найти параметры VK ID на странице входа")
        start = text.find("{", match.end())
        if start < 0:
            raise TokenSourceError("не удалось разобрать параметры VK ID на странице входа")
        try:
            payload, _ = json.JSONDecoder().raw_decode(text[start:])
        except ValueError as exc:
            raise TokenSourceError("не удалось разобрать параметры VK ID на странице входа") from exc
        if not isinstance(payload, dict):
            raise TokenSourceError("VK ID вернул некорректные параметры входа")
        return payload

    def _capture_cookies(self, response: Any) -> None:
        self._copy_cookie_items(getattr(response, "cookies", None))
        if self._own_http:
            self._copy_cookie_items(getattr(self._http, "cookies", None))

    def _copy_cookie_items(self, jar: Any) -> None:
        items = getattr(jar, "items", None)
        if callable(items):
            try:
                entries = cast(Iterable[tuple[object, object]], items())
                self._auth_cookies.update({str(key): str(value) for key, value in entries})
            except (TypeError, ValueError):
                return

    def _all_auth_cookies(self) -> dict[str, str]:
        if self._own_http:
            self._copy_cookie_items(getattr(self._http, "cookies", None))
        return dict(self._auth_cookies)
