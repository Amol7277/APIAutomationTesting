import requests

TokenURL = "https://restful-booker.herokuapp.com/auth"

headers = {
    "Content-Type":"application/json"
}

payload = {
    "username": "admin",
    "password": "password123"
}

tokenResponse = requests.post(url=TokenURL, headers=headers, json= payload)
token = tokenResponse.json()["token"]


deleteURL = "https://restful-booker.herokuapp.com/booking/2513"

deleteheaders= {
    "Cookie": f"token={token}"
}

deleteResponse = requests.delete(url=deleteURL, headers=deleteheaders)
print(deleteResponse.status_code)
assert deleteResponse.status_code == 201


GetBookingURL = "https://restful-booker.herokuapp.com/booking/2513"
getResponse = requests.get(url=GetBookingURL, headers=headers)
assert getResponse.status_code == 404