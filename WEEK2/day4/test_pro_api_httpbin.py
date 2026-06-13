import requests
import pytest

BASE_URL = "https://httpbin.org"

@pytest.fixture
def auth_token():
    return "my_test_token_from_login"

def test_acc_with_fixtrue_token(auth_token):
    headers = {"Authorization":f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/bearer",headers=headers)

    assert response.status_code == 200
    assert response.json()["token"] == auth_token

def test_custom_header_in_request():
    headers = {
        "X-Custom-Header":"MyTestValue",
        "Authorization":"Bearer some_token"
    }
    response = requests.get(f"{BASE_URL}/headers",headers=headers)

    assert response.status_code == 200
    received_headers = response.json()["headers"]
    assert received_headers["X-Custom-Header"] == "MyTestValue"
    assert received_headers["Authorization"] == "Bearer some_token"
    print("√ 自定义 Header 验证通过")

