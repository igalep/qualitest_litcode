from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AmazonSelectedItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart = 'add-to-cart-button'


    def add_item_to_cart(self):
        add_to_cart_btn = self.wait_for_element(by=By.ID, locator=self.add_to_cart)
        add_to_cart_btn.click()