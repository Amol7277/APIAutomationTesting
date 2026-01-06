import requests

class api_contant():

    def getToken(self, url, headers, payload):
        createToken = requests.post(url=url, headers=headers, json=payload)
        return createToken

    def getBookingIDs(self, url, headers):
        getBookingID = requests.get(url=url, headers=headers)
        return getBookingID

    def getSingleBooking(self, url, headers):
        getSingleBooking = requests.get(url=url, headers=headers)
        return getSingleBooking

    def createBooking(self, url, headers, payload):
        createBooking = requests.post(url=url, headers=headers, json=payload)
        return createBooking

    def updateBooking(self, url, headers, payload):
        updateBooking = requests.put(url=url, headers=headers, json=payload)
        return updateBooking

    def deleteBooking(self, url, headers):
        deleteBooking = requests.delete(url= url, headers=headers)
        return deleteBooking

