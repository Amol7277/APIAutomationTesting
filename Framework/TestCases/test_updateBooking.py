import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import createTokenPayload, updateBookingPayload

def test_updateBooking(create_token):

    updateResponse = api_contant().updateBooking(
        url=requestsURLs().updateBooking(bookingID=2120),
        headers=Utils().headers_updateBooking(create_token),
        payload=updateBookingPayload
    )
    print(updateResponse.url)
    print(updateResponse.text)
    # print(updateResponse.headers)
    assert  updateResponse.status_code == 200

