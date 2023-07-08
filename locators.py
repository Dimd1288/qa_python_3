from selenium.webdriver.common.by import By


# Локаторы формы регистрации/авторизаци, а также профиля пользователя
class AccountPageLocators:
    PAGE_TITLE = By.XPATH, '//form/..//h2'  # Заголовок формы
    USER_NAME = By.XPATH, "//form//input[@name='name']"  # Поле для ввода имени пользователя в форме регистрации
    USER_PASSWORD = By.XPATH, "//form//input[@name='Пароль']"   # Поле для ввода пароля пользователя на форме регистрации и авторизации
    USER_PASSWORD_ERROR = By.XPATH, "//p[contains(@class, 'input__error')]"  # Блок ошибки с подсказкой под полем пароля
    USER_EMAIL = By.XPATH, "//form//label[text()='Email']/../input"     # Поле для ввода электронной почты пользователя на всех формах
    SUBMIT_BUTTON = By.XPATH, "//form//button"      # Кнопка подтверждения на всех формах
    AUTH_LINK = By.XPATH, "//a[@href='/login']"     # Локатор ссылки с форм регистрации и сброса пароля на форму входа
    REGISTER_LINK = By.XPATH, "//a[@href='/register']"      # Локатор ссылки с формы входа на форму регистрации
    RECOVER_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']"  # Локатор ссылки с формы входа на форму сброса пароля
    EXIT_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Выход']"      # Кнопка выхода в профиле пользователя


class HeaderLocators:
    ACCOUNT_HEADER_LINK = By.XPATH, "//header//*[text()='Личный Кабинет']"    # Ссылка на личный кабинет в хэдере сайта
    CONSTRUCTOR_HEADER_LINK = By.XPATH, "//a[p[text()='Конструктор']]"      # Ссылка "Конструктор" в хэдере сайта
    LOGO_HEADER_LINK = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a"  # Ссылка в логотипе хэдера


class MainPageLocators:
    FORM_AUTH_REDIRECT_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"      # Кнопка для перехода на форму входа
    CONSTRUCTOR_TAB_BREAD = By.XPATH, "//span[text()='Булки']/.."       # Таб конструктора Булки
    CONSTRUCTOR_TAB_SAUCES = By.XPATH, "//span[text()='Соусы']/.."      # Таб конструктора Соусы
    CONSTRUCTOR_TAB_FILLING = By.XPATH, "//span[text()='Начинки']/.."       # Таб конструктора Начинки
