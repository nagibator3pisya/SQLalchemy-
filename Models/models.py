from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from DataBase.DataBase import Base










class Person(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer,nullable=True)
    email: Mapped[str] = mapped_column(String(50),nullable = True)
    # связб с постом
    post = relationship('Post',back_populates='person_post')

    def __str__(self):
        return f'{self.__class__.__name__}(id = {self.id} name = {self.name},age = {self.age}, email = {self.email})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text)
    # cсылка на его id
    person_id: Mapped[int] = mapped_column(ForeignKey('people.id'))
    # обратная ссылка один ко многим с человеком
    person_post = relationship('Person',back_populates='post')


class Profile(Base):
    __tablename__ = "profile"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    bio: Mapped[str]  = mapped_column(String(100))



    def __str__(self):
        return (f'{self.__class__.__name__}(id = {self.id} first_name = {self.first_name},last_name = {self.last_name},'
                f' bio = {self.bio})')

    def __repr__(self):
        return str(self)