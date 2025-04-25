"""
Type model module.

This module defines the Type model used to store type data in the database.
"""
import json
from typing import Any, List

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Type(Base):
    """
    Model for service types.
    
    Attributes:
        id: Unique identifier
        title: Title of the service type
        description: Detailed description of the service type
        features: List of features offered by this service type
        img_id: ID of the associated image
    """
    
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    _features = Column("features", Text, nullable=True)
    img_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    
    # Relationships
    image = relationship("Image", back_populates="types")

    @hybrid_property
    def features(self) -> List[str]:
        """
        Get the features as a Python list.
        
        Returns:
            List of features
        """
        try:
            return json.loads(self._features)
        except (TypeError, json.JSONDecodeError):
            return []

    @features.setter
    def features(self, features: List[str]) -> None:
        """
        Set the features, converting from a Python list to a JSON string.
        
        Args:
            features: List of features to store
        """
        if features is None:
            self._features = json.dumps([])
        else:
            self._features = json.dumps(features)
            
    def __getattribute__(self, name):
        """
        Custom attribute getter to handle special serialization of hybrid properties.
        
        Args:
            name: Name of the attribute to get
        
        Returns:
            Attribute value
        """
        # Special handling for features attribute to ensure it's always properly serialized
        if name == 'features':
            try:
                return json.loads(object.__getattribute__(self, '_features'))
            except (AttributeError, TypeError, json.JSONDecodeError):
                # Safely handle error cases
                return []
        return object.__getattribute__(self, name) 