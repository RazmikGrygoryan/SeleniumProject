import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sales


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sales(driver):
    return Sales(driver)
