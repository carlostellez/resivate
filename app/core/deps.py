"""
Dependencies module.

This module provides dependency injection functionality for the FastAPI application.
"""
from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Get database session dependency.
    
    Creates a new database session and ensures it's closed after use.
    
    Yields:
        SQLAlchemy Session object
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Type annotation for database dependency
DB = Annotated[Session, Depends(get_db)] 