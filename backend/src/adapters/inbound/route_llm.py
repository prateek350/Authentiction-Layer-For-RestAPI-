from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.logger import setup_logger
from src.core.database import get_db
from src.api.loginapi import get_current_user
logger=setup_logger(__name__)
router=APIRouter()

@router.post("/llm", tags=["LLM"])
async def llm_endpoint(request: Request, db: AsyncSession=Depends(get_db),current_user=Depends(get_current_user)):
    """Endpoint for LLM functionality
    Inputs-
    request: Request object to get client information
    db: AsyncSession of the database
    Output
    Response from the LLM functionality"""
    logger.info("LLM Endpoint: %s", "LLM endpoint called.")
    # Implement your LLM functionality here and return the response
    return {"message": "LLM endpoint is under construction."}   
