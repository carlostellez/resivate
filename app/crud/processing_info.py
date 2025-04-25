"""
CRUD operations for ProcessingInfo.

This module provides database operations for ProcessingInfo model.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.processing_info import ProcessingInfo
from app.schemas.processing_info import ProcessingInfoCreate, ProcessingInfoUpdate


class CRUDProcessingInfo(CRUDBase[ProcessingInfo, ProcessingInfoCreate, ProcessingInfoUpdate]):
    """
    CRUD operations for ProcessingInfo
    """
    
    def get_by_title(self, db: Session, *, title: str) -> Optional[ProcessingInfo]:
        """
        Get ProcessingInfo by title
        
        Args:
            db: Database session
            title: Title to search for
            
        Returns:
            ProcessingInfo object if found, None otherwise
        """
        return db.query(self.model).filter(self.model.title == title).first()
    
    def get_multi_by_pricing(self, db: Session, *, pricing: str, skip: int = 0, limit: int = 100) -> List[ProcessingInfo]:
        """
        Get ProcessingInfo items by pricing
        
        Args:
            db: Database session
            pricing: Pricing to filter by
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of ProcessingInfo objects matching the pricing
        """
        return db.query(self.model).filter(self.model.pricing == pricing).offset(skip).limit(limit).all()


processing_info = CRUDProcessingInfo(ProcessingInfo) 