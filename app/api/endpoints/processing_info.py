"""
ProcessingInfo API endpoints.

This module provides API endpoints for managing processing information.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.crud.processing_info import processing_info
from app.models.processing_info import ProcessingInfo
from app.schemas.processing_info import (
    ProcessingInfoCreate,
    ProcessingInfoList,
    ProcessingInfoSchema,
    ProcessingInfoUpdate,
)

router = APIRouter()


@router.get("/", response_model=ProcessingInfoList)
def read_processing_infos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve all processing information items.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of processing information items
    """
    items = processing_info.get_multi(db, skip=skip, limit=limit)
    return {"items": items, "count": len(items)}


@router.post("/", response_model=ProcessingInfoSchema, status_code=status.HTTP_201_CREATED)
def create_processing_info(
    *,
    db: Session = Depends(get_db),
    item_in: ProcessingInfoCreate,
) -> Any:
    """
    Create a new processing information item.
    
    Args:
        db: Database session
        item_in: ProcessingInfo data to create
        
    Returns:
        Created processing information item
    """
    return processing_info.create(db=db, obj_in=item_in)


@router.get("/{item_id}", response_model=ProcessingInfoSchema)
def read_processing_info(
    *,
    db: Session = Depends(get_db),
    item_id: int,
) -> Any:
    """
    Get a specific processing information item by ID.
    
    Args:
        db: Database session
        item_id: ID of the processing information item to retrieve
        
    Returns:
        The requested processing information item
        
    Raises:
        HTTPException: If processing information item not found
    """
    item = processing_info.get(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processing information not found",
        )
    return item


@router.put("/{item_id}", response_model=ProcessingInfoSchema)
def update_processing_info(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    item_in: ProcessingInfoUpdate,
) -> Any:
    """
    Update a processing information item.
    
    Args:
        db: Database session
        item_id: ID of the processing information item to update
        item_in: Updated processing information data
        
    Returns:
        Updated processing information item
        
    Raises:
        HTTPException: If processing information item not found
    """
    item = processing_info.get(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processing information not found",
        )
    return processing_info.update(db=db, db_obj=item, obj_in=item_in)


@router.delete("/{item_id}", response_model=ProcessingInfoSchema)
def delete_processing_info(
    *,
    db: Session = Depends(get_db),
    item_id: int,
) -> Any:
    """
    Delete a processing information item.
    
    Args:
        db: Database session
        item_id: ID of the processing information item to delete
        
    Returns:
        Deleted processing information item
        
    Raises:
        HTTPException: If processing information item not found
    """
    item = processing_info.get(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processing information not found",
        )
    return processing_info.remove(db=db, id=item_id) 