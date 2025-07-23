import pytest
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.skip(reason="Skipping WebKit test due to CI limitations")
def test_cart_loaded(browser_name, page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login_successful()
    cart_page.go_to_cart()
    assert cart_page.is_cart_loaded()

@pytest.mark.ui
def test_cart_items(browser_name, page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login_successful()
    inventory_page.add_first_item_to_cart()
    cart_page.go_to_cart()
    assert cart_page.cart_items().is_visible()

@pytest.mark.ui
def test_add_item_to_cart(browser_name, page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login_successful()
    inventory_page.add_first_item_to_cart()
    assert cart_page.is_cart_badge_visible()

