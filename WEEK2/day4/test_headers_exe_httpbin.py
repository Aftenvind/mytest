import requests

def test_path_with_custom_header():
    headers = {
        "X-Custom-Header":"MyTestValue"
    }

    response = requests.patch(
        "https://httpbin.org/patch",
        json={"title":"更新后的标题"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["headers"]["X-Custom-Header"] == "MyTestValue"
    print("√ 自定义 Header 验证通过")