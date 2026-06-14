import pytest

def test_get_all_users(api_session,base_url):
    response = api_session.get(f"{base_url}/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 10

@pytest.mark.parametrize("user_id,expected_name",[
    (1,"Leanne Graham"),
    (2,"Ervin Howell"),
    (3,"Clementine Bauch"),
])
def test_get_user_by_id(api_session,base_url,user_id,expected_name):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == expected_name

def test_user_str(api_session,base_url):
    response = api_session.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    for key in ["id","name","username","email","address","phone","website","company"]:
        assert key in data,f"缺少字段:{key}"