# для запуска теста: python3 -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_reg_page.py

import pytest
from pages.reg_page import RegPage
from settings import url_base_page, invalid_name, valid_email_or_phone, valid_password, valid_first_name, \
    valid_last_name, invalid_email_or_phone, invalid_password, valid_password2, random_int, first_name_en, \
    chinese_chars, russian_chars

class TestRegPage():
    # Расположение поля ввода имени, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def test_RT017_location_of_input_fields_and_buttons_and_links(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.location_of_input_fields_and_buttons_and_links()

    # Валидация поля ввода email (ввод валидных данных)
    @pytest.mark.parametrize('input_text', valid_email_or_phone)
    def test_RT018_email_or_phone_field_validation_valid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_valid_data(input_text)

    # Валидация поля ввода пароля (ввод валидных данных)
    @pytest.mark.parametrize('input_text', valid_password)
    def test_RT019_password_field_validation_valid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_valid_data(input_text)

    # Регистрация с валидными данными
    @pytest.mark.parametrize('first_name', valid_first_name)
    @pytest.mark.parametrize('last_name', valid_last_name)
    @pytest.mark.parametrize('email_phone', valid_email_or_phone)
    @pytest.mark.parametrize('password', valid_password)
    def test_RT020_registration_with_valid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_with_valid_data(first_name, last_name, email_phone, password)

    # Переход на страницу с пользовательским соглашением (ссылка под кнопкой "Зарегистрироваться")
    def test_RT021_link_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.link_to_the_user_agreement_page()

    # Переход на страницу с пользовательским соглашением (ссылка в футере)
    def test_RT022_link_fut_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.link_fut_to_the_user_agreement_page()

    # Валидация текстового поля (ввод невалидных данных)
    @pytest.mark.parametrize('input_text', invalid_name)
    def test_RT023_text_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.text_field_validation_invalid_data(input_text)

    # Валидация поля ввода email или мобильного телефона (ввод невалидных данных)
    @pytest.mark.parametrize('input_text', invalid_email_or_phone)
    def test_RT024_email_or_phone_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_invalid_data(input_text)

    # Валидация поля ввода пароля (ввод невалидных данных)
    @pytest.mark.parametrize('input_text', invalid_password)
    def test_RT025_password_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_invalid_data(input_text)

    # Заполнение поля подтверждения пароля данными, отличными от введенных в поле ввода пароля
    @pytest.mark.parametrize('password1', valid_password)
    @pytest.mark.parametrize('password2', valid_password2)
    def test_RT026_entering_data_in_the_password_confirmation_field(self, browser, password1, password2):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.entering_data_in_the_password_confirmation_field(password1, password2)

    # Регистрация с невалидными данными
    @pytest.mark.parametrize('first_name', [random_int()])
    @pytest.mark.parametrize('last_name', [first_name_en()])
    @pytest.mark.parametrize('email_phone', [chinese_chars()])
    @pytest.mark.parametrize('password', [russian_chars()])
    def test_RT027_registration_with_invalid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_with_invalid_data(first_name, last_name, email_phone, password)
