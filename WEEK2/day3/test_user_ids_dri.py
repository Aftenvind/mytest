import requests
import pytest
import json
import os

BASE_URL = "http://jsonplaceholder.typicode.com"

def load_user_ids():
    file_path = os.path.join(os.path.dirname(__file__),"test_user_ids.json")
    with open(file_path,"r") as f:
        return json.load(f)
    
@pytest.fixture(params=load_user_ids())
def user_id(request):
    return request.param

def test_get_post_by_user_id(user_id):
    response = requests.get(f"{BASE_URL}/posts/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id