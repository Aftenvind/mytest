import pytest
from conftest import assert_todo_structure

class TrstTodos:
    def test_get_all_todos(self,api_session,base_url):
        response = api_session.get(f"{base_url}/todos")
        assert response.status_code == 200
        todos = response.json()
        assert len(todos) == 200

    @pytest.mark.parametrize("todo_id",[1,2,3])
    def test_get_single_todo(self,api_session,base_url,todo_id):
        response = api_session.get(f"{base_url}/todos/{todo_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == todo_id

    def test_cre_todo(self,api_session,base_url,sample_todo):
        response = api_session.post(f"{base_url}/todos",json=sample_todo)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_todo["title"]
        assert data["completed"] == sample_todo["completed"]
        assert data["id"] == 201

    def test_update_todo_com(self,api_session,base_url):
        payload = {"title":"delectus aut autem","completed":True,"userId":1}
        response = api_session.put(f"{base_url}/todos/1",json=payload)
        assert response.status_code == 200
        assert response.json()["completed"] is True

    def test_del_todo(self,api_session,base_url):
        response = api_session.delete(f"{base_url}/todos/1")
        assert response.status_code == 200
        assert response.json() == {}
        