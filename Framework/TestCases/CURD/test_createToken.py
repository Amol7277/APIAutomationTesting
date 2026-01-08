import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import createTokenPayload


def test_CreateToekn():
    response = api_contant().getToken(
        url= requestsURLs().createToken(),
        headers= Utils().headers_CreateToken(),
        payload= createTokenPayload
    )
    print(response.status_code)
    assert response.status_code == 200
