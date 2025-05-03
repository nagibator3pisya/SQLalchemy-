from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from DataBase.DataBase import Base


class Person(Base):
    __tablename__ = "people"
    # id = Column(Integer, primary_key=True)
    # name = Column(String(length=128))
    # age = Column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)


class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text)
    person_id: Mapped[int] = mapped_column(ForeignKey('people.id'))