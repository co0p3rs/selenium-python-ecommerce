from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from pages.base_page import BasePage


class CartPage(BasePage):
    NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT = (By.ID, "checkout")
    CONTINUE = (By.ID, "continue-shopping")

    def product_names(self) -> list[str]:
        return self.texts(self.NAMES)

    def remove(self, product_slug: str) -> None:
        locator = (
            By.CSS_SELECTOR,
            f"[data-test='remove-{product_slug}']",
        )
        self.click(locator)
        self.wait.until(
            conditions.invisibility_of_element_located(locator)
        )

    def checkout(self) -> None:
        self.click(self.CHECKOUT)
        self.wait.until(
            conditions.url_contains("checkout-step-one.html")
        )

    def continue_shopping(self) -> None:
        self.click(self.CONTINUE)
        self.wait.until(
            conditions.url_contains("inventory.html")
        )