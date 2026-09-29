
from vkx.models.methods.base_category import BaseCategory
from vkx.models.objects import *
from vkx.models.responses.database import *  # type: ignore


class DatabaseCategory(BaseCategory):
    async def get_chairs(
        self,
        faculty_id: int,
        count: int | None = None,
        offset: int | None = None,
    ) -> GetChairsResponseModel:
        """Method `database.getChairs()`

        :param faculty_id: id of the faculty to get chairs from
        :param count: amount of chairs to get
        :param offset: offset required to get a certain subset of chairs
        """

        return await self._call("database.getChairs", locals(), GetChairsResponseModel)

    async def get_cities(
        self,
        count: int | None = None,
        fields: list[DatabaseCitiesFields] | None = None,
        need_all: bool | None = None,
        offset: int | None = None,
        q: str | None = None,
        region_id: int | None = None,
    ) -> GetCitiesResponseModel:
        """Method `database.getCities()`

        :param count: Number of cities to return.
        :param fields: Cities fields to return. Sample values: 'fias_guid'
        :param need_all: '1' - to return all cities in the country, '0' - to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param q: Search query.
        :param region_id: Region ID.
        """

        return await self._call("database.getCities", locals(), GetCitiesResponseModel)

    async def get_cities_by_id(
        self,
        city_ids: list[int] | None = None,
        fields: list[DatabaseCitiesFields] | None = None,
    ) -> list[CityById]:
        """Method `database.getCitiesById()`

        :param city_ids: City IDs.
        :param fields: Cities fields to return. Sample values: 'fias_guid'
        """

        return await self._call("database.getCitiesById", locals(), list[CityById])

    async def get_countries(
        self,
        code: str | None = None,
        count: int | None = None,
        need_all: bool | None = None,
        offset: int | None = None,
    ) -> GetCountriesResponseModel:
        """Method `database.getCountries()`

        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param count: Number of countries to return.
        :param need_all: '1' - to return a full list of all countries, '0' - to return a list of countries near the current user's country (default).
        :param offset: Offset needed to return a specific subset of countries.
        """

        return await self._call("database.getCountries", locals(), GetCountriesResponseModel)

    async def get_countries_by_id(
        self,
        country_ids: list[int] | None = None,
    ) -> list[BaseCountry]:
        """Method `database.getCountriesById()`

        :param country_ids: Country IDs.
        """

        return await self._call("database.getCountriesById", locals(), list[BaseCountry])

    async def get_faculties(
        self,
        university_id: int,
        count: int | None = None,
        offset: int | None = None,
    ) -> GetFacultiesResponseModel:
        """Method `database.getFaculties()`

        :param university_id: University ID.
        :param count: Number of faculties to return.
        :param offset: Offset needed to return a specific subset of faculties.
        """

        return await self._call("database.getFaculties", locals(), GetFacultiesResponseModel)

    async def get_metro_stations(
        self,
        city_id: int,
        count: int | None = None,
        extended: bool | None = None,
        offset: int | None = None,
    ) -> GetMetroStationsResponseModel:
        """Method `database.getMetroStations()`

        :param city_id:
        :param count:
        :param extended:
        :param offset:
        """

        return await self._call("database.getMetroStations", locals(), GetMetroStationsResponseModel)

    async def get_metro_stations_by_id(
        self,
        station_ids: list[int] | None = None,
    ) -> list[Station]:
        """Method `database.getMetroStationsById()`

        :param station_ids:
        """

        return await self._call("database.getMetroStationsById", locals(), list[Station])

    async def get_regions(
        self,
        count: int | None = None,
        offset: int | None = None,
        q: str | None = None,
    ) -> GetRegionsResponseModel:
        """Method `database.getRegions()`

        :param count: Number of regions to return.
        :param offset: Offset needed to return specific subset of regions.
        :param q: Search query.
        """

        return await self._call("database.getRegions", locals(), GetRegionsResponseModel)

    async def get_school_classes(
        self,
        country_id: int | None = None,
    ) -> list[SchoolClass]:
        """Method `database.getSchoolClasses()`

        :param country_id: Country ID.
        """

        return await self._call("database.getSchoolClasses", locals(), list[SchoolClass])

    async def get_schools(
        self,
        city_id: int,
        count: int | None = None,
        offset: int | None = None,
        q: str | None = None,
    ) -> GetSchoolsResponseModel:
        """Method `database.getSchools()`

        :param city_id: City ID.
        :param count: Number of schools to return.
        :param offset: Offset needed to return a specific subset of schools.
        :param q: Search query.
        """

        return await self._call("database.getSchools", locals(), GetSchoolsResponseModel)

    async def get_universities(
        self,
        city_id: int | None = None,
        count: int | None = None,
        offset: int | None = None,
        q: str | None = None,
    ) -> GetUniversitiesResponseModel:
        """Method `database.getUniversities()`

        :param city_id: City ID.
        :param count: Number of universities to return.
        :param offset: Offset needed to return a specific subset of universities.
        :param q: Search query.
        """

        return await self._call("database.getUniversities", locals(), GetUniversitiesResponseModel)


__all__ = ("DatabaseCategory",)
