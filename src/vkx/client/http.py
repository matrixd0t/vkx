"""Общие константы HTTP-слоя и абстракция HTTP-клиента.

HttpClient/HttpResponse — протоколы: VKClient и источники токенов работают
с любым объектом, у которого есть асинхронные get/post, а ответ несёт
status_code / text / json(). httpx — опциональная зависимость: если свой
клиент не передан, create_http_client лениво импортирует httpx.
"""

from __future__ import annotations

from typing import Any, Protocol, cast, runtime_checkable

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:159.0) Gecko/20100101 Firefox/159.0"
DEFAULT_ACCEPT_LANGUAGE = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"

DEFAULT_HEADERS = {"User-Agent": DEFAULT_USER_AGENT, "Accept-Language": DEFAULT_ACCEPT_LANGUAGE}

API_HOST = "https://api.vk.ru"
API_VERSION = "5.199"


@runtime_checkable
class HttpResponse(Protocol):
    """Минимальный ответ, достаточный библиотеке."""

    @property
    def status_code(self) -> int: ...

    @property
    def text(self) -> str: ...

    def json(self) -> Any: ...


@runtime_checkable
class HttpClient(Protocol):
    """Минимальный HTTP-клиент с асинхронными get и post."""

    async def get(self, url: str, **kwargs: Any) -> HttpResponse: ...

    async def post(self, url: str, **kwargs: Any) -> HttpResponse: ...

    async def aclose(self) -> None: ...


def create_http_client() -> HttpClient:
    """HTTP-клиент по умолчанию; httpx импортируется лениво (опциональная зависимость)."""
    try:
        import httpx
    except ImportError as exc:
        raise ImportError(
            "httpx не установлен. Установите его (pip install httpx) или передайте свой "
            "HTTP-клиент с асинхронными get/post в VKClient."
        ) from exc
    return cast(
        "HttpClient",
        httpx.AsyncClient(
            headers=DEFAULT_HEADERS,
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
        ),
    )
