createTokenPayload = {
    "username" : "admin",
    "password" : "password123"
}

createBookingPayload = {
    "firstname" : "Amol",
    "lastname" : "QA Tester",
    "totalprice" : 777,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

updateBookingPayload = {
    "firstname" : "Amol Update",
    "lastname" : "QA Tester",
    "totalprice" : 9999,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Dinner"
}


