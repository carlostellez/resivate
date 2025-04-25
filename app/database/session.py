"""
Database session module.

This module provides database connection and session management functionality.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 