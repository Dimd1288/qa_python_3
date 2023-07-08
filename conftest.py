import pytest

from pages.account_page import AccountPage
from selenium import webdriver


@pytest.fixture
def account_page():
    account_page = AccountPage()
    return account_page


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
