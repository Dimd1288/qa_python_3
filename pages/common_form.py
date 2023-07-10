from locators import FormLocators


class CommonForm:
    def assert_page_header(self, header, driver):
        assert driver.find_element(*FormLocators.PAGE_TITLE).text == header

    def set_user_name(self, value, driver):
        driver.find_element(*FormLocators.USER_NAME).send_keys(value)

    def set_user_password(self, value, driver):
        driver.find_element(*FormLocators.USER_PASSWORD).send_keys(value)

    def set_user_email(self, value, driver):
        driver.find_element(*FormLocators.USER_EMAIL).send_keys(value)

    def submit_form(self, driver):
        driver.find_element(*FormLocators.SUBMIT_BUTTON).click()

