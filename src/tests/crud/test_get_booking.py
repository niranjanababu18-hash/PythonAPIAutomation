import allure
import pytest
from src.modules.Wrapper.api_requests_wrapper import get_request
from src.endpoints.api_constants import base_url
from src.utils.utils import utils
from src.modules.verification.common_verification import *
class TestGetBooking:
    @pytest.mark.positive
    @allure.title("Verify booking id exists and returns 200")
    @allure.description("Test Get Booking with valid booking id")
    def test_verify_existing_booking_id_exists(self):
        bookingid = 1
        response = get_request(
            url=base_url(bookingid),
            auth=None,
            headers=utils.common_headers_json(),
            in_json=False
        )
        # Verify status code is 200
        verify_http_status_code(response_data=response, expected_data=200)
        # Verify bookingid is present in response
        data = response.json()
        assert data is not None, "Response JSON is empty"
        assert "firstname" in data, "Expected booking details not found"
    @pytest.mark.negative
    @allure.title("Verify booking id does not exist and returns error")
    @allure.description("Test Get Booking with invalid booking id")
    def test_invalid_booking_doesnotexist(self):
        invalid_bookingid = 999999  # assume this id does not exist
        response = get_request(
            url=base_url(invalid_bookingid),
            auth=None,
            headers=utils.common_headers_json(),
            in_json=False
        )

        # Verify status code is 404 (Not Found)
        verify_http_status_code(response_data=response, expected_data=404)

        # Response may be empty or contain an error message
        try:
            data = response.json()
            assert "error" in data or data == {}, "Expected error message or empty response"
        except ValueError:
            # Non‑JSON response (like plain text "Not Found")
            assert response.text != "", "Expected error text in response"
