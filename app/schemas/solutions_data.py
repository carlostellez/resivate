"""
SolutionsData schema module.

This module defines Pydantic models for SolutionsData validation and serialization.
"""
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict

from app.schemas.image import Image


class SolutionsDataBase(BaseModel):
    """
    Base schema for SolutionsData with common attributes
    """
    title: str = Field(..., description="Title of the solution")
    pricing: Optional[str] = Field(None, description="Pricing information")
    img_id: Optional[int] = Field(None, description="ID of the associated image")


class SolutionsDataCreate(SolutionsDataBase):
    """
    Schema for creating a new SolutionsData entry
    """
    pass


class SolutionsDataUpdate(BaseModel):
    """
    Schema for updating an existing SolutionsData entry
    """
    title: Optional[str] = Field(None, description="Title of the solution")
    pricing: Optional[str] = Field(None, description="Pricing information")
    img_id: Optional[int] = Field(None, description="ID of the associated image")


class SolutionsDataInDBBase(SolutionsDataBase):
    """
    Schema for SolutionsData as stored in the database
    """
    id: int = Field(..., description="Unique identifier")
    model_config = ConfigDict(from_attributes=True)


class SolutionsDataSchema(SolutionsDataInDBBase):
    """
    Schema for SolutionsData returned by the API
    """
    img: Optional[Image] = Field(None, description="Associated image object")


class SolutionsDataInDB(SolutionsDataInDBBase):
    """
    Schema for SolutionsData including all database fields
    """
    pass


class SolutionsDataList(BaseModel):
    """Schema for returning a list of solutions data items"""
    items: List[SolutionsDataSchema]
    count: int 