# import da classe 'Base'
from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.sql import func
from uuid import UUID

from sqlalchemy.orm import relationship

# Classe report que contem definição de chave-primaria, nome e tipo das colunas da tabela
class Report(Base):
    # define 'report' como nome da tabela
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    reportName = Column(String(100), nullable=False)
    typePlace = Column(Integer)
    operator = Column(String(100))
    gasAvg = Column(Float, default=0.00)
    createdAt = Column(TIMESTAMP(timezone=True),
                       server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
    isFinished = Column(Integer, default=0)
    images = relationship('Image')
    gasReadings = relationship('Gas')

    def return_json(self):
        return {
            "id": self.id,
            "reportName": self.reportName,
            "typePlace": self.typePlace,
            "operator": self.operator,
            "gasAvg": self.gasAvg,
            "isFinished": self.isFinished,
            "images": [image.return_json() for image in self.images]
        }


class Gas(Base):
    __tablename__ = 'gas'
    id = Column(Integer, primary_key=True)
    reportId = Column(Integer, ForeignKey("report.id"))
    gasValue = Column(Float)
    createdAt = Column(TIMESTAMP(timezone=True),
                       server_default=func.now())

    def return_json(self):
        return {
            "id": self.id,
            "reportId": self.reportId,
            "gasValue": self.gasValue,
        }


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    reportId = Column(Integer, ForeignKey("report.id"))
    url = Column(String(150))
    createdAt = Column(TIMESTAMP(timezone=True),
                       server_default=func.now())

    def return_json(self):
        return {
            "id": self.id,
            "reportId": self.reportId,
            "url": self.url,
        }
