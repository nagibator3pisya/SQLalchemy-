from sqlalchemy.ext.asyncio import create_async_engine,AsyncAttrs, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config.config import settings

DATABASE_URL = settings.get_db_url()

# Создаем асинхронный движок для работы с базой данных
engine = create_async_engine(url=DATABASE_URL)

# Создаем фабрику сессий для взаимодействия с базой данных
async_session_maker = async_sessionmaker(bind=engine,expire_on_commit=False,future=True,)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True