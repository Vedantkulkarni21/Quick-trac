from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "mysql+pymysql://root:password@localhost:3306/crud_fastapi"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)