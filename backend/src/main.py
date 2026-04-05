from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.base import router
from src.core.database import Base, engine, ensure_database
from src.data_models.user_model import User  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    await ensure_database()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Authentication System"}
