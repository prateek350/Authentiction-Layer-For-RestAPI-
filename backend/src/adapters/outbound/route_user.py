"""Creating a utility for saving the user in the database in the user table"""
from fastapi import HTTPException,status,Depends,APIRouter
from src.core.database import get_db
from src.core.logger import setup_logger
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, ShowUser
from src.api.userapi import create_user_endpoint

logger=setup_logger(__name__)
router=APIRouter()

@router.post("/users/", response_model=ShowUser, tags=["Users"],status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession=Depends(get_db)):
    """API endpoint to create a new user
    Inputs-
    user: UserCreate schema containing email and password
    db: AsyncSession of the database
    Output
    User object after creating the user in the database"""
    logger.info("User Endpoint: %s", f"Creating user with email {user.email}.")
    return await (create_user_endpoint(user, db))
