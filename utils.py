from selenium.webdriver.support.wait import WebDriverWait
import random
import string


def generate_name(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def generate_email():
    characters = string.ascii_letters.lower() + string.digits
    return ''.join(random.choice(characters) for _ in range(8)) + '@' + 'test.ru'

def wait_url_changed(driver, expected_url):
    wait = WebDriverWait(driver, 5)
    wait.until(
        lambda driver: driver.current_url == expected_url)