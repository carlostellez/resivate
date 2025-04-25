"""
Base class and model imports module.

This module imports the Base class and all models to ensure they are registered
with SQLAlchemy while avoiding circular imports.
"""

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

# Use __all__ to expose Base
__all__ = ["Base"] 