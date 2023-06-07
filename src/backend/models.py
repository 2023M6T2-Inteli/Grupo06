from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
class Report(Base):
    __tablename__ = 'Report'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    projectName = Column(String, nullable=False)
    typePlace = Column(int, nullable=False)
    operator = Column(String, nullable=False)
    date = Column(String, nullable=False)
    gasLevel1 = Column(float, nullable=False, default=True)
    gasLevel2 = Column(float, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())