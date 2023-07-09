import utils
from pages.main_page import MainPage
from constants import LOGIN_URL


class TestCommonElements:
    def test_redirect_from_main_to_login_button_is_active(self, driver):
        main = MainPage()
        main.go_auth_form_from_main(driver)
        utils.wait_url_changed(driver, LOGIN_URL)
        assert driver.current_url == LOGIN_URL


class TestConstructor:
    def test_sauces_tab(self, driver):
        main = MainPage()
        main.go_sauces_tab(driver)
        main.check_tab_is_active('sauces', driver)

    def test_bread_tab(self, driver):
        main = MainPage()
        main.go_sauces_tab(driver)
        main.check_tab_is_active('sauces', driver)
        main.go_bread_tab(driver)
        main.check_tab_is_active('bread', driver)

    def test_filling_tab(self, driver):
        main = MainPage()
        main.go_filling_tab(driver)
        main.check_tab_is_active('filling', driver)
