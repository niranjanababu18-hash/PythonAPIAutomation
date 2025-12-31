import allure
import pytest
from src.modules.Wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import url_create_booking
from src.utils.utils import utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verification.common_verification import *
import logging
class TestCreateBooking:
    @pytest.mark.positive
    @allure.title("Test Create Booking")
    @allure.description("Test Create Booking")
    def test_create_booking_positive(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("POST MAKING")
        response=post_request(
        #no authentication for post request
            url=url_create_booking(),
            auth=None,
            headers=utils.common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
            )
        LOGGER.info("Post request done")
        LOGGER.info("Now verify")
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Test Create Booking with Empty Payload")
    @allure.description("Should fail when payload is empty")
    def test_create_booking_negative(self):
        response = post_request(
            # no authentication for post request
            url=url_create_booking(),
            auth=None,
            headers=utils.common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
##       verify_json_key_for_not_null(response.json()["bookingid"])
        assert "error" in response.json()

    @pytest.mark.negative
    @allure.title("Test Create Booking with Partial Payload")
    @allure.description("Should fail when payload is incomplete")
    def test_booking_id_negative_tc2(self):
        response = post_request(
            # no authentication for post request
            url=url_create_booking(),
            auth=None,
            headers=utils.common_headers_json(),
            payload={"firstname":"Niranjana"},
            in_json=False
        )
        print("Actual status code:", response)
        print("Response body:", response.text)
        verify_http_status_code(response_data=response, expected_data=500)
  ##      verify_json_key_for_not_null(response.json()["bookingid"])
        assert "error" in response.json()


