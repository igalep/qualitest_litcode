from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = 10


    def wait_for_element_return_elem(self, by, locator):
        try:
            element = WebDriverWait(self.driver, self.wait).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {locator}")
            raise

    def open_url(self, url):
        self.driver.get(url)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)
