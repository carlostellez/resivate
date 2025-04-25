"""
ProcessingInfo model module.

This module defines the ProcessingInfo model used to store processing information in the database.
"""
from sqlalchemy import Column, Integer, String, Text

from app.database.base import Base


class ProcessingInfo(Base):
    """
    ProcessingInfo database model.
    
    Attributes:
        id: The unique identifier
        title: The title of the processing information
        description: Detailed description of the processing
        pricing: Pricing information as a string
    """
    __tablename__ = "processing_info"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    pricing = Column(String(100), nullable=True) 