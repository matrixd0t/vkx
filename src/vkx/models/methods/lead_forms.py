
from ..objects import *
from ..responses.lead_forms import *  # type: ignore
from .base_category import BaseCategory


class LeadFormsCategory(BaseCategory):
    async def create(
        self,
        description: str,
        group_id: int,
        name: str,
        policy_link_url: str,
        questions: str,
        title: str,
        active: bool | None = None,
        confirmation: str | None = None,
        notify_admins: list[int] | None = None,
        notify_emails: list[str] | None = None,
        once_per_user: bool | None = None,
        photo: str | None = None,
        pixel_code: str | None = None,
        site_link_url: str | None = None,
    ) -> LeadFormsCreateResponseModel:
        """Method `leadForms.create()`

        :param description:
        :param group_id:
        :param name:
        :param policy_link_url:
        :param questions:
        :param title:
        :param active:
        :param confirmation:
        :param notify_admins:
        :param notify_emails:
        :param once_per_user:
        :param photo:
        :param pixel_code:
        :param site_link_url:
        """

        return await self._call("leadForms.create", locals(), LeadFormsCreateResponseModel)

    async def delete(
        self,
        form_id: int,
        group_id: int,
    ) -> LeadFormsDeleteResponseModel:
        """Method `leadForms.delete()`

        :param form_id:
        :param group_id:
        """

        return await self._call("leadForms.delete", locals(), LeadFormsDeleteResponseModel)

    async def get(
        self,
        form_id: int,
        group_id: int,
    ) -> "Form":
        """Method `leadForms.get()`

        :param form_id:
        :param group_id:
        """

        return await self._call("leadForms.get", locals(), Form)

    async def get_leads(
        self,
        form_id: int,
        group_id: int,
        limit: int | None = None,
        next_page_token: str | None = None,
    ) -> GetLeadsResponseModel:
        """Method `leadForms.getLeads()`

        :param form_id:
        :param group_id:
        :param limit:
        :param next_page_token:
        """

        return await self._call("leadForms.getLeads", locals(), GetLeadsResponseModel)

    async def get_upload_url(
        self,
    ) -> str:
        """Method `leadForms.getUploadURL()`"""

        return await self._call("leadForms.getUploadURL", locals(), str)

    async def get_list(
        self,
        group_id: int,
    ) -> list[Form]:
        """Method `leadForms.list()`

        :param group_id:
        """

        return await self._call("leadForms.list", locals(), list[Form])

    async def update(
        self,
        description: str,
        form_id: int,
        group_id: int,
        name: str,
        policy_link_url: str,
        questions: str,
        title: str,
        active: bool | None = None,
        confirmation: str | None = None,
        notify_admins: list[int] | None = None,
        notify_emails: list[str] | None = None,
        once_per_user: bool | None = None,
        photo: str | None = None,
        pixel_code: str | None = None,
        site_link_url: str | None = None,
    ) -> LeadFormsCreateResponseModel:
        """Method `leadForms.update()`

        :param description:
        :param form_id:
        :param group_id:
        :param name:
        :param policy_link_url:
        :param questions:
        :param title:
        :param active:
        :param confirmation:
        :param notify_admins:
        :param notify_emails:
        :param once_per_user:
        :param photo:
        :param pixel_code:
        :param site_link_url:
        """

        return await self._call("leadForms.update", locals(), LeadFormsCreateResponseModel)


__all__ = ("LeadFormsCategory",)
