"""
Category model module.

This module defines the Category model used to store category data in the database.
"""
from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Category(Base):
    """
    Category database model.
    
    Attributes:
        id: The unique identifier of the category
        title: The title of the category
        link: The link associated with the category
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    link = Column(String(512), nullable=False) 