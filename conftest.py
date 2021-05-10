import pytest
from selenium import webdriver
import os


@pytest.fixture
def setup() -> None:
    caps = {'browserName': os.getenv('BROWSER', 'firefox')}
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=caps
    )

    yield driver

    driver.quit()
