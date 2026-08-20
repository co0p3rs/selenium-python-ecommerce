from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    @staticmethod
    def add_button(product_slug: str) -> tuple[str, str]:
        return By.CSS_SELECTOR, f"[data-test='add-to-cart-{product_slug}']"

    @staticmethod
    def remove_button(product_slug: str) -> tuple[str, str]:
        return By.CSS_SELECTOR, f"[data-test='remove-{product_slug}']"

    def assert_loaded(self) -> None:
        assert self.text(self.TITLE) == "Products"
        assert len(self.driver.find_elements(*self.ITEMS)) == 6

    def add(self, product_slug: str) -> None:
        previous_count = self.cart_count()
        self.click(self.add_button(product_slug))
        self.wait.until(
            lambda driver: self.cart_count() == previous_count + 1
        )

    def remove(self, product_slug: str) -> None:
        previous_count = self.cart_count()
        self.click(self.remove_button(product_slug))
        self.wait.until(
            lambda driver: self.cart_count() == max(previous_count - 1, 0)
        )

    def cart_count(self) -> int:
        badges = self.driver.find_elements(*self.BADGE)
        return int(badges[0].text) if badges else 0

    def sort(self, value: str) -> None:
        element = self.wait.until(
            lambda driver: driver.find_element(*self.SORT)
        )
        Select(element).select_by_value(value)

    def prices(self) -> list[float]:
        return [
            float(value.replace("$", ""))
            for value in self.texts(self.PRICES)
        ]

    def open_product(self, name: str) -> None:
        self.click(
            (
                By.XPATH,
                f"//*[@data-test='inventory-item-name' and text()='{name}']",
            )
        )

    def open_cart(self) -> None:
        self.click(self.CART)
        self.wait.until(conditions.url_contains("cart.html"))
        self.wait.until(
            conditions.text_to_be_present_in_element(
                self.TITLE,
                "Your Cart",
            )
        )