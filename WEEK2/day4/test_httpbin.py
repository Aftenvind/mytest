import requests
import pytest

BASE_URL = "https://httpbin.org"


def test_access_with_valid_token():
    """带正确 Token 访问受保护资源，应返回 200"""
    headers = {"Authorization": "Bearer my_secret_token_123"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)

    assert response.status_code == 200
    data = response.json()
    # httpbin 会把你的 token 原样返回
    assert data["token"] == "my_secret_token_123"
    print("✓ 有效 Token 访问成功")


def test_access_without_token():
    """不带 Token 访问，应返回 401"""
    response = requests.get(f"{BASE_URL}/bearer")
    assert response.status_code == 401
    print("✓ 无 Token 被正确拒绝，状态码 401")


def test_access_with_invalid_token():
    """带错误 Token 访问（对 httpbin 来说，任何 Token 都有效，但真实业务会拒绝）
       这里我们仍然验证带 Token 即可，同时提醒你真实业务的不同。"""
    headers = {"Authorization": "Bearer fake_token"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)
    # httpbin 接受任何 Bearer Token，所以返回 200
    assert response.status_code == 200
    print("提示：httpbin 接受任何 Token，但真实业务会验证有效性并可能返回 401")