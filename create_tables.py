"""
Script to create database tables.

This script initializes all database tables based on SQLAlchemy models.
"""
# Import base_class to ensure all models are properly registered
# This will automatically import all models registered in base_class.py
from app.database.base_class import Base
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