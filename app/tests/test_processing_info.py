"""
Tests for ProcessingInfo API endpoints.

This module contains tests for the ProcessingInfo API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_processing_info(test_db: Session):
    """Test creating a new processing information item."""
    response = client.post(
        "/api/processing-info/",
        json={
            "title": "Standard Processing",
            "description": "Our standard processing service",
            "pricing": "$99.99/month"
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Standard Processing"
    assert data["description"] == "Our standard processing service"
    assert data["pricing"] == "$99.99/month"
    assert "id" in data


def test_read_processing_infos(test_db: Session):
    """Test reading all processing information items."""
    # Create a test item first
    client.post(
        "/api/processing-info/",
        json={
            "title": "Express Processing",
            "description": "Our expedited processing service",
            "pricing": "$149.99/month"
        },
    )
    
    response = client.get("/api/processing-info/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "count" in data
    assert data["count"] >= 1
    assert len(data["items"]) >= 1


def test_read_processing_info(test_db: Session):
    """Test reading a specific processing information item."""
    # Create a test item first
    response = client.post(
        "/api/processing-info/",
        json={
            "title": "Premium Processing",
            "description": "Our premium processing service with extra features",
            "pricing": "$199.99/month"
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    response = client.get(f"/api/processing-info/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Premium Processing"
    assert data["description"] == "Our premium processing service with extra features"
    assert data["pricing"] == "$199.99/month"
    assert data["id"] == item_id


def test_update_processing_info(test_db: Session):
    """Test updating a processing information item."""
    # Create a test item first
    response = client.post(
        "/api/processing-info/",
        json={
            "title": "Basic Processing",
            "description": "Our basic processing service",
            "pricing": "$49.99/month"
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    response = client.put(
        f"/api/processing-info/{item_id}",
        json={
            "title": "Updated Basic Processing",
            "pricing": "$59.99/month"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Basic Processing"
    assert data["description"] == "Our basic processing service"  # Unchanged
    assert data["pricing"] == "$59.99/month"
    assert data["id"] == item_id


def test_delete_processing_info(test_db: Session):
    """Test deleting a processing information item."""
    # Create a test item first
    response = client.post(
        "/api/processing-info/",
        json={
            "title": "Temporary Processing",
            "description": "Processing service to be deleted",
            "pricing": "$29.99/month"
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/processing-info/{item_id}")
    assert response.status_code == 200
    
    # Verify it was deleted
    response = client.get(f"/api/processing-info/{item_id}")
    assert response.status_code == 404 