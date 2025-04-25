"""
Plan schema module.

This module defines Pydantic models for Plan data validation and serialization.
"""
from pydantic import BaseModel, Field, field_validator


class PlanBase(BaseModel):
    """
    Base schema for Plan data.
    
    Attributes:
        title: The title of the plan (limited to 100 characters)
        description: The detailed description of the plan
        price: The price of the plan with 2 decimal places
        btnMessage: The text to display on the plan's button
        blueBtn: Whether the button should be blue or not
    """
    title: str = Field(..., description="Plan title", min_length=1, max_length=100)
    description: str = Field(..., description="Plan description", min_length=1)
    price: float = Field(..., description="Plan price", ge=0)
    btnMessage: str = Field(..., description="Button message text", min_length=1, max_length=255)
    blueBtn: bool = Field(False, description="Whether the button should be blue")

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        """Validate price to ensure it has at most 2 decimal places."""
        if v != round(v, 2):
            raise ValueError('Price must have at most 2 decimal places')
        return v


class PlanCreate(PlanBase):
    """
    Schema for creating a new Plan.
    
    Inherits all fields from PlanBase.
    """
    pass


class PlanUpdate(BaseModel):
    """
    Schema for updating an existing Plan.
    
    Makes all fields from PlanBase optional.
    """
    title: str | None = Field(None, description="Plan title", min_length=1, max_length=100)
    description: str | None = Field(None, description="Plan description", min_length=1)
    price: float | None = Field(None, description="Plan price", ge=0)
    btnMessage: str | None = Field(None, description="Button message text", min_length=1, max_length=255)
    blueBtn: bool | None = Field(None, description="Whether the button should be blue")

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        """Validate price to ensure it has at most 2 decimal places."""
        if v is not None and v != round(v, 2):
            raise ValueError('Price must have at most 2 decimal places')
        return v


class PlanInDBBase(PlanBase):
    """
    Schema for Plan data as stored in the database.
    
    Attributes:
        id: The unique identifier of the plan
    """
    id: int = Field(..., description="Plan ID")

    class Config:
        """Configuration for the PlanInDBBase schema."""
        from_attributes = True
        populate_by_name = True


class Plan(PlanInDBBase):
    """
    Schema for Plan data used in responses.
    
    Inherits all fields from PlanInDBBase.
    """
    pass 