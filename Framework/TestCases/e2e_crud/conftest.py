import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import *

BASE_URL = "https://restful-booker.herokuapp.com"

# @pytest.fixture(scope="session")
# def auth_token():
#     url = f"{BASE_URL}/auth"
#     payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 200
#
#     return response.json()["token"]

# @pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def create_token():
    create_token_response = api_contant().getToken(
        url=requestsURLs().createToken(),
        headers=Utils().headers_CreateToken(),
        payload=createTokenPayload
    )
    print("Created Token = ",create_token_response.json()["token"])
    assert create_token_response.status_code == 200

    return create_token_response.json()["token"]

@pytest.fixture(scope="session")
def test_createBooking():
    createBookingResponse = api_contant().createBooking(
        url=requestsURLs().createBooking(),
        headers=Utils().headers_createBooking(),
        payload=createBookingPayload
    )
    print("Created Booking StatusCode ", createBookingResponse.status_code)
    print("Created BookingDetails is ", createBookingResponse.text)
    bookingID = createBookingResponse.json()["bookingid"]
    assert createBookingResponse.status_code == 200
    return bookingID