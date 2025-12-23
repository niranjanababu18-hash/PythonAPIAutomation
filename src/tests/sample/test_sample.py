import pytest
import allure
@allure.title("Test title")
def test_sample_pass():
    assert True==True
@allure.title("Test title2")
def test_sample_fail():
    assert True==False