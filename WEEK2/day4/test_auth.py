import requests
import pytest

BASE_URL = "http://reqres.in/api"

def test_login_success():
    login_data = {
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }
    response = requests.post(f"{BASE_URL}/login",json=login_data)

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    print("Token:",data["token"])

def test_login_fail_missing_password():
    login_data = {"email":"eve.holt@reqres.in"}
    response = requests.post(f"{BASE_URL}/login",json=login_data)

    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] == "Missing password"

def test_login_fail_user_not_found():
    login_data = {"email":"notexist@reqres.in","password":"123456"}
    response = requests.post(f"{BASE_URL}/login",json=login_data)

    assert response.status_code == 400
    assert response.json()["error"] == "user not found"