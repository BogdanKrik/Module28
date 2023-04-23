# для запуска теста: python3 -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_auth_page.py

from pages.auth_page import AuthPage
from settings import url_base_page
from settings import url_by_code

class TestAuthPage():
    # Переход на форму авторизации
    def test_RT001_the_authorization_form_is_open(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.the_authorization_form_is_open()

    # Проверка расположения элементов на странице
    def test_RT002_location_of_the_elements(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_of_the_elements()

    # Тип аутентификации по умолчанию
    def test_RT003_default_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.default_authentication_type()

    # Автоматическое изменение типа аутентификации
    def test_RT004_automatic_change_of_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.automatic_change_of_authentication_type()

    # Переход на форму восстановления пароля
    def test_RT005_link_to_the_password_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_password_recovery_form()

    # Переход на форму регистрации
    def test_RT006_link_to_the_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_registration_form()

    # Переход на страницу с пользовательским соглашением (ссылка под кнопкой "Войти")
    def test_RT007_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_user_agreement_page()

    # Переход по ссылке на страницу авторизации с помощью соцсети "ВКонтакте"
    def test_RT008_link_to_social_vk(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_social_vk()

    # Авторизация с незаполненными полями
    def test_RT09_authorization_with_blank_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_with_blank_fields()

    # Переход на форму авторизации по коду
    def test_RT028_the_authorization_form_by_code(self, browser):
        auth_page = AuthPage(browser, url_by_code)
        auth_page.open()
        auth_page.the_authorization_form_by_code()
