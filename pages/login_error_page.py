from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginError(BasePage):

    def __init__(self, driver) -> None:
        self.flash_locator = 'flash'
        super().__init__(driver)

    def get_flash_message_attribute(self) -> str:
        return self.driver.find_element(By.ID, self.flash_locator).get_attribute('class')
