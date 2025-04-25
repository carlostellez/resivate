"""
FAQ schema module.

This module defines Pydantic models for FAQ data validation and serialization.
"""
from pydantic import BaseModel, Field


class FAQBase(BaseModel):
    """
    Base schema for FAQ data.
    
    Attributes:
        question: The question text
        answer: The answer text
    """
    question: str = Field(..., description="FAQ question", min_length=1, max_length=255)
    answer: str = Field(..., description="FAQ answer", min_length=1)


class FAQCreate(FAQBase):
    """
    Schema for creating a new FAQ.
    
    Inherits all fields from FAQBase.
    """
    pass


class FAQUpdate(FAQBase):
    """
    Schema for updating an existing FAQ.
    
    Inherits all fields from FAQBase but makes them optional.
    """
    question: str | None = Field(None, description="FAQ question", min_length=1, max_length=255)
    answer: str | None = Field(None, description="FAQ answer", min_length=1)


class FAQInDBBase(FAQBase):
    """
    Schema for FAQ data as stored in the database.
    
    Attributes:
        id: The unique identifier of the FAQ
    """
    id: int = Field(..., description="FAQ ID")

    class Config:
        """Configuration for the FAQInDBBase schema."""
        from_attributes = True


class FAQ(FAQInDBBase):
    """
    Schema for FAQ data used in responses.
    
    Inherits all fields from FAQInDBBase.
    """
    pass 