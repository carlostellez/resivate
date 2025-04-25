"""
Script to create database tables.

This script initializes all database tables based on SQLAlchemy models.
"""
# Import Base class
from app.database.base import Base
from sqlalchemy import create_engine

# Import all models explicitly to ensure they are registered with SQLAlchemy
from app.models.category import Category
from app.models.image import Image
from app.models.faq import FAQ
from app.models.menu_option import MenuOption
from app.models.option import Option
from app.models.plan import Plan
from app.models.type import Type  # This must be imported after Image due to FK dependency
from app.models.processing_info import ProcessingInfo
from app.models.solutions_data import SolutionsData  # This must be imported after Image due to FK dependency

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