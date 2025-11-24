""" Creating a api router for user related operations """
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, ShowUser
from src.utils.user import create_new_user
from src.logger import setup_logger

logger=setup_logger(__name__)

async def create_user_endpoint(user: UserCreate, db: AsyncSession):
    """Creating a new user in the database
    Inputs-
    user: UserCreate schema containing email and password
    db: AsyncSession of the database
    Output
    User object after creating the user in the database"""
    created_user=await (create_new_user(user, db))
    logger.info("User Creation: %s", f"User with email {user.email} created successfully.")
    return ShowUser.from_orm(created_user)