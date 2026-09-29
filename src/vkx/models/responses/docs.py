from vkx.models.base_model import BaseModel, Field
from vkx.models.objects import (
    AudioMessage,
    Doc,
    DocAttachmentType,
    DocTypes,
    MessagesGraffiti,
)


class DocUploadResponseModel(BaseModel):
    file: str | None = Field(
        default=None,
    )

class GetTypesResponseModel(BaseModel):
    count: int = Field()
    items: list["DocTypes"] = Field()

class DocsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["Doc"] = Field()

class DocsSaveResponseModel(BaseModel):
    type: "DocAttachmentType | None" = Field(
        default=None,
    )
    audio_message: "AudioMessage | None" = Field(
        default=None,
    )
    doc: "Doc | None" = Field(
        default=None,
    )
    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )

    @property
    def as_att(self) -> str | None:
        """Строка-вложение сохранённого документа/граффити/голосового."""
        for item in (self.doc, self.graffiti, self.audio_message):
            if item is not None:
                return item.as_att
        return None


class DocsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["Doc"] = Field()

__all__ = (
    "DocUploadResponseModel",
    "DocsGetResponseModel",
    "DocsSaveResponseModel",
    "DocsSearchResponseModel",
    "GetTypesResponseModel",
)
