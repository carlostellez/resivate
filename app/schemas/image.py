"""
Image schema module.

This module defines Pydantic models for Image data validation and serialization.
"""
from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    """
    Base schema for Image data.
    
    Attributes:
        src: The source URL or path of the image
    """
    src: str = Field(..., description="Image source URL or path", min_length=1, max_length=512)


class ImageCreate(ImageBase):
    """
    Schema for creating a new Image.
    
    Inherits all fields from ImageBase.
    """
    pass


class ImageUpdate(ImageBase):
    """
    Schema for updating an existing Image.
    
    Inherits all fields from ImageBase but makes them optional.
    """
    src: str | None = Field(None, description="Image source URL or path", min_length=1, max_length=512)


class ImageInDBBase(ImageBase):
    """
    Schema for Image data as stored in the database.
    
    Attributes:
        id: The unique identifier of the image
    """
    id: int = Field(..., description="Image ID")

    class Config:
        """Configuration for the ImageInDBBase schema."""
        from_attributes = True


class Image(ImageInDBBase):
    """
    Schema for Image data used in responses.
    
    Inherits all fields from ImageInDBBase.
    """
    pass 