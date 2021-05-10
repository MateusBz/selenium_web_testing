import pytest
from decouple import config
from dropdown_list.page import DropdownPage

main_site = config('SITE_ADDRESS')


def test_dropdown_option_1(setup):
    page = setup
    page.get(main_site + '/dropdown')
    dropdown_list = DropdownPage(page)
    assert dropdown_list.select() == 'Option 1'


def test_dropdown_option_2(setup):
    page = setup
    page.get(main_site + '/dropdown')
    dropdown_list = DropdownPage(page)
    dropdown_list.option_visible_text = 'Option 2'
    assert dropdown_list.select() == 'Option 2'
