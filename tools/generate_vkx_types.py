"""Генератор самодостаточных типов vkx на основе vkbottle-types.

ЛЕГАСИ-БУТСТРАП: раскладка `vkx.callback.generated` больше не используется
(типы вручную поддерживаются в `src/vkx/models/`). Скрипт оставлен на случай
массового обновления схемы; его вывод нужно вручную разложить в `vkx/models/`.

Копирует пакет `vkbottle_types` в `src/vkx/callback/generated`, переписывает
импортные пути на `vkx.callback.generated`, убирает внешние зависимости
(`typing_extensions`, `vkbottle`, `msgspec` — последний правится вручную)
и переименовывает классы в vkx-стиль (снятие категорийного префикса).

Запуск:
    python tools/generate_vkx_types.py --dry-run
    python tools/generate_vkx_types.py
"""

from __future__ import annotations

import argparse
import ast
import re
import shutil
import sys
from pathlib import Path

try:
    import vkbottle_types
except ImportError:  # pragma: no cover
    print("vkbottle-types не установлен в текущем интерпретаторе", file=sys.stderr)
    raise SystemExit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC = Path(vkbottle_types.__file__).parent
DST = REPO_ROOT / "src" / "vkx" / "callback" / "generated"

SRC_PACKAGE = "vkbottle_types"
DST_PACKAGE = "vkx.callback.generated"

CATEGORY_PREFIXES = (
    "Account",
    "Ads",
    "AppWidgets",
    "Apps",
    "Audio",
    "Auth",
    "Board",
    "Bugtracker",
    "Calls",
    "Callback",
    "Database",
    "Docs",
    "Donut",
    "DownloadedGames",
    "Fave",
    "Friends",
    "Gifts",
    "Groups",
    "LeadForms",
    "Likes",
    "Market",
    "Messages",
    "Newsfeed",
    "Notes",
    "Notifications",
    "Orders",
    "Pages",
    "Photos",
    "Podcasts",
    "Polls",
    "PrettyCards",
    "Search",
    "Secure",
    "Stats",
    "Status",
    "Storage",
    "Store",
    "Stories",
    "Streaming",
    "Users",
    "Utils",
    "Video",
    "Wall",
    "Widgets",
    "Base",
)

# Классы/имена, которые не переименовываем и не должны быть целью переименования.
INFRA_NAMES = {
    "BaseModel",
    "BaseEnumMeta",
    "StrEnum",
    "IntEnum",
    "FloatEnum",
    "Field",
    "BaseCategory",
    "BaseResponse",
    "DictResponse",
    "BaseEventObject",
    "BaseGroupEvent",
    "BaseUserEvent",
    "Model",
}

# Целевые имена, слишком общие/конфликтующие с инфраструктурой и typing.
RESERVED_TARGETS = INFRA_NAMES | {
    "Any",
    "Attachments",
    "Callable",
    "Dict",
    "ExtraValues",
    "Generic",
    "JsonObject",
    "List",
    "Literal",
    "Optional",
    "Response",
    "Category",
    "Object",
    "Item",
    "Info",
    "Event",
    "Set",
    "Self",
    "Tuple",
    "Type",
    "TypeAlias",
    "Union",
}

# Модули, из которых не собираем имена для переименования.
EXCLUDED_MODULES = {
    "base_model.py",
    "categories.py",
    "methods/base_category.py",
    "responses/base_response.py",
    "responses/__init__.py",
}


def _is_excluded(rel: str) -> bool:
    return rel in EXCLUDED_MODULES or rel.endswith("__init__.py")


EVENT_WRAPPER_MODULES = {"events/bot_events.py", "events/user_events.py"}


def collect_class_names(src: Path) -> dict[str, set[str]]:
    """name -> модули, в которых он определён."""
    names: dict[str, set[str]] = {}
    for py in src.rglob("*.py"):
        rel = py.relative_to(src).as_posix()
        if _is_excluded(rel):
            continue
        try:
            tree = ast.parse(py.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                names.setdefault(node.name, set()).add(rel)
    return names


def strip_prefix(name: str) -> str:
    for prefix in CATEGORY_PREFIXES:
        if name.startswith(prefix) and len(name) > len(prefix) and name[len(prefix)].isupper():
            return name[len(prefix):]
    return name


def _candidate(name: str, modules: set[str]) -> str:
    if modules & EVENT_WRAPPER_MODULES:
        if not name.endswith("Event") and name not in INFRA_NAMES:
            return name + "Event"
        return name
    return strip_prefix(name)


# «Основные» категории: при коллизии короткое имя достаётся модели из них,
# а `Base*`/`Callback*`/нишевые остаются с полным именем.
PRIMARY_CATEGORIES = {
    "Messages",
    "Photos",
    "Users",
    "Groups",
    "Wall",
    "Video",
    "Audio",
    "Docs",
    "Market",
    "Board",
    "Notes",
    "Polls",
    "Pages",
    "Stories",
    "Friends",
    "Newsfeed",
    "Account",
    "Stats",
    "Database",
    "Gifts",
    "Fave",
    "Likes",
    "Orders",
    "Apps",
    "Search",
    "Secure",
    "Status",
    "Storage",
    "Store",
    "Streaming",
    "Utils",
    "Widgets",
}


def _is_primary(name: str) -> bool:
    for prefix in PRIMARY_CATEGORIES:
        if name.startswith(prefix) and len(name) > len(prefix) and name[len(prefix)].isupper():
            return True
    return False


def build_rename_map(modules_by_name: dict[str, set[str]]) -> dict[str, str]:
    """Инъективное отображение original -> vkx-имя.

    Переименовываем только если результат уникален и не конфликтует с
    существующими/зарезервированными именами. Иначе — оставляем исходное имя,
    чтобы не ломать forward-refs и сборку pydantic-моделей.
    """
    names = set(modules_by_name)
    groups: dict[str, list[str]] = {}
    for name, modules in modules_by_name.items():
        cand = _candidate(name, modules)
        if cand != name:
            groups.setdefault(cand, []).append(name)

    rename: dict[str, str] = {}
    for cand, originals in groups.items():
        if cand in names or cand in RESERVED_TARGETS:
            continue
        if len(originals) == 1:
            rename[originals[0]] = cand
            continue
        primary = [original for original in originals if _is_primary(original)]
        if len(primary) == 1:
            rename[primary[0]] = cand
    return rename


def _replace_import_line(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        indent = match.group(1)
        return f"{indent}pass  # vkbottle removed\n"

    return re.sub(r"^([ \t]*)from vkbottle import .*\n", repl, text, flags=re.MULTILINE)


def _rewrite_typing_extensions(text: str) -> str:
    text = text.replace("import typing_extensions as typing", "import typing")
    text = re.sub(r"from typing_extensions import", "from typing import", text)
    return text


def _rewrite_abcapi(text: str) -> str:
    text = text.replace('"ABCAPI | API"', '"Any"')
    text = text.replace("'ABCAPI | API'", "'Any'")
    text = text.replace('"ABCAPI"', '"typing.Any"')
    text = text.replace("'ABCAPI'", "'typing.Any'")
    return text


def _rewrite_codegen_objects_refs(text: str) -> str:
    """Убирает доступ к подмодулю через атрибуты пакета (ломался при
    частично инициализированном `vkx.callback.generated`)."""
    text = text.replace(
        f"import {DST_PACKAGE}.codegen.objects",
        f"from {DST_PACKAGE}.codegen import objects as _codegen_objects",
    )
    text = text.replace(
        f"vars({DST_PACKAGE}.codegen.objects)",
        "vars(_codegen_objects)",
    )
    text = text.replace(
        f"{DST_PACKAGE}.codegen.objects.__all__",
        "_codegen_objects.__all__",
    )

    aliases: dict[str, str] = {}
    pattern = re.compile(rf"^import ({re.escape(DST_PACKAGE)}\.codegen\.[\w.]+)\s*$", re.MULTILINE)

    def repl(match: re.Match[str]) -> str:
        module = match.group(1)
        alias = "_all_" + module.rsplit(".", 1)[1]
        aliases[module] = alias
        return f"from {module} import __all__ as {alias}  # noqa: F401"

    text = pattern.sub(repl, text)
    for module in sorted(aliases, key=len, reverse=True):
        text = text.replace(f"{module}.__all__", aliases[module])
    return text


# ---------- сворачивание типового тела сгенерированного метода ----------

# `**kwargs: typing.Any,` / `**kwargs,` — после BaseCategory._call больше не нужны,
# а их отсутствие даёт строгую проверку неизвестных аргументов на уровне Python.
_KWARGS_LINE = re.compile(r"^[ \t]*\*\*kwargs(?:: [^,\n]+)?,[ \t]*\n", re.MULTILINE)

# params = self.get_set_params(locals())
# response = await self.api.request("board.addTopic", params)
# model = AddTopicResponse
# return model(**response).response
_STANDARD_BODY = re.compile(
    r"^(?P<ind>[ \t]*)params = self\.get_set_params\(locals\(\)\)[^\n]*\n"
    r"[ \t]*response = await self\.api\.request\((?P<method>\"[^\"]*\"), params\)[^\n]*\n"
    r"[ \t]*model = (?P<model>[^\n]+?)\s*\n"
    r"[ \t]*return model\(\*\*response\)\.response\n",
    re.MULTILINE,
)

# тот же шаблон, но с выбором модели через self.get_model(...)
_GET_MODEL_BODY = re.compile(
    r"^(?P<ind>[ \t]*)params = self\.get_set_params\(locals\(\)\)[^\n]*\n"
    r"[ \t]*response = await self\.api\.request\((?P<method>\"[^\"]*\"), params\)[^\n]*\n"
    r"[ \t]*model = self\.get_model\([^\n]*\n"
    r"(?P<dependent>.*?),\n"
    r"[ \t]*default=(?P<default>[A-Za-z_]\w*),\n"
    r"[ \t]*params=params,\n"
    r"[ \t]*\)\n"
    r"[ \t]*return model\(\*\*response\)\.response\n",
    re.MULTILINE | re.DOTALL,
)


def _collapse_bodies(text: str) -> str:
    """Сворачивает 4-строчное тело метода в один вызов `self._call(...)`."""

    def standard(match: re.Match[str]) -> str:
        ind = match.group("ind")
        return f'{ind}return await self._call({match.group("method")}, locals(), {match.group("model")})\n'

    def dependent(match: re.Match[str]) -> str:
        ind = match.group("ind")
        dep = " ".join(part.strip() for part in match.group("dependent").splitlines())
        return (
            f"{ind}return await self._call(\n"
            f"{ind}    {match.group('method')},\n"
            f"{ind}    locals(),\n"
            f"{ind}    dependent={dep},\n"
            f"{ind}    default={match.group('default')},\n"
            f"{ind})\n"
        )

    text = _GET_MODEL_BODY.sub(dependent, text)
    return _STANDARD_BODY.sub(standard, text)


def transform(text: str, rename: dict[str, str]) -> str:
    text = text.replace(SRC_PACKAGE, DST_PACKAGE)
    text = _rewrite_codegen_objects_refs(text)
    text = _rewrite_typing_extensions(text)
    text = _replace_import_line(text)
    text = _rewrite_abcapi(text)
    if rename:
        pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(rename, key=len, reverse=True)) + r")\b")
        text = pattern.sub(lambda m: rename[m.group(1)], text)
    text = _KWARGS_LINE.sub("", text)
    return _collapse_bodies(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="только показать статистику")
    args = parser.parse_args()

    modules_by_name = collect_class_names(SRC)
    rename = build_rename_map(modules_by_name)

    print(f"source: {SRC}")
    print(f"dest:   {DST}")
    print(f"class names: {len(modules_by_name)}  renamed: {len(rename)}")
    print("event examples:")
    for old in sorted(rename):
        if modules_by_name[old] & EVENT_WRAPPER_MODULES:
            print(f"  {old} -> {rename[old]}")
    print("object examples:")
    for old in sorted(rename)[:15]:
        if not (modules_by_name[old] & EVENT_WRAPPER_MODULES):
            print(f"  {old} -> {rename[old]}")

    if args.dry_run:
        return 0

    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    written = 0
    for py in SRC.rglob("*.py"):
        rel = py.relative_to(SRC)
        out = DST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(transform(py.read_text(encoding="utf-8"), rename), encoding="utf-8")
        written += 1

    leftovers = 0
    for py in DST.rglob("*.py"):
        content = py.read_text(encoding="utf-8")
        leftovers += content.count("self.get_set_params(locals())")
        leftovers += content.count("await self.api.request(")
    if leftovers:
        print(
            f"ERROR: не свернуто тел методов: {leftovers}; проверь формат в vkbottle-types",
            file=sys.stderr,
        )
        return 2

    typed = SRC / "py.typed"
    if typed.exists():
        shutil.copy2(typed, DST / "py.typed")

    print(f"written .py files: {written}")

    overrides = REPO_ROOT / "tools" / "overrides"
    if overrides.exists():
        applied = 0
        for override in overrides.rglob("*"):
            if override.is_file():
                out = DST / override.relative_to(overrides)
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(override, out)
                applied += 1
        print(f"applied overrides: {applied}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
