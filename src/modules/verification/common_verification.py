#common verification
#HTTP STATUS CODE
#HEADERS
#DATA VERIFCATION
#JSON SCHEMA

def verify_http_status_code(status_code, expected_data):
    assert status_code == expected_data, \
        f"Expected {expected_data}, got {status_code}"
def verify_response_key(key, expected_data):
        assert key == expected_data, "Failed to match the key."
def verify_json_key_for_not_null(key):
    assert key is not None, f"Failed - key is None"
    assert str(key).strip() != "", f"Failed - key is empty"
def verify_json_key_for_not_null_token(key):
    assert key !=0,"Failed-key is non empty" +key
def verify_response_delete(response):
    assert "Created" in response

