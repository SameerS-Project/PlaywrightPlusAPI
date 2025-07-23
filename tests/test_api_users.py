import pytest
import requests


BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert all("email" in user for user in data["data"])



@pytest.mark.skip(reason="Reqres returns 401 Unauthorized on POST requests.")
@pytest.mark.api
def test_create_user():
    payload = {
        "name": "Sameer",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Sameer"
    assert data["job"] == "QA Automation Engineer"




@pytest.mark.skip(reason="Reqres returns 401 Unauthorized on PUT requests.")
@pytest.mark.api
def test_update_user():
    payload = {
        "name": "Sameer Updated",
        "job": "Lead QA Engineer"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == "Sameer Updated"
    assert response_data["job"] == "Lead QA Engineer"


@pytest.mark.skip(reason="Reqres returns 401 Unauthorized on PUT requests.")
@pytest.mark.api
def test_delete_user():
    headers = {"Content-Type": "application/json"}
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
