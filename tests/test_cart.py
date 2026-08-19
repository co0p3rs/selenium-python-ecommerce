import pytest

from pages.cart_page import CartPage
from tests.helpers import login_standard_user


@pytest.mark.smoke
def test_added_product_appears_in_cart(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.add("sauce-labs-backpack")
    inventory.open_cart()
    assert CartPage(driver).product_names() == ["Sauce Labs Backpack"]


@pytest.mark.regression
def test_multiple_products_appear_in_cart(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.add("sauce-labs-backpack")
    inventory.add("sauce-labs-bike-light")
    inventory.open_cart()
    assert CartPage(driver).product_names() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


@pytest.mark.regression
def test_product_can_be_removed_from_cart(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.add("sauce-labs-backpack")
    inventory.open_cart()
    cart = CartPage(driver)
    cart.remove("sauce-labs-backpack")
    assert cart.product_names() == []


@pytest.mark.regression
def test_continue_shopping_returns_to_inventory(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.open_cart()
    CartPage(driver).continue_shopping()
    assert driver.current_url.endswith("inventory.html")

