import requests

endpoint = "http://127.0.0.1:8000/product/create/"
response = requests.post(endpoint, json={'name': 'orange400', 'content': 'toto', 'price':300})
print(response.json())
print(response.status_code)