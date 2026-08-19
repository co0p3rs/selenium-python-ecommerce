import pytest

from config import LOCKED_USER, PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_standard_user_can_login(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(STANDARD_USER, PASSWORD)
    InventoryPage(driver).assert_loaded()


@pytest.mark.regression
def test_invalid_password_is_rejected(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(STANDARD_USER, "wrong-password")
    assert "Username and password do not match" in login.error()


@pytest.mark.regression
def test_locked_user_is_rejected(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(LOCKED_USER, PASSWORD)
    assert "locked out" in login.error()


@pytest.mark.regression
def test_empty_credentials_are_rejected(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.submit_empty()
    assert "Username is required" in login.error()

