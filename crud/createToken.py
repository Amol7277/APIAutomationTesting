import requests

baseurl = "https://restful-booker.herokuapp.com/auth"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url=baseurl, headers=headers, json=payload)
print(response.text)
print(response.status_code)