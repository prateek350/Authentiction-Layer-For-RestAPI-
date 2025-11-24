from sqlalchemy.ext.asyncio import AsyncSession
from src.data_models.user_model import User
from sqlalchemy import select

async def get_user_by_email(email: str, db: AsyncSession):
    """Fetching the user from the database using email
    Inputs-
    email: str- email of the user
    db: AsyncSession of the database
    Output
    User object if found else None"""
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    return user