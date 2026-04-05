import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)


class Settings:
    """Application settings loaded from environment variables."""

    PROJECT_TITLE: str = "Authentication Layer"
    PROJECT_VERSION: str = "0.1.0"

    USER: str = os.getenv("PG_USERNAME", "postgres")
    PASSWORD: str = os.getenv("PG_PASSWORD", "postgres")
    SERVER: str = os.getenv("PG_HOST", "localhost")
    PORT: str = os.getenv("PG_PORT", "5432")
    DB: str = os.getenv("PG_DB", "authentication_db")
    DATABASE_URL: str = (
        f"postgresql+asyncpg://{USER}:{PASSWORD}@{SERVER}:{PORT}/{DB}"
    )

    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
