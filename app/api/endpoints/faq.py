"""
FAQ API endpoints.

This module provides API endpoints for managing FAQs (Frequently Asked Questions).
"""
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.faq import FAQ as FAQModel
from app.schemas.faq import FAQ, FAQCreate, FAQUpdate

router = APIRouter()


@router.get("/", response_model=List[FAQ])
def read_faqs(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[FAQModel]:
    """
    Retrieve all FAQs.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of FAQs
    """
    return db.query(FAQModel).offset(skip).limit(limit).all()


@router.post("/", response_model=FAQ, status_code=status.HTTP_201_CREATED)
def create_faq(
    *,
    db: DB,
    faq_in: FAQCreate,
) -> FAQModel:
    """
    Create a new FAQ.
    
    Args:
        db: Database session
        faq_in: FAQ data to create
        
    Returns:
        Created FAQ
    """
    faq = FAQModel(question=faq_in.question, answer=faq_in.answer)
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq


@router.get("/{faq_id}", response_model=FAQ)
def read_faq(
    *,
    db: DB,
    faq_id: int,
) -> FAQModel:
    """
    Get a specific FAQ by ID.
    
    Args:
        db: Database session
        faq_id: ID of the FAQ to retrieve
        
    Returns:
        FAQ with the specified ID
        
    Raises:
        HTTPException: If FAQ not found
    """
    faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found",
        )
    return faq


@router.put("/{faq_id}", response_model=FAQ)
def update_faq(
    *,
    db: DB,
    faq_id: int,
    faq_in: FAQUpdate,
) -> FAQModel:
    """
    Update a FAQ.
    
    Args:
        db: Database session
        faq_id: ID of the FAQ to update
        faq_in: New FAQ data
        
    Returns:
        Updated FAQ
        
    Raises:
        HTTPException: If FAQ not found
    """
    faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found",
        )
    
    update_data = faq_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(faq, field, value)
    
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq


@router.delete("/{faq_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(
    *,
    db: DB,
    faq_id: int,
) -> None:
    """
    Delete a FAQ.
    
    Args:
        db: Database session
        faq_id: ID of the FAQ to delete
        
    Raises:
        HTTPException: If FAQ not found
    """
    faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found",
        )
    
    db.delete(faq)
    db.commit() 