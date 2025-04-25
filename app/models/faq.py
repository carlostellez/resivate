"""
FAQ model module.

This module defines the FAQ model used to store frequently asked questions in the database.
"""
from sqlalchemy import Column, Integer, String, Text

from app.database.base import Base


class FAQ(Base):
    """
    FAQ database model.
    
    Attributes:
        id: The unique identifier of the FAQ
        question: The question text
        answer: The answer text
    """
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(255), nullable=False, index=True)
    answer = Column(Text, nullable=False) 