from selenium.webdriver.common.by import By


class LoginError():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.flash_locator = 'flash'

    def get_flash_message_attribute(self) -> str:
        return self.driver.find_element(By.ID, self.flash_locator).get_attribute('class')
