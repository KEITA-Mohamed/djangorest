import requests
from getpass import getpass


endpoint = "http://127.0.0.1:8000/api/auth"
username = input('Entrez votre username:\n')
password = getpass("Entrez votre password:\n")
auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print(auth_response.json())
print(auth_response.status_code)

if auth_response.status_code == 200:

    endpoint = "http://127.0.0.1:8000/product/create/"
    headers = {
        'Authorization': 'Bearer 13c8846670f60021601cfce9f61423aef3e18bca'
    }

    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)