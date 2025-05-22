import asyncio
from asyncio import run
from sqlalchemy import select
from DaoBase.dao import UserDAO
from Models.models import Person, Post
from crud import connection
from sqlalchemy.ext.asyncio import AsyncSession


# @connection
# async def sel(session:AsyncSession):
#     user = await session.execute(select(Person))
#     us = user.scalars().all()
#
#     for i in us:
#         print(i)


# @connection
# async def filter_sel(age,session:AsyncSession):
#     user_age = await session.execute(select(Person).filter(Person.age == age))
#     result = user_age.scalars().all()
#     for i in result:
#         print(i)
#
#
# ss= run(filter_sel(12))
# вывод связанных таблицы
# @connection
# async def post(session:AsyncSession):
#     result = await session.execute(select(Person,Post).join(Post,Person.id == Post.person_id))
#     user_post = result.all()
#     for i,j in user_post:
#         print(i,j)
#
# ss = run(post())

@connection
async def add(user_data,session:AsyncSession):
    new_user = await UserDAO.add(session=session,**user_data)
    print(f'Добавлен с id {new_user.id}')
    return new_user.id

new = run(add({"name": "oliver_jackson", 'age':'12',"email": "oliver.jackson@example.com"}))