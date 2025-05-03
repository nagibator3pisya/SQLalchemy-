from DataBase.DataBase import Base, engine
import asyncio

from Models.models import Person
# from session.decor_session import connection


# @connection
# async def add_user(name: str, age: int, session):
#     # Создаём объект User (инстанс модели)
#     new_user = Person(name=name, age=age)
#     # Добавляем объект в сессию
#     session.add(new_user)
#     # Сохраняем изменения в базе данных
#     await session.commit()





# async def init():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
# async def main():
#     await init()
#     print("Database initialized!")
#
# async def close_engine():
#     await engine.dispose()
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     finally:
#         asyncio.run(close_engine())
