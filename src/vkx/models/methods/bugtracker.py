
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.base import (
    OkResponseModel,
)
from vkx.models.responses.bugtracker import *  # type: ignore


class BugtrackerCategory(BaseCategory):
    async def add_company_groups_members(
        self,
        company_group_ids: list[int],
        company_id: int,
        user_ids: list[int],
    ) -> AddCompanyGroupsMembersResponseModel:
        """Method `bugtracker.addCompanyGroupsMembers()`

        :param company_group_ids:
        :param company_id:
        :param user_ids:
        """

        return await self._call("bugtracker.addCompanyGroupsMembers", locals(), AddCompanyGroupsMembersResponseModel)

    async def add_company_members(
        self,
        company_id: int,
        user_ids: list[int],
    ) -> AddCompanyMembersResponseModel:
        """Method `bugtracker.addCompanyMembers()`

        :param company_id:
        :param user_ids:
        """

        return await self._call("bugtracker.addCompanyMembers", locals(), AddCompanyMembersResponseModel)

    async def change_bugreport_status(
        self,
        bugreport_id: int,
        comment: str | None = None,
        from_statuses: list[int] | None = None,
        not_in_statuses: list[int] | None = None,
        status: int | None = None,
    ) -> bool:
        """Method `bugtracker.changeBugreportStatus()`

        :param bugreport_id:
        :param comment:
        :param from_statuses:
        :param not_in_statuses:
        :param status:
        """

        return await self._call("bugtracker.changeBugreportStatus", locals(), bool)

    async def create_comment(
        self,
        bugreport_id: int,
        force: bool | None = None,
        hidden: bool | None = None,
        hidden_attachments: bool | None = None,
        text: str | None = None,
    ) -> BugtrackerCreateCommentResponseModel:
        """Method `bugtracker.createComment()`

        :param bugreport_id:
        :param force:
        :param hidden:
        :param hidden_attachments:
        :param text:
        """

        return await self._call("bugtracker.createComment", locals(), BugtrackerCreateCommentResponseModel)

    async def get_bugreport_by_id(
        self,
        bugreport_id: int,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
    ) -> GetBugreportByIdResponseModel:
        """Method `bugtracker.getBugreportById()`

        :param bugreport_id:
        :param extended:
        :param fields:
        """

        return await self._call("bugtracker.getBugreportById", locals(), GetBugreportByIdResponseModel)

    async def get_company_group_members(
        self,
        company_group_id: int,
        company_id: int,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        filter_name: str | None = None,
        offset: int | None = None,
    ) -> GetCompanyGroupMembersResponseModel:
        """Method `bugtracker.getCompanyGroupMembers()`

        :param company_group_id:
        :param company_id:
        :param count:
        :param extended:
        :param fields:
        :param filter_name:
        :param offset:
        """

        return await self._call("bugtracker.getCompanyGroupMembers", locals(), GetCompanyGroupMembersResponseModel)

    async def get_company_members(
        self,
        company_id: int,
        count: int | None = None,
        extended: bool | None = None,
        extra: bool | None = None,
        fields: list[UserGroupFields] | None = None,
        filter_member_ids: list[int] | None = None,
        filter_name: str | None = None,
        filter_not_group: int | None = None,
        filter_role: int | None = None,
        offset: int | None = None,
    ) -> GetCompanyMembersResponseModel:
        """Method `bugtracker.getCompanyMembers()`

        :param company_id:
        :param count:
        :param extended:
        :param extra:
        :param fields:
        :param filter_member_ids:
        :param filter_name:
        :param filter_not_group:
        :param filter_role:
        :param offset:
        """

        return await self._call("bugtracker.getCompanyMembers", locals(), GetCompanyMembersResponseModel)

    async def get_download_version_url(
        self,
        product_id: int,
        version_id: int,
        ttl: int | None = None,
    ) -> GetDownloadVersionUrlResponseModel:
        """Method `bugtracker.getDownloadVersionUrl()`

        :param product_id:
        :param version_id:
        :param ttl:
        """

        return await self._call("bugtracker.getDownloadVersionUrl", locals(), GetDownloadVersionUrlResponseModel)

    async def get_product_build_upload_server(
        self,
        product_id: int,
    ) -> "UploadServer":
        """Method `bugtracker.getProductBuildUploadServer()`

        :param product_id:
        """

        return await self._call("bugtracker.getProductBuildUploadServer", locals(), UploadServer)

    async def remove_company_group_member(
        self,
        company_group_id: int,
        company_id: int,
        user_id: int,
    ) -> OkResponseModel:
        """Method `bugtracker.removeCompanyGroupMember()`

        :param company_group_id:
        :param company_id:
        :param user_id:
        """

        return await self._call("bugtracker.removeCompanyGroupMember", locals(), OkResponseModel)

    async def remove_company_member(
        self,
        company_id: int,
        user_id: int,
    ) -> OkResponseModel:
        """Method `bugtracker.removeCompanyMember()`

        :param company_id:
        :param user_id:
        """

        return await self._call("bugtracker.removeCompanyMember", locals(), OkResponseModel)

    async def save_product_version(
        self,
        title: str,
        product_id: int | None = None,
        release_notes: str | None = None,
        set_rft: bool | None = None,
        version_id: int | None = None,
        visible: bool | None = None,
    ) -> OkResponseModel:
        """Method `bugtracker.saveProductVersion()`

        :param title:
        :param product_id:
        :param release_notes:
        :param set_rft:
        :param version_id:
        :param visible:
        """

        return await self._call("bugtracker.saveProductVersion", locals(), OkResponseModel)

    async def set_company_member_role(
        self,
        company_id: int,
        role: int,
        user_id: int,
    ) -> OkResponseModel:
        """Method `bugtracker.setCompanyMemberRole()`

        :param company_id:
        :param role:
        :param user_id:
        """

        return await self._call("bugtracker.setCompanyMemberRole", locals(), OkResponseModel)

    async def set_product_is_over(
        self,
        product_id: int,
        is_over: bool | None = None,
    ) -> OkResponseModel:
        """Method `bugtracker.setProductIsOver()`

        :param product_id:
        :param is_over:
        """

        return await self._call("bugtracker.setProductIsOver", locals(), OkResponseModel)


__all__ = ("BugtrackerCategory",)
