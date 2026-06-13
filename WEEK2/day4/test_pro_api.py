import requests
import pytest

BASE_URL = "https://reqres.in/api"


@pytest.fixture
def auth_token():
    """Fixture：先登录获取 token，给后续测试用"""
    login_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 200
    return response.json()["token"]


def test_access_with_valid_token(auth_token):
    """带有效 Token 访问接口"""
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}/users", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    print("✓ 带 Token 访问成功")


def test_access_without_token():
    """不带 Token 访问（演示：Reqres 也允许，但真实业务应返回 401）"""
    response = requests.get(f"{BASE_URL}/users")
    # Reqres 不强制鉴权，所以返回 200
    # 真实业务中应断言 401
    assert response.status_code == 200
    print("提示：真实业务中，不带 Token 应返回 401 Unauthorized")


def test_access_with_invalid_token():
    """带伪造 Token 访问（真实业务应返回 401）"""
    headers = {"Authorization": "Bearer fake_token_12345"}
    response = requests.get(f"{BASE_URL}/users", headers=headers)
    # Reqres 不验证 token，真实业务应返回 401
    print("带假 Token 访问结果：", response.status_code)
    assert response.status_code in [200, 401]


def test_register_and_login():
    """完整流程：注册 → 登录 → 获取用户信息"""
    # 注册
    register_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    reg_response = requests.post(f"{BASE_URL}/register", json=register_data)
    assert reg_response.status_code == 200
    reg_token = reg_response.json()["token"]
    print("注册成功，Token：", reg_token)

    # 用注册返回的 token 访问用户列表
    headers = {"Authorization": f"Bearer {reg_token}"}
    user_response = requests.get(f"{BASE_URL}/users", headers=headers)
    assert user_response.status_code == 200
    print("✓ 完整鉴权流程通过")