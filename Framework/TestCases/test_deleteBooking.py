import pytest
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils


def test_deletebooking(create_token):
    delete_response = api_contant().deleteBooking(
        url= requestsURLs().deleteBooking(bookingID=3675),
        headers=Utils().headers_deleteBooking(create_token)
    )
    print(delete_response.status_code)
    assert delete_response.status_code == 201

    get_response = api_contant().getSingleBooking(
        url=requestsURLs().getSingleBooking(bookingID=2120),
        headers=Utils().headers_getSingleBookingIDs()
    )

    print(get_response.status_code)
    assert get_response.status_code == 404