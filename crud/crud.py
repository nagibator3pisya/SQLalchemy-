import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DataBase.DataBase import async_session_maker, engine
from Models.models import Person,Profile

# добавление профиль + юзер
async def add_profile_and_user(name: str, age: int, email:str,first_name: str,
                     last_name: str, bio: str, session: AsyncSession):
    new_user = Person(name=name, age=age,email=email)
    session.add(new_user)
    await session.flush()

    profile = Profile(first_name=first_name,last_name=last_name,bio=bio,person_id=new_user.id)
    session.add(profile)
    await session.commit()

    return {'user_id': new_user.id, 'profile_id': profile.id}


# cессия
async def main():
    async with async_session_maker() as session:
        try:
           await add_profile_and_user('Тест_с_емаилом',22,'test@mail.com','эмаил_пользователь',
                                      'маил пользователь','биотест',session=session)
        except Exception as e:
            # Обрабатываем ошибки
            print(f"{e}")
            # Откатываем транзакцию в случае ошибки
            await session.rollback()

    # Явно закрываем соединение с базой данных
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
