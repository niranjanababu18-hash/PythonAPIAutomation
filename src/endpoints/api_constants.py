#API CONSTANTS -CLASS WHICH CONTAINS ALL THE ENDPOINTS
#RESTFULBOOKER API,/BOOKING,BOOKING/ID
class APIConstants:
    def base_url(self):
        return "https://restful-booker.herokuapp.com"
    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"
    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"
    def url_patch_put_delete(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+ str(bookingid)
