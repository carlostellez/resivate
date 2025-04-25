"""
Tests for MenuOption API endpoints.

This module contains tests for the MenuOption API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_menu_option(test_db):
    """Test creating a new menu option."""
    response = client.post(
        "/api/menu-options/",
        json={"type": "main", "items": ["Home", "About", "Contact"]},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "main"
    assert data["items"] == ["Home", "About", "Contact"]
    assert "id" in data


def test_create_restaurant_menu_option(test_db):
    """Test creating a restaurant menu option."""
    response = client.post(
        "/api/menu-options/",
        json={"type": "Restaurants", "items": ["Coffee shops", "Full service"]},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "Restaurants"
    assert data["items"] == ["Coffee shops", "Full service"]
    assert "id" in data


def test_read_menu_options(test_db):
    """Test reading all menu options."""
    # Create a test menu option first
    client.post(
        "/api/menu-options/",
        json={"type": "main", "items": ["Home", "About", "Contact"]},
    )
    
    response = client.get("/api/menu-options/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_read_menu_option(test_db):
    """Test reading a specific menu option."""
    # Create a test menu option first
    response = client.post(
        "/api/menu-options/",
        json={"type": "main", "items": ["Home", "About", "Contact"]},
    )
    assert response.status_code == 201
    menu_option_id = response.json()["id"]
    
    response = client.get(f"/api/menu-options/{menu_option_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "main"
    assert data["items"] == ["Home", "About", "Contact"]
    assert data["id"] == menu_option_id


def test_update_menu_option(test_db):
    """Test updating a menu option."""
    # Create a test menu option first
    response = client.post(
        "/api/menu-options/",
        json={"type": "main", "items": ["Home", "About", "Contact"]},
    )
    assert response.status_code == 201
    menu_option_id = response.json()["id"]
    
    response = client.put(
        f"/api/menu-options/{menu_option_id}",
        json={"type": "footer", "items": ["Privacy", "Terms", "Contact"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "footer"
    assert data["items"] == ["Privacy", "Terms", "Contact"]
    assert data["id"] == menu_option_id


def test_delete_menu_option(test_db):
    """Test deleting a menu option."""
    # Create a test menu option first
    response = client.post(
        "/api/menu-options/",
        json={"type": "main", "items": ["Home", "About", "Contact"]},
    )
    assert response.status_code == 201
    menu_option_id = response.json()["id"]
    
    response = client.delete(f"/api/menu-options/{menu_option_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/menu-options/{menu_option_id}")
    assert response.status_code == 404


def test_complex_items(test_db):
    """Test menu option with complex items structure."""
    # Create a test menu option with complex nested structure
    complex_items = [
        {
            "name": "Products",
            "url": "/products",
            "children": [
                {"name": "Software", "url": "/products/software"},
                {"name": "Hardware", "url": "/products/hardware"}
            ]
        },
        {
            "name": "Services",
            "url": "/services"
        }
    ]
    
    response = client.post(
        "/api/menu-options/",
        json={"type": "complex", "items": complex_items},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "complex"
    assert data["items"] == complex_items
    assert "id" in data 