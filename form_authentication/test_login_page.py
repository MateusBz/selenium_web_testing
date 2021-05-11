import pytest
from pages.login_page import LoginPage
from pages.secure_area import SecureArea
from pages.login_error_page import LoginError


def test_login_page_with_valid_data(setup):
    page = LoginPage(setup)
    page.open('login')
    page.login()
    redirect_page = SecureArea(setup)
    assert redirect_page.get_flash_message_attribute() == 'flash success'


def test_login_page_without_username(setup):
    page = LoginPage(setup)
    page.open('login')
    page.username = ''
    page.login()
    error_page = LoginError(setup)
    assert error_page.get_flash_message_attribute() == 'flash error'


def test_login_page_without_password(setup):
    page = LoginPage(setup)
    page.open('login')
    page.password = ''
    page.login()
    error_page = LoginError(setup)
    assert error_page.get_flash_message_attribute() == 'flash error'
