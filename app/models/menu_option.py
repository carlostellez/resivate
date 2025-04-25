"""
MenuOption model module.

This module defines the MenuOption model used to store menu options in the database.
"""
import json
from typing import Any, Dict, List

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.hybrid import hybrid_property

from app.database.base import Base


class MenuOption(Base):
    """
    MenuOption database model.
    
    Attributes:
        id: The unique identifier of the menu option
        type: The type of menu option
        items: An array of items for the menu option (stored as JSON)
    """
    __tablename__ = "menu_options"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), nullable=False, index=True)
    _items = Column("items", Text, nullable=False)

    @hybrid_property
    def items(self) -> List[Any]:
        """
        Get the items as a Python list.
        
        Returns:
            List of items
        """
        try:
            return json.loads(self._items)
        except (TypeError, json.JSONDecodeError):
            return []

    @items.setter
    def items(self, items: List[Any]) -> None:
        """
        Set the items, converting from a Python list to a JSON string.
        
        Args:
            items: List of items to store
        """
        if items is None:
            self._items = json.dumps([])
        else:
            self._items = json.dumps(items)
        
    def __getattribute__(self, name):
        """
        Custom attribute getter to handle special serialization of hybrid properties.
        
        Args:
            name: Name of the attribute to get
        
        Returns:
            Attribute value
        """
        # Special handling for items attribute to ensure it's always properly serialized
        if name == 'items':
            try:
                return json.loads(object.__getattribute__(self, '_items'))
            except (AttributeError, TypeError, json.JSONDecodeError):
                # Safely handle error cases
                return []
        return object.__getattribute__(self, name) 