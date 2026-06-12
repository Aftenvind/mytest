import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_todos():
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos,list)
    assert len(todos) == 200

@pytest.mark.parametrize("todo_id",[1,2,3])
def test_get_single_todos(todo_id):
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id
    assert "completed" in data

def test_cre_doto():
    new_todo = {
        "title":"完成接口测试练习",
        "completed":False,
        "userId":1
    }
    response = requests.post(f"{BASE_URL}/todos",json=new_todo)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 201
    assert data["title"] == "完成接口测试练习"

def test_update_todo():
    updated = {
        "title":"delete aut autem",
        "completed":True,
        "userId":1
    }
    response = requests.put(f"{BASE_URL}/todos/1",json=updated)
    assert response.status_code == 200
    assert response.json()["completed"] is True

def test_del_todo():
    response = requests.delete(f"{BASE_URL}/todos/1")
    assert response.status_code == 200
    assert response.json() == {}
