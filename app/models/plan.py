"""
Plan model module.

This module defines the Plan model used to store plan data in the database.
"""
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Numeric

from app.database.base import Base


class Plan(Base):
    """
    Plan database model.
    
    Attributes:
        id: The unique identifier of the plan
        title: The title of the plan (limited to 100 characters)
        description: The detailed description of the plan
        price: The price of the plan with 2 decimal places
        btnMessage: The text to display on the plan's button
        blueBtn: Whether the button should be blue or not
    """
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    btnMessage = Column(String(255), nullable=False)
    blueBtn = Column(Boolean, default=False) 