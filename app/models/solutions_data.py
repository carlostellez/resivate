"""
SolutionsData model module.

This module defines the SolutionsData model used to store solution data in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class SolutionsData(Base):
    """
    SolutionsData database model.
    
    Attributes:
        id: The unique identifier
        title: The title of the solution
        img_id: ID of the associated image
        pricing: Pricing information as a string
    """
    __tablename__ = "solutions_data"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    img_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    pricing = Column(String(100), nullable=True)
    
    # Relationships
    image = relationship("Image", foreign_keys=[img_id]) 