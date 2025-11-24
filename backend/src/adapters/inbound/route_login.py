"""Importing necessary modules and defining the router for login functionality"""
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException, Request, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.core.logger import setup_logger
from src.api.loginapi import login_for_access_token_endpoint

logger=setup_logger(__name__)
router=APIRouter()

@router.post("/login", tags=["Authentication"])
async def login(request: Request, form_data: OAuth2PasswordRequestForm=Depends(),
                db: AsyncSession=Depends(get_db)):
    """Endpoint for user login and token generation
    Inputs-
    request: Request object to get client information
    form_data: OAuth2PasswordRequestForm containing username and password
    db: AsyncSession of the database
    Output
    Access token for authenticated user"""
    logger.info("Login Endpoint: %s", "Login endpoint called.")
    return await (login_for_access_token_endpoint(request, form_data, db))