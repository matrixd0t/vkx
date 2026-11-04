"""Типизированное хранилище состояния источников токенов.

Запись State адресуется осмысленными колонками (app_id, client, source) —
никаких составных строковых ключей и анонимных k/v: каждая колонка таблицы
имеет собственный смысл (cookie_p / cookie_remixsid — имена cookie,
token_expires — срок токена, user_id — владелец-пользователь, group_id —
владелец-сообщество, login / password — данные PasswordCookieSource).

Реализации Store: SQLiteStore (по умолчанию, CWD/.vkx/vkx.sqlite), JSONStore, MemoryStore.
"""

from __future__ import annotations

import asyncio
import json
import os
import sqlite3
import threading
import time
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

DEFAULT_STATE_DIR = Path.cwd() / ".vkx"
DEFAULT_DB_PATH = DEFAULT_STATE_DIR / "vkx.sqlite"

_UPSERT = """
INSERT INTO states (
    app_id, client, source, user_id, group_id, token,
    token_expires, cookie_p, cookie_remixsid, updated_at, login, password
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(app_id, client, source) DO UPDATE SET
    user_id = excluded.user_id,
    group_id = excluded.group_id,
    token = excluded.token,
    token_expires = excluded.token_expires,
    cookie_p = excluded.cookie_p,
    cookie_remixsid = excluded.cookie_remixsid,
    updated_at = excluded.updated_at,
    login = excluded.login,
    password = excluded.password
"""


@dataclass(slots=True)
class State:
    """Состояние одного источника: колонки (app_id, client, source) — его адрес."""

    app_id: int
    client: str
    source: str
    user_id: int | None = None  # владелец-пользователь (>0)
    group_id: int | None = None  # владелец-сообщество; для групп user_id пуст
    token: str | None = None
    token_expires: float | None = None
    cookie_p: str | None = None
    cookie_remixsid: str | None = None
    updated_at: float = 0.0
    login: str | None = None
    password: str | None = None


def state_from_dict(data: dict[str, Any]) -> State:
    """dict -> State (лишние/неизвестные поля отбрасываются)."""
    names = {f.name for f in fields(State)}
    payload = {key: value for key, value in data.items() if key in names}
    payload["app_id"] = int(payload["app_id"])
    return State(**payload)


class Store(ABC):
    """Асинхронное хранилище State; замена драйвера — реализовать этот ABC."""

    @abstractmethod
    async def load(self, app_id: int, client: str, source: str) -> State | None: ...

    @abstractmethod
    async def save(self, state: State) -> None: ...

    @abstractmethod
    async def delete(self, app_id: int, client: str, source: str) -> None: ...

    async def aclose(self) -> None:
        return None


class MemoryStore(Store):
    """Состояние только в памяти (словарь по колонкам app_id/client/source)."""

    def __init__(self) -> None:
        self._data: dict[tuple[int, str, str], State] = {}

    async def load(self, app_id: int, client: str, source: str) -> State | None:
        return self._data.get((int(app_id), client, source))

    async def save(self, state: State) -> None:
        self._data[(state.app_id, state.client, state.source)] = state

    async def delete(self, app_id: int, client: str, source: str) -> None:
        self._data.pop((int(app_id), client, source), None)


def _state_key(state: State) -> str:
    return f"{int(state.app_id)}/{state.client}/{state.source}"


def _cookie_state(state: State) -> bool:
    return bool(
        state.user_id is not None
        and state.user_id > 0
        and state.group_id is None
        and state.cookie_p
        and state.cookie_remixsid
    )


def _state_from_cookie_record(record: dict[str, Any]) -> State | None:
    metadata = record.get("_vkx")
    if not isinstance(metadata, dict) or not all(
        name in metadata for name in ("app_id", "client", "source")
    ):
        return None
    payload = dict(metadata)
    payload.update(
        user_id=record.get("user_id"),
        cookie_p=record.get("p"),
        cookie_remixsid=record.get("remixsid"),
        updated_at=metadata.get("updated_at", record.get("created_at", 0)),
    )
    return state_from_dict(payload)


def _cookie_record(state: State, previous: dict[str, Any] | None = None) -> dict[str, Any]:
    record = dict(previous or {})
    record.update(
        created_at=int(state.updated_at or time.time()),
        user_id=state.user_id,
        p=state.cookie_p,
        remixsid=state.cookie_remixsid,
    )
    previous_metadata = record.get("_vkx")
    metadata = dict(previous_metadata) if isinstance(previous_metadata, dict) else {}
    metadata.update(
        app_id=state.app_id,
        client=state.client,
        source=state.source,
        group_id=state.group_id,
        token=state.token,
        token_expires=state.token_expires,
        updated_at=state.updated_at,
        login=state.login,
        password=state.password,
    )
    record["_vkx"] = metadata
    return record


def _same_cookie_record(record: dict[str, Any], state: State) -> bool:
    record_user_id = record.get("user_id")
    if record_user_id is not None and state.user_id is not None:
        try:
            if int(record_user_id) != state.user_id:
                return False
        except (TypeError, ValueError):
            return False
    if any(
        record.get(name) and record.get(name) == value
        for name, value in (("p", state.cookie_p), ("remixsid", state.cookie_remixsid))
    ):
        return True
    return bool(
        record_user_id is not None
        and state.user_id is not None
        and int(record_user_id) == state.user_id
    )


class JSONStore(Store):
    """Store в JSON-файле, совместимом с форматом cookies из vkqr."""

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()
        self._data: dict[str, dict[str, Any]] | None = None
        self._document: dict[str, Any] = {}
        self._vkx_document: dict[str, Any] = {}
        self._cookie_records: list[tuple[dict[str, Any], str | None]] = []

    @staticmethod
    def _key(app_id: int, client: str, source: str) -> str:
        return f"{int(app_id)}/{client}/{source}"

    def _load(self) -> dict[str, dict[str, Any]]:
        if self._data is not None:
            return self._data

        if self._path.exists():
            text = self._path.read_text(encoding="utf-8").strip()
            document = json.loads(text) if text else {}
        else:
            document = {}
        if not isinstance(document, dict):
            raise ValueError(f"JSONStore: корень {self._path} должен быть JSON-объектом")

        # Читаем прежний формат JSONStore: {"app_id/client/source": State}.
        if document and not {"cookies", "_vkx"}.intersection(document) and all(
            isinstance(key, str) and "/" in key and isinstance(value, dict)
            for key, value in document.items()
        ):
            self._data = document
            return self._data

        # Также допускаем простой файл cookies {"p": ..., "remixsid": ...}.
        if "cookies" not in document and "_vkx" not in document and all(
            name in document for name in ("p", "remixsid")
        ):
            self._cookie_records = [(dict(document), None)]
            self._data = {}
            return self._data

        cookies = document.get("cookies", [])
        extension = document.get("_vkx", {})
        if not isinstance(cookies, list):
            raise ValueError(f'JSONStore: поле "cookies" в {self._path} должно быть списком')
        if not isinstance(extension, dict):
            raise ValueError(f'JSONStore: поле "_vkx" в {self._path} должно быть объектом')

        self._document = {
            key: value for key, value in document.items() if key not in {"cookies", "_vkx"}
        }
        self._vkx_document = {key: value for key, value in extension.items() if key != "states"}
        self._data = {}
        for record in cookies:
            if not isinstance(record, dict):
                raise ValueError(f"JSONStore: cookie-записи в {self._path} должны быть объектами")
            state = _state_from_cookie_record(record)
            if state is not None:
                key = _state_key(state)
                self._cookie_records.append((dict(record), key))
                self._data[key] = asdict(state)
            else:
                self._cookie_records.append((dict(record), None))

        states = extension.get("states", [])
        if isinstance(states, dict):
            state_values = states.values()
        elif isinstance(states, list):
            state_values = states
        else:
            raise ValueError(f'JSONStore: поле "_vkx.states" в {self._path} должно быть списком')
        for value in state_values:
            if not isinstance(value, dict):
                raise ValueError(f"JSONStore: состояния в {self._path} должны быть объектами")
            state = state_from_dict(value)
            self._data[self._key(state.app_id, state.client, state.source)] = asdict(state)
        return self._data

    def _flush(self) -> None:
        tmp = self._path.with_suffix(self._path.suffix + ".tmp")
        data = self._load()
        records: list[dict[str, Any]] = []
        pending: list[dict[str, Any]] = []
        represented: set[str] = set()

        for record, key in self._cookie_records:
            if key is None:
                pending.append(record)
                continue
            if key in represented:
                continue
            value = data.get(key)
            if value is None:
                continue
            state = state_from_dict(value)
            if _cookie_state(state):
                records.append(_cookie_record(state, record))
                represented.add(key)

        candidates: dict[str, State] = {}
        for key, value in data.items():
            state = state_from_dict(value)
            if key not in represented and _cookie_state(state):
                candidates[key] = state
        for record in pending:
            matches = [
                key for key, state in candidates.items() if _same_cookie_record(record, state)
            ]
            if len(matches) == 1:
                key = matches[0]
                state = candidates.pop(key)
                records.append(_cookie_record(state, record))
                represented.add(key)
            else:
                records.append(record)

        states: list[dict[str, Any]] = []
        for key, value in data.items():
            state = state_from_dict(value)
            if _cookie_state(state):
                if key not in represented:
                    records.append(_cookie_record(state))
                    represented.add(key)
            else:
                states.append(asdict(state))

        extension = dict(self._vkx_document)
        extension["states"] = states
        document = dict(self._document)
        document["cookies"] = records
        document["_vkx"] = extension
        tmp.write_text(json.dumps(document, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, self._path)
        self._cookie_records = [
            (record, _state_key(state) if (state := _state_from_cookie_record(record)) else None)
            for record in records
        ]

    async def load(self, app_id: int, client: str, source: str) -> State | None:
        async with self._lock:
            data = self._load().get(self._key(app_id, client, source))
            return state_from_dict(data) if data else None

    async def save(self, state: State) -> None:
        async with self._lock:
            self._load()[self._key(state.app_id, state.client, state.source)] = asdict(state)
            self._flush()

    async def delete(self, app_id: int, client: str, source: str) -> None:
        async with self._lock:
            self._load().pop(self._key(app_id, client, source), None)
            self._flush()


class SQLiteStore(Store):
    """SQLite: таблица states с осмысленными колонками вместо kv (k/v)."""

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(str(self._path), check_same_thread=False)
        with self._lock:
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute(
                """
                CREATE TABLE IF NOT EXISTS states (
                    app_id          INTEGER NOT NULL,
                    client          TEXT    NOT NULL,
                    source          TEXT    NOT NULL,
                    user_id         INTEGER,
                    group_id        INTEGER,
                    token           TEXT,
                    token_expires   REAL,
                    cookie_p        TEXT,
                    cookie_remixsid TEXT,
                    updated_at      REAL    NOT NULL DEFAULT 0,
                    login           TEXT,
                    password        TEXT,
                    PRIMARY KEY (app_id, client, source)
                )
                """
            )
            columns = {
                row[1] for row in self._conn.execute("PRAGMA table_info(states)")
            }
            if "group_id" not in columns:
                self._conn.execute("ALTER TABLE states ADD COLUMN group_id INTEGER")
            if "login" not in columns:
                self._conn.execute("ALTER TABLE states ADD COLUMN login TEXT")
            if "password" not in columns:
                self._conn.execute("ALTER TABLE states ADD COLUMN password TEXT")
            self._conn.commit()

    def _load(self, app_id: int, client: str, source: str) -> State | None:
        row = self._conn.execute(
            "SELECT user_id, group_id, token, token_expires, cookie_p, cookie_remixsid,"
            " updated_at, login, password FROM states"
            " WHERE app_id = ? AND client = ? AND source = ?",
            (int(app_id), client, source),
        ).fetchone()
        if row is None:
            return None
        return State(
            app_id=int(app_id),
            client=client,
            source=source,
            user_id=row[0],
            group_id=row[1],
            token=row[2],
            token_expires=row[3],
            cookie_p=row[4],
            cookie_remixsid=row[5],
            updated_at=row[6],
            login=row[7],
            password=row[8],
        )

    def _save(self, state: State) -> None:
        self._conn.execute(
            _UPSERT,
            (
                state.app_id,
                state.client,
                state.source,
                state.user_id,
                state.group_id,
                state.token,
                state.token_expires,
                state.cookie_p,
                state.cookie_remixsid,
                state.updated_at,
                state.login,
                state.password,
            ),
        )
        self._conn.commit()

    def _delete(self, app_id: int, client: str, source: str) -> None:
        self._conn.execute(
            "DELETE FROM states WHERE app_id = ? AND client = ? AND source = ?",
            (int(app_id), client, source),
        )
        self._conn.commit()

    async def load(self, app_id: int, client: str, source: str) -> State | None:
        return await asyncio.to_thread(self._load, app_id, client, source)

    async def save(self, state: State) -> None:
        await asyncio.to_thread(self._save, state)

    async def delete(self, app_id: int, client: str, source: str) -> None:
        await asyncio.to_thread(self._delete, app_id, client, source)

    async def aclose(self) -> None:
        await asyncio.to_thread(self._conn.close)


_default_store: Store | None = None


def default_store() -> Store:
    """Хранилище по умолчанию: SQLite в CWD/.vkx/vkx.sqlite."""
    global _default_store
    if _default_store is None:
        _default_store = SQLiteStore(DEFAULT_DB_PATH)
    return _default_store


def open_store(path: str | Path | None = None) -> Store:
    """None -> SQLite по умолчанию; '*.json' -> JSONStore; иначе SQLiteStore по пути."""
    if path is None:
        return default_store()
    target = Path(path)
    if target.suffix == ".json":
        return JSONStore(target)
    return SQLiteStore(target)
