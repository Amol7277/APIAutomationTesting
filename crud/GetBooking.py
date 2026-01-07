import requests

baseurl = "https://restful-booker.herokuapp.com/booking/2000"

headers = {
    "Content-Type": "application/json"
}

response = requests.get(url=baseurl, headers=headers)
print(response.status_code)
print(len(response.text))
print(response.text)
assert response.status_code == 200
# assert response.json()["firstname"] == "Susan"
# assert response.json()["bookingdates"]["checkin"] == "2022-08-04"
