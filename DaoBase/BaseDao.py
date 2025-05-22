from typing import List, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAO:
    """
    BaseDAO — это базовый класс для работы с базой данных,
    который предоставляет универсальные методы для добавления данных в таблицы
    """
    model = None

    @classmethod
    async def add(cls,session:AsyncSession,**values):
        # Добавление одной записи
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    async def add_all(cls,session:AsyncSession,instances: List[Dict[str,Any]]):
        new_instance = [cls.model(**values) for values in instances]
        session.add_all(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance