import os


BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
STANDARD_USER = os.getenv("TEST_USERNAME", "standard_user")
LOCKED_USER = "locked_out_user"
PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")

