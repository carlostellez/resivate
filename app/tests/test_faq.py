"""
Tests for FAQ API endpoints.

This module contains tests for the FAQ API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_category import client, override_get_db, test_db  # reuse test setup


def test_create_faq(test_db):
    """Test creating a new FAQ."""
    response = client.post(
        "/api/faqs/",
        json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework for building APIs with Python."},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["question"] == "What is FastAPI?"
    assert data["answer"] == "FastAPI is a modern web framework for building APIs with Python."
    assert "id" in data


def test_read_faqs(test_db):
    """Test reading all FAQs."""
    # Create a test FAQ first
    response = client.post(
        "/api/faqs/",
        json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework for building APIs with Python."},
    )
    assert response.status_code == 201
    
    response = client.get("/api/faqs/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["question"] == "What is FastAPI?"


def test_read_faq(test_db):
    """Test reading a specific FAQ."""
    # Create a test FAQ first
    response = client.post(
        "/api/faqs/",
        json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework for building APIs with Python."},
    )
    assert response.status_code == 201
    faq_id = response.json()["id"]
    
    response = client.get(f"/api/faqs/{faq_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What is FastAPI?"
    assert data["id"] == faq_id


def test_update_faq(test_db):
    """Test updating a FAQ."""
    # Create a test FAQ first
    response = client.post(
        "/api/faqs/",
        json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework for building APIs with Python."},
    )
    assert response.status_code == 201
    faq_id = response.json()["id"]
    
    response = client.put(
        f"/api/faqs/{faq_id}",
        json={"question": "What is FastAPI framework?", "answer": "FastAPI is a high-performance web framework for building APIs with Python."},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What is FastAPI framework?"
    assert data["answer"] == "FastAPI is a high-performance web framework for building APIs with Python."
    assert data["id"] == faq_id


def test_delete_faq(test_db):
    """Test deleting a FAQ."""
    # Create a test FAQ first
    response = client.post(
        "/api/faqs/",
        json={"question": "What is FastAPI?", "answer": "FastAPI is a modern web framework for building APIs with Python."},
    )
    assert response.status_code == 201
    faq_id = response.json()["id"]
    
    response = client.delete(f"/api/faqs/{faq_id}")
    assert response.status_code == 204
    
    # Verify it was deleted
    response = client.get(f"/api/faqs/{faq_id}")
    assert response.status_code == 404 