import pytest
from conftest import assert_user_structure

class TestUsers:
    def test_get_all_user(self,api_session,base_url):
        response = api_session.get(f"{base_url}/users")
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 10
    
    @pytest.mark.parametrize("user_id,expcted_name",[
        (1,"Leanne Graham"),
        (2,"Ervin Howell"),
        (3,"Clementine Bauch"),
    ])
    def test_get_user_byid(self,api_session,base_url,user_id,expcted_name):
        response = api_session.get(f"{base_url}/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == expcted_name
    
    def test_user_str(self,api_session,base_url):
        response = api_session.get(f"{base_url}/users/1")
        assert response.status_code == 200
        assert_user_structure(response.json())

    def test_filter_user_byusername(self,api_session,base_url):
        response = api_session.get(f"{base_url}/users",params={"username":"Bret"})
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 1
        assert users[0]["name"] == "Leanne Graham"
        