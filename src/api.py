import requests

BASE_URL = "http://jsonplaceholder.typicode.com"

def fetch_users():
    """Fetches all users from the API."""
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return response.json()

def fetch_todos():
    """Fetches all todos from the API."""
    response = requests.get(f"{BASE_URL}/todos")
    response.raise_for_status()
    return response.json()
