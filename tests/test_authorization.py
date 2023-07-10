import utils
from pages.profile_page import ProfilePage
from pages.registration_form import RegistrationForm
from pages.authorization_form import AuthorizationForm
from pages.main_page import MainPage
from pages.header import Header
from constants import PROFILE_URL, LOGIN_URL, DEFAULT_USER, DEFAULT_PASSWORD


class TestUserAuthorization:
    def test_login_of_user_is_successful(self, driver):
        auth_form = AuthorizationForm()
        header = Header()
        header.go_account_header_link(driver)
        auth_form.set_user_email(DEFAULT_USER, driver)
        auth_form.set_user_password(DEFAULT_PASSWORD, driver)
        auth_form.submit_form(driver)
        header.go_account_header_link(driver)
        utils.wait_url_changed(driver, PROFILE_URL)
        assert ProfilePage().get_user_login(driver) == DEFAULT_USER

    def test_redirect_link_from_reset_form_to_auth_is_correct(self, driver):
        auth_form = AuthorizationForm()
        reg_form = RegistrationForm()
        main = MainPage()
        main.go_auth_form_from_main(driver)
        auth_form.go_password_recovering_form(driver)
        reg_form.go_auth_form(driver)
        utils.wait_url_changed(driver, LOGIN_URL)
        assert driver.current_url == LOGIN_URL
