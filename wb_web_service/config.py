import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    SERVER_PORT: int = 8000
    API_SERVER = os.getenv("API_SERVER")
    API_NAME = os.getenv("API_NAME")
    BACKEND_CORS_ORIGINS: list[str] = ["http://127.0.0.1:8000",
                                       "http://localhost:8000"]


settings = Settings()
