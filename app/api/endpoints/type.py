"""
Type API endpoints.

This module provides API endpoints for managing types.
"""
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.type import Type as TypeModel
from app.schemas.type import TypeSchema, TypeCreate, TypeUpdate

router = APIRouter()


@router.get("/", response_model=List[TypeSchema])
def read_types(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """
    Retrieve all types.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of types
    """
    types = db.query(TypeModel).offset(skip).limit(limit).all()
    return [
        {
            "id": type_item.id,
            "title": type_item.title,
            "description": type_item.description,
            "features": type_item.features,
            "img_id": type_item.img_id,
            "img": type_item.image
        } 
        for type_item in types
    ]


@router.post("/", response_model=TypeSchema, status_code=status.HTTP_201_CREATED)
def create_type(
    *,
    db: DB,
    type_in: TypeCreate,
) -> Dict[str, Any]:
    """
    Create a new type.
    
    Args:
        db: Database session
        type_in: Type data to create
        
    Returns:
        Created type
    """
    type_obj = TypeModel(
        title=type_in.title,
        description=type_in.description,
        features=type_in.features,
        img_id=type_in.img_id
    )
    db.add(type_obj)
    db.commit()
    db.refresh(type_obj)
    
    return {
        "id": type_obj.id,
        "title": type_obj.title,
        "description": type_obj.description,
        "features": type_obj.features,
        "img_id": type_obj.img_id,
        "img": type_obj.image
    }


@router.get("/{type_id}", response_model=TypeSchema)
def read_type(
    *,
    db: DB,
    type_id: int,
) -> Dict[str, Any]:
    """
    Get a specific type by ID.
    
    Args:
        db: Database session
        type_id: ID of the type to retrieve
        
    Returns:
        Type with the specified ID
        
    Raises:
        HTTPException: If type not found
    """
    type_obj = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not type_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Type not found",
        )
    
    return {
        "id": type_obj.id,
        "title": type_obj.title,
        "description": type_obj.description,
        "features": type_obj.features,
        "img_id": type_obj.img_id,
        "img": type_obj.image
    }


@router.put("/{type_id}", response_model=TypeSchema)
def update_type(
    *,
    db: DB,
    type_id: int,
    type_in: TypeUpdate,
) -> Dict[str, Any]:
    """
    Update a type.
    
    Args:
        db: Database session
        type_id: ID of the type to update
        type_in: New type data
        
    Returns:
        Updated type
        
    Raises:
        HTTPException: If type not found
    """
    type_obj = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not type_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Type not found",
        )
    
    if type_in.title is not None:
        type_obj.title = type_in.title
    if type_in.description is not None:
        type_obj.description = type_in.description
    if type_in.features is not None:
        type_obj.features = type_in.features
    if type_in.img_id is not None:
        type_obj.img_id = type_in.img_id
    
    db.add(type_obj)
    db.commit()
    db.refresh(type_obj)
    
    return {
        "id": type_obj.id,
        "title": type_obj.title,
        "description": type_obj.description,
        "features": type_obj.features,
        "img_id": type_obj.img_id,
        "img": type_obj.image
    }


@router.delete("/{type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_type(
    *,
    db: DB,
    type_id: int,
) -> None:
    """
    Delete a type.
    
    Args:
        db: Database session
        type_id: ID of the type to delete
        
    Raises:
        HTTPException: If type not found
    """
    type_obj = db.query(TypeModel).filter(TypeModel.id == type_id).first()
    if not type_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Type not found",
        )
    
    db.delete(type_obj)
    db.commit() 