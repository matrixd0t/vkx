"""Хелперы загрузки файлов в VK: изображения (photos.*) и документы (docs.*).

Полный цикл одного хелпера:

1. запрос сервера загрузки (getUploadServer) идёт через обычную очередь
   клиента — со всеми повторами и батчингом;
2. сами байты отправляются multipart-запросом прямо на полученный upload_url
   HTTP-клиентом клиента: загрузка — не вызов VK API, поэтому очередь она не
   занимает и паузу ``interval`` не ждёт;
3. сохранение (save) снова идёт через очередь, а хелпер возвращает
   типизированное вложение.

Свободные функции принимают клиент первым аргументом:

    photo = await upload_photo_to_wall(vk, data, group_id=1, caption="hi")

Тот же набор доступен как namespace ``vk.upload`` (имена без префикса
``upload_``), привязанный к клиенту:

    photo = await vk.upload.photo_to_wall(data, group_id=1, caption="hi")

Загрузка идёт HTTP-клиентом клиента (``vk.http_client``), который должен
принимать httpx-совместимые ``files``/``data``; штатный ``httpx.AsyncClient``
подходит. Поле multipart-формы можно переопределить параметром ``field``.
"""

from __future__ import annotations

import mimetypes
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from .http import HttpClient

if TYPE_CHECKING:
    from vkx.models.objects import Photo
    from vkx.models.responses.docs import DocsSaveResponseModel
    from vkx.models.responses.messages import SetChatPhotoResponseModel
    from vkx.models.responses.photos import (
        SaveOwnerCoverPhotoResponseModel,
        SaveOwnerPhotoResponseModel,
    )

    from .client import VKClient

PHOTO_FILENAME = "photo.jpg"
DOC_FILENAME = "file"
PHOTO_CONTENT_TYPE = "image/jpeg"
DOC_CONTENT_TYPE = "application/octet-stream"


def _error(client: VKClient, message: str, *, raw: Any = None) -> Exception:
    from .client import VKError

    return VKError(message, client=client, raw=raw)


def _guess_content_type(filename: str, fallback: str) -> str:
    guessed, _ = mimetypes.guess_type(filename)
    return guessed or fallback


def _upload_url(payload: Any, *, client: VKClient, method: str) -> str:
    url = payload.get("upload_url") if isinstance(payload, Mapping) else None
    if not isinstance(url, str) or not url:
        raise _error(client, f"{method}: сервер не вернул upload_url", raw=payload)
    return url


def _as_mapping(payload: Any, *, client: VKClient, method: str) -> Mapping[str, Any]:
    if not isinstance(payload, Mapping):
        raise _error(
            client, f"{method}: сервер загрузки вернул неожиданный ответ", raw=payload
        )
    return payload


def _normalize_payload(payload: Any) -> Any:
    """Upload-серверы VK иногда оборачивают поля в ``{"response": {...}}`` — снимаем."""
    if isinstance(payload, Mapping):
        inner = payload.get("response")
        if isinstance(inner, Mapping):
            return inner
    return payload


async def _post_file(
    client: VKClient,
    url: str,
    data: bytes,
    *,
    field: str,
    filename: str,
    content_type: str,
    form: Mapping[str, Any] | None = None,
    http_client: HttpClient | None = None,
) -> Any:
    """Multipart-отправка байтов на upload_url; возвращает ответ как есть."""
    kwargs: dict[str, Any] = {"files": {field: (filename, data, content_type)}}
    if form:
        kwargs["data"] = dict(form)
    response = await (http_client or client.http_client).post(url, **kwargs)
    status = int(getattr(response, "status_code", 200) or 0)
    if status >= 400:
        text = str(getattr(response, "text", ""))
        raise _error(client, f"загрузка файла: HTTP {status}", raw=text[:300])
    try:
        return _normalize_payload(response.json())
    except ValueError:
        return getattr(response, "text", "")


async def _upload(
    client: VKClient,
    data: bytes,
    *,
    server_method: str,
    field: str,
    filename: str,
    content_type: str | None,
    default_content_type: str,
    server_params: Mapping[str, Any],
    form: Mapping[str, Any] | None = None,
    http_client: HttpClient | None = None,
) -> Any:
    """Сервер загрузки через очередь -> multipart напрямую -> ответ сервера."""
    payload = await client.call(server_method, **server_params)
    url = _upload_url(payload, client=client, method=server_method)
    resolved = content_type or _guess_content_type(filename, default_content_type)
    return await _post_file(
        client,
        url,
        data,
        field=field,
        filename=filename,
        content_type=resolved,
        form=form,
        http_client=http_client,
    )


# ---------- изображения (photos.*) ----------


async def upload_photo_to_album(
    client: VKClient,
    data: bytes,
    *,
    album_id: int | None = None,
    group_id: int | None = None,
    caption: str | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "file1",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> list[Photo]:
    """Загрузить фото в альбом: photos.getUploadServer -> photos.save."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={"album_id": album_id, "group_id": group_id, **server_params},
        http_client=http_client,
    )
    uploaded = _as_mapping(raw, client=client, method="photos.getUploadServer")
    return await client.photos.save(
        album_id=album_id,
        group_id=group_id,
        caption=caption,
        latitude=latitude,
        longitude=longitude,
        server=uploaded.get("server"),
        photos_list=uploaded.get("photos_list"),
        hash=uploaded.get("hash"),
    )


async def upload_photo_to_wall(
    client: VKClient,
    data: bytes,
    *,
    group_id: int | None = None,
    user_id: int | None = None,
    caption: str | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "photo",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> list[Photo]:
    """Загрузить фото на стену: photos.getWallUploadServer -> photos.saveWallPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getWallUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={"group_id": group_id, **server_params},
        http_client=http_client,
    )
    uploaded = _as_mapping(raw, client=client, method="photos.getWallUploadServer")
    return await client.photos.save_wall_photo(
        photo=uploaded.get("photo"),
        server=uploaded.get("server"),
        hash=uploaded.get("hash"),
        group_id=group_id,
        user_id=user_id,
        caption=caption,
        latitude=latitude,
        longitude=longitude,
    )


async def upload_photo_to_messages(
    client: VKClient,
    data: bytes,
    *,
    peer_id: int | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "photo",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> list[Photo]:
    """Загрузить фото в сообщения: getMessagesUploadServer -> saveMessagesPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getMessagesUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={"peer_id": peer_id, **server_params},
        http_client=http_client,
    )
    uploaded = _as_mapping(raw, client=client, method="photos.getMessagesUploadServer")
    return await client.photos.save_messages_photo(
        photo=uploaded.get("photo"),
        hash=uploaded.get("hash"),
        server=uploaded.get("server"),
    )


async def upload_photo_as_owner_photo(
    client: VKClient,
    data: bytes,
    *,
    owner_id: int | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "photo",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> SaveOwnerPhotoResponseModel:
    """Аватар владельца: getOwnerPhotoUploadServer -> saveOwnerPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getOwnerPhotoUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={"owner_id": owner_id, **server_params},
        http_client=http_client,
    )
    uploaded = _as_mapping(raw, client=client, method="photos.getOwnerPhotoUploadServer")
    return await client.photos.save_owner_photo(
        hash=uploaded.get("hash"),
        photo=uploaded.get("photo"),
        server=uploaded.get("server"),
    )


async def upload_photo_as_owner_cover(
    client: VKClient,
    data: bytes,
    *,
    group_id: int | None = None,
    crop_x: int | None = None,
    crop_y: int | None = None,
    crop_x2: int | None = None,
    crop_y2: int | None = None,
    is_video_cover: bool | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "file",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> SaveOwnerCoverPhotoResponseModel:
    """Обложка владельца: getOwnerCoverPhotoUploadServer -> saveOwnerCoverPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getOwnerCoverPhotoUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={
            "group_id": group_id,
            "crop_x": crop_x,
            "crop_y": crop_y,
            "crop_x2": crop_x2,
            "crop_y2": crop_y2,
            "is_video_cover": is_video_cover,
            **server_params,
        },
        http_client=http_client,
    )
    uploaded = _as_mapping(
        raw, client=client, method="photos.getOwnerCoverPhotoUploadServer"
    )
    return await client.photos.save_owner_cover_photo(
        hash=uploaded.get("hash"),
        photo=uploaded.get("photo"),
    )


async def upload_photo_to_chat(
    client: VKClient,
    data: bytes,
    *,
    chat_id: int,
    crop_x: int | None = None,
    crop_y: int | None = None,
    crop_width: int | None = None,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "photo",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> SetChatPhotoResponseModel:
    """Обложка чата: photos.getChatUploadServer -> messages.setChatPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getChatUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={
            "chat_id": chat_id,
            "crop_x": crop_x,
            "crop_y": crop_y,
            "crop_width": crop_width,
            **server_params,
        },
        http_client=http_client,
    )
    file = raw.get("response") if isinstance(raw, Mapping) and "response" in raw else raw
    return await client.messages.set_chat_photo(file=file)


async def upload_photo_to_market_album(
    client: VKClient,
    data: bytes,
    *,
    group_id: int,
    filename: str = PHOTO_FILENAME,
    content_type: str | None = None,
    field: str = "file",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> list[Photo]:
    """Фото подборки товаров: getMarketAlbumUploadServer -> saveMarketAlbumPhoto."""
    raw = await _upload(
        client,
        data,
        server_method="photos.getMarketAlbumUploadServer",
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=PHOTO_CONTENT_TYPE,
        server_params={"group_id": group_id, **server_params},
        http_client=http_client,
    )
    uploaded = _as_mapping(
        raw, client=client, method="photos.getMarketAlbumUploadServer"
    )
    return await client.photos.save_market_album_photo(
        group_id=group_id,
        hash=uploaded.get("hash"),
        photo=uploaded.get("photo"),
        server=uploaded.get("server"),
    )


# ---------- документы (docs.*) ----------


async def _save_doc(
    client: VKClient,
    data: bytes,
    *,
    server_method: str,
    server_params: Mapping[str, Any],
    title: str | None,
    tags: str | None,
    return_tags: bool | None,
    filename: str,
    content_type: str | None,
    field: str,
    http_client: HttpClient | None,
) -> DocsSaveResponseModel:
    raw = await _upload(
        client,
        data,
        server_method=server_method,
        field=field,
        filename=filename,
        content_type=content_type,
        default_content_type=DOC_CONTENT_TYPE,
        server_params=server_params,
        http_client=http_client,
    )
    uploaded = _as_mapping(raw, client=client, method=server_method)
    return await client.docs.save(
        file=uploaded.get("file"),
        title=title,
        tags=tags,
        return_tags=return_tags,
    )


async def upload_doc(
    client: VKClient,
    data: bytes,
    *,
    group_id: int | None = None,
    title: str | None = None,
    tags: str | None = None,
    return_tags: bool | None = None,
    filename: str = DOC_FILENAME,
    content_type: str | None = None,
    field: str = "file",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> DocsSaveResponseModel:
    """Загрузить документ: docs.getUploadServer -> docs.save."""
    return await _save_doc(
        client,
        data,
        server_method="docs.getUploadServer",
        server_params={"group_id": group_id, **server_params},
        title=title,
        tags=tags,
        return_tags=return_tags,
        filename=filename,
        content_type=content_type,
        field=field,
        http_client=http_client,
    )


async def upload_doc_to_wall(
    client: VKClient,
    data: bytes,
    *,
    group_id: int | None = None,
    title: str | None = None,
    tags: str | None = None,
    return_tags: bool | None = None,
    filename: str = DOC_FILENAME,
    content_type: str | None = None,
    field: str = "file",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> DocsSaveResponseModel:
    """Загрузить документ на стену: docs.getWallUploadServer -> docs.save."""
    return await _save_doc(
        client,
        data,
        server_method="docs.getWallUploadServer",
        server_params={"group_id": group_id, **server_params},
        title=title,
        tags=tags,
        return_tags=return_tags,
        filename=filename,
        content_type=content_type,
        field=field,
        http_client=http_client,
    )


async def upload_doc_to_messages(
    client: VKClient,
    data: bytes,
    *,
    peer_id: int | None = None,
    doc_type: str | None = None,
    group_id: int | None = None,
    title: str | None = None,
    tags: str | None = None,
    return_tags: bool | None = None,
    filename: str = DOC_FILENAME,
    content_type: str | None = None,
    field: str = "file",
    http_client: HttpClient | None = None,
    **server_params: Any,
) -> DocsSaveResponseModel:
    """Загрузить документ в сообщения: getMessagesUploadServer -> docs.save."""
    return await _save_doc(
        client,
        data,
        server_method="docs.getMessagesUploadServer",
        server_params={
            "peer_id": peer_id,
            "type": doc_type,
            "group_id": group_id,
            **server_params,
        },
        title=title,
        tags=tags,
        return_tags=return_tags,
        filename=filename,
        content_type=content_type,
        field=field,
        http_client=http_client,
    )


# ---------- namespace vk.upload ----------


class UploadNamespace:
    """Хелперы загрузки, привязанные к клиенту: ``vk.upload.photo_to_wall(data, ...)``.

    Сигнатуры объявлены явно (не через ``__getattr__``), чтобы их видел IDE:
    каждый метод повторяет одноимённую свободную функцию модуля, но клиент
    подставляется автоматически.
    """

    __slots__ = ("_client",)

    def __init__(self, client: VKClient) -> None:
        self._client = client

    async def photo_to_album(
        self,
        data: bytes,
        *,
        album_id: int | None = None,
        group_id: int | None = None,
        caption: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "file1",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> list[Photo]:
        """Загрузить фото в альбом: ``photos.getUploadServer -> photos.save``."""
        return await upload_photo_to_album(
            self._client,
            data,
            album_id=album_id,
            group_id=group_id,
            caption=caption,
            latitude=latitude,
            longitude=longitude,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_to_wall(
        self,
        data: bytes,
        *,
        group_id: int | None = None,
        user_id: int | None = None,
        caption: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "photo",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> list[Photo]:
        """Загрузить фото на стену: ``getWallUploadServer -> saveWallPhoto``."""
        return await upload_photo_to_wall(
            self._client,
            data,
            group_id=group_id,
            user_id=user_id,
            caption=caption,
            latitude=latitude,
            longitude=longitude,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_to_messages(
        self,
        data: bytes,
        *,
        peer_id: int | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "photo",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> list[Photo]:
        """Загрузить фото в сообщения: ``getMessagesUploadServer -> saveMessagesPhoto``."""
        return await upload_photo_to_messages(
            self._client,
            data,
            peer_id=peer_id,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_as_owner_photo(
        self,
        data: bytes,
        *,
        owner_id: int | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "photo",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> SaveOwnerPhotoResponseModel:
        """Аватар владельца: ``getOwnerPhotoUploadServer -> saveOwnerPhoto``."""
        return await upload_photo_as_owner_photo(
            self._client,
            data,
            owner_id=owner_id,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_as_owner_cover(
        self,
        data: bytes,
        *,
        group_id: int | None = None,
        crop_x: int | None = None,
        crop_y: int | None = None,
        crop_x2: int | None = None,
        crop_y2: int | None = None,
        is_video_cover: bool | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "file",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> SaveOwnerCoverPhotoResponseModel:
        """Обложка владельца: ``getOwnerCoverPhotoUploadServer -> saveOwnerCoverPhoto``."""
        return await upload_photo_as_owner_cover(
            self._client,
            data,
            group_id=group_id,
            crop_x=crop_x,
            crop_y=crop_y,
            crop_x2=crop_x2,
            crop_y2=crop_y2,
            is_video_cover=is_video_cover,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_to_chat(
        self,
        data: bytes,
        *,
        chat_id: int,
        crop_x: int | None = None,
        crop_y: int | None = None,
        crop_width: int | None = None,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "photo",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> SetChatPhotoResponseModel:
        """Обложка чата: ``getChatUploadServer -> messages.setChatPhoto``."""
        return await upload_photo_to_chat(
            self._client,
            data,
            chat_id=chat_id,
            crop_x=crop_x,
            crop_y=crop_y,
            crop_width=crop_width,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def photo_to_market_album(
        self,
        data: bytes,
        *,
        group_id: int,
        filename: str = PHOTO_FILENAME,
        content_type: str | None = None,
        field: str = "file",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> list[Photo]:
        """Фото подборки товаров: ``getMarketAlbumUploadServer -> saveMarketAlbumPhoto``."""
        return await upload_photo_to_market_album(
            self._client,
            data,
            group_id=group_id,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def doc(
        self,
        data: bytes,
        *,
        group_id: int | None = None,
        title: str | None = None,
        tags: str | None = None,
        return_tags: bool | None = None,
        filename: str = DOC_FILENAME,
        content_type: str | None = None,
        field: str = "file",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> DocsSaveResponseModel:
        """Загрузить документ: ``docs.getUploadServer -> docs.save``."""
        return await upload_doc(
            self._client,
            data,
            group_id=group_id,
            title=title,
            tags=tags,
            return_tags=return_tags,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def doc_to_wall(
        self,
        data: bytes,
        *,
        group_id: int | None = None,
        title: str | None = None,
        tags: str | None = None,
        return_tags: bool | None = None,
        filename: str = DOC_FILENAME,
        content_type: str | None = None,
        field: str = "file",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> DocsSaveResponseModel:
        """Загрузить документ на стену: ``docs.getWallUploadServer -> docs.save``."""
        return await upload_doc_to_wall(
            self._client,
            data,
            group_id=group_id,
            title=title,
            tags=tags,
            return_tags=return_tags,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )

    async def doc_to_messages(
        self,
        data: bytes,
        *,
        peer_id: int | None = None,
        doc_type: str | None = None,
        group_id: int | None = None,
        title: str | None = None,
        tags: str | None = None,
        return_tags: bool | None = None,
        filename: str = DOC_FILENAME,
        content_type: str | None = None,
        field: str = "file",
        http_client: HttpClient | None = None,
        **server_params: Any,
    ) -> DocsSaveResponseModel:
        """Загрузить документ в сообщения: ``getMessagesUploadServer -> docs.save``."""
        return await upload_doc_to_messages(
            self._client,
            data,
            peer_id=peer_id,
            doc_type=doc_type,
            group_id=group_id,
            title=title,
            tags=tags,
            return_tags=return_tags,
            filename=filename,
            content_type=content_type,
            field=field,
            http_client=http_client,
            **server_params,
        )


__all__ = (
    "DOC_CONTENT_TYPE",
    "DOC_FILENAME",
    "PHOTO_CONTENT_TYPE",
    "PHOTO_FILENAME",
    "UploadNamespace",
    "upload_doc",
    "upload_doc_to_messages",
    "upload_doc_to_wall",
    "upload_photo_as_owner_cover",
    "upload_photo_as_owner_photo",
    "upload_photo_to_album",
    "upload_photo_to_chat",
    "upload_photo_to_market_album",
    "upload_photo_to_messages",
    "upload_photo_to_wall",
)
