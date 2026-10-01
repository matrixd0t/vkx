"""Типизированное хранилище состояния источников токенов.

Запись State адресуется осмысленными колонками (app_id, client, source) —
никаких составных строковых ключей и анонимных k/v: каждая колонка таблицы
имеет собственный смысл (cookie_p / cookie_remixsid — имена cookie,
token_expires — срок токена, user_id — владелец-пользователь, group_id —
владелец-сообщество).

Реализации Store: SQLiteStore (по умолчанию, CWD/.vkx/vkx.sqlite), JSONStore, MemoryStore.
"""

from __future__ import annotations

import asyncio
import json
import os
import sqlite3
import threading
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

DEFAULT_STATE_DIR = Path.cwd() / ".vkx"
DEFAULT_DB_PATH = DEFAULT_STATE_DIR / "vkx.sqlite"

_UPSERT = """
INSERT INTO states (
    app_id, client, source, user_id, group_id, token,
    token_expires, cookie_p, cookie_remixsid, updated_at
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(app_id, client, source) DO UPDATE SET
    user_id = excluded.user_id,
    group_id = excluded.group_id,
    token = excluded.token,
    token_expires = excluded.token_expires,
    cookie_p = excluded.cookie_p,
    cookie_remixsid = excluded.cookie_remixsid,
    updated_at = excluded.updated_at
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


class JSONStore(Store):
    """Store в JSON-файле (без БД нет колонок — запись ключуется app_id/client/source)."""

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()
        self._data: dict[str, dict[str, Any]] | None = None

    @staticmethod
    def _key(app_id: int, client: str, source: str) -> str:
        return f"{int(app_id)}/{client}/{source}"

    def _load(self) -> dict[str, dict[str, Any]]:
        data = self._data
        if data is None:
            data = (
                json.loads(self._path.read_text(encoding="utf-8"))
                if self._path.exists()
                else {}
            )
            self._data = data
        return data

    def _flush(self) -> None:
        tmp = self._path.with_suffix(self._path.suffix + ".tmp")
        tmp.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, self._path)

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
                    PRIMARY KEY (app_id, client, source)
                )
                """
            )
            columns = {
                row[1] for row in self._conn.execute("PRAGMA table_info(states)")
            }
            if "group_id" not in columns:
                self._conn.execute("ALTER TABLE states ADD COLUMN group_id INTEGER")
            self._conn.commit()

    def _load(self, app_id: int, client: str, source: str) -> State | None:
        row = self._conn.execute(
            "SELECT user_id, group_id, token, token_expires, cookie_p, cookie_remixsid,"
            " updated_at FROM states WHERE app_id = ? AND client = ? AND source = ?",
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
