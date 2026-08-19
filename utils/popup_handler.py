from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class PopupHandler:
    """Best-effort cleanup for optional cookie banners, overlays, and dialogs."""

    CLOSE_CANDIDATES = (
        (By.CSS_SELECTOR, "[data-test='close-popup']"),
        (By.CSS_SELECTOR, "button[aria-label='Close']"),
        (By.CSS_SELECTOR, "button[aria-label='Dismiss']"),
        (By.XPATH, "//button[normalize-space()='Accept']"),
        (By.XPATH, "//button[normalize-space()='Accept all']"),
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def close_optional_popups(self) -> int:
        closed = 0
        for locator in self.CLOSE_CANDIDATES:
            try:
                WebDriverWait(self.driver, 0.5).until(conditions.element_to_be_clickable(locator)).click()
                closed += 1
            except TimeoutException:
                continue
        return closed

