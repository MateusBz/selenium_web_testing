import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from page import UploadPage


@pytest.fixture
def setup() -> None:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path='../geckodriver', options=options)

    yield driver

    driver.quit()


def test_upload_page(setup):
    filename = 'test_file.txt'
    file = os.path.join(os.getcwd(), filename)
    page = setup
    page.get('https://the-internet.herokuapp.com/upload')
    upload_page = UploadPage(page)
    assert upload_page.upload(file) == 'test_file.txt'
