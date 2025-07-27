import requests

endpoint = "http://127.0.0.1:8000/product/"
response = requests.post(endpoint, json={'name': 'Pasteque', 'content': 'just pasteque', 'price':20})
print(response.json())
print(response.status_code)