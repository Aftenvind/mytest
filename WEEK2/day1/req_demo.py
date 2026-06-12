import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("状态码:",response.status_code)

print("\n原始响应(前200字符:)")
print(response.text[:200])

data = response.json()
print("\n解析后的数据类型L:",type(data))
print("\n文章标题:",data["title"])
print("文章ID:",data["id"])
print("用户id:",data["userId"])