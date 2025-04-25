"""
Configuration module for the application.

This module contains settings for database connections, API settings, and other configurations.
"""
import os
from typing import Any, Dict, Optional

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.
    
    This class handles all configuration parameters for the application,
    including database connection settings, API settings, and other
    environment-specific configurations.
    """
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Resivate API"
    
    # Database configuration
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "C4nc3rb3r0**")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "resivate_db")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    DATABASE_URL: str = ""
    
    def __init__(self, **data: Any):
        super().__init__(**data)
        self.DATABASE_URL = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings() 
