"""Creating a utility for saving the user in the database in the user table"""
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.user import UserCreate
from src.data_models.user_model import User
from src.core.hashing import Hasher


async def create_new_user(user: UserCreate, db: AsyncSession):
    """Create a user in the database."""
    db_user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
    )
    db.add(db_user)
    try:
        await db.commit()
    except Exception as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already present in the database",
        )
    await db.refresh(db_user)
    return db_user
