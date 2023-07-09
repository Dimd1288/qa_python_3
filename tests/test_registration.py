import utils
from pages.registration_form import RegistrationForm
from pages.authorization_form import AuthorizationForm
from pages.main_page import MainPage
from pages.header import Header
from constants import LOGIN_URL


class TestUserRegister:
    def test_register_of_user_is_successful(self, driver):
        auth_form = AuthorizationForm()
        reg_form = RegistrationForm()
        header = Header()
        header.go_account_header_link(driver)
        auth_form.go_register_form(driver)
        reg_form.set_user_name(utils.generate_name(9), driver)
        reg_form.set_user_email(utils.generate_email(), driver)
        reg_form.set_user_password(utils.generate_password(8), driver)
        reg_form.submit_form(driver)
        utils.wait_url_changed(driver, LOGIN_URL)
        assert driver.current_url == LOGIN_URL

    def test_register_form_validation(self, driver):
        auth_form = AuthorizationForm()
        reg_form = RegistrationForm()
        header = Header()
        header.go_account_header_link(driver)
        auth_form.go_register_form(driver)
        reg_form.set_user_name(utils.generate_name(9), driver)
        reg_form.set_user_email(utils.generate_email(), driver)
        reg_form.set_user_password('1', driver)
        reg_form.submit_form(driver)
        assert reg_form.check_error_is_visible(driver)
        assert reg_form.check_error_text('Некорректный пароль', driver)

    def test_redirect_link_from_registration_form_to_auth_is_correct(self, driver):
        auth_form = AuthorizationForm()
        reg_form = RegistrationForm()
        main = MainPage()
        main.go_auth_form_from_main(driver)
        auth_form.go_register_form(driver)
        reg_form.go_auth_form(driver)
        utils.wait_url_changed(driver, LOGIN_URL)
        assert driver.current_url == LOGIN_URL
