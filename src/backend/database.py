from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definição do endereço da base de dados
MYSQL_DATABASE_URL = "mysql+pymysql://admin:Gerdaudb#1@db-gerdau.cfssllf0qlz6.us-east-1.rds.amazonaws.com:3306/dbgerdau"

# cria a engine de database do sqlalchemy
engine = create_engine(
    MYSQL_DATABASE_URL, pool_pre_ping=True, echo=True)

# classe que cria uma sessão de acesso ao db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Abre uma sessão para acesso ao db e fecha após o uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
