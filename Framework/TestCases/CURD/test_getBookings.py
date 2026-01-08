import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import *


def test_getBookings():
    getBooking_Response = api_contant().getBookingIDs(
        url=requestsURLs().getBookingIds(),
        headers=Utils().headers_getBookingIDs()
    )
    print(getBooking_Response.status_code)
    print(getBooking_Response.text)
    assert getBooking_Response.status_code == 200
