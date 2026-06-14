import pytest

def test_get_all_post(api_session,base_url):
    response = api_session.get(f"{base_url}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts,list)
    assert len(posts) == 100

@pytest.mark.parametrize("post_id",[1,2,3,10,50])
def test_get_single_post(api_session,base_url,post_id):
    response = api_session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_cre_post(api_session,base_url,sample_post):
    response = api_session.post(f"{base_url}/posts",json=sample_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == sample_post["title"]
    assert data["id"] == 101

def test_update_post(api_session,base_url,sample_post):
    sample_post["title"] = "【重构后更新】"
    response = api_session.put(f"{base_url}/posts/1",json=sample_post)
    assert response.status_code == 200
    assert response.json()["title"] == "【重构后更新】"

def test_del_post(api_session,base_url):
    response = api_session.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}

#=================================封装通用断言函数==========================

def assert_post_str(data):
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

def test_get_post_with_str_check(api_session,base_url):
    response = api_session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert_post_str(response.json())

#==========================数据驱动 + 通用断言=========================

@pytest.mark.parametrize("resoure,expected_id_fidle",[
    ("posts","id"),
    ("users","id"),
    ("todos","id"),
    ("comments","id"),
])
def test_res_have_id_field(api_session,base_url,resoure,expected_id_fidle):
    response = api_session.get(f"{base_url}/{resoure}/1")
    assert response.status_code == 200
    assert expected_id_fidle in response.json()

def test_acc_pro_end(auth_session):
    response = auth_session.get("https://httpbin.org/bearer")
    assert response.status_code == 200
    assert response.json()["token"] == "my_test_token_123"