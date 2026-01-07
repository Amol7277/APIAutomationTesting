import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import createTokenPayload

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

@pytest.fixture(scope="session")
def create_token():
    create_token_response = api_contant().getToken(
        url=requestsURLs().createToken(),
        headers=Utils().headers_CreateToken(),
        payload=createTokenPayload
    )
    assert create_token_response.status_code == 200

    return create_token_response.json()["token"]