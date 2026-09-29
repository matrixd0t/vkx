"""Автопагинация VK-методов (offset/count) на стороне клиента.

VK отдаёт не более ``PAGINATION_LIMITS[method]`` элементов за один запрос и
отклоняет больший ``count`` ошибкой. Поэтому клиент:

1. зажимает ``count`` до лимита метода (если ``count`` не задан — берёт лимит);
2. если VK всё же сообщает точный предел («count should be less or equal to N»),
   запоминает его и повторяет запрос;
3. добирает остаток страницами, увеличивая ``offset``, и сливает тела
   ``{count, items, ...}`` в один ответ:

- ``count`` — общее число элементов (VK кладёт его в каждый ответ);
- ``items`` — склейка страниц с сохранением порядка;
- прочие списочные поля (``profiles``, ``groups``, ...) — склейка с
  дедупликацией по ``id``.

Пагинация включается лениво, по телу ответа: если тело не похоже на
``{count, items}``, оно отдаётся как есть.
"""

from __future__ import annotations

import re
import typing

DEFAULT_PAGINATION_LIMIT = 100

PAGINATION_LIMITS: dict[str, int] = {
    "account.getActiveOffers": 100,
    "account.getBanned": 200,
    "appWidgets.getAppImages": 100,
    "appWidgets.getGroupImages": 100,
    "apps.getCatalog": 100,
    "apps.getFriendsList": 5000,
    "board.getComments": 100,
    "board.getTopics": 100,
    "bugtracker.getCompanyGroupMembers": 100,
    "bugtracker.getCompanyMembers": 100,
    "database.getChairs": 100,
    "database.getCities": 1000,
    "database.getCountries": 1000,
    "database.getFaculties": 500,
    "database.getMetroStations": 500,
    "database.getRegions": 1000,
    "database.getSchools": 10000,
    "database.getUniversities": 10000,
    "docs.get": 1000,
    "docs.search": 100,
    "donut.getFriends": 100,
    "donut.getSubscriptions": 100,
    "fave.get": 100,
    "fave.getPages": 500,
    "friends.get": 5000,
    "friends.getSuggestions": 100,
    "friends.search": 1000,
    "gifts.get": 100,
    "groups.get": 1000,
    "groups.getAddresses": 100,
    "groups.getBanned": 200,
    "groups.getInvitedUsers": 100,
    "groups.getInvites": 100,
    "groups.getMembers": 1000,
    "groups.getRequests": 200,
    "groups.search": 1000,
    "likes.getList": 1000,
    "market.get": 200,
    "market.getAlbums": 100,
    "market.getComments": 100,
    "market.getFavesForAttach": 100,
    "market.getGroupOrders": 50,
    "market.getOrderItems": 100,
    "market.getOrders": 10,
    "market.search": 200,
    "market.searchItems": 300,
    "market.searchItemsBasic": 300,
    "messages.getConversationMembers": 1000,
    "messages.getConversations": 200,
    "messages.getHistory": 200,
    "messages.getHistoryAttachments": 200,
    "messages.getImportantMessages": 200,
    "messages.getIntentUsers": 100,
    "messages.search": 100,
    "newsfeed.getMentions": 100,
    "newsfeed.getSuggestedSources": 100,
    "notes.get": 100,
    "notes.getComments": 100,
    "orders.get": 100,
    "photos.get": 1000,
    "photos.getAlbums": 100,
    "photos.getAll": 200,
    "photos.getAllComments": 100,
    "photos.getComments": 100,
    "photos.getNewTags": 100,
    "photos.getUserPhotos": 1000,
    "photos.search": 1000,
    "podcasts.searchPodcast": 100,
    "polls.getVoters": 1000,
    "prettyCards.get": 100,
    "storage.getKeys": 1000,
    "stories.getViewers": 100,
    "users.getFollowers": 1000,
    "users.getSubscriptions": 200,
    "users.search": 1000,
    "utils.getLastShortenedLinks": 200,
    "video.get": 200,
    "video.getAlbums": 100,
    "video.getComments": 200,
    "video.search": 200,
    "wall.get": 100,
    "wall.getComments": 100,
    "wall.getReposts": 100,
    "wall.search": 100,
    "widgets.getComments": 100,
    "widgets.getPages": 100,
}

FetchPage = typing.Callable[[dict[str, typing.Any]], typing.Awaitable[typing.Any]]

_LIMIT_PATTERNS = (
    re.compile(r"less or equal to (\d+)"),
    re.compile(r"count should be (\d+) or less"),
)


def limit_for(method: str) -> int | None:
    """Лимит count для метода или None, если метод не пагинируется."""
    return PAGINATION_LIMITS.get(method)


def parse_count_limit(error: BaseException) -> int | None:
    """Точный предел count из текста ошибки VK, если он там назван."""
    message = str(error)
    for pattern in _LIMIT_PATTERNS:
        match = pattern.search(message)
        if match:
            return int(match.group(1))
    return None


def remember_limit(method: str, limit: int) -> None:
    """Запомнить уточнённый предел метода (не повышаем известный)."""
    known = PAGINATION_LIMITS.get(method)
    PAGINATION_LIMITS[method] = limit if known is None else min(known, limit)


def _is_count_items(body: typing.Any) -> bool:
    return (
        isinstance(body, dict)
        and isinstance(body.get("items"), list)
        and isinstance(body.get("count"), int)
    )


def _merge_lists(key: str, pages: list[dict[str, typing.Any]]) -> list[typing.Any]:
    """Склейка списочного поля по страницам с дедупликацией словарей по id."""
    merged: list[typing.Any] = []
    seen: set[typing.Any] = set()
    for page in pages:
        for value in page.get(key) or []:
            marker = value.get("id") if isinstance(value, dict) else None
            if marker is not None:
                if marker in seen:
                    continue
                seen.add(marker)
            merged.append(value)
    return merged


def merge_pages(pages: list[dict[str, typing.Any]]) -> dict[str, typing.Any]:
    """Слияние страниц: общий count, склейка items и прочих списочных полей.

    ``items`` склеивается как есть (порядок страниц сохраняется); остальные
    списки (``profiles``, ``groups``, ...) — с дедупликацией по ``id``.
    """
    result = dict(pages[0])
    result["count"] = max(int(page["count"]) for page in pages)
    result["items"] = [value for page in pages for value in page.get("items") or []]
    for key in {key for page in pages for key in page}:
        if key in ("count", "items"):
            continue
        values = [page[key] for page in pages if key in page]
        if values and all(isinstance(value, list) for value in values):
            result[key] = _merge_lists(key, pages)
    return result


def _truncate(body: dict[str, typing.Any], requested: int | None) -> dict[str, typing.Any]:
    """Обрезать items до запрошенного count (VK иногда отдаёт лишнее)."""
    if requested is None or len(body["items"]) <= requested:
        return body
    return {**body, "items": body["items"][:requested]}


async def paginate(
    fetch: FetchPage,
    method: str,
    params: dict[str, typing.Any],
    first_result: typing.Any,
    requested: int | None = None,
) -> typing.Any:
    """Добрать страницы метода и слить их в один ответ.

    ``fetch(params)`` — вызов метода с новыми параметрами. ``first_result`` —
    уже полученный ответ на исходный запрос. ``requested`` — исходный ``count``
    пользователя (None = без ограничения). Если метод не пагинируется, тело не
    годится или запрошено не больше лимита, возвращается ``first_result``.
    """
    limit = limit_for(method)
    if limit is None or not _is_count_items(first_result):
        return first_result

    requested_int = None if requested is None else int(requested)
    base = int(params.get("offset") or 0)
    pages = [first_result]
    items = list(first_result["items"])
    total = int(first_result["count"])
    target = total - base if requested_int is None else min(requested_int, total - base)
    target = max(0, target)

    # Шаг offset = фактическая длина страницы: VK подмешивает рекламные объекты,
    # и offset считает их тоже, поэтому идём последовательно.
    while len(items) < target and pages[-1]["items"]:
        remaining = target - len(items)
        page = await fetch(
            {**params, "offset": base + len(items), "count": min(limit, remaining)}
        )
        if not _is_count_items(page) or not page["items"]:
            break
        pages.append(page)
        items.extend(page["items"])

    merged = first_result if len(pages) == 1 else merge_pages(pages)
    return _truncate(merged, target)


__all__ = (
    "DEFAULT_PAGINATION_LIMIT",
    "PAGINATION_LIMITS",
    "limit_for",
    "merge_pages",
    "paginate",
    "parse_count_limit",
    "remember_limit",
)
