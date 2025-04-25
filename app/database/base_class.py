"""
Base class and model imports module.

This module imports the Base class and all models to ensure they are registered
with SQLAlchemy while avoiding circular imports.
"""

from app.database.base import Base

# Import all models here to register them with SQLAlchemy
from app.models.category import Category  # noqa
from app.models.image import Image  # noqa
from app.models.faq import FAQ  # noqa
from app.models.menu_option import MenuOption  # noqa
from app.models.option import Option  # noqa 