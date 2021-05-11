import pytest
from selenium.webdriver.remote.file_detector import LocalFileDetector
from pages.upload_page import UploadPage


def test_upload_page(setup):
    file_path = 'file_uploader/test_file.txt'
    page = UploadPage(setup)
    page.file_detector = LocalFileDetector()
    page.open('upload')
    assert page.upload(file_path) == 'test_file.txt'
