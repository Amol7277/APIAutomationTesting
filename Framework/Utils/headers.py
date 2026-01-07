class Utils():
    def headers_CreateToken(self):
        headers_CreateToken = {
        "Content-Type":"application/json"
        }
        return headers_CreateToken

    def headers_getBookingIDs(self):
        headers_getBookingIDs = {
        "Content-Type":"application/json"
    }
        return headers_getBookingIDs

    def headers_getSingleBookingIDs(self):
        headers_getSingleBookingIDs = {
        "Content-Type":"application/json"
    }
        return headers_getSingleBookingIDs

    def headers_createBooking(self):
        headers_createBooking = {
            "Content-Type": "application/json"
        }
        return headers_createBooking

    def headers_updateBooking(self, token):
        headers_updateBooking = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }
        return headers_updateBooking

    # def headers_updateBooking(self):
    #     return {
    #         "Content-Type": "application/json",
    #         "Accept": "application/json"
    #     }

    def headers_deleteBooking(self, token):
        headers_deleteBooking = {
            "Cookie": f"token={token}"
        }
        return headers_deleteBooking
