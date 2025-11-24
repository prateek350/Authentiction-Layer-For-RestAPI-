"""Creating a utility for saving the user in the database in the user table"""
from sqlalchemy import Boolean, Column, Integer, String
from src.core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    """User data model representing the user table in the database"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # relationships can be defined here if needed
