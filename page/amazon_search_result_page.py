from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AmazonSearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_results = 'div[data-component-type="s-search-result"]'




    def select_nth_product(self, selected_item):
        self.wait_for_element_return_elem(by=By.CSS_SELECTOR, locator=self.search_results, ) #wait for the results to load

        products = self.find_elements(by=By.CSS_SELECTOR, locator=self.search_results)
        if len(products) >= selected_item:
            products[selected_item - 1].click()
        else:
            raise ValueError(f'Less than {selected_item} products found in search results')