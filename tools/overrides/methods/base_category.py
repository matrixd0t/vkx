"""Базовый класс категорий VK API.

Накатывается поверх генерации: содержит общий хелпер `_call`, который сворачивает
типовое тело сгенерированного метода (`get_set_params` -> `api.request` ->
`model(**response).response`) в одну строку.
"""

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from vkx.callback.generated.base_model import BaseModel

Model = typing.TypeVar("Model")


class BaseCategory:
    def __init__(self, api: typing.Any) -> None:
        self.api = api

    @staticmethod
    def _clean(params: dict[str, typing.Any]) -> dict[str, typing.Any]:
        """Готовит параметры метода к отправке: убирает self/None, bool -> int, снимает '_'."""
        return {
            k.removeprefix("_"): int(v) if isinstance(v, bool) else v
            for k, v in params.items()
            if k != "self" and k != "kwargs" and v is not None
        }

    @classmethod
    def get_set_params(cls, params: dict[str, typing.Any]) -> dict[str, typing.Any]:
        """Совместимость: раньше сливал kwargs; теперь просто чистит параметры."""
        return cls._clean(params)

    async def _call(
        self,
        method: str,
        params: dict[str, typing.Any],
        model: type[Model] | None = None,
        *,
        dependent: tuple[typing.Any, ...] = (),
        default: type[Model] | None = None,
    ) -> Model:
        """Общий путь вызова: очистить params, запросить метод, развернуть `.response`."""
        clean = self._clean(params)
        response = await self.api.request(method, clean)
        if dependent:
            model = self.get_model(dependent, default, clean)  # type: ignore[arg-type]
        if model is None:
            raise TypeError(f"{method}: не задана модель ответа")
        return model(**response).response

    @classmethod
    def get_model(
        cls,
        dependent: tuple[
            tuple[
                tuple[str | typing.Sequence[str], ...],
                type[BaseModel],
            ]
            | dict[str, dict[str, type[BaseModel]]],
            ...,
        ],
        default: Model,
        params: dict[str, typing.Any],
    ) -> Model:
        """Выбирает модель ответа в зависимости от параметров."""

        for items in sorted(dependent, key=lambda x: len(x[0]) if isinstance(x, tuple) else bool(x)):
            if isinstance(items, dict):
                for key, models in items.items():
                    if isinstance(string_value := params.get(key), str) and (model := models.get(string_value)) is not None:
                        return model  # type: ignore
            else:
                keys, model = items

                for key in keys:
                    if (isinstance(key, str) and params.get(key) in (None, False)) or (
                        isinstance(key, (tuple, list)) and params.get(key[0]) not in key[1:]
                    ):
                        break
                else:
                    return model  # type: ignore

        return default

    @classmethod
    def construct_api(cls, api: typing.Any) -> BaseCategory:
        return cls(api)


__all__ = ("BaseCategory",)
