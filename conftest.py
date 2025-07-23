import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
import requests

# --- BROWSER and PAGE setup below ---

#@pytest.fixture(params=["chromium","firefox","webkit"])
@pytest.fixture
def browser_name():
    return "chromium"
    #return request.param

@pytest.fixture
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page
        browser.close()

@pytest.fixture
def context(page):
    return page.context

# --- API pre set up fixture ---

def pytest_generate_tests(metafunc):
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"
    browsers = ["chromium", "firefox"] if is_ci else ["chromium", "firefox", "webkit"]

    if "browser_name" in metafunc.fixturenames and "ui" in metafunc.definition.keywords:
        metafunc.parametrize("browser_name", browsers)


# --- SCREENSHOT + TRACE setup ---

os.makedirs("screenshots", exist_ok=True)
os.makedirs("traces", exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, f"rep_{result.when}", result)

@pytest.fixture(scope="function", autouse=True)
def screenshot_and_trace_on_failure(request):
    page = request.node.funcargs.get("page")
    context = request.node.funcargs.get("context")

    if not page or not context:
        yield
        return

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        test_name=request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        page.screenshot(path=f"screenshots/{test_name}_{timestamp}.png")
        context.tracing.stop(path=f"traces/{test_name}_{timestamp}.zip")
    else:
        context.tracing.stop()


# --- API Contexts Fixture ---

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def api_request_context():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert all("email" in user for user in data["data"])