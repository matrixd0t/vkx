# vkx

Библиотека для работы с VK API от Точки aka d0tmatrix. В каком-то смысле альтернатива бутылке.

- **Клиент** — `vkx.VKClient`: выбор токена по правам (scope), привязка к владельцу,
  очередь и батчинг `execute` (вкл. по умолчанию, отключается), автопагинация
  (тоже вкл. по умолчанию), повторы, троттлинг, капча, таймауты.
- **Типы** — `vkx.models`: VK-объекты (`Photo`, `Message`, `Keyboard`, …),
  модели ответов и события Callback/Long Poll. Поддерживаются вручную.
- **Типизированные методы** — категории `vk.users.*`, `vk.messages.*`,
  `vk.board.*`, `vk.photos.*` и т.д. с строго типизированными аргументами.
- **Загрузка файлов** — `vk.upload.*`: фото, документы, голосовые.
- **Сервер** — `parse_callback`, `CallbackServer`/`CallbackListener`,
  `LongPoll`, `BotsLongPoll`.
- **Адаптеры** — готовые роуты Callback API для FastAPI, Starlette, aiohttp,
  Sanic, Flask, Django (фреймворки опциональны).

## Установка

```bash
pip install "vkx[http]"
```
Требуется Python ≥ 3.12.
`httpx` подключается лениво: если передать свой HTTP-клиент, `httpx` не нужен.
Фреймворки для адаптеров в зависимости `vkx` не входят — их вы ставите сами.

## Быстрый старт

```python
import asyncio

from vkx import VKClient


async def main() -> None:
    vk = VKClient(tokens="vk1.a....")
    owner = (await vk.users.get())[0]      # типизированный метод
    print(vk.user_id, owner.first_name)
    await vk.aclose()


asyncio.run(main())
```

Клиент жёстко привязан к одному владельцу: при первом запросе он «прощупывает»
токены (`probe`) и определяет, кому они принадлежат — пользователю или
сообществу.

---

# Клиент

## Создание клиента

Передать можно статичный токен, веб-cookies, готовые источники или всё вместе.

```python
from vkx import VKClient

vk = VKClient(tokens="vk1.a....")
```

## Конструктор не ходит в сеть

`VKClient(...)` только сохраняет настройки. Сеть трогается при первом `call()`
или явном `await vk.probe()`.

```python
vk = VKClient(tokens="vk1.a....")
print(vk.user_id)        # None — ещё не опрошен
await vk.probe()
print(vk.user_id)        # 123456
```

## Владелец: пользователь или сообщество

Тип владельца определяется автоматически. Для сообщества `user_id`
отрицательный, а `group_id` — положительный.

```python
await vk.probe()
if vk.is_group:
    print("сообщество", vk.group_id)
else:
    print("пользователь", vk.user_id)
```

## Права клиента

`scope` — битовая маска доступных категорий методов, `permissions` — их
человекочитаемые названия.

```python
await vk.probe()
print(vk.permissions)   # ['Сообщения', 'Друзья', ...]
print(vk.scope)         # 2 | 4096 | ...
```

## Токен из веб-cookies

Вместо токена можно передать cookies веб-сессии (`p` и `remixsid`): клиент сам
получит веб-токен и будет обновлять его.

```python
vk = VKClient(cookies={"p": "...", "remixsid": "..."})
```

Нужные cookie проверяются сразу, `WebCookieSource` импортировать не требуется.

## Несколько источников

Можно смешивать токены, cookies и готовые источники. Источники с чужим
владельцем отбрасываются, нерабочие — логируются и пропускаются.

```python
from vkx import StaticTokenSource, VKClient, WebCookieSource

vk = VKClient(
    tokens=["vk1.a....", "vk1.b...."],
    cookies={"p": "...", "remixsid": "..."},
    sources=[StaticTokenSource("vk1.c....", label="резерв")],
)
```

## Хранилище токенов

С `store` введённые токены и владелец запоминаются. `StaticTokenSource` можно
создать без токена — он восстановится из базы. При ошибке «токен недействителен»
(код 5) запись удаляется.

```python
from vkx import SQLiteStore, StaticTokenSource, VKClient

store = SQLiteStore("vk-state.sqlite")
vk = VKClient(tokens=["vk1.a...."], store=store)   # токен запомнится
```

```python
vk = VKClient(sources=[StaticTokenSource()], store=store)  # токен из store
```

Форматы хранилища: `SQLiteStore` (по умолчанию `CWD/.vkx/vkx.sqlite`),
`JSONStore`, `MemoryStore`.

```python
from vkx import JSONStore, MemoryStore, open_store

store = open_store("state.json")   # *.json -> JSONStore
store = open_store()               # SQLite по умолчанию
```

## Типизированные методы

Категории VK доступны как атрибуты клиента. Аргументы строго типизированы: лишний
аргумент — `TypeError`. Возвращаются pydantic-модели.

```python
user = (await vk.users.get(user_ids=[1]))[0]
print(user.first_name, user.last_name)
```

```python
await vk.messages.send(peer_id=1, message="Привет", random_id=0)
```

## Сырой вызов `call`

Любой метод можно вызвать строкой, без типизации — вернётся тело `response`.

```python
result = await vk.call("users.get", user_ids=[1])
```

`call` тоже идёт через очередь и батчинг, но не разбирает ответ в модель и не
пагинирует.

## Автобатчинг

Обычные вызовы автоматически группируются через `execute`: до 25 вызовов и до
260 000 байт VKScript на пакет. Снаружи это невидимо. Батчинг включён по
умолчанию.

```python
users = await asyncio.gather(
    vk.users.get(user_ids=[1]),
    vk.users.get(user_ids=[2]),
    vk.users.get(user_ids=[3]),
)   # уедет одним execute-запросом
```

### Отключить батчинг у клиента

`batching=False` у клиента — все запросы уходят прямыми вызовами, без `execute`.

```python
vk = VKClient(tokens="vk1.a....", batching=False)
```

### Отключить батчинг у одного запроса

`batching=False` в `vk.call` — не батчится только этот вызов.

```python
await vk.call("users.get", user_ids=[1], batching=False)
```

### Отключить батчинг на блок

`vk.overrides(...)` временно переопределяет настройки, в том числе для
типизированных методов внутри блока.

```python
async with vk.overrides(batching=False):
    await vk.users.get(user_ids=[1])   # прямым вызовом
```

## Автопагинация

Методы с `offset`/`count` добирают страницы сами и сливают результат в один
ответ. `vk.database.get_countries(count=1500)` вернёт 1500 стран одним вызовом.
Автопагинация включена по умолчанию.

```python
countries = await vk.database.get_countries(count=1500)
print(len(countries.items), countries.count)
```

Если `count=None`, клиент забирает всё, что отдаёт VK (по лимитам метода).

```python
all_topics = await vk.board.get_topics(group_id=1, count=None)
```

### Отключить автопагинацию у клиента

`pagination=False` — метод вызывается один раз, тело ответа возвращается как есть.

```python
vk = VKClient(tokens="vk1.a....", pagination=False)
```

### Отключить автопагинацию на блок

```python
async with vk.overrides(pagination=False):
    countries = await vk.database.get_countries(count=1500)   # одна страница
```

### Оба переопределения сразу

```python
async with vk.overrides(batching=False, pagination=False):
    await vk.users.get(user_ids=[1])
```

## Пауза между запросами

`interval` — пауза между пакетами. По умолчанию 0.5 с для пользователя и 0.1 с
для сообщества.

```python
vk = VKClient(tokens="vk1.a....", interval=1.0)
```

## Немедленная отправка очереди

`drain` отправляет накопленную очередь, не дожидаясь `interval`.

```python
await vk.call("users.get", user_ids=[1])
await vk.drain()   # отправить прямо сейчас
```

## Таймаут запроса

`timeout` ограничивает ожидание ответа. Истёк — `VKTimeoutError`, запрос
помечается отменённым. Можно задать клиенту или одному вызову.

```python
from vkx import VKTimeoutError

vk = VKClient(tokens="vk1.a....", timeout=5.0)
try:
    await vk.call("users.get", user_ids=[1], timeout=1.0)
except VKTimeoutError as exc:
    print("не дождались:", exc)
```

## Повторы и backoff

Транзиентные сбои (сеть, HTTP 5xx/429, коды 1/6/9/10/29) повторяются
`max_retries` раз с экспоненциальной паузой. Коды 6/29 поднимают общий cooldown
для всех запросов, а успех его сбрасывает.

```python
vk = VKClient(tokens="vk1.a....", max_retries=3, retry_backoff=0.5)
```

## Переопределение HTTP-настроек на один запрос

`http_client`, `base_api_url` и `v` можно задать у клиента и переопределить на
конкретный вызов.

```python
await vk.call("users.get", user_ids=[1], v="5.131", base_api_url="https://api.vk.com")
```

Запросы с разными настройками не попадают в один батч.

## Свой HTTP-клиент

Клиент работает по протоколу `HttpClient` (асинхронные `get`/`post`). Можно
передать своё, и тогда `httpx` не импортируется.

```python
import httpx2
from vkx import VKClient

http = httpx2.AsyncClient()
vk = VKClient(tokens="vk1.a....", http_client=http)
```

## Свой код VKScript

`execute` доступен и напрямую — для произвольного кода.

```python
code = "return API.users.get({'user_ids': '1'});"
users = await vk.execute(code)
```

## Закрытие клиента

`aclose(drain=True)` сначала дожидается отправки очереди, затем закрывает
HTTP-клиент.

```python
await vk.aclose(drain=True, timeout=5.0)
```

---

# Загрузка файлов

Хелперы получают сервер загрузки через очередь, отправляют байты напрямую
HTTP-клиентом и сохраняют файл через `save`-метод. Свободные функции принимают
клиент первым аргументом, namespace `vk.upload.*` — не принимает.

## Фото в сообщения

```python
data = open("cat.jpg", "rb").read()
photos = await vk.upload.photo_to_messages(data, peer_id=1)
```

## Фото на стену

```python
photos = await vk.upload.photo_to_wall(data, group_id=1, caption="кот")
```

## Документ

```python
doc = await vk.upload.doc_to_messages(data, peer_id=1, title="отчёт.pdf")
```

## Голосовое сообщение

```python
voice = await vk.upload.audio_message(ogg_bytes, peer_id=1)
```

## Свободные функции

Тот же набор доступен как функции модуля.

```python
from vkx.client.upload import upload_audio_message, upload_photo_to_wall

photo = await upload_photo_to_wall(vk, data, group_id=1)
voice = await upload_audio_message(vk, ogg_bytes, peer_id=1)
```

## Строка-вложение `.as_att`

Вложения отдают готовую строку для параметра `attachment`.

```python
photo = (await vk.upload.photo_to_wall(data, group_id=1))[0]
await vk.messages.send(peer_id=1, message="фото", attachment=photo.as_att, random_id=0)
```

## Вложение документа

```python
doc = await vk.upload.doc(data)
await vk.messages.send(peer_id=1, message="док", attachment=doc.as_att, random_id=0)
```

---

# Клавиатуры

`Keyboard` и `Button` неизменяемы и умеют и разбор, и сборку. Для отправки
используйте `keyboard=keyboard.to_json()`.

## Inline callback-клавиатура

`Button("Текст")` по умолчанию — callback-кнопка: нажатие приходит событием,
сообщение не отправляется.

```python
from vkx.models import Button, Keyboard

keyboard = Keyboard.from_rows([
    [Button("Да", payload={"cmd": "yes"})],
    [Button("Нет", payload={"cmd": "no"})],
])
await vk.messages.send(peer_id=1, message="Выбирай", keyboard=keyboard.to_json(), random_id=0)
```

## Обычная клавиатура

По умолчанию `inline=True`; для чатовой клавиатуры передайте `inline=False`
(лимит — 10 рядов вместо 6).

```python
keyboard = Keyboard.from_rows(
    [[Button("Помощь", type="text")]],
    inline=False,
    one_time=True,
)
```

## Несколько кнопок в ряду

```python
keyboard = Keyboard.from_rows(
    [[Button("Да", payload={"cmd": "yes"}), Button("Нет", payload={"cmd": "no"})]],
)
```

## Типы кнопок

Помимо `callback` (по умолчанию): `text`, `open_link`, `location`, `vkpay`,
`open_app`, `open_photo`.

```python
Button("Написать", type="text")
Button("Сайт", type="open_link", link="https://vk.com")
Button("Гео", type="location")
Button("Оплатить", type="vkpay", hash="...")
Button(type="open_app", app_id=1, owner_id=2, label="Приложение")
Button(type="open_photo")
```

## Цвет кнопки

```python
from vkx.models import KeyboardButtonColor

Button("Да", payload={"cmd": "yes"}, color=KeyboardButtonColor.POSITIVE)
```

## Payload — dict или JSON

`payload` принимает dict, а хранится компактной JSON-строкой.

```python
Button("Открыть", payload={"screen": "menu", "id": 3})
```

## Низкоуровневые фабрики

Если нужна именно `KeyboardButton` (например, при разборе), есть фабрики
`callback`/`text`/`link`/`location`/`vkpay`/`open_app`/`open_photo`.

```python
from vkx.models import KeyboardButton

KeyboardButton.callback("Да", payload={"cmd": "yes"})
KeyboardButton.link("Сайт", "https://vk.com")
```

---

# Callback API: разбор уведомлений

`parse_callback` — чистый парсер без состояния. Он не проверяет `secret`,
`confirmation` и не дедуплицирует — это задача интеграции (см. ниже).

## Разбор события

```python
from vkx import parse_callback

event = parse_callback(body)          # bytes/str/dict
print(event.type, event.group_id)
```

## Конкретные типы событий

По полю `type` возвращается конкретный класс, `object` уже типизирован.

```python
from vkx.models import CallbackEventType, MessageNewCallbackEvent

event = parse_callback(body)
if isinstance(event, MessageNewCallbackEvent):
    print(event.object.message.text, event.object.message.peer_id)
```

## Неизвестный тип не роняет парсер

Вернётся `BaseCallbackEvent` с `NOT_SUPPORTED_MEMBER` и сырым `object`.

```python
event = parse_callback({"type": "future_event", "object": {}})
print(event.type is CallbackEventType.NOT_SUPPORTED_MEMBER)
```

---

# Callback API: серверная обвязка

`CallbackServer` хранит `group_id`, ожидаемый `secret`, `confirmation`-код и
дедуплицирует `event_id`. `CallbackListener` маршрутизирует по `group_id`.

## `CallbackListener.handle`

Возвращает событие или `None`, если уведомление чужое, подделано или дубликат.

```python
from vkx import CallbackListener, CallbackServer

server = CallbackServer(group_id=1, secret="s3cret", confirmation_code="abc123")
listener = CallbackListener([server])

event = listener.handle(body)
if event is None:
    ...   # чужой group_id / плохой secret / дубликат
```

## Ответ на `confirmation`

Код подтверждения адреса нужно вернуть синхронно.

```python
from vkx.models import CallbackEventType

if event and event.type is CallbackEventType.CONFIRMATION:
    return server.confirmation_code   # "abc123"
```

## Проверка секрета

Если `secret` задан, уведомления с другим `secret` отбрасываются.

```python
server = CallbackServer(group_id=1, secret="s3cret")
assert server.accepts(event)   # False, если secret не совпал
```

## Дедупликация `event_id`

Каждый `event_id` обрабатывается один раз (кольцевой буфер на 200 записей —
`DEFAULT_DEDUP_SIZE`). Размер настраивается.

```python
server = CallbackServer(group_id=1, dedup_size=5000)
```

## Регистрация сервера в сообществе

`create_callback_server` вызывает `groups.addCallbackServer` и забирает
`confirmation`-код.

```python
from vkx import create_callback_server

server = await create_callback_server(
    vk, group_id=1, url="https://example.com/vk/callback",
    title="мой-бот", secret="s3cret",
)
```

`title` — не длиннее 14 символов, `secret` — не длиннее 50.

## Несколько сообществ на одном URL

`CallbackListener` держит набор серверов и сам выбирает нужный по `group_id`.

```python
listener = CallbackListener([server_a, server_b])
```

---

# Веб-адаптеры

Пакет `vkx.adapters`. Фреймворки импортируются лениво, в зависимости `vkx` не
тянутся. Адаптер импортируют только те, у кого фреймворк уже стоит.

## Два диспетчера

- `CallbackDispatch` — для async-фреймворков: ответ `ok` отдаётся сразу,
  обработчик запускается фоновой задачей. Синхронный обработчик уходит в
  отдельный поток, чтобы не блокировать loop.
- `SyncCallbackDispatch` — для Flask/Django WSGI: обработчик обязан быть
  **синхронным** и вызывается в том же потоке. Async-функция даёт `TypeError`.

В обоих `confirmation` возвращается немедленно.

## Синхронный обработчик (Flask/Django)

Для `SyncCallbackDispatch` обработчик обязан быть обычной функцией — он
вызывается прямо в потоке WSGI-запроса.

```python
def handle_vk_event(event: CallbackEvent) -> None:
    ...   # синхронно; async-функция вызовет TypeError
```

## FastAPI

```python
from vkx.adapters import CallbackDispatch
from vkx.adapters.fastapi import create_callback_router

dispatch = CallbackDispatch(listener, handler=handle_vk_event)
app.include_router(create_callback_router(dispatch))
```

## Starlette

```python
from starlette.applications import Starlette

from vkx.adapters.starlette import create_callback_router

router = create_callback_router(dispatch)
app = Starlette(routes=[*router.routes])
```

## aiohttp

```python
from aiohttp import web

from vkx.adapters.aiohttp import create_callback_router

app = web.Application()
app.add_routes(create_callback_router(dispatch))
```

## Sanic

```python
from vkx.adapters.sanic import create_callback_router

app.blueprint(create_callback_router(dispatch))
```

## Flask

Flask WSGI синхронный — используем `SyncCallbackDispatch` и обычный обработчик.

```python
from vkx.adapters import SyncCallbackDispatch
from vkx.adapters.flask import create_callback_router

dispatch = SyncCallbackDispatch(listener, handler=handle_vk_event)
app.register_blueprint(create_callback_router(dispatch))
```

## Django

```python
from django.urls import path

from vkx.adapters import SyncCallbackDispatch
from vkx.adapters.django import create_callback_view

dispatch = SyncCallbackDispatch(listener, handler=handle_vk_event)
urlpatterns = [path("vk/callback", create_callback_view(dispatch))]
```

По умолчанию view освобождён от CSRF-проверки (`csrf_exempt=True`).

## Асинхронный обработчик в background

Обработчик `CallbackDispatch` получает событие после того, как VK прочитает
`ok`.

```python
async def handle_vk_event(event: CallbackEvent) -> None:
    if isinstance(event, MessageNewCallbackEvent):
        await vk.messages.send(
            peer_id=event.object.message.peer_id,
            message="принято",
            random_id=0,
        )
```

## Ожидание фоновых задач

На остановке приложения дождитесь задач `CallbackDispatch` через `aclose`.

```python
dispatch = CallbackDispatch(listener, handler=handle_vk_event)
...
await dispatch.aclose(timeout=5.0)
```

Также поддерживается `async with dispatch:`.

## Изменение пути роута

```python
create_callback_router(dispatch, path="/webhooks/vk", name="vk")
```

---

# Long Poll

## Bots Long Poll

События разбираются тем же `parse_callback`, что и Callback API.

```python
from vkx.server import BotsLongPoll

async with BotsLongPoll(vk) as longpoll:
    async for event in longpoll:
        print(event.type)
```

`group_id` берётся из клиента; можно передать явно.

```python
longpoll = BotsLongPoll(vk, group_id=1, wait=25)
```

## Одно событие

```python
event = await longpoll.get_event()
```

## User Long Poll

```python
from vkx.server import LongPoll

async with LongPoll(vk) as longpoll:
    async for event in longpoll:
        print(event.object)
```

## Режим user Long Poll

```python
longpoll = LongPoll(vk, mode=234, lp_version=3, wait=25)
```

## Остановка

`__aexit__`/`aclose()` останавливает фоновый поллинг; `stop()` просит завершиться
после текущего запроса.

```python
await longpoll.aclose()
```

---

# Типы и события

## Объекты VK

```python
from vkx.models import Button, Keyboard, KeyboardButton, Message, Photo
```

## События Callback API

```python
from vkx.models import (
    CallbackEvent,
    CallbackEventType,
    MessageEventCallbackEvent,
    MessageNewCallbackEvent,
)
```

## Payload нажатия кнопки

```python
if isinstance(event, MessageEventCallbackEvent):
    print(event.object.payload, event.object.user_id)
```

## События user Long Poll

Конкретные классы user-событий живут в `vkx.models.events.user_events` (из
`vkx.models` реэкспортируется только базовый `BaseUserEvent` и парсер).

```python
from vkx.models import parse_user_event
from vkx.models.events.user_events import MessageNewEvent

# [код события, message_id, flags, peer_id, timestamp, text, ...]
event = parse_user_event([4, 123, 0, 1, 1700000000, "привет"])
if isinstance(event, MessageNewEvent):
    print(event.object.text)
```

---

# Ошибки

Все ошибки — `VKError` (по коду выбирается подкласс), поэтому `except VKError`
ловит всё, а `exc.code` — исходный числовой код.

```python
from vkx import VKError

try:
    await vk.messages.send(peer_id=1, message="hi", random_id=0)
except VKError as exc:
    print(exc.code, exc.is_auth, exc.is_rate_limit, exc.is_captcha)
```

Подклассы: `VKInvalidTokenError`, `VKAuthError`, `VKPermissionError`,
`VKRequestError`, `VKRateLimitError`, `VKFloodError`, `VKServerError`,
`VKCaptchaError`, `VKTransportError`, `VKTimeoutError`.

## Пауза из ошибки

```python
except VKError as exc:
    if exc.is_retryable:
        await asyncio.sleep(exc.retry_after or 1.0)
```

## Контекст ошибки

`exc.client` — клиент, `exc.call` — `PendingApiCall` (метод и параметры).

```python
except VKError as exc:
    print(exc.call.method, exc.call.params)
```

## Свой парсер ошибок

```python
from vkx import build_error

error = build_error("слишком много запросов", code=6)
print(type(error).__name__)   # VKRateLimitError
```

