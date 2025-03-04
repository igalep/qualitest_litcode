from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AmazonCartMidPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.proceed_to_checkout = 'sc-buy-box-ptc-button'


    def go_to_checkout(self):
        proceed_to_checkout_btn = self.wait_for_element_return_elem(by=By.ID, locator=self.proceed_to_checkout)
        proceed_to_checkout_btn.click()