import requests
import pytest
import json
import os

BASE_URL = "http://jsonplaceholder.typicode.com"

def load_test_data():
    file_path = os.path.join(os.path.dirname(__file__),"test_data.json")
    with open(file_path,"r",encoding="utf-8") as f:
        data = json.load(f)
    return data["test_cases"]

@pytest.fixture(params=load_test_data())
def test_case(request):
    return request.param

def test_create_post_from_json(test_case):
    response = requests.post(
        f"{BASE_URL}/posts",
        json=test_case["payload"]
    )

    assert response.status_code == test_case["expected_status"], \
        f"用例「{test_case['name']}」状态码不符"
    
    data = response.json()
    assert data["title"] == test_case["expected_title"], \
        f"用例「{test_case['name']}」标题不符"
    
    print(f"√ 用例通过:{test_case['name']}")