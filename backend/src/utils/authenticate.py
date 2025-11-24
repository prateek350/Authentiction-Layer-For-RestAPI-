from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.login import get_user_by_email
from src.core.hashing import Hasher
from src.core.logger import setup_logger

logger=setup_logger(__name__)

async def authenticate_user(email: str, password: str, db: AsyncSession):
    """Authenticating the user using email and password
    Inputs-
    email: str- email of the user
    password: str- password of the user
    db: AsyncSession of the database
    Output
    User object if authenticated else None"""
    user=await (get_user_by_email(email, db))
    if not user:
        logger.error("Error: %s", f"User with email {email} not found.")
        return None
    if not Hasher.verify_password(password, user.password):
        logger.error("Error: %s", f"Password mismatch for user with email {email}.")
        return None
    return user
    