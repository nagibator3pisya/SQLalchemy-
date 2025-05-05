import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DataBase.DataBase import async_session_maker, engine
from Models.models import Person,Profile

# cоздать юзера
async def add_user(name: str, age: int, session: AsyncSession):
    # Создаём объект User (инстанс модели)
    new_user = Person(name=name, age=age)
    # Добавляем объект в сессию
    session.add(new_user)
    # Сохраняем изменения в базе данных
    await session.commit()
    return new_user

# cессия
async def main():
    async with async_session_maker() as session:
        try:
            user = await add_user('Тестовый4', 14, session=session)
            # Выводим сообщение об успешном добавлении
            print(f"Пользователь добавлен: {user.name}, Возраст: {user.age}")
        except Exception as e:
            # Обрабатываем ошибки
            print(f"Ошибка при добавлении пользователя: {e}")
            # Откатываем транзакцию в случае ошибки
            await session.rollback()

    # Явно закрываем соединение с базой данных
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
