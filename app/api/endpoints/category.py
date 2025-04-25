"""
Category API endpoints.

This module provides API endpoints for managing categories.
"""
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.category import Category as CategoryModel
from app.schemas.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter()


@router.get("/", response_model=List[Category])
def read_categories(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[CategoryModel]:
    """
    Retrieve all categories.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of categories
    """
    return db.query(CategoryModel).offset(skip).limit(limit).all()


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(
    *,
    db: DB,
    category_in: CategoryCreate,
) -> CategoryModel:
    """
    Create a new category.
    
    Args:
        db: Database session
        category_in: Category data to create
        
    Returns:
        Created category
    """
    category = CategoryModel(title=category_in.title, link=category_in.link)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.get("/{category_id}", response_model=Category)
def read_category(
    *,
    db: DB,
    category_id: int,
) -> CategoryModel:
    """
    Get a specific category by ID.
    
    Args:
        db: Database session
        category_id: ID of the category to retrieve
        
    Returns:
        Category with the specified ID
        
    Raises:
        HTTPException: If category not found
    """
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category


@router.put("/{category_id}", response_model=Category)
def update_category(
    *,
    db: DB,
    category_id: int,
    category_in: CategoryUpdate,
) -> CategoryModel:
    """
    Update a category.
    
    Args:
        db: Database session
        category_id: ID of the category to update
        category_in: New category data
        
    Returns:
        Updated category
        
    Raises:
        HTTPException: If category not found
    """
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    
    update_data = category_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)
    
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    *,
    db: DB,
    category_id: int,
) -> None:
    """
    Delete a category.
    
    Args:
        db: Database session
        category_id: ID of the category to delete
        
    Raises:
        HTTPException: If category not found
    """
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    
    db.delete(category)
    db.commit() 