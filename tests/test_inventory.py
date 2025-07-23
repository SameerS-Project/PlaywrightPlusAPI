import pytest
from pages.inventory_page import InventoryPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

@pytest.mark.ui
def test_inventory_page_loaded(browser_name, page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    assert inventory_page.inventory_page_loaded()

@pytest.mark.ui
def test_all_add_to_cart_buttons_visible(browser_name, page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    assert inventory_page.is_add_to_cart_visible_for_all()

@pytest.mark.ui
def test_inventory_product_count(browser_name, page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    assert inventory_page.number_of_products() == 6

