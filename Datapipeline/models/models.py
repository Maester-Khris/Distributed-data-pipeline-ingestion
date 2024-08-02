from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

# Notes: specify the schema you are using to save your tales
# 1- Base = declarative_base(metadata=MetaData(schema="myschema"))
# 2- __table_args__ = {'schema' : 'myschema'}  other way to speciy the schema

Base = declarative_base()
metadata = Base.metadata

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    domain = Column(String)
    create_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"