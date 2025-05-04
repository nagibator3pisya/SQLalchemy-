from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # DATABASE_SQLITE = 'sqlite+aiosqlite:///data/db.sqlite3'
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )

    def get_db_url(self):
        return (f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")


settings = Settings()

# print(settings.get_db_url())