"""Базовый класс категорий VK API.

Содержит общий хелпер `_call`: очищает параметры, запрашивает метод и возвращает
тело ответа (`response` из envelope), провалидированное в нужный тип.
"""

from __future__ import annotations

import functools
import typing

import pydantic

from ..base_model import attachment_to_string

Model = typing.TypeVar("Model")

_ATTACHMENT_KEYS: typing.Final = ("attachment", "attachments")


@functools.cache
def _adapter(model: typing.Any) -> pydantic.TypeAdapter:
    """Кэш TypeAdapter: тип тела ответа -> валидатор."""
    return pydantic.TypeAdapter(model)


class BaseCategory:
    def __init__(self, api: typing.Any) -> None:
        self.api = api

    @staticmethod
    def _clean(params: dict[str, typing.Any]) -> dict[str, typing.Any]:
        """Готовит параметры метода к отправке.

        Убирает self/None, bool -> int, снимает '_'; вложения (объекты с ``.as_att``
        и их списки) сворачивает в строку VK.
        """
        clean: dict[str, typing.Any] = {}
        for key, value in params.items():
            if key in ("self", "kwargs") or value is None:
                continue
            name = key.removeprefix("_")
            if name in _ATTACHMENT_KEYS:
                value = attachment_to_string(value)
                if not value:
                    continue
            elif isinstance(value, bool):
                value = int(value)
            clean[name] = value
        return clean

    @classmethod
    def get_set_params(cls, params: dict[str, typing.Any]) -> dict[str, typing.Any]:
        """Совместимость: раньше сливал kwargs; теперь просто чистит параметры."""
        return cls._clean(params)

    async def _call(
        self,
        method: str,
        params: dict[str, typing.Any],
        model: typing.Any = None,
        *,
        dependent: tuple[typing.Any, ...] = (),
        default: typing.Any = None,
    ) -> typing.Any:
        """Общий путь вызова: очистить params, запросить метод, вернуть тело `response`."""
        clean = self._clean(params)
        response = await self.api.request(method, clean)
        if dependent:
            model = self.get_model(dependent, default, clean)
        if model is None:
            raise TypeError(f"{method}: не задана модель ответа")
        payload = response.get("response") if isinstance(response, dict) and "response" in response else response
        try:
            return _adapter(model).validate_python(payload)
        except pydantic.ValidationError as exc:
            from ...client.errors import VKValidationError

            metadata = response if isinstance(response, dict) else {}
            call = metadata.get("_vkx_call")
            raw_responses = tuple(metadata.get("_vkx_raw_responses", ()))
            model_name = getattr(model, "__name__", repr(model))
            raise VKValidationError(
                f"{method}: ответ не прошёл валидацию для {model_name}: {exc}",
                client=getattr(call, "client", None),
                call=call,
                raw=payload,
                raw_response=metadata.get("_vkx_raw_response"),
                raw_responses=raw_responses,
                validation_error=exc,
            ) from exc

    @classmethod
    def get_model(
        cls,
        dependent: tuple[typing.Any, ...],
        default: Model,
        params: dict[str, typing.Any],
    ) -> Model:
        """Выбирает модель ответа в зависимости от параметров."""

        for items in sorted(dependent, key=lambda x: len(x[0]) if isinstance(x, tuple) else bool(x)):
            if isinstance(items, dict):
                for key, models in items.items():
                    if isinstance(string_value := params.get(key), str) and (model := models.get(string_value)) is not None:
                        return model
            else:
                keys, model = items

                for key in keys:
                    if (isinstance(key, str) and params.get(key) in (None, False)) or (
                        isinstance(key, (tuple, list)) and params.get(key[0]) not in key[1:]
                    ):
                        break
                else:
                    return model

        return default

    @classmethod
    def construct_api(cls, api: typing.Any) -> BaseCategory:
        return cls(api)


__all__ = ("BaseCategory",)
