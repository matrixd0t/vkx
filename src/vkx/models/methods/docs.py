from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.docs import *  # type: ignore
from .base_category import BaseCategory


class DocsCategory(BaseCategory):
    async def add(
        self,
        doc_id: int,
        owner_id: int,
        access_key: str | None = None,
    ) -> int:
        """Method `docs.add()`

        :param doc_id: Document ID.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """

        return await self._call("docs.add", locals(), int)

    async def delete(
        self,
        doc_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `docs.delete()`

        :param doc_id: Document ID.
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        """

        return await self._call("docs.delete", locals(), OkResponseModel)

    async def edit(
        self,
        doc_id: int,
        title: str,
        owner_id: int | None = None,
        tags: list[str] | None = None,
    ) -> OkResponseModel:
        """Method `docs.edit()`

        :param doc_id: Document ID.
        :param title: Document title.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param tags: Document tags.
        """

        return await self._call("docs.edit", locals(), OkResponseModel)

    async def get(
        self,
        count: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        return_tags: bool | None = None,
        type: int | None = None,
    ) -> DocsGetResponseModel:
        """Method `docs.get()`

        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags:
        :param type:
        """

        return await self._call("docs.get", locals(), DocsGetResponseModel)

    async def get_by_id(
        self,
        docs: list[str],
        return_tags: bool | None = None,
    ) -> list[Doc]:
        """Method `docs.getById()`

        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags:
        """

        return await self._call("docs.getById", locals(), list[Doc])

    async def get_messages_upload_server(
        self,
        peer_id: int | None = None,
        type: str | None = None,
    ) -> "UploadServer":
        """Method `docs.getMessagesUploadServer()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param type: Document type.
        """

        return await self._call("docs.getMessagesUploadServer", locals(), UploadServer)

    async def get_types(
        self,
        owner_id: int | None = None,
    ) -> GetTypesResponseModel:
        """Method `docs.getTypes()`

        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """

        return await self._call("docs.getTypes", locals(), GetTypesResponseModel)

    async def get_upload_server(
        self,
        group_id: int | None = None,
    ) -> "UploadServer":
        """Method `docs.getUploadServer()`

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        return await self._call("docs.getUploadServer", locals(), UploadServer)

    async def get_wall_upload_server(
        self,
        group_id: int | None = None,
    ) -> "UploadServer":
        """Method `docs.getWallUploadServer()`

        :param group_id: Community ID (if the document will be uploaded to the community).
        """

        return await self._call("docs.getWallUploadServer", locals(), UploadServer)

    async def restore(
        self,
        doc_id: int,
        owner_id: int,
    ) -> OkResponseModel:
        """Method `docs.restore()`

        :param doc_id:
        :param owner_id:
        """

        return await self._call("docs.restore", locals(), OkResponseModel)

    async def save(
        self,
        file: str,
        return_tags: bool | None = None,
        tags: str | None = None,
        title: str | None = None,
    ) -> DocsSaveResponseModel:
        """Method `docs.save()`

        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param return_tags:
        :param tags: Document tags.
        :param title: Document title.
        """

        return await self._call("docs.save", locals(), DocsSaveResponseModel)

    async def search(
        self,
        count: int | None = None,
        offset: int | None = None,
        q: str | None = None,
        return_tags: bool | None = None,
        search_own: bool | None = None,
    ) -> DocsSearchResponseModel:
        """Method `docs.search()`

        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param q: Search query string.
        :param return_tags:
        :param search_own:
        """

        return await self._call("docs.search", locals(), DocsSearchResponseModel)


__all__ = ("DocsCategory",)
