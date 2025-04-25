"""
Image model module.

This module defines the Image model used to store image data in the database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Image(Base):
    """
    Image database model.
    
    Attributes:
        id: The unique identifier of the image
        src: The source URL or path of the image
    """
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    src = Column(String(512), nullable=False)
    
    # Relationships
    types = relationship("Type", back_populates="image") 