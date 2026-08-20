from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: tuple[str, str]) -> None:
        element = self.wait.until(
            conditions.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait.until(
            conditions.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    def text(self, locator: tuple[str, str]) -> str:
        return self.wait.until(
            conditions.visibility_of_element_located(locator)
        ).text

    def texts(self, locator: tuple[str, str]) -> list[str]:
        return [
            element.text
            for element in self.driver.find_elements(*locator)
        ]