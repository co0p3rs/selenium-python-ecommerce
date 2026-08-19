from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    ITEM_TOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH = (By.ID, "finish")
    COMPLETE = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def submit_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    def continue_without_information(self) -> None:
        self.click(self.CONTINUE)

    def finish(self) -> None:
        self.click(self.FINISH)

