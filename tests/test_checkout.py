import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.helpers import login_standard_user
from utils.test_data import unique_customer


def open_checkout(driver, base_url) -> CheckoutPage:
    inventory = login_standard_user(driver, base_url)
    inventory.add("sauce-labs-backpack")
    inventory.open_cart()
    CartPage(driver).checkout()
    return CheckoutPage(driver)


@pytest.mark.regression
def test_checkout_requires_customer_information(driver, base_url):
    checkout = open_checkout(driver, base_url)
    checkout.continue_without_information()
    assert "First Name is required" in checkout.text(checkout.ERROR)


@pytest.mark.regression
def test_checkout_overview_contains_totals(driver, base_url):
    checkout = open_checkout(driver, base_url)
    customer = unique_customer()
    checkout.submit_information(customer.first_name, customer.last_name, customer.postal_code)
    assert checkout.text(checkout.ITEM_TOTAL).startswith("Item total: $")
    assert checkout.text(checkout.TAX).startswith("Tax: $")
    assert checkout.text(checkout.TOTAL).startswith("Total: $")


@pytest.mark.e2e
@pytest.mark.smoke
def test_complete_purchase_flow(driver, base_url):
    checkout = open_checkout(driver, base_url)
    customer = unique_customer()
    checkout.submit_information(customer.first_name, customer.last_name, customer.postal_code)
    checkout.finish()
    assert checkout.text(checkout.COMPLETE) == "Thank you for your order!"
