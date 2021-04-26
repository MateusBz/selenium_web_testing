from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Dropdown_Page():
    def __init__(self, driver) -> None:
        self.driver = driver

        self.dropdown_list_locator = 'dropdown'
        self.option_visible_text = 'Option 1'

    def select(self) -> str:
        self.select = Select(self.driver.find_element(By.ID, self.dropdown_list_locator))
        self.select.select_by_visible_text(self.option_visible_text)
        return self.select.first_selected_option.text
