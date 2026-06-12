import requests
import pytest
#======================测试单篇文章接口=====================
def test_get_single_post():
    response = requests.get("http://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()
    assert isinstance(data,dict)

    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

    assert data["id"] == 1
    assert data["userId"] == 1
#================================测试全部文章接口=======================================
def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,list)
    assert len(data) == 100

    first_post = data[0]
    assert first_post["id"] == 1
    assert "title" in first_post
#================================测试创建文章接口===========================================
def test_create_post():
    new_post = {
        "title":"pytest 接口测试练习",
        "body": "这是通过 requests 库创建的测试内容",
        "userId":1 
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "pytest 接口测试练习"
    assert data["body"] == "这是通过 requests 库创建的测试内容"
    assert data["userId"] == 1
    assert data["id"] == 101
#=========================================测试异常情况======================================
def test_get_nonexistent_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
    assert response.status_code in [200,404]
