import requests
#=========================PUT 请求：更新一篇文章====================================
print("=== PUT请求:更新文章 ===")

update_post = {
    "id":1,
    "title":"更新后的标题 - pytest 接口测试",
    "body":"这是更新胡的正文内容",
    "userId": 1
}

response = requests.put(
    "http://jsonplaceholder.typicode.com/posts/1",
    json=update_post
)

print("状态码",response.status_code)
print("返回数据:")
data = response.json()
print(data)

#===========================DELETE 请求：删除一篇文章=========================================

print("\n=== DELETE 请求：删除文章 ===")

response = requests.delete("http://jsonplaceholder.typicode.com/posts/1")

print("状态码:",response.status_code)
print("返回数据:",response.text)

assert response.status_code == 200
print("√ DELETE 请求通过")