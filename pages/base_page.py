class BasePage:

    base_url = 'http://172.21.0.1:7080/'

    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver.implicitly_wait(3)

    def open(self, url):
        site = self.base_url + url
        self.driver.get(site)
