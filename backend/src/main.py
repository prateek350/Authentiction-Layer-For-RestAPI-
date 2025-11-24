from fastapi import FastAPI
from src.api import base
from src.core.database import engine,Base,ensure_database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await ensure_database()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app=FastAPI(lifespan=lifespan)

app.include_router(base.router)

@app.get("/")
async def root():
    """Root Endpoint"""
    {"message":"Authentication System"}