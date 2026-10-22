# vkx

[![PyPI](https://img.shields.io/pypi/v/vkx)](https://pypi.org/project/vkx/)
[![Python](https://img.shields.io/pypi/pyversions/vkx)](https://pypi.org/project/vkx/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![CI](https://github.com/matrixd0t/vkx/actions/workflows/ci.yml/badge.svg)](https://github.com/matrixd0t/vkx/actions/workflows/ci.yml)

Библиотека для работы с VK API. Асинхронный клиент с выбором токена по правам,
батчингом через `execute`, автопагинацией, типизированными методами и
Python-моделями ответов. Плюс серверный блок (Callback API / Long Poll) и
адаптеры для популярных веб-фреймворков.

## Киллер-фичи

- **Python-модели ответов** — каждый метод возвращает pydantic-модель
  (`UserFull`, `Message`, `GroupFull`, `Keyboard`…). Всё типизировано, IDE
  подсказывает поля, валидация на границе API. Модели поддерживаются вручную.
- **Батчинг `execute`** — десятки вызовов сворачиваются в один HTTP-запрос к VK
  API (лимит 25 вызовов / 260 КБ кода на батч). Снаружи `await vk.call(...)` —
  как обычный одиночный вызов.
- **Автопагинация** — методы с `offset`/`count` сами добирают страницы и
  склеивают тело (`count`, `items`, `profiles`, `groups`). `vk.database.get_countries(count=1500)`
  вернёт 1500 стран одним вызовом.
- **Cookie-авторизация** — `VKClient(cookies={"p": ..., "remixsid": ...})`
  получает веб-токен и обновляет его сам; токен и владелец сохраняются в Store.
- **`resolve()`** — по тексту находит упоминания пользователей и сообществ
  (`vk.com/durov`, `vk.com/id123`, `@durov`, `[id123|@Имя]`, приглашения
  `vk.com/invite/CODE`) и возвращает их данные одним запросом. Общий кеш на
  приложение с TTL и лимитом размера.
- **Выбор токена по scope** — несколько источников (статичные токены, cookies,
  готовые `TokenSource`), клиент сам выбирает подходящий по правам метода и
  отбрасывает источники чужого владельца при `probe`.
- **Клавиатуры** — `Keyboard`/`KeyboardButton`/`Button`: immutable, разбор и
  сборка, `keyboard.to_json()` для `messages.send`.
- **Разметка сообщений** — HTML/markdown в `message` разбирается в `format_data`
  VK (смещения в UTF-16 code units).
- **Серверный блок** — `parse_callback`, `CallbackServer`/`CallbackListener`,
  `LongPoll`, `BotsLongPoll` + адаптеры для FastAPI, Starlette, aiohttp, Sanic,
  Flask, Django.
- **Загрузка файлов** — `vk.upload.*`: фото, документы, голосовые (multipart
  напрямую HTTP-клиентом, save через очередь).

## Установка

```bash
pip install "vkx[http]"
```

Требуется Python ≥ 3.12. `httpx` подключается лениво: если передать свой
HTTP-клиент, `httpx` не нужен. Фреймворки для адаптеров в `vkx` не входят.

## Быстрый старт

```python
import asyncio
from vkx import VKClient

async def main() -> None:
    vk = VKClient(tokens="vk1.a....")
    owner = (await vk.users.get())[0]
    print(vk.user_id, owner.first_name)
    await vk.aclose()

asyncio.run(main())
```

Клиент жёстко привязан к одному владельцу: при первом запросе он «прощупывает»
токены (`probe`) и определяет, кому они принадлежат — пользователю или
сообществу.

## Клиент

### Создание

Передать можно статичный токен, веб-cookies, готовые источники или всё вместе:

```python
from vkx import VKClient

vk = VKClient(tokens="vk1.a....")
vk = VKClient(cookies={"p": "...", "remixsid": "..."})
vk = VKClient(tokens=["tok_a", "tok_b"], cookies=[{"p": ..., "remixsid": ...}])
```

Конструктор не ходит в сеть; сеть трогается при первом `call()` или явном
`await vk.probe()`.

### Владелец и права

```python
await vk.probe()
print(vk.user_id, vk.is_group, vk.group_id)   # user_id < 0 — сообщество
print(vk.permissions)                          # ['Сообщения', 'Друзья', ...]
```

### Батчинг (по умолчанию включён)

```python
# эти три вызова уйдут одним execute-запросом
a = await vk.call("users.get", user_ids=1)
b = await vk.call("users.get", user_ids=2)
c = await vk.call("users.get", user_ids=3)
# отключить на один запрос:
await vk.call("users.get", user_ids=1, batching=False)
```

### Автопагинация (по умолчанию включена)

```python
# доберёт страницы сам, вернёт 1500 стран
countries = await vk.database.get_countries(count=1500)
# выключить: async with vk.overrides(pagination=False): ...
```

### Cookie-авторизация

```python
vk = VKClient(cookies={"p": "...", "remixsid": "..."})
```

Веб-токен получается и обновляется автоматически; токен и владелец сохраняются
в Store (по умолчанию SQLite в `.vkx/vkx.sqlite`).

### `resolve()`

```python
result = await vk.resolve("Привет @durov, см. vk.com/club123 и vk.com/invite/abc")
print(result.users)    # [UserFull(...)]
print(result.groups)   # [GroupFull(...)]
print(result.mentions) # [ResolvedMention(...), ...]
```

Принимает строку, список строк или словарь `{ключ: текст}` — возвращает тот же
вид. Все запросы идут одним `execute`. Кеш общий на приложение:

```python
vk.resolve_cache_ttl = 1800   # секунды (0 — выключить)
vk.resolve_cache_size = 500   # записей в общем кеше
```

### Ошибки, повторы, таймауты

- `max_retries` / `retry_backoff` — повторы транзиентных сбоев (сеть, HTTP 5xx/429,
  коды 1/6/9/10/29) с экспоненциальной паузой.
- `timeout` — ограничение ожидания ответа для `call()` (переопределяется на запрос).
- `captcha_handler` — обработчик капчи (код 14).
- `interval` — пауза между HTTP-запросами (по умолчанию 0.5 с для пользователя,
  0.1 с для сообщества).
- `await vk.drain()` — отправить очередь немедленно; `await vk.aclose(drain=True)` —
  сначала отправить очередь, потом закрыть.

### Загрузка файлов

```python
photo = await vk.upload.photo_to_wall(data, peer_id=123)
await vk.messages.send(peer_id=123, attachment=photo.as_att)
```

## Типы и модели

`vkx.models` — VK-объекты, модели ответов и события. Типизированные методы
(`vk.users.get`, `vk.messages.send`, …) возвращают pydantic-модели из
`vkx.models.responses` / `vkx.models.objects`. Клавиатуры:

```python
from vkx.models.objects import Keyboard, KeyboardButton

kb = Keyboard(
    [KeyboardButton.callback("ОК", payload={"a": 1})],
    inline=True,
)
await vk.messages.send(peer_id=123, message="выбор", keyboard=kb.to_json())
```

Разметка сообщений (HTML/markdown → `format_data` VK):

```python
from vkx.models.formatting import parse_format

text, items = parse_format("**жирный** и _курсив_")
```

## Серверный блок

### Callback API

```python
from vkx.server import parse_callback, CallbackServer, CallbackListener, create_callback_server

event = parse_callback(raw_bytes)   # bytes/str/dict -> CallbackEvent
```

`CallbackServer` — состояние одного колбек-сервера (secret, confirmation-код,
group_id, дедупликация `event_id` и контентная дедупликация комментариев).
`CallbackListener` — набор серверов, маршрутизация по `group_id`.
`create_callback_server(client, group_id, url, ...)` — регистрирует сервер через
`groups.addCallbackServer` и забирает confirmation-код.

### Адаптеры

Готовые роуты для FastAPI, Starlette, aiohttp, Sanic, Flask, Django (фреймворки
опциональны, импортируются лениво):

```python
from vkx.adapters.fastapi import create_callback_router
from vkx.server import CallbackDispatch

dispatch = CallbackDispatch(server)
router = create_callback_router(dispatch, path="/vk/callback")
```

### Long Poll

```python
from vkx.server import LongPoll, BotsLongPoll

async with LongPoll(vk) as lp:
    async for event in lp:
        ...
```

`BotsLongPoll(client, group_id=...)` — для сообществ (требует group_id при
пользовательском токене).

## Примеры и тесты

Ручные/живые скрипты: `_example_client.py`, `_test_batch.py`, `_test_pagination.py`,
`_probe_format.py`. Тесты: `tests/test_*.py` (unittest, Python ≥ 3.12).

```bash
.venv\Scripts\python.exe tests\test_message_format.py
.venv\Scripts\python.exe tests\test_resolve.py
```

Линтер: `uvx ruff check src`. Типы: `uvx pyright`.
