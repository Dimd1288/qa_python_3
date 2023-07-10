from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import ProfilePageLocators


class ProfilePage:

    def logout_of_account(self, driver):
        driver.find_element(*ProfilePageLocators.EXIT_PROFILE_BUTTON).click()

    def get_user_login(self, driver):
        return driver.find_element(*ProfilePageLocators.PROFILE_LOGIN_INPUT).get_attribute('value')

    def assert_user_login_not_found(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(*ProfilePageLocators.PROFILE_LOGIN_INPUT))
            not_found = False
        except:
            not_found = True

        assert not_found
