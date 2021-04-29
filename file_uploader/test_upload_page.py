import pytest
import os
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector
from file_uploader.page import UploadPage


@pytest.fixture
def setup() -> None:
    caps = {'browserName': os.getenv('BROWSER', 'firefox')}
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=caps
    )

    yield driver

    driver.quit()


def test_upload_page(setup):
    file_path = 'file_uploader/test_file.txt'
    page = setup
    page.file_detector = LocalFileDetector()
    page.get('https://the-internet.herokuapp.com/upload')
    upload_page = UploadPage(page)
    assert upload_page.upload(file_path) == 'test_file.txt'
