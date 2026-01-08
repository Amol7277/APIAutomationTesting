import pytest
from Framework.API_Constant.api_contant import api_contant
from Framework.URLs.RequestURL import requestsURLs
from Framework.Payload_Manager.payloads import *
from Framework.Utils.headers import Utils


# '''
# 1. Get Token
# 2. Create the Booking
# 3. Get booking ID
# 4. Update Booking ID
# 5. Delete Booking ID
# '''


class test_EndtoEndCrud(object):

    # def test_createBooking(self):
    #     createBookingResponse = api_contant().createBooking(
    #         url=requestsURLs().createBooking(),
    #         headers=Utils().headers_createBooking(),
    #         payload=createBookingPayload
    #     )
    #     print("StatusCode ", createBookingResponse.status_code)
    #     print("BookingDetails is ", createBookingResponse.text)
    #     bookingID = createBookingResponse.json()["bookingid"]
    #     assert createBookingResponse.status_code == 200
    #     return bookingID

    def test_getBookingid(self, test_createBooking):
        getBookingResponse = api_contant().getSingleBooking(
            url=requestsURLs().getSingleBooking(bookingID=test_createBooking),
            headers=Utils().headers_getSingleBookingIDs()
        )
        print("StatusCode ", getBookingResponse.status_code)
        print("BookingDetails is ", getBookingResponse.text)
        assert getBookingResponse.status_code == 200 or getBookingResponse.status_code == 404

    def test_updateBookng(self, create_token, test_createBooking):
        updateBookingResponse = api_contant().updateBooking(
            url=requestsURLs().updateBooking(bookingID=test_createBooking),
            headers=Utils().headers_updateBooking(token=create_token),
            payload=updateBookingPayload
        )
        print("StatusCode ", updateBookingResponse.status_code)
        print("BookingDetails is ", updateBookingResponse.text)
        assert updateBookingResponse.status_code == 200

        # print("Updated Booking Details is ", test_getBookingid())

    def test_deleteBooking(self, create_token, test_createBooking):
        deleteBookingResponse = api_contant().deleteBooking(
            url=requestsURLs().deleteBooking(bookingID=test_createBooking),
            headers=Utils().headers_deleteBooking(token=create_token)
        )
        print("StatusCode ", deleteBookingResponse.status_code)
        print("BookingDetails is ", deleteBookingResponse.text)
        assert deleteBookingResponse.status_code == 201

        # test_getBookingid()
