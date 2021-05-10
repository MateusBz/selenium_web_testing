import pytest
import os
from selenium import webdriver

from pages.login_page import Login
from pages.secure_area import SecureArea
from pages.login_error_page import LoginError


@pytest.fixture
def setup() -> None:
    caps = {'browserName': os.getenv('BROWSER', 'firefox')}
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=caps
    )

    yield driver

    driver.quit()


def test_login_page_with_valid_data(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.login()
    redirect_page = SecureArea(page)
    assert redirect_page.get_flash_message_attribute() == 'flash success'


def test_login_page_without_username(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.username = ''
    login_form.login()
    error_page = LoginError(page)
    assert error_page.get_flash_message_attribute() == 'flash error'


def test_login_page_without_password(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.password = ''
    login_form.login()
    error_page = LoginError(page)
    assert error_page.get_flash_message_attribute() == 'flash error'
