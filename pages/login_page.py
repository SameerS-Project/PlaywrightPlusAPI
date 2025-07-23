from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"

    def login(self, username, password):
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.click(self.login_button)

    def login_successful(self):
        self.login("standard_user", "secret_sauce")
        return self.is_inventory_visible()

    def logout_successful(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()
        return self.page.locator("#login_button_container")

    def is_inventory_visible(self):
        return self.page.locator(".inventory_list").is_visible()

    def login_failed(self):
        self.login("standard_user", "wrongpass")
        return self.page.locator("h3[data-test ='error']").is_visible()


