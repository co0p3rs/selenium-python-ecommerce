import pytest

from tests.helpers import login_standard_user


@pytest.mark.smoke
def test_inventory_contains_six_products(driver, base_url):
    login_standard_user(driver, base_url).assert_loaded()


@pytest.mark.regression
def test_price_sort_low_to_high(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.sort("lohi")
    assert inventory.prices() == sorted(inventory.prices())


@pytest.mark.regression
def test_price_sort_high_to_low(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.sort("hilo")
    assert inventory.prices() == sorted(inventory.prices(), reverse=True)


@pytest.mark.regression
def test_add_and_remove_updates_cart_badge(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.add("sauce-labs-backpack")
    assert inventory.cart_count() == 1
    inventory.remove("sauce-labs-backpack")
    assert inventory.cart_count() == 0


@pytest.mark.regression
def test_product_details_open_from_inventory(driver, base_url):
    inventory = login_standard_user(driver, base_url)
    inventory.open_product("Sauce Labs Backpack")
    assert "inventory-item.html" in driver.current_url

