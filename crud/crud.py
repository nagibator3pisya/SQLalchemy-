import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DataBase.DataBase import async_session_maker, engine
from Models.models import Person,Profile
# cоздать юзера
# async def add_user(name: str, age: int, session: AsyncSession):
#     # Создаём объект User (инстанс модели)
#     new_user = Person(name=name, age=age)
#     # Добавляем объект в сессию
#     session.add(new_user)
#     # Сохраняем изменения в базе данных
#     await session.commit()


# добавление профиль + юзер
# async def addprofile(name: str, age: int, first_name: str,
#                      last_name: str, bio: str, session: AsyncSession):
#     new_user = Person(name=name, age=age)
#     session.add(new_user)
#     await session.flush()
#
#     profile = Profile(first_name=first_name,last_name=last_name,bio=bio,person_id=new_user.id)
#     session.add(profile)
#     await session.commit()
#
#     return {'user_id': new_user.id, 'profile_id': profile.id}

async def get_all_users(session: AsyncSession):
    # Выполняем запрос для получения всех пользователей
    result = await session.execute(select(Profile))
    # Возвращаем всех пользователей
    return result.scalars().all()



async def main():
    async with async_session_maker() as session:
        profile = await get_all_users(session=session)


    # Явно закрываем соединение с базой данных
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())





#
# async def add_user(name: str, age: int, session: AsyncSession):
#     # Создаём объект User (инстанс модели)
#     new_user = Person(name=name, age=age)
#     # Добавляем объект в сессию
#     session.add(new_user)
#     # Сохраняем изменения в базе данных
#     await session.commit()
# async def get_all_users(session: AsyncSession):
#     # Выполняем запрос для получения всех пользователей
#     result = await session.execute(select(Person))
#     # Возвращаем всех пользователей
#     return result.scalars().all()