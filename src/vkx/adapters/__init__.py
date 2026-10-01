"""Веб-адаптеры Callback API для конкретных фреймворков.

Ядро живёт в ``._common`` и не зависит от фреймворков. Каждый модуль
(``fastapi``, ``starlette``, ``aiohttp``, ``sanic``, ``django``, ``flask``)
подключает свой фреймворк лениво — при импорте самого модуля, поэтому в
зависимостях vkx ничего лишнего не появляется: адаптер импортируют только те,
у кого этот фреймворк уже установлен.

Async-фреймворки используют ``CallbackDispatch`` (задача в текущем loop),
синхронные — ``SyncCallbackDispatch`` (handler выполняется в том же потоке, что
и обработка колбека, и обязан быть синхронным). Ни отдельный loop, ни пул
потоков не нужны.
"""

from ._common import CallbackDispatch, EventHandler, SyncCallbackDispatch

__all__ = ("CallbackDispatch", "EventHandler", "SyncCallbackDispatch")
