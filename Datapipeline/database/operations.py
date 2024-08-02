from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


print(os.getenv("DEVELOPMENT_DATABASE_URL"))
# engine = create_engine('postgresql://user:password@localhost:5432/database_name')
# Session = sessionmaker(bind=engine)
# session = Session()