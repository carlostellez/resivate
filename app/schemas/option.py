"""
Option schema module.

This module defines Pydantic models for Option data validation and serialization.
"""
from pydantic import BaseModel, Field


class OptionBase(BaseModel):
    """
    Base schema for Option data.
    
    Attributes:
        name: The name of the option
        icon: The icon associated with the option
    """
    name: str = Field(..., description="Option name", min_length=1, max_length=255)
    icon: str = Field(..., description="Option icon", min_length=1, max_length=255)


class OptionCreate(OptionBase):
    """
    Schema for creating a new Option.
    
    Inherits all fields from OptionBase.
    """
    pass


class OptionUpdate(BaseModel):
    """
    Schema for updating an existing Option.
    
    Makes all fields from OptionBase optional.
    """
    name: str | None = Field(None, description="Option name", min_length=1, max_length=255)
    icon: str | None = Field(None, description="Option icon", min_length=1, max_length=255)


class OptionInDBBase(OptionBase):
    """
    Schema for Option data as stored in the database.
    
    Attributes:
        id: The unique identifier of the option
    """
    id: int = Field(..., description="Option ID")

    class Config:
        """Configuration for the OptionInDBBase schema."""
        from_attributes = True
        populate_by_name = True


class Option(OptionInDBBase):
    """
    Schema for Option data used in responses.
    
    Inherits all fields from OptionInDBBase.
    """
    pass 