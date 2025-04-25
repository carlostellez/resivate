"""
Option API endpoints.

This module provides API endpoints for managing options.
"""
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.option import Option as OptionModel
from app.schemas.option import Option, OptionCreate, OptionUpdate

router = APIRouter()


@router.get("/", response_model=List[Option])
def read_options(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """
    Retrieve all options.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of options
    """
    options = db.query(OptionModel).offset(skip).limit(limit).all()
    return [
        {
            "id": option.id, 
            "name": option.name, 
            "icon": option.icon
        } 
        for option in options
    ]


@router.post("/", response_model=Option, status_code=status.HTTP_201_CREATED)
def create_option(
    *,
    db: DB,
    option_in: OptionCreate,
) -> Dict[str, Any]:
    """
    Create a new option.
    
    Args:
        db: Database session
        option_in: Option data to create
        
    Returns:
        Created option
    """
    option = OptionModel(
        name=option_in.name,
        icon=option_in.icon
    )
    db.add(option)
    db.commit()
    db.refresh(option)
    
    return {
        "id": option.id,
        "name": option.name,
        "icon": option.icon
    }


@router.get("/{option_id}", response_model=Option)
def read_option(
    *,
    db: DB,
    option_id: int,
) -> Dict[str, Any]:
    """
    Get a specific option by ID.
    
    Args:
        db: Database session
        option_id: ID of the option to retrieve
        
    Returns:
        Option with the specified ID
        
    Raises:
        HTTPException: If option not found
    """
    option = db.query(OptionModel).filter(OptionModel.id == option_id).first()
    if not option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Option not found",
        )
    
    return {
        "id": option.id,
        "name": option.name,
        "icon": option.icon
    }


@router.put("/{option_id}", response_model=Option)
def update_option(
    *,
    db: DB,
    option_id: int,
    option_in: OptionUpdate,
) -> Dict[str, Any]:
    """
    Update an option.
    
    Args:
        db: Database session
        option_id: ID of the option to update
        option_in: New option data
        
    Returns:
        Updated option
        
    Raises:
        HTTPException: If option not found
    """
    option = db.query(OptionModel).filter(OptionModel.id == option_id).first()
    if not option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Option not found",
        )
    
    if option_in.name is not None:
        option.name = option_in.name
    if option_in.icon is not None:
        option.icon = option_in.icon
    
    db.add(option)
    db.commit()
    db.refresh(option)
    
    return {
        "id": option.id,
        "name": option.name,
        "icon": option.icon
    }


@router.delete("/{option_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_option(
    *,
    db: DB,
    option_id: int,
) -> None:
    """
    Delete an option.
    
    Args:
        db: Database session
        option_id: ID of the option to delete
        
    Raises:
        HTTPException: If option not found
    """
    option = db.query(OptionModel).filter(OptionModel.id == option_id).first()
    if not option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Option not found",
        )
    
    db.delete(option)
    db.commit() 