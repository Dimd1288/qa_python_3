import time

import utils
from pages.account_page import AccountPage
from pages.common import Header, MainPage
from constants import URL, LOGIN_URL, PROFILE_URL, DEFAULT_USER, DEFAULT_PASSWORD

account_page = AccountPage()
header = Header()
main = MainPage()


def test_register_of_user_is_successful(driver):
    header.go_account_header_link(driver)
    account_page.go_register_form(driver)
    account_page.set_user_name(utils.generate_name(9), driver)
    account_page.set_user_email(utils.generate_email(), driver)
    account_page.set_user_password(utils.generate_password(8), driver)
    account_page.submit_form(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    assert driver.current_url == LOGIN_URL


def test_register_form_validation(driver):
    header.go_account_header_link(driver)
    account_page.go_register_form(driver)
    account_page.set_user_name(utils.generate_name(9), driver)
    account_page.set_user_email(utils.generate_email(), driver)
    account_page.set_user_password('1', driver)
    account_page.submit_form(driver)
    assert account_page.check_error_is_visible(driver)
    assert account_page.check_error_text('Некорректный пароль', driver)


def test_login_of_user_is_successful(driver):
    header.go_account_header_link(driver)
    account_page.set_user_email(DEFAULT_USER, driver)
    account_page.set_user_password(DEFAULT_PASSWORD, driver)
    account_page.submit_form(driver)
    utils.wait_url_changed(driver, URL)
    assert driver.current_url == URL


def test_redirect_link_from_registration_form_to_auth_is_correct(driver):
    main.go_auth_form_from_main(driver)
    account_page.go_register_form(driver)
    account_page.go_auth_form(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    assert driver.current_url == LOGIN_URL


def test_redirect_link_from_reset_form_to_auth_is_correct(driver):
    main.go_auth_form_from_main(driver)
    account_page.go_password_recovering_form(driver)
    account_page.go_auth_form(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    assert driver.current_url == LOGIN_URL


def test_profile_page_is_opened(driver):
    header.go_account_header_link(driver)
    account_page.set_user_email(DEFAULT_USER, driver)
    account_page.set_user_password(DEFAULT_PASSWORD, driver)
    account_page.submit_form(driver)
    utils.wait_url_changed(driver, URL)
    header.go_account_header_link(driver)
    utils.wait_url_changed(driver, PROFILE_URL)
    assert driver.current_url == PROFILE_URL


def test_user_is_logged_out(driver):
    header.go_account_header_link(driver)
    account_page.set_user_email(DEFAULT_USER, driver)
    account_page.set_user_password(DEFAULT_PASSWORD, driver)
    account_page.submit_form(driver)
    utils.wait_url_changed(driver, URL)
    header.go_account_header_link(driver)
    utils.wait_url_changed(driver, PROFILE_URL)
    account_page.logout_of_account(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    assert driver.current_url == LOGIN_URL
