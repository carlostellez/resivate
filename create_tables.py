"""
Script to create database tables.

This script initializes all database tables based on SQLAlchemy models.
"""
from app.database.base import Base
from app.models.category import Category  # noqa
from app.models.image import Image  # noqa
from app.models.faq import FAQ  # noqa
from sqlalchemy import create_engine

from app.core.config import settings

def create_tables() -> None:
    """
    Create all database tables.
    
    This function creates all database tables defined in models,
    if they don't already exist.
    """
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    create_tables() 