"""Creating a base api router for the application"""
from fastapi import APIRouter
from src.adapters.outbound.route_user import router as user_router
from src.adapters.inbound.route_login import router as login_router

router=APIRouter()
router.include_router(user_router, prefix="/api")
router.include_router(login_router, prefix="/api")