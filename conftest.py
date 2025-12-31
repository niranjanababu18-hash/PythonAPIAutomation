import pytest
import allure
import logging
from src.modules.Wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import utils
from src.modules.payload_manager.payload_manager import payload_create_booking, payload_create_token
from src.modules.verification.common_verification import *

@pytest.fixture(scope="session")
def setup():
    logging.info("Setup is started")
    yield
    logging.info("Setup is ended")

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants.url_create_token(),
        auth=None,
        headers=utils.common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response.status_code, 200)
    data = response.json()
    logging.info("Login response: %s", data)

    token = data.get("token")
    assert token is not None, f"Login response missing token: {data}"
    verify_json_key_for_not_null(token)
    return token  # ✅ only one return, after validation

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants.url_create_booking(),
        auth=None,
        headers=utils.common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )

    verify_http_status_code(response.status_code, 200)
    booking_id = response.json().get("bookingid")
    verify_json_key_for_not_null(booking_id)

    return booking_id






