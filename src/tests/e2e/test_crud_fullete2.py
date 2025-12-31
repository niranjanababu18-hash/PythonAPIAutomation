import pytest
import allure
from src.modules.Wrapper.api_requests_wrapper import *
from src.endpoints.api_constants import APIConstants
from src.utils.utils import utils
from src.modules.payload_manager.payload_manager import (
    payload_create_booking,
    payload_create_token,
    payload_update_booking,
    payload_delete_booking
)
from src.modules.verification.common_verification import *

class TestCRUDBooking:

    @pytest.mark.put
    @allure.title("Update Booking Test")
    @allure.description("Verify that full update with booking id and token is working")
    def test_update_booking_id(self, setup, create_token, get_booking_id):
        put_url = APIConstants.url_patch_put_delete(bookingid=get_booking_id)
        response = put_requests(
            url=put_url,
            headers=utils().common_headers_put_patch_delete_patch_cookie(token=create_token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        print("Response status:", response.status_code)
        print("Response body:", response.text)
        print("bookingid", get_booking_id)
        # ✅ Ensure verification matches your helper signature
        verify_http_status_code(response.status_code, 200)
        verify_response_key(response.json()["firstname"], expected_data="Jim")
        verify_response_key(response.json()["lastname"], expected_data="Brown")
    @pytest.mark.delete
    @allure.title("Delete Booking Test")
    @allure.description("Verify that delete with booking id and id not present")
    def test_delete_booking_id(self, setup, create_token, get_booking_id):
        delete_url = f"https://restful-booker.herokuapp.com/booking/{get_booking_id}"
        headers = {
            "Cookie": f"token={create_token}"
        }
        response = requests.delete(delete_url, headers=headers)
        print("Response status:", response.status_code)
        print("Response body:", response.text)
        print("bookingid", get_booking_id)
        # ✅ Ensure verification matches your helper signature
        verify_http_status_code(response.status_code, 201)

