from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT = (By.ID, "checkout")
    CONTINUE = (By.ID, "continue-shopping")

    def product_names(self) -> list[str]:
        return self.texts(self.NAMES)

    def remove(self, product_slug: str) -> None:
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{product_slug}']"))

    def checkout(self) -> None:
        self.click(self.CHECKOUT)

    def continue_shopping(self) -> None:
        self.click(self.CONTINUE)

