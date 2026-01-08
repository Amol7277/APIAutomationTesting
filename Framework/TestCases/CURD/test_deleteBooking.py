from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Utils.headers import Utils
from Framework.TestCases.CURD.test_createBooking import test_createBooking


def test_deletebooking(create_token):
    mybooking = test_createBooking()
    print("mybooking =",mybooking)
    delete_response = api_contant().deleteBooking(
        url= requestsURLs().deleteBooking(bookingID=mybooking),
        headers=Utils().headers_deleteBooking(create_token)
    )
    print(delete_response.text)
    print(delete_response.status_code)
    # assert delete_response.status_code in [201,405]
    assert delete_response.status_code == 201

    get_response = api_contant().getSingleBooking(
        url=requestsURLs().getSingleBooking(bookingID=mybooking),
        headers=Utils().headers_getSingleBookingIDs()
    )

    print(get_response.status_code)
    assert get_response.status_code == 404