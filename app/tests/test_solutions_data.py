"""
Tests for SolutionsData API endpoints.

This module contains tests for the SolutionsData API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_solutions_data(test_db: Session):
    """Test creating a new solutions data item."""
    # First create an image to reference
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/solution1.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    response = client.post(
        "/api/solutions-data/",
        json={
            "title": "Enterprise Solution",
            "pricing": "$199.99/month",
            "img_id": image_id
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Enterprise Solution"
    assert data["pricing"] == "$199.99/month"
    assert data["img_id"] == image_id
    assert "id" in data


def test_read_solutions_data_items(test_db: Session):
    """Test reading all solutions data items."""
    # Create a test item first
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/solution2.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    client.post(
        "/api/solutions-data/",
        json={
            "title": "Small Business Solution",
            "pricing": "$99.99/month",
            "img_id": image_id
        },
    )
    
    response = client.get("/api/solutions-data/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "count" in data
    assert data["count"] >= 1
    assert len(data["items"]) >= 1


def test_read_solutions_data(test_db: Session):
    """Test reading a specific solutions data item."""
    # Create a test item first
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/solution3.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    response = client.post(
        "/api/solutions-data/",
        json={
            "title": "Premium Solution",
            "pricing": "$299.99/month",
            "img_id": image_id
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    response = client.get(f"/api/solutions-data/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Premium Solution"
    assert data["pricing"] == "$299.99/month"
    assert data["img_id"] == image_id
    assert data["id"] == item_id


def test_update_solutions_data(test_db: Session):
    """Test updating a solutions data item."""
    # Create a test item first
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/solution4.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    response = client.post(
        "/api/solutions-data/",
        json={
            "title": "Basic Solution",
            "pricing": "$49.99/month",
            "img_id": image_id
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    response = client.put(
        f"/api/solutions-data/{item_id}",
        json={
            "title": "Updated Basic Solution",
            "pricing": "$59.99/month"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Basic Solution"
    assert data["pricing"] == "$59.99/month"
    assert data["img_id"] == image_id
    assert data["id"] == item_id


def test_delete_solutions_data(test_db: Session):
    """Test deleting a solutions data item."""
    # Create a test item first
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/solution5.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    response = client.post(
        "/api/solutions-data/",
        json={
            "title": "Temporary Solution",
            "pricing": "$29.99/month",
            "img_id": image_id
        },
    )
    assert response.status_code == 201
    item_id = response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/solutions-data/{item_id}")
    assert response.status_code == 200
    
    # Verify it was deleted
    response = client.get(f"/api/solutions-data/{item_id}")
    assert response.status_code == 404 