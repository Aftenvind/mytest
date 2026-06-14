# conftest.py —— 第二周综合实战项目，共享 fixture
import requests
import pytest

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def api_session():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    yield session
    session.close()


@pytest.fixture
def sample_post():
    """标准文章测试数据"""
    return {
        "title": "综合实战测试文章",
        "body": "这是自动化测试生成的内容",
        "userId": 1
    }


@pytest.fixture
def sample_todo():
    """标准待办测试数据"""
    return {
        "title": "完成接口自动化测试",
        "completed": False,
        "userId": 1
    }


# 通用断言函数
def assert_post_structure(data):
    """验证文章对象必须包含的字段"""
    required = ["id", "title", "body", "userId"]
    for key in required:
        assert key in data, f"缺少字段：{key}"


def assert_user_structure(data):
    """验证用户对象必须包含的字段"""
    required = ["id", "name", "username", "email", "address", "phone", "website", "company"]
    for key in required:
        assert key in data, f"缺少字段：{key}"


def assert_todo_structure(data):
    """验证待办对象必须包含的字段"""
    required = ["id", "title", "completed", "userId"]
    for key in required:
        assert key in data, f"缺少字段：{key}"