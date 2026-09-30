from ..objects import *
from ..responses.base import OkResponseModel
from ..responses.notes import *  # type: ignore
from .base_category import BaseCategory


class NotesCategory(BaseCategory):
    async def add(
        self,
        text: str,
        title: str,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
    ) -> int:
        """Method `notes.add()`

        :param text: Note text.
        :param title: Note title.
        :param privacy_comment:
        :param privacy_view:
        """

        return await self._call("notes.add", locals(), int)

    async def create_comment(
        self,
        message: str,
        note_id: int,
        guid: str | None = None,
        owner_id: int | None = None,
        reply_to: int | None = None,
    ) -> int:
        """Method `notes.createComment()`

        :param message: Comment text.
        :param note_id: Note ID.
        :param guid:
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        """

        return await self._call("notes.createComment", locals(), int)

    async def delete(
        self,
        note_id: int,
    ) -> OkResponseModel:
        """Method `notes.delete()`

        :param note_id: Note ID.
        """

        return await self._call("notes.delete", locals(), OkResponseModel)

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `notes.deleteComment()`

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        return await self._call("notes.deleteComment", locals(), OkResponseModel)

    async def edit(
        self,
        note_id: int,
        text: str,
        title: str,
        privacy_comment: list[str] | None = None,
        privacy_view: list[str] | None = None,
    ) -> OkResponseModel:
        """Method `notes.edit()`

        :param note_id: Note ID.
        :param text: Note text.
        :param title: Note title.
        :param privacy_comment:
        :param privacy_view:
        """

        return await self._call("notes.edit", locals(), OkResponseModel)

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `notes.editComment()`

        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """

        return await self._call("notes.editComment", locals(), OkResponseModel)

    async def get(
        self,
        count: int | None = None,
        note_ids: list[int] | None = None,
        offset: int | None = None,
        sort: int | None = None,
        user_id: int | None = None,
    ) -> NotesGetResponseModel:
        """Method `notes.get()`

        :param count: Number of notes to return.
        :param note_ids: Note IDs.
        :param offset:
        :param sort:
        :param user_id: Note owner ID.
        """

        return await self._call("notes.get", locals(), NotesGetResponseModel)

    async def get_by_id(
        self,
        note_id: int,
        need_wiki: bool | None = None,
        owner_id: int | None = None,
    ) -> "Note":
        """Method `notes.getById()`

        :param note_id: Note ID.
        :param need_wiki:
        :param owner_id: Note owner ID.
        """

        return await self._call("notes.getById", locals(), Note)

    async def get_comments(
        self,
        note_id: int,
        count: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        sort: int | None = None,
    ) -> NotesGetCommentsResponseModel:
        """Method `notes.getComments()`

        :param note_id: Note ID.
        :param count: Number of comments to return.
        :param offset:
        :param owner_id: Note owner ID.
        :param sort:
        """

        return await self._call("notes.getComments", locals(), NotesGetCommentsResponseModel)

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: int | None = None,
    ) -> OkResponseModel:
        """Method `notes.restoreComment()`

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        return await self._call("notes.restoreComment", locals(), OkResponseModel)


__all__ = ("NotesCategory",)
