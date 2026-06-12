import requests
import pytest

#=================================FIxtrue:公用的基础 URL====================================
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_post():
    """一份标准的新文章数据，给 POST 和 PUT 复用"""
    return{
        "title":"pytest 接口测试教程",
        "body":"这是通过 requests 库进行的接口自动化测试练习",
        "userId":1
    }

#========================================GET：获取数据========================================

def test_get_all_posts():
    """GET /posts 获取全部文章"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts,list)
    assert len(posts) == 100

@pytest.mark.parametrize("post_id",[1,2,3,10,50])
def test_get_single_post(post_id):
    """参数化:GET /posts/{id} 获取不同文章"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id

#=========================================PUT: 更新数据===========================================

def test_update_post(sample_post):
    """PUT /post/1 更新已有文章"""
    sample_post["title"] = "[已更新]测试驱动开发"
    
    response = requests.put(f"{BASE_URL}/posts/1",json=sample_post)
    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "[已更新]测试驱动开发"
    assert data["body"] == sample_post["body"]

    assert data["id"] == 1

def test_update_none_post():
    """PUT /posts/99999 更新不存在的文章(边界值)"""
    fake_post = {
        "id":99999,
        "title":"假数据",
        "body":"无意义",
        "userId": 99
    }
    response = requests.put(f"{BASE_URL}/posts/99999",json=fake_post)

    assert response.status_code == 500


#===============================DELETE:删除数据=========================================================

def test_del_post():
    """DELETE /posts/1 删除文章"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}

@pytest.mark.parametrize("post_id",[1,5,10,99])
def test_del_multiple_posts(post_id):
    """参数化:DELETE 不同 ID 的文章"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

#===============================异常场景==============================================================

def test_get_post_with_inva_id():
    """GET 请求使用非数字 ID (应返回 404 或忽略)"""
    response = requests.get(f"{BASE_URL}/posts/abc")
    assert response.status_code == 404

def test_create_post_with_empty_body():
    """POST 发送空数据(边界值)"""
    response = requests.post(f"{BASE_URL}/posts",json={})
    assert response.status_code in [201,400]
