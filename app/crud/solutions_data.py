"""
CRUD operations for SolutionsData.

This module provides database operations for SolutionsData model.
"""
from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.solutions_data import SolutionsData
from app.schemas.solutions_data import SolutionsDataCreate, SolutionsDataUpdate


class CRUDSolutionsData(CRUDBase[SolutionsData, SolutionsDataCreate, SolutionsDataUpdate]):
    """
    CRUD operations for SolutionsData
    """
    
    def get_by_title(self, db: Session, *, title: str) -> Optional[SolutionsData]:
        """
        Get SolutionsData by title
        
        Args:
            db: Database session
            title: Title to search for
            
        Returns:
            SolutionsData object if found, None otherwise
        """
        return db.query(self.model).filter(self.model.title == title).first()
    
    def get_multi_by_pricing(self, db: Session, *, pricing: str, skip: int = 0, limit: int = 100) -> List[SolutionsData]:
        """
        Get SolutionsData items by pricing
        
        Args:
            db: Database session
            pricing: Pricing to filter by
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of SolutionsData objects matching the pricing
        """
        return db.query(self.model).filter(self.model.pricing == pricing).offset(skip).limit(limit).all()
    
    def get_with_image(self, db: Session, *, id: int) -> Optional[SolutionsData]:
        """
        Get SolutionsData including the image relationship
        
        Args:
            db: Database session
            id: ID of the record to get
            
        Returns:
            SolutionsData object with loaded image if found, None otherwise
        """
        # Use joinedload to eagerly load the image relationship
        return db.query(self.model).options(joinedload(self.model.image)).filter(self.model.id == id).first()
    
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[SolutionsData]:
        """
        Get multiple SolutionsData records with images preloaded
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of SolutionsData objects with preloaded images
        """
        # Override base method to eager load image relationships
        return db.query(self.model).options(joinedload(self.model.image)).offset(skip).limit(limit).all()


solutions_data = CRUDSolutionsData(SolutionsData) 