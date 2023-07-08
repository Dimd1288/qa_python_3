import utils
from pages.common import Header, MainPage
from constants import URL, LOGIN_URL

header = Header()
main = MainPage()


def test_redirect_from_main_to_login_button_is_active(driver):
    main.go_auth_form_from_main(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    assert driver.current_url == LOGIN_URL


def test_constructor_tabs(driver):
    main.go_sauces_tab(driver)
    main.check_tab_is_active('sauces', driver)
    main.go_filling_tab(driver)
    main.check_tab_is_active('filling', driver)
    main.go_bread_tab(driver)
    main.check_tab_is_active('bread', driver)


def test_return_to_home_page(driver):
    main.go_auth_form_from_main(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    header.go_constructor_header_link(driver)
    utils.wait_url_changed(driver, URL)
    assert driver.current_url == URL
    main.go_auth_form_from_main(driver)
    utils.wait_url_changed(driver, LOGIN_URL)
    header.go_logo_header_link(driver)
    utils.wait_url_changed(driver, URL)
    assert driver.current_url == URL
