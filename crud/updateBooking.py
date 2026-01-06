import requests

Tokenbaseurl = "https://restful-booker.herokuapp.com/auth"

headers = {
    "Content-Type": "application/json"
    # "Accept": "application/json"
}

payload = {
    "username": "admin",
    "password": "password123"
}

responseToken = requests.post(url=Tokenbaseurl, headers=headers, json=payload)
print(responseToken.text)
print(responseToken.status_code)
responseToken.json()
token = responseToken.json()["token"]
# print(token)

baseurl = "https://restful-booker.herokuapp.com/booking/2021"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={token}"
}

# auth = {
#     "username": "admin",
#     "password": "password123"
# }

payload = {
    "firstname": "Amol",
    "lastname": "QA",
    "totalprice": 250,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

response = requests.put(url=baseurl, headers=headers, json = payload)

print(response.text)
print(response.status_code)
assert response.status_code == 200
