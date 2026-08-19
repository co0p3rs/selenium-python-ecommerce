from config import PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.popup_handler import PopupHandler


def login_standard_user(driver, base_url: str) -> InventoryPage:
    login = LoginPage(driver)
    login.open(base_url)
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    PopupHandler(driver).close_optional_popups()
    login.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(driver)
    inventory.assert_loaded()
    return inventory
