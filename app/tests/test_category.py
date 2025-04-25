"""
Tests for Category API endpoints.

This module contains tests for the Category API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.core.deps import get_db
from app.main import app
from app.models.category import Category

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency to use test database
def override_get_db():
    """
    Override the get_db dependency for testing.
    
    Returns:
        Database session for testing
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def test_db():
    """
    Create test database tables and remove them after test.
    
    Yields:
        Test database session
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_create_category(test_db):
    """Test creating a new category."""
    response = client.post(
        "/api/categories/",
        json={"title": "Test Category", "link": "https://example.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Category"
    assert data["link"] == "https://example.com"
    assert "id" in data


def test_read_categories(test_db):
    """Test reading all categories."""
    # Create a test category first
    response = client.post(
        "/api/categories/",
        json={"title": "Test Category", "link": "https://example.com"},
    )
    assert response.status_code == 201
    
    response = client.get("/api/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == "Test Category"


def test_read_category(test_db):
    """Test reading a specific category."""
    # Create a test category first
    response = client.post(
        "/api/categories/",
        json={"title": "Test Category", "link": "https://example.com"},
    )
    assert response.status_code == 201
    category_id = response.json()["id"]
    
    response = client.get(f"/api/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Category"
    assert data["id"] == category_id


def test_update_category(test_db):
    """Test updating a category."""
    # Create a test category first
    response = client.post(
        "/api/categories/",
        json={"title": "Test Category", "link": "https://example.com"},
    )
    assert response.status_code == 201
    category_id = response.json()["id"]
    
    response = client.put(
        f"/api/categories/{category_id}",
        json={"title": "Updated Category", "link": "https://updated.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Category"
    assert data["link"] == "https://updated.com"
    assert data["id"] == category_id


def test_delete_category(test_db):
    """Test deleting a category."""
    # Create a test category first
    response = client.post(
        "/api/categories/",
        json={"title": "Test Category", "link": "https://example.com"},
    )
    assert response.status_code == 201
    category_id = response.json()["id"]
    
    response = client.delete(f"/api/categories/{category_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/categories/{category_id}")
    assert response.status_code == 404 