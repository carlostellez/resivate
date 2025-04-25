from typing import List, Optional, Dict, Any

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.type import Type
from app.schemas.type import TypeCreate, TypeUpdate


class CRUDType(CRUDBase[Type, TypeCreate, TypeUpdate]):
    """
    CRUD operations for Type
    """
    
    def get_by_title(self, db: Session, *, title: str) -> Optional[Type]:
        """
        Get Type by title
        
        Args:
            db: Database session
            title: Title to search for
            
        Returns:
            Type object if found, None otherwise
        """
        return db.query(self.model).filter(self.model.title == title).first()
    
    def create_with_features(
        self, db: Session, *, obj_in: TypeCreate
    ) -> Type:
        """
        Create a new Type with features list
        
        Args:
            db: Database session
            obj_in: Type creation data including features
            
        Returns:
            Created Type object
        """
        db_obj = self.model(
            title=obj_in.title,
            description=obj_in.description,
            features=obj_in.features,
            img_id=obj_in.img_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(
        self, db: Session, *, db_obj: Type, obj_in: TypeUpdate
    ) -> Type:
        """
        Update Type object
        
        Args:
            db: Database session
            db_obj: Existing Type object to update
            obj_in: Update data
            
        Returns:
            Updated Type object
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
            
        return super().update(db, db_obj=db_obj, obj_in=update_data)


type = CRUDType(Type) 