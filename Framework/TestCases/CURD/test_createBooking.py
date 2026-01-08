import pytest
import requests
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.Payload_Manager.payloads import *


def test_createBooking():
    createBooking_Response = api_contant().createBooking(
        url=requestsURLs().createBooking(),
        headers=Utils().headers_createBooking(),
        payload=createBookingPayload
    )

    print(createBooking_Response.status_code)
    booking_id = createBooking_Response.json()["bookingid"]
    print("createdbookingID =",booking_id)
    return booking_id
    assert createBooking_Response.status_code == 200

    get_response = api_contant().getSingleBooking(
        url=requestsURLs().getSingleBooking(bookingID=booking_id),
        headers=Utils().headers_getSingleBookingIDs()
    )
    print(get_response.status_code)
    assert get_response.status_code == 200
