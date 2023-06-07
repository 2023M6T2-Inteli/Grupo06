from datetime import datetime
from typing import List
from pydantic import BaseModel


class ReportBaseSchema(BaseModel):
    id: int | None = None
    projectName: str
    typePlace: int
    operator: str | None = None
    date: datetime | None = None
    gasLevel1: float
    gasLevel2: float
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListReportResponse(BaseModel):
    status: str
    results: int
    report: List[ReportBaseSchema]

