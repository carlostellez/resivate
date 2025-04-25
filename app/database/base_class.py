"""
Base class and model imports module.

This module imports the Base class and all models to ensure they are registered
with SQLAlchemy while avoiding circular imports.
"""
# This file is primarily used for Alembic migrations and model registration
# Import Base only - models will be imported in create_tables.py
from app.database.base import Base

# Import all models here to register them with SQLAlchemy
# These imports are needed to make SQLAlchemy aware of the models
from app.models.category import Category
from app.models.image import Image
from app.models.faq import FAQ
from app.models.menu_option import MenuOption
from app.models.option import Option
from app.models.plan import Plan
from app.models.type import Type
from app.models.processing_info import ProcessingInfo
from app.models.solutions_data import SolutionsData

# Export Base only
__all__ = ["Base"] 