"""
Tests for Type API endpoints.

This module contains tests for the Type API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_type(test_db):
    """Test creating a new type."""
    response = client.post(
        "/api/types/",
        json={
            "title": "Service Type",
            "description": "Description of service type",
            "features": ["Feature 1", "Feature 2", "Feature 3"]
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Service Type"
    assert data["description"] == "Description of service type"
    assert data["features"] == ["Feature 1", "Feature 2", "Feature 3"]
    assert data["img_id"] is None
    assert "id" in data


def test_create_type_with_image(test_db):
    """Test creating a type with image reference."""
    # First create an image to reference
    image_response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"}
    )
    assert image_response.status_code == 201
    image_id = image_response.json()["id"]
    
    # Now create a type that references this image
    response = client.post(
        "/api/types/",
        json={
            "title": "Service Type with Image",
            "description": "Description with image",
            "features": ["Feature 1", "Feature 2"],
            "img_id": image_id
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Service Type with Image"
    assert data["img_id"] == image_id
    assert data["img"] is not None
    assert "id" in data


def test_read_types(test_db):
    """Test reading all types."""
    # Create a test type first
    client.post(
        "/api/types/",
        json={
            "title": "Service Type",
            "description": "Description of service type",
            "features": ["Feature 1", "Feature 2", "Feature 3"]
        },
    )
    
    response = client.get("/api/types/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_read_type(test_db):
    """Test reading a specific type."""
    # Create a test type first
    response = client.post(
        "/api/types/",
        json={
            "title": "Service Type",
            "description": "Description of service type",
            "features": ["Feature 1", "Feature 2", "Feature 3"]
        },
    )
    assert response.status_code == 201
    type_id = response.json()["id"]
    
    response = client.get(f"/api/types/{type_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Service Type"
    assert data["description"] == "Description of service type"
    assert data["features"] == ["Feature 1", "Feature 2", "Feature 3"]
    assert data["id"] == type_id


def test_update_type(test_db):
    """Test updating a type."""
    # Create a test type first
    response = client.post(
        "/api/types/",
        json={
            "title": "Service Type",
            "description": "Description of service type",
            "features": ["Feature 1", "Feature 2", "Feature 3"]
        },
    )
    assert response.status_code == 201
    type_id = response.json()["id"]
    
    response = client.put(
        f"/api/types/{type_id}",
        json={
            "title": "Updated Service Type",
            "features": ["Feature 1", "Feature 2", "Feature 3", "Feature 4"]
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Service Type"
    assert data["description"] == "Description of service type"  # Unchanged
    assert data["features"] == ["Feature 1", "Feature 2", "Feature 3", "Feature 4"]
    assert data["id"] == type_id


def test_delete_type(test_db):
    """Test deleting a type."""
    # Create a test type first
    response = client.post(
        "/api/types/",
        json={
            "title": "Service Type",
            "description": "Description of service type",
            "features": ["Feature 1", "Feature 2", "Feature 3"]
        },
    )
    assert response.status_code == 201
    type_id = response.json()["id"]
    
    response = client.delete(f"/api/types/{type_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/types/{type_id}")
    assert response.status_code == 404 