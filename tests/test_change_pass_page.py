# для запуска теста: python3 -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_change_pass_page.py

import pytest
from pages.change_pass_page import ChangePassPage
from settings import url_change_page


class TestChangePassPage():

    #  Тип восстановления пароля по умолчанию
    def test_RT010_default_password_recovery_type(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.default_password_recovery_type()

    # Валидация поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного номера)
    @pytest.mark.xfail
    def test_RT011_phone_field_validation_valid_data(self, browser):
        """ Поле принимает 11-значное число в случае если первая цифра 3, 7 или 8.
        В остальных случаях поле принимает 10-значное число """
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.phone_field_validation_valid_data()

    # Валидация поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного email)
    def test_RT012_email_field_validation_valid_data(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.email_field_validation_valid_data()

    # Возврат на форму авторизации
    def test_RT013_go_back_button(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.go_back_button()

    # Переход по ссылке на пользовательское соглашение
    def test_RT014_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.link_to_the_user_agreement_page()

    # Восстановление пароля с незаполненными полями
    def test_RT015_password_recovery_with_blank_fields(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()

    # Восстановление пароля с незаполненным значением капчи
    def test_RT016_password_recovery_with_blank_captcha(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()
