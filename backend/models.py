"""Database models for the movie recommendation system.

This module defines SQLAlchemy ORM models for storing user data.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class User(Base):
    """User model for storing authentication and profile information.
    
    Attributes:
        id: Unique user identifier (primary key)
        first_name: User's first name
        last_name: User's last name
        email: User's email address (unique)
        hashed_password: Bcrypt hashed password
        is_active: Whether the user account is active
        created_at: Account creation timestamp
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())