from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class AmazonHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = 'twotabsearchtextbox'
        self.home_page_url = 'https://www.amazon.com'

    def open_landing_page(self):
        self.open_url(self.home_page_url)

    def search_product(self, product_name):
        search_box_elem = self.wait_for_element(by=By.ID, locator=self.search_box)
        search_box_elem.clear()

        search_box_elem.send_keys(product_name)
        search_box_elem.send_keys(Keys.RETURN) #click 'Enter' for search