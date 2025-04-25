"""
Restaurant Menu Options Example.

This script demonstrates how to create and retrieve restaurant menu options
using the API.
"""
import json
import requests

# Base URL for the API
BASE_URL = "http://localhost:8000/api"

def create_restaurant_menu():
    """Create a restaurant menu option."""
    url = f"{BASE_URL}/menu-options/"
    data = {
        "type": "Restaurants",
        "items": ["Coffee shops", "Full service"]
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print("Restaurant menu created successfully!")
        print(json.dumps(response.json(), indent=2))
        return response.json()["id"]
    else:
        print(f"Error creating restaurant menu: {response.status_code}")
        print(response.text)
        return None

def get_restaurant_menu(menu_id):
    """Get a specific restaurant menu option."""
    url = f"{BASE_URL}/menu-options/{menu_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Restaurant menu retrieved successfully!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error getting restaurant menu: {response.status_code}")
        print(response.text)

def get_all_menu_options():
    """Get all menu options."""
    url = f"{BASE_URL}/menu-options/"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("All menu options retrieved successfully!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error getting all menu options: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("Creating restaurant menu option...")
    menu_id = create_restaurant_menu()
    
    if menu_id:
        print("\nRetrieving the created restaurant menu option...")
        get_restaurant_menu(menu_id)
    
    print("\nRetrieving all menu options...")
    get_all_menu_options() 