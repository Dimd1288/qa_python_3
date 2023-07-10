import utils
from pages.profile_page import ProfilePage
from pages.authorization_form import AuthorizationForm
from pages.header import Header
from constants import URL, LOGIN_URL, PROFILE_URL, DEFAULT_USER, DEFAULT_PASSWORD


class TestProfilePage:
    def test_profile_page_is_opened(self, driver):
        auth_form = AuthorizationForm()
        profile_page = ProfilePage()
        header = Header()
        header.go_account_header_link(driver)
        auth_form.set_user_email(DEFAULT_USER, driver)
        auth_form.set_user_password(DEFAULT_PASSWORD, driver)
        auth_form.submit_form(driver)
        utils.wait_url_changed(driver, URL)
        header.go_account_header_link(driver)
        utils.wait_url_changed(driver, PROFILE_URL)
        assert profile_page.get_user_login(driver) == DEFAULT_USER

    def test_user_is_logged_out(self, driver):
        profile_page = ProfilePage()
        auth_form = AuthorizationForm()
        header = Header()
        header.go_account_header_link(driver)
        auth_form.set_user_email(DEFAULT_USER, driver)
        auth_form.set_user_password(DEFAULT_PASSWORD, driver)
        auth_form.submit_form(driver)
        utils.wait_url_changed(driver, URL)
        header.go_account_header_link(driver)
        utils.wait_url_changed(driver, PROFILE_URL)
        profile_page.logout_of_account(driver)
        utils.wait_url_changed(driver, LOGIN_URL)
        profile_page.assert_user_login_not_found(driver)
        auth_form.assert_page_header('Вход', driver)
