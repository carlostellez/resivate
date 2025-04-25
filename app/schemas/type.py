"""
Type schema module.

This module defines Pydantic models for Type data validation and serialization.
"""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator

from app.schemas.image import Image


class TypeBase(BaseModel):
    """
    Base schema for Type with common attributes
    """
    title: str = Field(..., description="Title of the service type")
    description: Optional[str] = Field(None, description="Detailed description of the service type")
    features: Optional[List[str]] = Field(None, description="List of features offered by this service type")
    img_id: Optional[int] = Field(None, description="ID of the associated image")


class TypeCreate(TypeBase):
    """
    Schema for creating a new Type
    """
    pass


class TypeUpdate(BaseModel):
    """
    Schema for updating an existing Type
    """
    title: Optional[str] = Field(None, description="Title of the service type")
    description: Optional[str] = Field(None, description="Detailed description of the service type")
    features: Optional[List[str]] = Field(None, description="List of features offered by this service type")
    img_id: Optional[int] = Field(None, description="ID of the associated image")


class TypeInDBBase(TypeBase):
    """
    Schema for Type as stored in the database
    """
    id: int = Field(..., description="Unique identifier")

    class Config:
        orm_mode = True


class TypeSchema(TypeInDBBase):
    """
    Schema for Type returned by the API
    """
    pass


class TypeInDB(TypeInDBBase):
    """
    Schema for Type including all database fields
    """
    pass


class TypeList(BaseModel):
    """Schema for returning a list of service types"""
    types: List[TypeSchema]
    count: int 