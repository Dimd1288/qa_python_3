from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import AccountPageLocators


# driver = webdriver.Chrome


class AccountPage:
    def check_page_header(self, header, driver):
        assert driver.find_element(*AccountPageLocators.PAGE_TITLE).text == header

    def set_user_name(self, value, driver):
        driver.find_element(*AccountPageLocators.USER_NAME).send_keys(value)

    def set_user_password(self, value, driver):
        driver.find_element(*AccountPageLocators.USER_PASSWORD).send_keys(value)

    def set_user_email(self, value, driver):
        driver.find_element(*AccountPageLocators.USER_EMAIL).send_keys(value)

    def submit_form(self, driver):
        driver.find_element(*AccountPageLocators.SUBMIT_BUTTON).click()

    def go_register_form(self, driver):
        driver.find_element(*AccountPageLocators.REGISTER_LINK).click()
        assert 'register' in driver.current_url

    def go_auth_form(self, driver):
        driver.find_element(*AccountPageLocators.AUTH_LINK).click()
        assert 'login' in driver.current_url

    def go_password_recovering_form(self, driver):
        driver.find_element(*AccountPageLocators.RECOVER_PASSWORD_LINK).click()
        assert 'forgot-password' in driver.current_url

    def logout_of_account(self, driver):
        driver.find_element(*AccountPageLocators.EXIT_ACCOUNT_BUTTON).click()

    def check_error_is_visible(self, driver):
        return driver.find_element(*AccountPageLocators.USER_PASSWORD_ERROR).is_displayed()

    def check_error_text(self, expected_text, driver):
        return driver.find_element(*AccountPageLocators.USER_PASSWORD_ERROR).text == expected_text
