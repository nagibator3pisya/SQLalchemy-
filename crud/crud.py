import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DataBase.DataBase import async_session_maker, engine
from Models.models import Person,Profile

# добавление множества пользователей
async  def all_add_user(users_data: list[dict],session:AsyncSession):
    users_list = [
        Person(
            name = user_data['name'],
            age  = user_data['age'],
        ) for user_data in users_data
    ]
    session.add_all(users_list)
    await session.commit()
    return [i.id for i in users_list]


# cессия
async def main():
    async with async_session_maker() as session:
        try:
           user_all =  await all_add_user(
               [
                {"name": "michael_brown",'age':12 },
                {"name": "sarah_wilson", 'age':13 },
                {"name": "david_clark", 'age': 13  },
                {"name": "emma_walker", 'age': 14  },
                {"name": "james_martin",'age': 15   }
               ],
               session=session
           )

           print(user_all)
        except Exception as e:
            # Обрабатываем ошибки
            print(f"{e}")
            # Откатываем транзакцию в случае ошибки
            await session.rollback()

    # Явно закрываем соединение с базой данных
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
