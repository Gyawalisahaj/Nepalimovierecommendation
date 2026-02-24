"""Database configuration and session management.

This module sets up SQLAlchemy connection, creates sessions,
and provides the declarative base for all models.
"""

import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

# Get database URL from environment or use default
# In many deployment environments (e.g. Vercel) the working
# directory may be read-only, so creating a file-backed SQLite
# database will fail with "unable to open database file".  The
# recommendation engine doesn't actually use persistent storage
# today, therefore we default to an in-memory database to avoid
# errors.  Consumers can still override via DATABASE_URL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Base class for all models
Base = declarative_base()

logger.info(f"Database configured: {DATABASE_URL}")