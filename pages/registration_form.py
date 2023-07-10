from locators import FormLocators
from pages.common_form import CommonForm


class RegistrationForm(CommonForm):

    def go_auth_form(self, driver):
        driver.find_element(*FormLocators.AUTH_LINK).click()
        assert 'login' in driver.current_url

    def check_error_is_visible(self, driver):
        return driver.find_element(*FormLocators.USER_PASSWORD_ERROR).is_displayed()

    def check_error_text(self, expected_text, driver):
        return driver.find_element(*FormLocators.USER_PASSWORD_ERROR).text == expected_text
