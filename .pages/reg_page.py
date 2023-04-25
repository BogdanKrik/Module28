от . base_page импорт BasePage
от . локаторы импортируют BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators 


класс RegPage(BasePage):
    # TRT016 метод проверки расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        Самоутвердиться. is_element_present(RegPageLocators. REG_FIRST_NAME_INPUT_PAGE_RIGHT), "элемент не найден"
        Самоутвердиться. is_element_present(RegPageLocators. REG_REGISTER_BUTTON_PAGE_RIGHT), "элемент не найден"
        Самоутвердиться. is_element_present(RegPageLocators. REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "элемент не найден"

    # RT017 метод проверки валидации текстового поля (ввод валидных данных)
    def text_field_validation_valid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_FIRST_NAME_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_not_element_present(RegPageLocators. REG_ERROR_FIRST_NAME_INPUT), "найденный элемент"

    # TRT018 метод проверки на валидацию поля ввода email или мобильного телефона (ввод валидных данных)
    def email_or_phone_field_validation_valid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_EMAIL_PHONE_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        элемент = самость. find_element(RegPageLocators. REG_EMAIL_PHONE_INPUT_VALUE)
        value = элемент. get_attribute("значение")
        Assert  input_text == значение, "электронная почта или телефон не совпадают"
        Самоутвердиться. is_not_element_present(RegPageLocators. REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "найденный элемент"

    # RT019 метод проверки на валидацию поля ввода пароля (ввод валидных данных)
    def password_field_validation_valid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_PASSWORD_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_not_element_present(RegPageLocators. REG_ERROR_INVALID_PASSWORD_INPUT), "элемент найден"

    # TRT020 метод проверки регистрации с валидными данными
    def registration_with_valid_data(self, first_name, last_name, email_phone, пароль):
        себя. find_element(RegPageLocators. REG_FIRST_NAME_INPUT). send_keys(first_name)
        себя. find_element(RegPageLocators. REG_LAST_NAME_INPUT). send_keys(last_name)
        себя. find_element(RegPageLocators. REG_EMAIL_PHONE_INPUT). send_keys(email_phone)
        себя. find_element(RegPageLocators. REG_PASSWORD_INPUT). send_keys(пароль)
        себя. find_element(RegPageLocators. REG_PASSWORD_CONFIRM_INPUT). send_keys(пароль)
        себя. find_element(RegPageLocators. REG_ENTER_BUTTON). щелчок()
        Самоутвердиться. is_element_present(EmailConfirmPageLocators. EMAIL_CONF_HEADING), "элемент не найден"

    # TRT021 метод проверки ссылки под кнопкой "Зарегистрироваться" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = себя. браузер. current_window_handle
        Assert len(self. браузер. window_handles) == 1
        себя. find_element(RegPageLocators. REG_USER_AGREEMENT_LINK). щелчок()
        для window_handle в себе. браузер. window_handles:
            Если window_handle != original_window:
                себя. браузер. switch_to. окно(window_handle)
            Еще:
                проходить
        Самоутвердиться. is_element_present(UserAgreementPageLocators. USER_AGREEMENT_HEADING), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/sso-static/agreement/agreement.html» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

    # TRT022 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = себя. браузер. current_window_handle
        Assert len(self. браузер. window_handles) == 1
        себя. find_element(RegPageLocators. REG_PRIVACY_POLICY_LINK). щелчок()
        для window_handle в себе. браузер. window_handles:
            Если window_handle != original_window:
                себя. браузер. switch_to. окно(window_handle)
            Еще:
                проходить
        Самоутвердиться. is_element_present(UserAgreementPageLocators. USER_AGREEMENT_HEADING), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/sso-static/agreement/agreement.html» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

    # TRT023 метод проверки валидации текстового поля (ввод невалидных данных)
    def text_field_validation_invalid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_FIRST_NAME_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_element_present(RegPageLocators. REG_ERROR_FIRST_NAME_INPUT), "элемент не найден"

    # TRT024 метод проверки валидации поля ввода email или мобильного телефона (ввод невалидных данных)
    def email_or_phone_field_validation_invalid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_EMAIL_PHONE_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_element_present(RegPageLocators. REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "элемент не найден"

    # TRT025 метод проверки валидации поля ввода пароля (ввод невалидных данных)
    def password_field_validation_invalid_data(self, input_text):
        себя. find_element(RegPageLocators. REG_PASSWORD_INPUT). send_keys(input_text)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_element_present(RegPageLocators. REG_ERROR_INVALID_PASSWORD_INPUT), "элемент не найден"

    # TRT026 метод проверки заполнения поля подтверждения пароля данными, отличными от введенных в поле ввода пароля
    def entering_data_in_the_password_confirmation_field(self, password1, password2): 
        себя. find_element(RegPageLocators. REG_PASSWORD_INPUT). send_keys(пароль1)
        себя. find_element(RegPageLocators. REG_PASSWORD_CONFIRM_INPUT). send_keys(пароль2)
        себя. find_element(RegPageLocators. REG_ENTER_BUTTON). щелчок()
        Самоутвердиться. is_element_present(RegPageLocators. REG_ERROR_PASSWORD_DONT_MATCH), "элемент не найден"

    # TRT027 метод проверки регистрации с невалидными данными
    def registration_with_invalid_data(self, first_name, last_name, email_phone, пароль):
        себя. find_element(RegPageLocators. REG_FIRST_NAME_INPUT). send_keys(first_name)
        себя. find_element(RegPageLocators. REG_LAST_NAME_INPUT). send_keys(last_name)
        себя. find_element(RegPageLocators. REG_EMAIL_PHONE_INPUT). send_keys(email_phone)
        себя. find_element(RegPageLocators. REG_PASSWORD_INPUT). send_keys(пароль)
        себя. find_element(RegPageLocators. REG_PASSWORD_CONFIRM_INPUT). send_keys(пароль)
        себя. find_element(RegPageLocators. REG_ENTER_BUTTON). щелчок()
        Самоутвердиться. is_not_element_present(EmailConfirmPageLocators. EMAIL_CONF_HEADING), "найденный элемент"
