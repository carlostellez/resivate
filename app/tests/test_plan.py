"""
Tests for Plan API endpoints.

This module contains tests for the Plan API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_plan(test_db):
    """Test creating a new plan."""
    response = client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan",
            "description": "Basic features for small businesses",
            "price": 19.99,
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Basic Plan"
    assert data["description"] == "Basic features for small businesses"
    assert data["price"] == 19.99
    assert data["btnMessage"] == "Get Started"
    assert data["blueBtn"] is True
    assert "id" in data


def test_read_plans(test_db):
    """Test reading all plans."""
    # Create a test plan first
    client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan",
            "description": "Basic features for small businesses",
            "price": 19.99,
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    
    response = client.get("/api/plans/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_read_plan(test_db):
    """Test reading a specific plan."""
    # Create a test plan first
    response = client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan",
            "description": "Basic features for small businesses",
            "price": 19.99,
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    assert response.status_code == 201
    plan_id = response.json()["id"]
    
    response = client.get(f"/api/plans/{plan_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Basic Plan"
    assert data["description"] == "Basic features for small businesses"
    assert data["price"] == 19.99
    assert data["btnMessage"] == "Get Started"
    assert data["blueBtn"] is True
    assert data["id"] == plan_id


def test_update_plan(test_db):
    """Test updating a plan."""
    # Create a test plan first
    response = client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan",
            "description": "Basic features for small businesses",
            "price": 19.99,
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    assert response.status_code == 201
    plan_id = response.json()["id"]
    
    response = client.put(
        f"/api/plans/{plan_id}",
        json={
            "title": "Premium Plan",
            "price": 29.99,
            "btnMessage": "Upgrade Now"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Premium Plan"
    assert data["description"] == "Basic features for small businesses"  # Unchanged
    assert data["price"] == 29.99
    assert data["btnMessage"] == "Upgrade Now"
    assert data["blueBtn"] is True  # Unchanged
    assert data["id"] == plan_id


def test_price_validation(test_db):
    """Test price validation for plans."""
    # Try to create with invalid price (more than 2 decimal places)
    response = client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan",
            "description": "Basic features for small businesses",
            "price": 19.999,  # Invalid: more than 2 decimal places
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    assert response.status_code == 422  # Unprocessable Entity


def test_delete_plan(test_db):
    """Test deleting a plan."""
    # Create a test plan first
    response = client.post(
        "/api/plans/",
        json={
            "title": "Basic Plan", 
            "description": "Basic features for small businesses",
            "price": 19.99,
            "btnMessage": "Get Started",
            "blueBtn": True
        },
    )
    assert response.status_code == 201
    plan_id = response.json()["id"]
    
    response = client.delete(f"/api/plans/{plan_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/plans/{plan_id}")
    assert response.status_code == 404 