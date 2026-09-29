
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.translations import *  # type: ignore


class TranslationsCategory(BaseCategory):
    async def translate(
        self,
        texts: list[str],
        translation_language: str,
    ) -> TranslationsTranslateResponseModel:
        """Method `translations.translate()`

        :param texts:
        :param translation_language:
        """

        return await self._call("translations.translate", locals(), TranslationsTranslateResponseModel)


__all__ = ("TranslationsCategory",)
