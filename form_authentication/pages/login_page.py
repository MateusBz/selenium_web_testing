from selenium.webdriver.common.by import By


class Login():
    def __init__(self, driver) -> None:
        self.driver = driver

        self.username = 'tomsmith'
        self.password = 'SuperSecretPassword!'

        self.username_locator = 'username'
        self.password_locator = 'password'
        self.login_button = '.fa.fa-2x.fa-sign-in'

    def login(self) -> None:
        self.driver.find_element(By.ID, self.username_locator).send_keys(self.username)
        self.driver.find_element(By.ID, self.password_locator).send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

