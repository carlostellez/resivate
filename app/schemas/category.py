"""
Category schema module.

This module defines Pydantic models for Category data validation and serialization.
"""
from pydantic import BaseModel, Field, HttpUrl


class CategoryBase(BaseModel):
    """
    Base schema for Category data.
    
    Attributes:
        title: The title of the category
        link: The link associated with the category
    """
    title: str = Field(..., description="Category title", min_length=1, max_length=255)
    link: str = Field(..., description="Category link", min_length=1, max_length=512)


class CategoryCreate(CategoryBase):
    """
    Schema for creating a new Category.
    
    Inherits all fields from CategoryBase.
    """
    pass


class CategoryUpdate(CategoryBase):
    """
    Schema for updating an existing Category.
    
    Inherits all fields from CategoryBase but makes them optional.
    """
    title: str | None = Field(None, description="Category title", min_length=1, max_length=255)
    link: str | None = Field(None, description="Category link", min_length=1, max_length=512)


class CategoryInDBBase(CategoryBase):
    """
    Schema for Category data as stored in the database.
    
    Attributes:
        id: The unique identifier of the category
    """
    id: int = Field(..., description="Category ID")

    class Config:
        """Configuration for the CategoryInDBBase schema."""
        from_attributes = True


class Category(CategoryInDBBase):
    """
    Schema for Category data used in responses.
    
    Inherits all fields from CategoryInDBBase.
    """
    pass 