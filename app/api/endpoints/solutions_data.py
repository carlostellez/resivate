"""
SolutionsData API endpoints.

This module provides API endpoints for managing solutions data.
"""
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.crud.solutions_data import solutions_data
from app.models.solutions_data import SolutionsData
from app.schemas.solutions_data import (
    SolutionsDataCreate,
    SolutionsDataList,
    SolutionsDataSchema,
    SolutionsDataUpdate,
)

router = APIRouter()


@router.get("/", response_model=SolutionsDataList)
def read_solutions_data_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve all solutions data items.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of solutions data items
    """
    items = solutions_data.get_multi(db, skip=skip, limit=limit)
    return {"items": items, "count": len(items)}


@router.post("/", response_model=SolutionsDataSchema, status_code=status.HTTP_201_CREATED)
def create_solutions_data(
    *,
    db: Session = Depends(get_db),
    item_in: SolutionsDataCreate,
) -> Any:
    """
    Create a new solutions data item.
    
    Args:
        db: Database session
        item_in: SolutionsData information to create
        
    Returns:
        Created solutions data item
    """
    return solutions_data.create(db=db, obj_in=item_in)


@router.get("/{item_id}", response_model=SolutionsDataSchema)
def read_solutions_data(
    *,
    db: Session = Depends(get_db),
    item_id: int,
) -> Any:
    """
    Get a specific solutions data item by ID.
    
    Args:
        db: Database session
        item_id: ID of the solutions data item to retrieve
        
    Returns:
        The requested solutions data item
        
    Raises:
        HTTPException: If solutions data item not found
    """
    item = solutions_data.get_with_image(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solutions data not found",
        )
    return item


@router.put("/{item_id}", response_model=SolutionsDataSchema)
def update_solutions_data(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    item_in: SolutionsDataUpdate,
) -> Any:
    """
    Update a solutions data item.
    
    Args:
        db: Database session
        item_id: ID of the solutions data item to update
        item_in: Updated solutions data information
        
    Returns:
        Updated solutions data item
        
    Raises:
        HTTPException: If solutions data item not found
    """
    item = solutions_data.get(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solutions data not found",
        )
    return solutions_data.update(db=db, db_obj=item, obj_in=item_in)


@router.delete("/{item_id}", response_model=SolutionsDataSchema)
def delete_solutions_data(
    *,
    db: Session = Depends(get_db),
    item_id: int,
) -> Any:
    """
    Delete a solutions data item.
    
    Args:
        db: Database session
        item_id: ID of the solutions data item to delete
        
    Returns:
        Deleted solutions data item
        
    Raises:
        HTTPException: If solutions data item not found
    """
    item = solutions_data.get(db=db, id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solutions data not found",
        )
    return solutions_data.remove(db=db, id=item_id) 