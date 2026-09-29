
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.base import (
    OkResponseModel,
)
from vkx.models.responses.pages import *  # type: ignore


class PagesCategory(BaseCategory):
    async def clear_cache(
        self,
        url: str,
    ) -> OkResponseModel:
        """Method `pages.clearCache()`

        :param url: Address of the page where you need to refesh the cached version
        """

        return await self._call("pages.clearCache", locals(), OkResponseModel)

    async def get(
        self,
        global_: bool | None = None,
        need_html: bool | None = None,
        need_source: bool | None = None,
        owner_id: int | None = None,
        page_id: int | None = None,
        site_preview: bool | None = None,
        title: str | None = None,
    ) -> "WikipageFull":
        """Method `pages.get()`

        :param global: '1' - to return information about a global wiki page
        :param need_html: '1' - to return the page as HTML,
        :param need_source:
        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param site_preview: '1' - resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        """

        return await self._call("pages.get", locals(), WikipageFull)

    async def get_history(
        self,
        page_id: int,
        group_id: int | None = None,
        user_id: int | None = None,
    ) -> list[WikipageHistory]:
        """Method `pages.getHistory()`

        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        """

        return await self._call("pages.getHistory", locals(), list[WikipageHistory])

    async def get_titles(
        self,
        group_id: int | None = None,
    ) -> list[Wikipage]:
        """Method `pages.getTitles()`

        :param group_id: ID of the community that owns the wiki page.
        """

        return await self._call("pages.getTitles", locals(), list[Wikipage])

    async def get_version(
        self,
        version_id: int,
        group_id: int | None = None,
        need_html: bool | None = None,
        user_id: int | None = None,
    ) -> GetVersionResponseModel:
        """Method `pages.getVersion()`

        :param version_id:
        :param group_id: ID of the community that owns the wiki page.
        :param need_html: '1' - to return the page as HTML
        :param user_id:
        """

        return await self._call("pages.getVersion", locals(), GetVersionResponseModel)

    async def parse_wiki(
        self,
        text: str,
        group_id: int | None = None,
    ) -> str:
        """Method `pages.parseWiki()`

        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """

        return await self._call("pages.parseWiki", locals(), str)

    async def save(
        self,
        group_id: int | None = None,
        page_id: int | None = None,
        text: str | None = None,
        title: str | None = None,
        user_id: int | None = None,
    ) -> int:
        """Method `pages.save()`

        :param group_id: ID of the community that owns the wiki page.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param text: Text of the wiki page in wiki-format.
        :param title: Wiki page title.
        :param user_id: User ID
        """

        return await self._call("pages.save", locals(), int)

    async def save_access(
        self,
        page_id: int,
        edit: int | None = None,
        group_id: int | None = None,
        user_id: int | None = None,
        view: int | None = None,
    ) -> int:
        """Method `pages.saveAccess()`

        :param page_id: Wiki page ID.
        :param edit: Who can edit the wiki page: '1' - only community members, '2' - all users can edit the page, '0' - only community managers
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param view: Who can view the wiki page: '1' - only community members, '2' - all users can view the page, '0' - only community managers
        """

        return await self._call("pages.saveAccess", locals(), int)


__all__ = ("PagesCategory",)
