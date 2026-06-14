import requests
import pytest

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_session():
    session = requests.Session()
    session.headers.update({
        "Content-type":"application/json",
        "ACcept":"application/json",
    })
    yield session
    session.close()

@pytest.fixture
def sample_post():
    return{
        "title":"封装后的测试文章",
        "body":"通过 fixture 共享的数据",
        "userId":1
    }

@pytest.fixture(scope="module")
def auth_headers():
    return {"Authorization":"Bearer my_test_token_123"}

@pytest.fixture(scope="module")
def auth_session(auth_headers):
    session = requests.Session()
    session.headers.update(auth_headers)
    yield session
    session.close()