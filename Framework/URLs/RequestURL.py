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

    def getSingleBooking(self, id):
        getSingleBookingURL = "https://restful-booker.herokuapp.com/booking/"+str(id)
        return getSingleBookingURL

    def createBooking(self):
        createBookingURL = "https://restful-booker.herokuapp.com/booking"
        return createBookingURL

    def updateBooking(self):
        updateBookingURL = "https://restful-booker.herokuapp.com/booking/2120" #+ str(bookingID)
        return updateBookingURL

    def deleteBooking(self, bookingID):
        deleteBookingURL = "https://restful-booker.herokuapp.com/booking/" + str(bookingID)
        return deleteBookingURL

