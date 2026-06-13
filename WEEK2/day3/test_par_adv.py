import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

#=====================参数化：批量测试不同用户的文章=======================

@pytest.mark.parametrize("user_id,expected_count",[
    (1,10),
    (2,10),
    (3,10),
    (10,10),
])
def test_post_by_user_id(user_id,expected_count):
    response = requests.get(
        f"{BASE_URL}/posts",
        params={"userId":user_id}
    )
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts,list)
    assert len(posts) == expected_count

#========================参数化:组合不同的查询条件========================

@pytest.mark.parametrize("resource,resource_id,expcted_key",[
    ("posts",1,"title"),
    ("users",1,"name"),
    ("todos",1,"completed"),
    ("comments",1,"email"),
])
def test_get_resource_by_id(resource,resource_id,expcted_key):
    response = requests.get(f"{BASE_URL}/{resource}/{resource_id}")
    assert response.status_code == 200
    data = response.json()
    assert expcted_key in data

#=========================参数化 POST:批量创建不同内容=======================

@pytest.mark.parametrize("title,body,user_id,expected_status",[
    ("测试1","正文1",1,201),
    ("测试2","正文2",2,201),
    ("","",1,201),
    ("长标题"*20,"长正文"*50,5,201),
])
def test_cre_post_with_car_data(title,body,user_id,expected_status):
    new_post = {"title":title,"body":body,"userId":user_id}
    response = requests.post(f"{BASE_URL}/posts",json=new_post)
    assert response.status_code == expected_status
    data = response.json()
    assert data["title"] == title
    assert data["body"] == body

#============================参数化:异常情况测试==========================

@pytest.mark.parametrize("invalid_id",[
    -1,
    0,
    9999999,
    "abc",
])
def test_get_post_with_invalid_id(invalid_id):
    response = requests.get(f"{BASE_URL}/posts/{invalid_id}")
    assert response.status_code in [200,404,500]

