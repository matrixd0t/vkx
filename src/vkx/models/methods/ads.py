import typing

from ..objects import *
from ..objects import (
    TargSuggestions,
    TargSuggestionsCities,
    TargSuggestionsRegions,
    TargSuggestionsSchools,
)
from ..responses.ads import *  # type: ignore
from ..responses.base import OkResponseModel
from .base_category import BaseCategory


class AdsCategory(BaseCategory):
    async def add_office_users(
        self,
        account_id: int,
        data: str,
    ) -> list[bool]:
        """Method `ads.addOfficeUsers()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        return await self._call("ads.addOfficeUsers", locals(), list[bool])

    async def check_link(
        self,
        account_id: int,
        link_type: str,
        link_url: str,
        campaign_id: int | None = None,
    ) -> "LinkStatus":
        """Method `ads.checkLink()`

        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' - community,, *'post' - community post,, *'application' - VK application,, *'video' - video,, *'site' - external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """

        return await self._call("ads.checkLink", locals(), LinkStatus)

    async def create_ads(
        self,
        account_id: int,
        data: str,
    ) -> list[CreateAdStatus]:
        """Method `ads.createAds()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """

        return await self._call("ads.createAds", locals(), list[CreateAdStatus])

    async def create_campaigns(
        self,
        account_id: int,
        data: str,
    ) -> list[CreateCampaignStatus]:
        """Method `ads.createCampaigns()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """

        return await self._call("ads.createCampaigns", locals(), list[CreateCampaignStatus])

    async def create_clients(
        self,
        account_id: int,
        data: str,
    ) -> list[CreateClientsStatus]:
        """Method `ads.createClients()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """

        return await self._call("ads.createClients", locals(), list[CreateClientsStatus])

    async def create_lookalike_request(
        self,
        account_id: int,
        source_type: str,
        client_id: int | None = None,
        retargeting_group_id: int | None = None,
    ) -> CreateLookalikeRequestResponseModel:
        """Method `ads.createLookalikeRequest()`

        :param account_id:
        :param source_type:
        :param client_id:
        :param retargeting_group_id:
        """

        return await self._call("ads.createLookalikeRequest", locals(), CreateLookalikeRequestResponseModel)

    async def create_target_group(
        self,
        account_id: int,
        lifetime: int,
        name: str,
        client_id: int | None = None,
        target_pixel_id: int | None = None,
        target_pixel_rules: str | None = None,
    ) -> CreateTargetGroupResponseModel:
        """Method `ads.createTargetGroup()`

        :param account_id: Advertising account ID.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param name: Name of the target group - a string up to 64 characters long.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        return await self._call("ads.createTargetGroup", locals(), CreateTargetGroupResponseModel)

    async def create_target_pixel(
        self,
        account_id: int,
        category_id: int,
        name: str,
        client_id: int | None = None,
        domain: str | None = None,
    ) -> CreateTargetPixelResponseModel:
        """Method `ads.createTargetPixel()`

        :param account_id:
        :param category_id:
        :param name:
        :param client_id:
        :param domain:
        """

        return await self._call("ads.createTargetPixel", locals(), CreateTargetPixelResponseModel)

    async def delete_ads(
        self,
        account_id: int,
        ids: str,
    ) -> list[int]:
        """Method `ads.deleteAds()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """

        return await self._call("ads.deleteAds", locals(), list[int])

    async def delete_campaigns(
        self,
        account_id: int,
        ids: str,
    ) -> list[int]:
        """Method `ads.deleteCampaigns()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """

        return await self._call("ads.deleteCampaigns", locals(), list[int])

    async def delete_clients(
        self,
        account_id: int,
        ids: str,
    ) -> list[int]:
        """Method `ads.deleteClients()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """

        return await self._call("ads.deleteClients", locals(), list[int])

    async def delete_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: int | None = None,
    ) -> OkResponseModel:
        """Method `ads.deleteTargetGroup()`

        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        return await self._call("ads.deleteTargetGroup", locals(), OkResponseModel)

    async def delete_target_pixel(
        self,
        account_id: int,
        target_pixel_id: int,
        client_id: int | None = None,
    ) -> dict[str, typing.Any]:
        """Method `ads.deleteTargetPixel()`

        :param account_id:
        :param target_pixel_id:
        :param client_id:
        """

        return await self._call("ads.deleteTargetPixel", locals(), dict[str, typing.Any])

    async def get_accounts(
        self,
    ) -> list[Account]:
        """Method `ads.getAccounts()`"""

        return await self._call("ads.getAccounts", locals(), list[Account])

    async def get_ads(
        self,
        account_id: int,
        ad_ids: str | None = None,
        campaign_ids: str | None = None,
        client_id: int | None = None,
        include_deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        only_deleted: bool | None = None,
    ) -> list[Ad]:
        """Method `ads.getAds()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        """

        return await self._call("ads.getAds", locals(), list[Ad])

    async def get_ads_layout(
        self,
        account_id: int,
        ad_ids: str | None = None,
        campaign_ids: str | None = None,
        client_id: int | None = None,
        include_deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        only_deleted: bool | None = None,
    ) -> list[AdLayout]:
        """Method `ads.getAdsLayout()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        """

        return await self._call("ads.getAdsLayout", locals(), list[AdLayout])

    async def get_ads_targeting(
        self,
        account_id: int,
        ad_ids: str | None = None,
        campaign_ids: str | None = None,
        client_id: int | None = None,
        include_deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        only_deleted: bool | None = None,
    ) -> list[TargSettings]:
        """Method `ads.getAdsTargeting()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        :param only_deleted:
        """

        return await self._call("ads.getAdsTargeting", locals(), list[TargSettings])

    async def get_budget(
        self,
        account_id: int,
    ) -> str:
        """Method `ads.getBudget()`

        :param account_id: Advertising account ID.
        """

        return await self._call("ads.getBudget", locals(), str)

    async def get_campaigns(
        self,
        account_id: int,
        campaign_ids: str | None = None,
        client_id: int | None = None,
        fields: list[typing.Literal["ads_count"]] | None = None,
        include_deleted: bool | None = None,
    ) -> list[Campaign]:
        """Method `ads.getCampaigns()`

        :param account_id: Advertising account ID.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param fields:
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active campaigns,, *1 - show all campaigns.
        """

        return await self._call("ads.getCampaigns", locals(), list[Campaign])

    async def get_categories(
        self,
        lang: str | None = None,
    ) -> GetCategoriesResponseModel:
        """Method `ads.getCategories()`

        :param lang: Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        """

        return await self._call("ads.getCategories", locals(), GetCategoriesResponseModel)

    async def get_clients(
        self,
        account_id: int,
    ) -> list[Client]:
        """Method `ads.getClients()`

        :param account_id: Advertising account ID.
        """

        return await self._call("ads.getClients", locals(), list[Client])

    async def get_demographics(
        self,
        account_id: int,
        date_from: str,
        date_to: str,
        ids: str,
        ids_type: str,
        period: str,
    ) -> list[DemoStats]:
        """Method `ads.getDemographics()`

        :param account_id: Advertising account ID.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        """

        return await self._call("ads.getDemographics", locals(), list[DemoStats])

    async def get_flood_stats(
        self,
        account_id: int,
    ) -> "FloodStats":
        """Method `ads.getFloodStats()`

        :param account_id: Advertising account ID.
        """

        return await self._call("ads.getFloodStats", locals(), FloodStats)

    async def get_lookalike_requests(
        self,
        account_id: int,
        client_id: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        requests_ids: str | None = None,
        sort_by: str | None = None,
    ) -> GetLookalikeRequestsResponseModel:
        """Method `ads.getLookalikeRequests()`

        :param account_id:
        :param client_id:
        :param limit:
        :param offset:
        :param requests_ids:
        :param sort_by:
        """

        return await self._call("ads.getLookalikeRequests", locals(), GetLookalikeRequestsResponseModel)

    async def get_musicians(
        self,
        artist_name: str,
    ) -> GetMusiciansResponseModel:
        """Method `ads.getMusicians()`

        :param artist_name:
        """

        return await self._call("ads.getMusicians", locals(), GetMusiciansResponseModel)

    async def get_musicians_by_ids(
        self,
        ids: list[int],
    ) -> GetMusiciansResponseModel:
        """Method `ads.getMusiciansByIds()`

        :param ids:
        """

        return await self._call("ads.getMusiciansByIds", locals(), GetMusiciansResponseModel)

    async def get_office_users(
        self,
        account_id: int,
    ) -> list[Users]:
        """Method `ads.getOfficeUsers()`

        :param account_id: Advertising account ID.
        """

        return await self._call("ads.getOfficeUsers", locals(), list[Users])

    async def get_posts_reach(
        self,
        account_id: int,
        ids: str,
        ids_type: str,
    ) -> list[PromotedPostReach]:
        """Method `ads.getPostsReach()`

        :param account_id: Advertising account ID.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        """

        return await self._call("ads.getPostsReach", locals(), list[PromotedPostReach])

    async def get_rejection_reason(
        self,
        account_id: int,
        ad_id: int,
    ) -> "RejectReason":
        """Method `ads.getRejectionReason()`

        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """

        return await self._call("ads.getRejectionReason", locals(), RejectReason)

    async def get_statistics(
        self,
        account_id: int,
        date_from: str,
        date_to: str,
        ids: str,
        ids_type: str,
        period: str,
        stats_fields: list[typing.Literal["views_times"]] | None = None,
    ) -> list[AdsStats]:
        """Method `ads.getStatistics()`

        :param account_id: Advertising account ID.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns,, *client - clients,, *office - account.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param stats_fields: Additional fields to add to statistics
        """

        return await self._call("ads.getStatistics", locals(), list[AdsStats])






    async def get_target_groups(
        self,
        account_id: int,
        client_id: int | None = None,
        extended: bool | None = None,
    ) -> list[TargetGroup]:
        """Method `ads.getTargetGroups()`

        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' - to return pixel code.
        """

        return await self._call("ads.getTargetGroups", locals(), list[TargetGroup])

    async def get_target_pixels(
        self,
        account_id: int,
        client_id: int | None = None,
    ) -> list[TargetPixelInfo]:
        """Method `ads.getTargetPixels()`

        :param account_id:
        :param client_id:
        """

        return await self._call("ads.getTargetPixels", locals(), list[TargetPixelInfo])

    async def get_targeting_stats(
        self,
        account_id: int,
        link_url: str,
        ad_format: int | None = None,
        ad_id: int | None = None,
        ad_platform: str | None = None,
        ad_platform_no_ad_network: str | None = None,
        ad_platform_no_wall: str | None = None,
        client_id: int | None = None,
        criteria: str | None = None,
        impressions_limit_period: int | None = None,
        link_domain: str | None = None,
        need_precise: bool | None = None,
        publisher_platforms: str | None = None,
    ) -> "TargStats":
        """Method `ads.getTargetingStats()`

        :param account_id: Advertising account ID.
        :param link_url: URL for the advertised object.
        :param ad_format: Ad format. Possible values: *'1' - image and text,, *'2' - big image,, *'3' - exclusive format,, *'4' - community, square image,, *'7' - special app format,, *'8' - special community format,, *'9' - post in community,, *'10' - app board.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' - VK and partner sites,, *'1' - VK only. (for 'ad_format' = '9'), *'all' - all platforms,, *'desktop' - desktop version,, *'mobile' - mobile version and apps.
        :param ad_platform_no_ad_network:
        :param ad_platform_no_wall:
        :param client_id:
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param impressions_limit_period: Impressions limit period in seconds, must be a multiple of 86400(day)
        :param link_domain: Domain of the advertised object.
        :param need_precise: Additionally return recommended cpc and cpm to reach 5,10..95 percents of audience.
        :param publisher_platforms:
        """

        return await self._call("ads.getTargetingStats", locals(), TargStats)

    async def get_upload_url(
        self,
        ad_format: int,
        icon: int | None = None,
    ) -> str:
        """Method `ads.getUploadURL()`

        :param ad_format: Ad format: *1 - image and text,, *2 - big image,, *3 - exclusive format,, *4 - community, square image,, *7 - special app format.
        :param icon:
        """

        return await self._call("ads.getUploadURL", locals(), str)

    async def get_video_upload_url(
        self,
    ) -> str:
        """Method `ads.getVideoUploadURL()`"""

        return await self._call("ads.getVideoUploadURL", locals(), str)

    async def import_target_contacts(
        self,
        account_id: int,
        contacts: str,
        target_group_id: int,
        client_id: int | None = None,
    ) -> int:
        """Method `ads.importTargetContacts()`

        :param account_id: Advertising account ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        :param target_group_id: Target group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        return await self._call("ads.importTargetContacts", locals(), int)

    async def remove_office_users(
        self,
        account_id: int,
        ids: str,
    ) -> list[bool]:
        """Method `ads.removeOfficeUsers()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """

        return await self._call("ads.removeOfficeUsers", locals(), list[bool])

    async def remove_target_contacts(
        self,
        account_id: int,
        contacts: str,
        target_group_id: int,
        client_id: int | None = None,
    ) -> RemoveTargetContactsResponseModel:
        """Method `ads.removeTargetContacts()`

        :param account_id:
        :param contacts:
        :param target_group_id:
        :param client_id:
        """

        return await self._call("ads.removeTargetContacts", locals(), RemoveTargetContactsResponseModel)

    async def save_lookalike_request_result(
        self,
        account_id: int,
        level: int,
        request_id: int,
        client_id: int | None = None,
    ) -> SaveLookalikeRequestResultResponseModel:
        """Method `ads.saveLookalikeRequestResult()`

        :param account_id:
        :param level:
        :param request_id:
        :param client_id:
        """

        return await self._call("ads.saveLookalikeRequestResult", locals(), SaveLookalikeRequestResultResponseModel)

    async def share_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: int | None = None,
        share_with_client_id: int | None = None,
    ) -> ShareTargetGroupResponseModel:
        """Method `ads.shareTargetGroup()`

        :param account_id:
        :param target_group_id:
        :param client_id:
        :param share_with_client_id:
        """

        return await self._call("ads.shareTargetGroup", locals(), ShareTargetGroupResponseModel)

    async def update_ads(
        self,
        account_id: int,
        data: str,
    ) -> list[UpdateAdsStatus]:
        """Method `ads.updateAds()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """

        return await self._call("ads.updateAds", locals(), list[UpdateAdsStatus])

    async def update_campaigns(
        self,
        account_id: int,
        data: str,
    ) -> list[CreateCampaignStatus]:
        """Method `ads.updateCampaigns()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """

        return await self._call("ads.updateCampaigns", locals(), list[CreateCampaignStatus])

    async def update_clients(
        self,
        account_id: int,
        data: str,
    ) -> list[UpdateClientsStatus]:
        """Method `ads.updateClients()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """

        return await self._call("ads.updateClients", locals(), list[UpdateClientsStatus])

    async def update_office_users(
        self,
        account_id: int,
        data: str,
    ) -> list[UpdateOfficeUsersResult]:
        """Method `ads.updateOfficeUsers()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        return await self._call("ads.updateOfficeUsers", locals(), list[UpdateOfficeUsersResult])

    async def update_target_group(
        self,
        account_id: int,
        lifetime: int,
        name: str,
        target_group_id: int,
        client_id: int | None = None,
        domain: str | None = None,
        target_pixel_id: int | None = None,
        target_pixel_rules: str | None = None,
    ) -> OkResponseModel:
        """Method `ads.updateTargetGroup()`

        :param account_id: Advertising account ID.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' - automatic exclusion is off.
        :param name: New name of the target group - a string up to 64 characters long.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param domain: Domain of the site where user accounting code will be placed.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        return await self._call("ads.updateTargetGroup", locals(), OkResponseModel)

    async def update_target_pixel(
        self,
        account_id: int,
        category_id: int,
        name: str,
        target_pixel_id: int,
        client_id: int | None = None,
        domain: str | None = None,
    ) -> dict[str, typing.Any]:
        """Method `ads.updateTargetPixel()`

        :param account_id:
        :param category_id:
        :param name:
        :param target_pixel_id:
        :param client_id:
        :param domain:
        """

        return await self._call("ads.updateTargetPixel", locals(), dict[str, typing.Any])
    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        q: typing.Literal["regions"],
        country: int,
        ids: list[str] | None = None,
        lang: str | None = None,
    ) -> list[TargSuggestionsRegions]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        q: typing.Literal["schools"],
        cities: list[str],
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
    ) -> list[TargSuggestionsSchools]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
    ) -> list[TargSuggestions]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        cities: list[str],
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
    ) -> list[TargSuggestionsCities]: ...

    async def get_suggestions(
        self,
        section: str,
        *,
        cities: list[str] | None = None,
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
    ) -> list[TargSuggestionsSchools] | list[TargSuggestionsCities] | list[TargSuggestionsRegions] | list[TargSuggestions]:
        """Method `ads.getSuggestions()`

        :param section: Section, suggestions are retrieved in. Available values: *countries - request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions - requested list of regions. 'country' parameter is required. *cities - requested list of cities. 'country' parameter is required. *districts - requested list of districts. 'cities' parameter is required. *stations - requested list of subway stations. 'cities' parameter is required. *streets - requested list of streets. 'cities' parameter is required. *schools - requested list of educational organizations. 'cities' parameter is required. *interests - requested list of interests. *positions - requested list of positions (professions). *group_types - requested list of group types. *religions - requested list of religious commitments. *browsers - requested list of browsers and mobile devices.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param country: ID of the country objects are searched in.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param lang: Language of the returned string values. Supported languages: *ru - Russian,, *ua - Ukrainian,, *en - English.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        """

        return await self._call(
            "ads.getSuggestions",
            locals(),
            dependent=( {"q": {"regions": list[TargSuggestionsRegions], "schools": list[TargSuggestionsSchools]}}, (("cities",), list[TargSuggestionsCities]), ),
            default=list[TargSuggestions],
        )


__all__ = ("AdsCategory",)
