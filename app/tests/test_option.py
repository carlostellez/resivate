"""
Tests for Option API endpoints.

This module contains tests for the Option API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_option(test_db):
    """Test creating a new option."""
    response = client.post(
        "/api/options/",
        json={"name": "Configuration", "icon": "settings"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Configuration"
    assert data["icon"] == "settings"
    assert "id" in data


def test_read_options(test_db):
    """Test reading all options."""
    # Create a test option first
    client.post(
        "/api/options/",
        json={"name": "Configuration", "icon": "settings"},
    )
    
    response = client.get("/api/options/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_read_option(test_db):
    """Test reading a specific option."""
    # Create a test option first
    response = client.post(
        "/api/options/",
        json={"name": "Configuration", "icon": "settings"},
    )
    assert response.status_code == 201
    option_id = response.json()["id"]
    
    response = client.get(f"/api/options/{option_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Configuration"
    assert data["icon"] == "settings"
    assert data["id"] == option_id


def test_update_option(test_db):
    """Test updating an option."""
    # Create a test option first
    response = client.post(
        "/api/options/",
        json={"name": "Configuration", "icon": "settings"},
    )
    assert response.status_code == 201
    option_id = response.json()["id"]
    
    response = client.put(
        f"/api/options/{option_id}",
        json={"name": "Advanced Settings", "icon": "advanced_settings"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Settings"
    assert data["icon"] == "advanced_settings"
    assert data["id"] == option_id


def test_delete_option(test_db):
    """Test deleting an option."""
    # Create a test option first
    response = client.post(
        "/api/options/",
        json={"name": "Configuration", "icon": "settings"},
    )
    assert response.status_code == 201
    option_id = response.json()["id"]
    
    response = client.delete(f"/api/options/{option_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/options/{option_id}")
    assert response.status_code == 404 