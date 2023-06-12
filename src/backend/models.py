# import da classe 'Base' 
from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Boolean
from sqlalchemy.sql import func
from uuid import UUID

# Classe report que contem definição de chave-primaria, nome e tipo das colunas da tabela
class Report(Base):
    # define 'report' como nome da tabela
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    projectName = Column(String(100), nullable=False)
    typePlace = Column(Integer)
    operator = Column(String(100))
    date = Column(TIMESTAMP)
    gasLevel1 = Column(Float)
    gasLevel2 = Column(Float)
    gasLevel3 = Column(Float)
    gasLevel4 = Column(Float)
    createdAt = Column(TIMESTAMP(timezone=True),
                       server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())

