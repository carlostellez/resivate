"""
Base database module.

This module defines the Base class for all ORM models and handles imports
of models to ensure they are registered with SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base

# Create Base class for SQLAlchemy models
Base = declarative_base()

# Import all models here to register them with SQLAlchemy
# This is commented out to avoid circular imports
# Uncomment and add new models as they are created
# from app.models.category import Category  # noqa
# from app.models.image import Image  # noqa 