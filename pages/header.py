from locators import HeaderLocators


class Header:
    def go_account_header_link(self, driver):
        driver.find_element(*HeaderLocators.ACCOUNT_HEADER_LINK).click()

    def go_constructor_header_link(self, driver):
        driver.find_element(*HeaderLocators.CONSTRUCTOR_HEADER_LINK).click()

    def go_logo_header_link(self, driver):
        driver.find_element(*HeaderLocators.LOGO_HEADER_LINK).click()