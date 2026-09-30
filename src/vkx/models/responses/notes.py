from ..base_model import BaseModel, Field
from ..objects import Note, NoteComment


class NotesGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["NoteComment"] = Field()


class NotesGetResponseModel(BaseModel):
    count: int = Field()
    items: list["Note"] = Field()


__all__ = (
    "NotesGetCommentsResponseModel",
    "NotesGetResponseModel",
)
