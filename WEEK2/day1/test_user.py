import requests
import pytest

def test_get_all_users():
    response = requests.get("http://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users,list)
    assert len(users) == 10

def test_get_single_user():
    response = requests.get("http://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == "Leanne Graham"
    assert user["username"] == "Bret"
    assert user["email"] == "Sincere@april.biz"

def test_filer_by_username():
    respone = requests.get(
        "http://jsonplaceholder.typicode.com/users",
        params={"username": "Bret"}
    )
    assert respone.status_code == 200
    users = respone.json()
    assert len(users) == 1
    assert users[0]["name"] == "Leanne Graham"
    assert users[0]["username"] == "Bret"
