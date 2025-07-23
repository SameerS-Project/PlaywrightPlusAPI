from pages.base_page import BasePage
from pages.login_page import LoginPage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_button = ".shopping_cart_link"
        self.cart_title = ".title"
        self.continue_shopping = "#continue-shopping"
        self.cart_item = ".cart_item"

    def go_to_cart(self):
        self.page.locator(self.cart_button).click()

    def is_cart_loaded(self):
        return self.page.locator(self.cart_title).is_visible()

    def cart_items(self):
        return self.page.locator(self.cart_item)

    def click_continue_shopping(self):
        self.click(self.continue_shopping)

    def is_cart_badge_visible(self):
        return self.page.locator(".shopping_cart_badge").count() > 0
