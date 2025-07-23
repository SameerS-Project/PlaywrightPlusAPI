from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = ".inventory_list"
        self.product_items = ".inventory_item"
        self.cart_buttons = ".btn_inventory"

    def inventory_page_loaded(self):
        return self.page.locator(self.inventory_list).is_visible()

    def number_of_products(self):
        return self.page.locator(self.product_items).count()

    def add_first_item_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def is_add_to_cart_visible_for_all(self):
        count = self.page.locator(self.cart_buttons).count()
        for i in range(count):
            if not self.page.locator(self.cart_buttons).nth(i).is_visible():
                return False
        return True
