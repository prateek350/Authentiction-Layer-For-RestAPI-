from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from src.core.config import Settings
from contextlib import asynccontextmanager

DATABASE_URL=Settings.DATABASE_URL
engine =create_async_engine(DATABASE_URL)

AsyncSessionLocal=sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def ensure_database():
    if not database_exists(DATABASE_URL.replace("+asyncpg", "")): # Remove async driver for check
        create_database(DATABASE_URL.replace("+asyncpg", "")) # Remove async driver for creation
        print("Database created successfully!") 
    else:
        print("Database already exists.")

async def get_db()->AsyncGenerator [AsyncSession, None]:
    """Generator for creating a session with the database"""
    async with AsyncSessionLocal() as session:
        yield session

Base=declarative_base()
https://github.com/prateek350/Authentiction-Layer-For-RestAPI-.git