import asyncio
from asyncio import run

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from DataBase.DataBase import async_session_maker, engine
from Models.models import Person, Profile, Post


def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                # Явно не открываем транзакции, так как они уже есть в контексте
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()  # Откатываем сессию при ошибке
                raise e  # Поднимаем исключение дальше
            finally:
                await engine.dispose()  # Закрываем сессию

    return wrapper

# @connection
# async def add_user_post(session,name,age,email):
#     user = Person(name=name,age=age,email=email)
#     session.add(user)
#     await  session.commit()
#     return user.id


# @connection
# async def add_user_and_post(session,name,age,email,title,body):
#     user = Person(name=name,age=age,email=email)
#     session.add(user)
#     await session.flush()
#
#     post = Post(person_id=user.id,title=title,body=body)
#     session.add(post)
#     await session.commit()
#
#
# new_user_and_post = run(add_user_and_post(name='Толя',age=14,
#                                           email='saw@mail.ru',
#                                           title='Название поста',
#                                           body='Описание поста'))
# print(new_user_and_post)

# new_user = run(add_user_post(name='Санёк',age=12,email='saw@mail.ru'))
# print(new_user)

@connection
async def all_user(session,user_data):
    user=[
        Person(
            name=i['name'],
            age=i['age'],
            email=i['email']
        )
        for i in user_data
    ]
    session.add_all(user)
    await session.commit()
    # return [i.id for i in user ]

users_datas = [
    {'name': 'Толя', 'age': 13, 'email': 'saw@mail.ru'},
    {'name': 'Маша', 'age': 25, 'email': 'masha@mail.ru'},
    {'name': 'Петя', 'age': 30, 'email': 'petya@mail.ru'}
]

all = run(all_user(user_data=users_datas))
print(all)
