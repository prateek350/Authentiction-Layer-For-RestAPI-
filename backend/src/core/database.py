from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from src.core.config import Settings

DATABASE_URL = Settings.DATABASE_URL
engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)


async def ensure_database():
    sync_database_url = DATABASE_URL.replace("+asyncpg", "")
    if not database_exists(sync_database_url):
        create_database(sync_database_url)
        print("Database created successfully!") 
    else:
        print("Database already exists.")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async SQLAlchemy session."""
    async with AsyncSessionLocal() as session:
        yield session


Base = declarative_base()
