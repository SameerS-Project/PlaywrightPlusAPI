import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_valid_login(browser_name, page):
    login_page = LoginPage(page)
    assert login_page.login_successful()

@pytest.mark.ui
def test_invalid_login(browser_name, page):
    login_page = LoginPage(page)
    assert login_page.login_failed()

@pytest.mark.ui
def test_logout_page(browser_name, page):
    login_page = LoginPage(page)
    login_page.login_successful()
    assert login_page.logout_successful()

