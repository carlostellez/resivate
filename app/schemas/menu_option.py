"""
MenuOption schema module.

This module defines Pydantic models for MenuOption data validation and serialization.
"""
from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field, field_validator


class MenuOptionBase(BaseModel):
    """
    Base schema for MenuOption data.
    
    Attributes:
        type: The type of menu option
        items: An array of items for the menu option
    """
    type: str = Field(..., description="Menu option type", min_length=1, max_length=255)
    items: List[Union[str, Dict[str, Any]]] = Field(..., description="Menu option items array")
    
    @field_validator('items')
    @classmethod
    def validate_items(cls, v):
        """Validate items and ensure it's a list."""
        if v is None:
            return []
        return v


class MenuOptionCreate(MenuOptionBase):
    """
    Schema for creating a new MenuOption.
    
    Inherits all fields from MenuOptionBase.
    """
    pass


class MenuOptionUpdate(BaseModel):
    """
    Schema for updating an existing MenuOption.
    
    Makes all fields from MenuOptionBase optional.
    """
    type: str | None = Field(None, description="Menu option type", min_length=1, max_length=255)
    items: List[Union[str, Dict[str, Any]]] | None = Field(None, description="Menu option items array")
    
    @field_validator('items')
    @classmethod
    def validate_items(cls, v):
        """Validate items and ensure it's a list or None."""
        if v is None:
            return None
        return v


class MenuOptionInDBBase(MenuOptionBase):
    """
    Schema for MenuOption data as stored in the database.
    
    Attributes:
        id: The unique identifier of the menu option
    """
    id: int = Field(..., description="Menu option ID")

    class Config:
        """Configuration for the MenuOptionInDBBase schema."""
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            # Custom encoders can be defined here if needed
        }


class MenuOption(MenuOptionInDBBase):
    """
    Schema for MenuOption data used in responses.
    
    Inherits all fields from MenuOptionInDBBase.
    """
    pass 