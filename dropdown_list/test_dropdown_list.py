import pytest
from pages.dropdown_page import DropdownPage


def test_dropdown_option_1(setup):
    page = DropdownPage(setup)
    page.open('dropdown')
    assert page.select() == 'Option 1'


def test_dropdown_option_2(setup):
    page = DropdownPage(setup)
    page.open('dropdown')
    page.option_visible_text = 'Option 2'
    assert page.select() == 'Option 2'
