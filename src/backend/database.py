from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = "sqlite:///report.db"
# SQLITE_DATABASE_URL = "sqlite://admin:Gerdaudb#1@db-gerdau.cfssllf0qlz6.us-east-1.rds.amazonaws.com/db-gerdau.db"


engine = create_engine(
    SQLITE_DATABASE_URL, pool_pre_ping=True, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

