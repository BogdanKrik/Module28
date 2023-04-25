Из импорта настроек valid_phone, valid_email, sql_injection 
от . base_page импорт BasePage
от . локаторы импортируют AuthPageLocators, ChangePassPageLocators, UserAgreementPageLocators, \
    RejectedRequestPageLocators, BaseLocators


класс ChangePassPage(BasePage):
    # TRT009 метод проверки типа восстановления пароля по умолчанию
    def default_password_recovery_type(self):
        Самоутвердиться. is_element_present(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "Элемент не найден"

    # TRT010 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного номера)
    def phone_field_validation_valid_data(self):
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_TAB_PHONE). щелчок()
        телефон = valid_phone()
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT). send_keys(телефон)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        элемент = самость. find_element(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = элемент. get_attribute("значение")
        assert ("7"+str(phone)) == значение, "phone не совпадает"

    # TRT011 метод проверки на валидацию поля ввода номера телефона /почты /логина /лицевого счета (ввод валидного email)
    def email_field_validation_valid_data(self):
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_TAB_MAIL). щелчок()
        username_input = себя. find_element(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT)
        электронная почта = valid_email()
        username_input. send_keys(электронная почта)
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        элемент = самость. find_element(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = элемент. get_attribute("значение")
        assert email == значение, "email не совпадает" 

    # TRT012 метод проверки кнопки на форму авторизации
    def go_back_button(self):
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_GO_BACK_BUTTON). щелчок()
        Самоутвердиться. is_element_present(AuthPageLocators. AUTH_HEADING), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

    # TRT013 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = себя. браузер. current_window_handle
        Assert len(self. браузер. window_handles) == 1
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_PRIVACY_POLICY_LINK). щелчок()
        для window_handle в себе. браузер. window_handles:
            Если window_handle != original_window:
                себя. браузер. switch_to. окно(window_handle)
            Еще:
                проходить
        Самоутвердиться. is_element_present(UserAgreementPageLocators. USER_AGREEMENT_HEADING), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/sso-static/agreement/agreement.html» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

    # TRT014 метод проверки восстановления пароля с незаполненными полями
    def password_recovery_with_blank_fields(self):
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_TAB_PHONE). щелчок()
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_CONTINUE_BUTTON). щелчок()
        Утверждение "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               в себе. браузер. current_url, "URL не совпадает"
        Самоутвердиться. is_element_present(ChangePassPageLocators. CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER), \
            "Элемент не найден"

    # TRT015 метод проверки восстановления пароля с незаполненным значением капчи
    def password_recovery_with_blank_captcha(self):
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_TAB_MAIL). щелчок()
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_USERNAME_INPUT). send_keys(valid_email())
        себя. find_element(ChangePassPageLocators. CHANGE_PASS_CONTINUE_BUTTON). щелчок()
        Утверждение "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               в себе. браузер. current_url, "URL не совпадает"
        Самоутвердиться. is_element_present(ChangePassPageLocators. CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT), \
            "Элемент не найден"

    
