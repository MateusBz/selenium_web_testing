from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UploadPage(BasePage):

    def __init__(self, driver) -> None:
        self.file_upload_locator = 'file-upload'
        self.file_submit_locator = 'file-submit'
        self.file_uploaded_locator = 'uploaded-files'
        super().__init__(driver)

    def upload(self, file) -> str:
        self.driver.find_element(By.ID, self.file_upload_locator).send_keys(file)
        self.driver.find_element(By.ID, self.file_submit_locator).click()
        uploaded_file_name = self.driver.find_element(By.ID, self.file_uploaded_locator).text
        return uploaded_file_name
