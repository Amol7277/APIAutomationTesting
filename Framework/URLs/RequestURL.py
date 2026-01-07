import requests
import pytest

class requestsURLs():

    def baseURl(self):
        baseURL = "https://restful-booker.herokuapp.com/"
        return baseURL

    def createToken(self):
        tokenURL = "https://restful-booker.herokuapp.com/auth"
        return tokenURL

    def getBookingIds(self):
        getbookingIDsURL = "https://restful-booker.herokuapp.com/booking"
        return getbookingIDsURL

    def getSingleBooking(self, bookingID):
        getSingleBookingURL = "https://restful-booker.herokuapp.com/booking/"+str(bookingID)
        return getSingleBookingURL

    def createBooking(self):
        createBookingURL = "https://restful-booker.herokuapp.com/booking"
        return createBookingURL

    def updateBooking(self,bookingID):
        updateBookingURL = "https://restful-booker.herokuapp.com/booking/" + str(bookingID)
        return updateBookingURL

    def deleteBooking(self, bookingID):
        deleteBookingURL = "https://restful-booker.herokuapp.com/booking/" + str(bookingID)
        return deleteBookingURL

