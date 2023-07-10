from locators import MainPageLocators


class MainPage:
    def go_auth_form_from_main(self, driver):
        driver.find_element(*MainPageLocators.FORM_AUTH_REDIRECT_BUTTON).click()

    def go_bread_tab(self, driver):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_BREAD).click()

    def go_sauces_tab(self, driver):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_SAUCES).click()

    def go_filling_tab(self, driver):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_FILLING).click()

    def check_tab_is_active(self, tab: str, driver):
        if tab == 'bread':
            return 'current' in driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_BREAD).get_attribute("class")
        elif tab == 'sauces':
            return 'current' in driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_SAUCES).get_attribute("class")
        elif tab == 'filling':
            return 'current' in driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB_FILLING).get_attribute("class")
