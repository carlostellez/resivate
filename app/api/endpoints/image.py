"""
Image API endpoints.

This module provides API endpoints for managing images.
"""
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.image import Image as ImageModel
from app.schemas.image import Image, ImageCreate, ImageUpdate

router = APIRouter()


@router.get("/", response_model=List[Image])
def read_images(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[ImageModel]:
    """
    Retrieve all images.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of images
    """
    return db.query(ImageModel).offset(skip).limit(limit).all()


@router.post("/", response_model=Image, status_code=status.HTTP_201_CREATED)
def create_image(
    *,
    db: DB,
    image_in: ImageCreate,
) -> ImageModel:
    """
    Create a new image.
    
    Args:
        db: Database session
        image_in: Image data to create
        
    Returns:
        Created image
    """
    image = ImageModel(src=image_in.src)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image


@router.get("/{image_id}", response_model=Image)
def read_image(
    *,
    db: DB,
    image_id: int,
) -> ImageModel:
    """
    Get a specific image by ID.
    
    Args:
        db: Database session
        image_id: ID of the image to retrieve
        
    Returns:
        Image with the specified ID
        
    Raises:
        HTTPException: If image not found
    """
    image = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found",
        )
    return image


@router.put("/{image_id}", response_model=Image)
def update_image(
    *,
    db: DB,
    image_id: int,
    image_in: ImageUpdate,
) -> ImageModel:
    """
    Update an image.
    
    Args:
        db: Database session
        image_id: ID of the image to update
        image_in: New image data
        
    Returns:
        Updated image
        
    Raises:
        HTTPException: If image not found
    """
    image = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found",
        )
    
    update_data = image_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(image, field, value)
    
    db.add(image)
    db.commit()
    db.refresh(image)
    return image


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(
    *,
    db: DB,
    image_id: int,
) -> None:
    """
    Delete an image.
    
    Args:
        db: Database session
        image_id: ID of the image to delete
        
    Raises:
        HTTPException: If image not found
    """
    image = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found",
        )
    
    db.delete(image)
    db.commit() 