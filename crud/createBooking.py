import requests


baseURL = "https://restful-booker.herokuapp.com/booking"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "firstname": "Amol",
    "lastname": "QA",
    "totalprice": 199,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

response = requests.post(url=baseURL, headers=headers, json=payload)
print(response.status_code)
print(len(response.text))
print(response.text)
id = response.json()["bookingid"]
assert response.status_code == 200
assert response.json()["bookingid"] == id


# Deletebaseurl = "https://restful-booker.herokuapp.com/booking/1053"#+str(id)
# response = requests.delete(url=Deletebaseurl, headers=headers)
# print(response.status_code)