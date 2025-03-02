import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from page.amazon_home_page import AmazonHomePage
from page.amazon_search_result_page import AmazonSearchResultsPage
from page.amazon_selected_item_page import AmazonSelectedItemPage
from page.amazon_cart_mid_page import AmazonCartMidPage



@pytest.mark.parametrize(
    'product_to_buy, product_index',
    [
        ('mobile', 3),
     ])
def test_amazon_checkout(driver, product_to_buy, product_index):
    home = AmazonHomePage(driver)
    search_results = AmazonSearchResultsPage(driver)
    selected_item = AmazonSelectedItemPage(driver)
    mid_cart = AmazonCartMidPage(driver)

    #navigate to amazon and search product - parameterized
    home.open_landing_page()
    home.search_product(product_to_buy)


    #select the 3rd product - parameterized
    search_results.select_nth_product(selected_item=product_index)


    #add product to cart
    selected_item.add_item_to_cart()

    #proceed to checkout
    mid_cart.go_to_checkout()