"""
Option model module.

This module defines the Option model used to store option data in the database.
"""
from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Option(Base):
    """
    Option database model.
    
    Attributes:
        id: The unique identifier of the option
        name: The name of the option
        icon: The icon associated with the option
    """
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    icon = Column(String(255), nullable=False) 