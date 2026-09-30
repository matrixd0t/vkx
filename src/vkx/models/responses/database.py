from ..base_model import BaseModel, Field
from ..objects import (
    BaseCountry,
    BaseObject,
    DatabaseCity,
    DatabaseSchool,
    DatabaseUniversity,
    Faculty,
    Region,
    Station,
)


class GetChairsResponseModel(BaseModel):
    count: int = Field()
    items: list["BaseObject"] = Field()


class GetCitiesResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseCity"] = Field()


class GetCountriesResponseModel(BaseModel):
    count: int = Field()
    items: list["BaseCountry"] = Field()


class GetFacultiesResponseModel(BaseModel):
    count: int = Field()
    items: list["Faculty"] = Field()


class GetMetroStationsResponseModel(BaseModel):
    count: int = Field()
    items: list["Station"] = Field()


class GetRegionsResponseModel(BaseModel):
    count: int = Field()
    items: list["Region"] = Field()


class GetSchoolsResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseSchool"] = Field()


class GetUniversitiesResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseUniversity"] = Field()


__all__ = (
    "GetChairsResponseModel",
    "GetCitiesResponseModel",
    "GetCountriesResponseModel",
    "GetFacultiesResponseModel",
    "GetMetroStationsResponseModel",
    "GetRegionsResponseModel",
    "GetSchoolsResponseModel",
    "GetUniversitiesResponseModel",
)
