import pytest
import os
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from dropdown_list.page import DropdownPage


@pytest.fixture
def setup() -> None:
    # options = Options()
    # options.headless = True
    # driver = webdriver.Firefox(executable_path='../geckodriver', options=options)
    caps = {'browserName': os.getenv('BROWSER', 'firefox')}
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=caps
    )
    yield driver

    driver.quit()


def test_dropdown_option_1(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/dropdown')
    dropdown_list = DropdownPage(page)
    assert dropdown_list.select() == 'Option 1'


def test_dropdown_option_2(setup):
    page = setup
    page.get('https://the-internet.herokuapp.com/dropdown')
    dropdown_list = DropdownPage(page)
    dropdown_list.option_visible_text = 'Option 2'
    assert dropdown_list.select() == 'Option 2'
