"""
ProcessingInfo schema module.

This module defines Pydantic models for ProcessingInfo data validation and serialization.
"""
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class ProcessingInfoBase(BaseModel):
    """
    Base schema for ProcessingInfo with common attributes
    """
    title: str = Field(..., description="Title of the processing information")
    description: Optional[str] = Field(None, description="Detailed description of the processing")
    pricing: Optional[str] = Field(None, description="Pricing information")


class ProcessingInfoCreate(ProcessingInfoBase):
    """
    Schema for creating a new ProcessingInfo
    """
    pass


class ProcessingInfoUpdate(BaseModel):
    """
    Schema for updating an existing ProcessingInfo
    """
    title: Optional[str] = Field(None, description="Title of the processing information")
    description: Optional[str] = Field(None, description="Detailed description of the processing")
    pricing: Optional[str] = Field(None, description="Pricing information")


class ProcessingInfoInDBBase(ProcessingInfoBase):
    """
    Schema for ProcessingInfo as stored in the database
    """
    id: int = Field(..., description="Unique identifier")
    model_config = ConfigDict(from_attributes=True)


class ProcessingInfoSchema(ProcessingInfoInDBBase):
    """
    Schema for ProcessingInfo returned by the API
    """
    pass


class ProcessingInfoInDB(ProcessingInfoInDBBase):
    """
    Schema for ProcessingInfo including all database fields
    """
    pass


class ProcessingInfoList(BaseModel):
    """Schema for returning a list of processing information items"""
    items: List[ProcessingInfoSchema]
    count: int 