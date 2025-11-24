"Importing the essential libraries for authenticating and logging the user"""
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt
from src.core.config import Settings
from src.core.database import get_db
from src.utils.login import get_user_by_email
from src.utils.authenticate import authenticate_user
from src.core.security import create_access_token
from src.core.logger import setup_logger
from src.core.rate_limitter import check_login_attempts, reset_login_attempts

logger=setup_logger(__name__)

async def login_for_access_token_endpoint(request: Request, form_data: OAuth2PasswordRequestForm,
                                          db:AsyncSession):
    """Creating the token for maintaining the Asyncsession
    Inputs-
    fore_data-OAuth2Password RequestForm (username="", password="")
    db: AsyncSession of the database
    Output
    Authorization of the user and creating the token"""
    client_ip=request.client.host
    logger.info("Login Attempt: %s", f"Login attempt for{client_ip}, username:{form_data.username}")
    try:
        check_login_attempts(client_ip)
    except HTTPException as e:
        raise e
    user=await (authenticate_user(form_data.username, form_data.password, db))
    if not user:
        logger.error("Error: %s", f"The email id or password doesn't match for username: {form_data.username}.")
        raise HTTPException( 
            detail="Incorrect email or password",
            Status_code=status.HTTP_401_UNAUTHORIZED
        )
    reset_login_attempts(client_ip)
    access_token=await (create_access_token(data={"sub":user.email})) 
    logger.info("Token: %s", f"Token created successfully for (form data.username).")
    return {"access_token":access_token, "token_type": "bearer"}

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/token")

async def get_current_user(token: str=Depends (oauth2_scheme), db: AsyncSession=Depends(get_db)):
    """Creating a dependency which can be used for token validation
    Inputs-
    token-OAuth2PasswordBearer (tokenUrl-"/token")
    db: AsyncSession of the database
    Output
    Authentication of the user to any function with this dependency"""
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detall="Could not validate the credentials, Please login again."
    )
    try:
        payload=jwt.decode(token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
        email:str=payload.get("sub")
        if email is None:
            logger.error("Error: %s", "The email is not present in the database.")
            raise credentials_exception
    except Exception as e:
        logger.error("Error: %s", "Doesn't able to decode the token.")
        raise credentials_exception from e
    user=await get_user_by_email(email=email,db=db)
    if user is None:
        raise credentials_exception
    logger.info("Validation: %s", "validation of the token is successfull.")
    return user