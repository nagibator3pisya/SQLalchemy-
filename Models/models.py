from sqlalchemy import Column, Integer, String

from DataBase.DataBase import Base


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=128))
    age = Column(Integer)