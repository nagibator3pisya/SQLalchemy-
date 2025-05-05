import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from DataBase.DataBase import async_session_maker, engine
from Models.models import Person,Profile
# вывод профиля + юзера
async def selest(session: AsyncSession):
    result = await session.execute(select(Person).options(selectinload(Person.profile)))
    return result.scalars().all()



# cессия
async def main():
    async with async_session_maker() as session:
        try:
          result = await selest(session=session)
          for i in result:
              print(i)
              if i.profile:
                  print(f'Profile: {i.profile}')
              else:
                  print('No profile')
        except Exception as e:
            # Обрабатываем ошибки
            print(f"{e}")
            # Откатываем транзакцию в случае ошибки
            await session.rollback()

    # Явно закрываем соединение с базой данных
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
