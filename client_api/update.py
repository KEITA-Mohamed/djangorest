import requests

endpoint = "http://127.0.0.1:8000/product/7/update"
response = requests.put(endpoint, json={'name': 'Orange300', 'content': '', 'price':1000})
print(response.json())
print(response.status_code)