import utils
from pages.main_page import MainPage
from pages.header import Header
from constants import URL, LOGIN_URL


class TestHeaderLinks:
    def test_return_to_home_page(self, driver):
        header = Header()
        main = MainPage()
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
