import requests

def test_patch_with_custom_header():
    """PATCH 请求带自定义 headers"""
    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "MyTestValue"
    }
    update_data = {"title": "通过 PATCH 更新标题"}

    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=update_data,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["title"] == "通过 PATCH 更新标题"

    # 验证发出的请求确实带了自定义头
    sent_headers = response.request.headers
    assert sent_headers["X-Custom-Header"] == "MyTestValue"
    print("✓ 自定义头验证通过")
    print("实际发送的 headers：", dict(sent_headers))