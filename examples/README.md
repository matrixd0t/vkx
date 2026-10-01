# Примеры vkx

Атомарные примеры: каждый файл посвящён одной возможности библиотеки и,
где это возможно, запускается без сети. Примеры с реальными запросами берут
токен из переменной окружения `VK_TOKEN` (токен пользователя или сообщества).

Запуск из корня проекта (используется venv проекта):

```powershell
$env:VK_TOKEN = "vk1.a...."
.venv\Scripts\python.exe examples\01_token.py
```

Быстрая проверка синтаксиса всех примеров без запуска:

```powershell
Get-ChildItem examples\*.py | ForEach-Object { python -m py_compile $_.FullName }
```

## Индекс

Клиент:

- `01_token.py` — клиент по статичному токену, `probe`, владелец, права.
- `02_cookies.py` — веб-вход по cookies (`p` + `remixsid`).
- `03_sources_and_store.py` — несколько источников и хранилище состояния.
- `04_typed_methods.py` — типизированные категории (`vk.users.*` и т.д.).
- `05_raw_call.py` — сырой вызов `vk.call`.
- `06_batching.py` — батчинг `execute`, `gather`, `drain`, интервал.
- `07_pagination.py` — автопагинация `count`/`offset`.
- `08_overrides.py` — переопределение батчинга/пагинации на блок.
- `09_timeout.py` — таймаут ожидания ответа.
- `10_errors.py` — типизированные ошибки и их свойства.
- `11_retries_and_captcha.py` — повторы, backoff и обработчик капчи.
- `12_raw_execute.py` — произвольный VKScript через `vk.execute`.
- `13_custom_http_client.py` — свой HTTP-клиент (протокол `HttpClient`).
- `14_custom_token_source.py` — свой источник токена (протокол `TokenSource`).

Контент:

- `15_upload_photo.py` — загрузка фото в сообщения и на стену.
- `16_upload_doc.py` — загрузка документа.
- `17_upload_voice.py` — голосовое сообщение.
- `18_keyboards.py` — сборка клавиатуры и отправка сообщения.

Сервер:

- `19_parse_callback.py` — разбор уведомления Callback API.
- `20_callback_server.py` — состояние сервера, `secret`, дедупликация.
- `21_create_callback_server.py` — регистрация сервера в сообществе.
- `22_longpoll_user.py` — User Long Poll.
- `23_longpoll_bots.py` — Bots Long Poll.

Веб-адаптеры:

- `24_web_fastapi.py`, `25_web_starlette.py`, `26_web_aiohttp.py`,
  `27_web_sanic.py`, `28_web_flask.py`, `29_web_django.py`.

Типы:

- `30_models_and_events.py` — объекты и события без сетевого клиента.
