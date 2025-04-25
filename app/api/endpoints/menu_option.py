"""
MenuOption API endpoints.

This module provides API endpoints for managing menu options.
"""
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.menu_option import MenuOption as MenuOptionModel
from app.schemas.menu_option import MenuOption, MenuOptionCreate, MenuOptionUpdate

router = APIRouter()


@router.get("/", response_model=List[MenuOption])
def read_menu_options(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """
    Retrieve all menu options.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of menu options
    """
    menu_options = db.query(MenuOptionModel).offset(skip).limit(limit).all()
    # Return list of dictionaries to ensure proper JSON serialization
    return [
        {
            "id": option.id, 
            "type": option.type, 
            "items": option.items
        } 
        for option in menu_options
    ]


@router.post("/", response_model=MenuOption, status_code=status.HTTP_201_CREATED)
def create_menu_option(
    *,
    db: DB,
    menu_option_in: MenuOptionCreate,
) -> Dict[str, Any]:
    """
    Create a new menu option.
    
    Args:
        db: Database session
        menu_option_in: Menu option data to create
        
    Returns:
        Created menu option
    """
    menu_option = MenuOptionModel(
        type=menu_option_in.type,
        items=menu_option_in.items
    )
    db.add(menu_option)
    db.commit()
    db.refresh(menu_option)
    
    # Manual serialization to ensure proper JSON handling
    return {
        "id": menu_option.id,
        "type": menu_option.type,
        "items": menu_option.items
    }


@router.get("/{menu_option_id}", response_model=MenuOption)
def read_menu_option(
    *,
    db: DB,
    menu_option_id: int,
) -> Dict[str, Any]:
    """
    Get a specific menu option by ID.
    
    Args:
        db: Database session
        menu_option_id: ID of the menu option to retrieve
        
    Returns:
        Menu option with the specified ID
        
    Raises:
        HTTPException: If menu option not found
    """
    menu_option = db.query(MenuOptionModel).filter(MenuOptionModel.id == menu_option_id).first()
    if not menu_option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu option not found",
        )
    
    # Manual serialization to ensure proper JSON handling
    return {
        "id": menu_option.id,
        "type": menu_option.type,
        "items": menu_option.items
    }


@router.put("/{menu_option_id}", response_model=MenuOption)
def update_menu_option(
    *,
    db: DB,
    menu_option_id: int,
    menu_option_in: MenuOptionUpdate,
) -> Dict[str, Any]:
    """
    Update a menu option.
    
    Args:
        db: Database session
        menu_option_id: ID of the menu option to update
        menu_option_in: New menu option data
        
    Returns:
        Updated menu option
        
    Raises:
        HTTPException: If menu option not found
    """
    menu_option = db.query(MenuOptionModel).filter(MenuOptionModel.id == menu_option_id).first()
    if not menu_option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu option not found",
        )
    
    if menu_option_in.type is not None:
        menu_option.type = menu_option_in.type
    if menu_option_in.items is not None:
        menu_option.items = menu_option_in.items
    
    db.add(menu_option)
    db.commit()
    db.refresh(menu_option)
    
    # Manual serialization to ensure proper JSON handling
    return {
        "id": menu_option.id,
        "type": menu_option.type,
        "items": menu_option.items
    }


@router.delete("/{menu_option_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_option(
    *,
    db: DB,
    menu_option_id: int,
) -> None:
    """
    Delete a menu option.
    
    Args:
        db: Database session
        menu_option_id: ID of the menu option to delete
        
    Raises:
        HTTPException: If menu option not found
    """
    menu_option = db.query(MenuOptionModel).filter(MenuOptionModel.id == menu_option_id).first()
    if not menu_option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu option not found",
        )
    
    db.delete(menu_option)
    db.commit() 