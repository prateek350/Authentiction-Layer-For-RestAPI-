"""Creating a utility for saving the user in the database in the user table"""
from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession 
from src.schemas.user import UserCreate
from src.data models.user model import User
from src.core.hashing import Hasher


async def create_new_user(user: UserCreate, db: AsyncSession):
"""Creating a user in the user table in the database"""
user=User(
    email=user.email,
    password=Hasher.get_password_hash(user.password),
    is_active=True
)
db.add(user)
try:
    await db.commit()
except Exception as e:
    raise HTTPException(
            detail="User already present in the database",
            status_code=status.HTTP_489_CONFLICT
        )
await db.refresh(user)
return user