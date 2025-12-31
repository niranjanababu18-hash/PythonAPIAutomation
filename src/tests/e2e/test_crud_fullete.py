#flow of ETE
#create token
#create bookingid
#update bookingid
#delete bookingid
#verify if bookingid does not exist
#conftest-python configuration file shared by all python test program
#anootaton,connections before runnin etc
import pytest
#no need to import manually from conftest
#Pytest automatically finds fixtures defined in conftest.py and makes them available to your tests. You don’t need to import them.
#no need of line-from conftest import create_token
import pytest

# no need to import from conftest

def test_login(setup, create_token, get_booking_id):
    print(create_token)
    print(get_booking_id)
    print("Executing")

def test_login2(setup, create_token, get_booking_id):
    print(create_token)
    print(get_booking_id)
    print("Executing")
