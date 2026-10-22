"""Разбор разметки сообщения (HTML/markdown) в ``format_data`` VK.

VK принимает форматирование текста отдельным параметром ``format_data`` — JSON-строкой
``{"version": "1", "items": [{"type": "bold", "offset": 0, "length": 4}]}``. Смещения и
длины считаются в code units UTF-16 (единица, которой индексирует текст веб-клиент
VK), поэтому эмодзи занимают две позиции.

Разбираются:

* HTML: ``<b>``/``<strong>`` — жирный, ``<i>``/``<em>`` — курсив,
  ``<u>``/``<ins>`` — подчёркнутый, ``<a href="...">`` — ссылка, ``<br>`` — перенос строки.
* Markdown: ``**жирный**``, ``*курсив*``/``_курсив_``, ``__подчёркнутый__``,
  ``[текст](ссылка)``.

Зачёркивание (``<s>``, ``<del>``, ``~~текст~~``) VK не рисует, а неподдерживаемый тип
обнуляет весь ``format_data`` — поэтому такие теги снимаются, но элемент не создаётся.
"""

from __future__ import annotations

import collections.abc
import json
import re
import typing

from .objects import FormatData, FormatItem

type FormatDataInput = str | FormatData | typing.Mapping[str, typing.Any]
"""``format_data`` на входе: JSON-строка, модель или обычный dict."""

SUPPORTED_FORMAT_TYPES: typing.Final = ("bold", "italic", "underline", "url")
"""Типы форматирования, которые VK действительно рисует."""

_STYLE_RANK: typing.Final[dict[str, int]] = {
    "bold": 0,
    "italic": 1,
    "underline": 2,
    "url": 3,
}

_HTML_STYLES: typing.Final[dict[str, str | None]] = {
    "b": "bold",
    "strong": "bold",
    "i": "italic",
    "em": "italic",
    "u": "underline",
    "ins": "underline",
    "s": None,
    "strike": None,
    "del": None,
    "a": "url",
}
"""HTML-тег -> тип ``format_data``. ``None`` — тег снимается, но стиль не создаётся
(зачёркивания VK не умеет)."""

_MD_DELIMITERS: typing.Final = (
    ("**", "bold"),
    ("*", "italic"),
    ("__", "underline"),
    ("_", "italic"),
    ("~~", None),
    ("~", None),
)
"""Markdown-разделители и соответствующие типы ``format_data``."""

_TAG_RE = re.compile(
    r"<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:[^<>\"']|\"[^\"]*\"|'[^']*')*)(/?)>"
)
"""HTML-тег: ``<b>``, ``</b>``, ``<a href="...">``."""

_ATTR_RE = re.compile(
    r"""([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+))"""
)


def u16_len(text: str) -> int:
    """Длина текста в code units UTF-16 — единица смещений в ``format_data``."""
    return len(text.encode("utf-16-le")) // 2


class _Token(typing.NamedTuple):
    kind: str
    """``text`` — обычный текст, ``open`` — открыть стиль, ``close`` — закрыть стиль."""

    text: str = ""
    style: str = ""
    url: str = ""


def _is_escaped(text: str, index: int) -> bool:
    """True, если символ перед ``index`` — нечётное число обратных слэшей."""
    backslashes = 0
    position = index - 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return backslashes % 2 == 1


def _attr_value(attrs: str, name: str) -> str:
    """Значение HTML-атрибута (пустая строка, если атрибута нет)."""
    for match in _ATTR_RE.finditer(attrs):
        if match.group(1).lower() == name:
            value = match.group(2) or match.group(3) or match.group(4) or ""
            return value.strip()
    return ""


def _opens(text: str, index: int, delim: str) -> bool:
    """Разделитель может открывать разметку (не заканчивается пробелом)."""
    after = text[index + len(delim): index + len(delim) + 1]
    if not after or after.isspace():
        return False
    if delim.startswith("_"):
        # подчёркивание не работает внутри слова: snake_case_name — обычный текст
        return not text[index - 1: index].isalnum()
    return True


def _closes(text: str, index: int, delim: str) -> bool:
    """Разделитель может закрывать разметку (перед ним не пробел)."""
    if not text[index - 1: index] or text[index - 1: index].isspace():
        return False
    if delim.startswith("_"):
        after = text[index + len(delim): index + len(delim) + 1]
        if after.isalnum():
            return False
    return True


def _find_closer(text: str, start: int, delim: str) -> int:
    """Позиция закрывающего разделителя (или -1)."""
    index = text.find(delim, start)
    while index != -1:
        if not _is_escaped(text, index):
            return index
        index = text.find(delim, index + 1)
    return -1


def _match_markdown(text: str, index: int) -> tuple[int, str | None, str] | None:
    """Markdown-разметка в позиции ``index``: -> (конец, тип, внутренний текст)."""
    for delim, style in _MD_DELIMITERS:
        if not text.startswith(delim, index):
            continue
        if _is_escaped(text, index):
            return None
        body = index + len(delim)
        close = _find_closer(text, body, delim)
        if close == -1:
            continue
        inner = text[body:close]
        if not inner.strip():
            continue
        if not _opens(text, index, delim) or not _closes(text, close, delim):
            continue
        return close + len(delim), style, inner
    return None


def _match_link(text: str, index: int) -> tuple[str, str, int] | None:
    """Markdown-ссылка ``[текст](адрес)`` в позиции ``index``: -> (текст, адрес, конец)."""
    close = text.find("]", index + 1)
    if close == -1 or text[close + 1: close + 2] != "(":
        return None
    end = text.find(")", close + 2)
    if end == -1:
        return None
    label = text[index + 1: close]
    url = text[close + 2: end].strip()
    if not label.strip() or not url:
        return None
    return label, url, end + 1


def _html_tokens(match: re.Match[str]) -> list[_Token]:
    """Токены HTML-тега: открытие/закрытие стиля, перенос строки или ничего."""
    closing, name, attrs = match.group(1), match.group(2).lower(), match.group(3)
    if closing:
        style = _HTML_STYLES.get(name)
        return [_Token("close", style=style)] if style else []
    if name == "br":
        return [_Token("text", "\n")]
    if name not in _HTML_STYLES:
        return []  # неизвестный тег — просто снимаем
    style = _HTML_STYLES[name]
    if style == "url":
        url = _attr_value(attrs, "href")
        return [_Token("open", style="url", url=url)] if url else []
    if style is None:
        return []  # зачёркивание VK не рисует
    return [_Token("open", style=style)]


def _tokenize(text: str, *, markdown: bool = True, html: bool = True) -> list[_Token]:
    """Текст -> токены (текст, открытие/закрытие стиля).

    Выключенный синтаксис (markdown/html) не разбирается: его маркеры остаются
    обычным текстом.
    """
    tokens: list[_Token] = []
    buf: list[str] = []
    index = 0
    length = len(text)

    def flush() -> None:
        if buf:
            tokens.append(_Token("text", "".join(buf)))
            buf.clear()

    while index < length:
        char = text[index]

        if char == "<" and html:
            match = _TAG_RE.match(text, index)
            if match:
                flush()
                tokens.extend(_html_tokens(match))
                index = match.end()
                continue

        if char == "[" and markdown:
            link = _match_link(text, index)
            if link is not None:
                label, url, end = link
                flush()
                tokens.append(_Token("open", style="url", url=url))
                tokens.extend(_tokenize(label, markdown=markdown, html=html))
                tokens.append(_Token("close", style="url"))
                index = end
                continue

        if char in "*_~" and markdown:
            found = _match_markdown(text, index)
            if found is not None:
                end, style, inner = found
                flush()
                if style:
                    tokens.append(_Token("open", style=style))
                    tokens.extend(_tokenize(inner, markdown=markdown, html=html))
                    tokens.append(_Token("close", style=style))
                else:
                    # стиль VK не поддерживает — маркеры снимаем, текст оставляем
                    tokens.extend(_tokenize(inner, markdown=markdown, html=html))
                index = end
                continue
            if _is_escaped(text, index):
                for delim, _ in _MD_DELIMITERS:
                    if text.startswith(delim, index):
                        buf.append(delim)
                        index += len(delim)
                        break
                else:
                    buf.append(char)
                    index += 1
                continue

        buf.append(char)
        index += 1

    flush()
    return tokens


def _build_runs(tokens: list[_Token]) -> list[tuple[str, frozenset[str], str | None]]:
    """Токены -> фрагменты текста с набором активных стилей."""
    runs: list[tuple[str, frozenset[str], str | None]] = []
    stack: list[tuple[str, str]] = []
    buf: list[str] = []

    def styles_now() -> frozenset[str]:
        return frozenset(style for style, _ in stack)

    def url_now() -> str | None:
        for style, url in reversed(stack):
            if style == "url" and url:
                return url
        return None

    def flush() -> None:
        if buf:
            runs.append(("".join(buf), styles_now(), url_now()))
            buf.clear()

    for token in tokens:
        if token.kind == "text":
            buf.append(token.text)
            continue
        flush()
        if token.kind == "open":
            stack.append((token.style, token.url))
        else:
            for position in range(len(stack) - 1, -1, -1):
                if stack[position][0] == token.style:
                    del stack[position]
                    break

    flush()
    return runs


def _merge_runs(
    runs: list[tuple[str, frozenset[str], str | None]],
) -> list[tuple[str, frozenset[str], str | None]]:
    """Склеить соседние фрагменты с одинаковыми стилями (непрерывный участок)."""
    merged: list[tuple[str, frozenset[str], str | None]] = []
    for text, styles, url in runs:
        if merged and merged[-1][1] == styles and merged[-1][2] == url:
            merged[-1] = (merged[-1][0] + text, styles, url)
        else:
            merged.append((text, styles, url))
    return merged


def _build_items(runs: list[tuple[str, frozenset[str], str | None]]) -> list[FormatItem]:
    """Фрагменты -> элементы ``format_data`` (смещения в UTF-16).

    Участки одного типа, идущие внахлёст или подряд, склеиваются в один —
    VK ограничивает количество элементов, а выглядит результат одинаково.
    """
    spans: dict[tuple[str, str], list[tuple[int, int]]] = {}
    offset = 0
    for text, styles, url in runs:
        length = u16_len(text)
        if length:
            for style in sorted(styles, key=lambda name: _STYLE_RANK.get(name, 99)):
                if style not in SUPPORTED_FORMAT_TYPES:
                    continue
                if style == "url":
                    if not url:
                        continue
                    spans.setdefault((style, url), []).append((offset, offset + length))
                else:
                    spans.setdefault((style, ""), []).append((offset, offset + length))
        offset += length

    items: list[FormatItem] = []
    for (style, url), ranges in spans.items():
        merged: list[tuple[int, int]] = []
        for start, end in sorted(ranges):
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        for start, end in merged:
            if style == "url":
                items.append(
                    FormatItem(type=style, offset=start, length=end - start, url=url)
                )
            else:
                items.append(FormatItem(type=style, offset=start, length=end - start))
    items.sort(key=lambda item: (item.offset, _STYLE_RANK.get(item.type, 99)))
    return items


def parse_format(
    text: str,
    *,
    markdown: bool = True,
    html: bool = True,
) -> tuple[str, list[FormatItem]]:
    """Разобрать разметку в тексте сообщения.

    Возвращает ``(текст без разметки, элементы format_data)``. Если разметки нет —
    текст возвращается как есть, элементов пустой список.

    ``markdown``/``html`` включают соответствующий синтаксис; выключенный
    синтаксис остаётся обычным текстом (маркеры не снимаются).
    """
    if not text:
        return text, []
    runs = _merge_runs(_build_runs(_tokenize(text, markdown=markdown, html=html)))
    plain = "".join(run[0] for run in runs)
    return plain, _build_items(runs)


def format_data_json(items: typing.Iterable[FormatItem]) -> str:
    """Собрать JSON-строку ``format_data`` из элементов."""
    return FormatData(items=list(items)).model_dump_json(exclude_none=True)


def format_data_to_json(value: typing.Any) -> str | None:
    """Привести переданный ``format_data`` к JSON-строке (или ``None``)."""
    if value is None:
        return None
    if isinstance(value, str):
        return value or None
    if isinstance(value, FormatData):
        return value.model_dump_json(exclude_none=True)
    if isinstance(value, collections.abc.Mapping):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, (list, tuple)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)
    return str(value)


def slice_items(items: typing.Iterable[FormatItem], start: int, end: int) -> list[FormatItem]:
    """Оставить части элементов, попавшие в диапазон ``[start, end)`` (UTF-16)."""
    result: list[FormatItem] = []
    for item in items:
        item_end = item.offset + item.length
        low = max(item.offset, start)
        high = min(item_end, end)
        if high <= low:
            continue
        result.append(item.model_copy(update={"offset": low - start, "length": high - low}))
    return result


__all__ = (
    "SUPPORTED_FORMAT_TYPES",
    "FormatDataInput",
    "format_data_json",
    "format_data_to_json",
    "parse_format",
    "slice_items",
    "u16_len",
)
