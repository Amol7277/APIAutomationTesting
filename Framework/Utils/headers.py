class Utils():
    def headers_CreateToken(self):
        headers_CreateToken = {
        "Content-Type":"application/json"
        }

    def headers_getBookingIDs(self):
        headers_getBookingIDs = {
        "Content-Type":"application/json"
    }

    def headers_getSingleBookingIDs(self):
        headers_getSingleBookingIDs = {
        "Content-Type":"application/json"
    }

    def headers_createBooking(self):
        headers_createBooking = {
            "Content-Type": "application/json"
        }

    def headers_updateBooking(self, token):
        headers_updateBooking = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
            # "Cookie": f"token=token"
        }

    def headers_deleteBooking(self, token):
        headers_deleteBooking = {
            "Cookie": f"token={token}"
        }
