"""
Base database module.

This module defines the Base class for all ORM models and handles imports
of models to ensure they are registered with SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base

# Create Base class for SQLAlchemy models
Base = declarative_base()

# DO NOT import models here to avoid circular imports
# Models will be imported in a separate module (base_class.py) 