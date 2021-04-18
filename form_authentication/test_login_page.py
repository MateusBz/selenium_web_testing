import pytest
from selenium import webdriver

from pages.login_page import Login
from pages.secure_area import Secure_Area
from pages.login_error_page import Login_Error


@pytest.fixture
def setup() -> None:
    driver = webdriver.Firefox(executable_path='../geckodriver')

    driver.implicitly_wait(5)

    yield driver

    driver.quit()


def test_login_page_with_valid_data(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.login()
    redirect_page = Secure_Area(page)
    assert redirect_page.get_flash_message_attribute() == 'flash success'


def test_login_page_without_username(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.username = ''
    login_form.login()
    error_page = Login_Error(page)
    assert error_page.get_flash_message_attribute() == 'flash error'


def test_login_page_without_password(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/login')
    login_form = Login(page)
    login_form.password = ''
    login_form.login()
    error_page = Login_Error(page)
    assert error_page.get_flash_message_attribute() == 'flash error'
