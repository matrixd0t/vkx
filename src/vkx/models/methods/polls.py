import typing

from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.base import (
    OkResponseModel,
)


class PollsCategory(BaseCategory):
    async def add_vote(
        self,
        answer_ids: list[int],
        poll_id: int,
        is_board: bool | None = None,
        owner_id: int | None = None,
    ) -> bool:
        """Method `polls.addVote()`

        :param answer_ids:
        :param poll_id: Poll ID.
        :param is_board:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        return await self._call("polls.addVote", locals(), bool)

    async def create(
        self,
        add_answers: str | None = None,
        app_id: int | None = None,
        background_id: str | None = None,
        disable_unvote: bool | None = None,
        end_date: int | None = None,
        is_anonymous: bool | None = None,
        is_multiple: bool | None = None,
        owner_id: int | None = None,
        photo_id: int | None = None,
        question: str | None = None,
    ) -> "Poll":
        """Method `polls.create()`

        :param add_answers: available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param app_id:
        :param background_id:
        :param disable_unvote:
        :param end_date:
        :param is_anonymous: '1' - anonymous poll, participants list is hidden,, '0' - public poll, participants list is available,, Default value is '0'.
        :param is_multiple:
        :param owner_id: If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param photo_id:
        :param question: question text
        """

        return await self._call("polls.create", locals(), Poll)

    async def delete_vote(
        self,
        poll_id: int,
        is_board: bool | None = None,
        owner_id: int | None = None,
    ) -> bool:
        """Method `polls.deleteVote()`

        :param poll_id: Poll ID.
        :param is_board:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        return await self._call("polls.deleteVote", locals(), bool)

    async def edit(
        self,
        poll_id: int,
        add_answers: str | None = None,
        background_id: str | None = None,
        delete_answers: str | None = None,
        edit_answers: str | None = None,
        end_date: int | None = None,
        owner_id: int | None = None,
        photo_id: int | None = None,
        question: str | None = None,
    ) -> OkResponseModel:
        """Method `polls.edit()`

        :param poll_id: edited poll's id
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param background_id:
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param edit_answers: object containing answers that need to be edited,, key - answer id, value - new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param end_date:
        :param owner_id: poll owner id
        :param photo_id:
        :param question: new question text
        """

        return await self._call("polls.edit", locals(), OkResponseModel)

    async def get_backgrounds(
        self,
    ) -> list[Background]:
        """Method `polls.getBackgrounds()`"""

        return await self._call("polls.getBackgrounds", locals(), list[Background])

    async def get_by_id(
        self,
        poll_id: int,
        extended: bool | None = None,
        fields: list[str] | None = None,
        friends_count: int | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        owner_id: int | None = None,
    ) -> "PollExtended":
        """Method `polls.getById()`

        :param poll_id: Poll ID.
        :param extended:
        :param fields:
        :param friends_count:
        :param is_board: '1' - poll is in a board, '0' - poll is on a wall. '0' by default.
        :param name_case:
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        return await self._call("polls.getById", locals(), PollExtended)

    async def get_photo_upload_server(
        self,
        owner_id: int | None = None,
    ) -> "UploadServer":
        """Method `polls.getPhotoUploadServer()`

        :param owner_id:
        """

        return await self._call("polls.getPhotoUploadServer", locals(), UploadServer)

    @typing.overload
    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields],
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> list[FieldsVoters]: ...

    @typing.overload
    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> list[Voters]: ...

    async def get_voters(
        self,
        answer_ids: list[int],
        poll_id: int,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        friends_only: bool | None = None,
        is_board: bool | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
    ) -> list[FieldsVoters] | list[Voters]:
        """Method `polls.getVoters()`

        :param answer_ids: Answer IDs.
        :param poll_id: Poll ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' - (default)
        :param friends_only: '1' - to return only current user's friends, '0' - to return all users (default),
        :param is_board:
        :param name_case: Case for declension of user name and surname: , 'nom' - nominative (default) , 'gen' - genitive , 'dat' - dative , 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of voters. '0' - (default)
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        """

        return await self._call(
            "polls.getVoters",
            locals(),
            dependent=((("fields",), list[FieldsVoters]),),
            default=list[Voters],
        )

    async def save_photo(
        self,
        hash: str | None = None,
        photo: str | None = None,
    ) -> "Background":
        """Method `polls.savePhoto()`

        :param hash:
        :param photo:
        """

        return await self._call("polls.savePhoto", locals(), Background)


__all__ = ("PollsCategory",)
