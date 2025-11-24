"""Validating user schema for creating a new user"""
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Schema for creating a new user"""
    email: EmailStr = Field(..., description="Email of the user")
    password: str = Field(..., min_length=8, description="Password of the user")

    class Config:
        orm_mode = True     


class ShowUser(BaseModel):
    """Schema for showing user details"""
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

