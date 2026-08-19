from pathlib import Path

import pytest
from selenium import webdriver

from config import BASE_URL


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox"))
    parser.addoption("--base-url", default=BASE_URL)


@pytest.fixture
def base_url(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--base-url")).rstrip("/")


@pytest.fixture
def driver(request: pytest.FixtureRequest):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        browser_driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser_driver = webdriver.Chrome(options=options)

    browser_driver.set_window_size(1440, 1000)
    browser_driver.implicitly_wait(0)
    yield browser_driver

    if request.node.rep_call.failed:
        artifacts = Path("artifacts")
        artifacts.mkdir(exist_ok=True)
        safe_name = request.node.nodeid.replace("/", "_").replace("::", "__")
        browser_driver.save_screenshot(str(artifacts / f"{safe_name}.png"))
        (artifacts / f"{safe_name}.html").write_text(browser_driver.page_source, encoding="utf-8")
    browser_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

