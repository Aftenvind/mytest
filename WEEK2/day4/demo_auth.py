import requests

response = requests.get("http://reqres.in/api/users/2")
print("状态码",response.status_code)
print("返回数据",response.json())