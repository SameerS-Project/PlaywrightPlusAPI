
class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()

    def type(self, selector, value):
        self.page.locator(selector).fill(value) # NEED TO FILL VALUE

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def get_title(self):
        return self.page.title()