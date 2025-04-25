"""
Tests for Image API endpoints.

This module contains tests for the Image API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_image(test_db):
    """Test creating a new image."""
    response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["src"] == "https://example.com/image.jpg"
    assert "id" in data


def test_read_images(test_db):
    """Test reading all images."""
    # Create a test image first
    response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"},
    )
    assert response.status_code == 201
    
    response = client.get("/api/images/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["src"] == "https://example.com/image.jpg"


def test_read_image(test_db):
    """Test reading a specific image."""
    # Create a test image first
    response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"},
    )
    assert response.status_code == 201
    image_id = response.json()["id"]
    
    response = client.get(f"/api/images/{image_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["src"] == "https://example.com/image.jpg"
    assert data["id"] == image_id


def test_update_image(test_db):
    """Test updating an image."""
    # Create a test image first
    response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"},
    )
    assert response.status_code == 201
    image_id = response.json()["id"]
    
    response = client.put(
        f"/api/images/{image_id}",
        json={"src": "https://example.com/updated-image.jpg"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["src"] == "https://example.com/updated-image.jpg"
    assert data["id"] == image_id


def test_delete_image(test_db):
    """Test deleting an image."""
    # Create a test image first
    response = client.post(
        "/api/images/",
        json={"src": "https://example.com/image.jpg"},
    )
    assert response.status_code == 201
    image_id = response.json()["id"]
    
    response = client.delete(f"/api/images/{image_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/images/{image_id}")
    assert response.status_code == 404 