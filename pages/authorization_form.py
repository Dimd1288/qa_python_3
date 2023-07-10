from locators import FormLocators
from pages.common_form import CommonForm


class AuthorizationForm(CommonForm):

    def go_register_form(self, driver):
        driver.find_element(*FormLocators.REGISTER_LINK).click()
        assert 'register' in driver.current_url

    def go_password_recovering_form(self, driver):
        driver.find_element(*FormLocators.RECOVER_PASSWORD_LINK).click()
        assert 'forgot-password' in driver.current_url
