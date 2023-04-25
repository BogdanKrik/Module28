Из valid_email импорта настроек  
от . base_page импорт BasePage
от . локаторы импортируют BaseLocators, AuthPageLocators, ChangePassPageLocators, RegPageLocators, \
    UserAgreementPageLocators


класс AuthPage(BasePage):
    # RT001 метод проверки перехода на форму авторизации
    def the_authorization_form_is_open(self):
        Самоутвердиться. is_element_present(AuthPageLocators. AUTH_HEADING)
        утверждать «https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth» в себе. браузер. current_url, \
            «URL-адрес не совпадает»


    # RT002 метод проверки типа аутентификации по умолчанию
    def default_authentication_type(self):
        Самоутвердиться. is_element_present(AuthPageLocators. AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "Элемент не найден"

    # RT003 метод проверки автоматического изменения типа аутентификации
    def automatic_change_of_authentication_type(self):
        себя. find_element(AuthPageLocators. AUTH_USERNAME_INPUT). send_keys(valid_email())
        себя. find_element(BaseLocators. ТЕЛО). щелчок()
        Самоутвердиться. is_element_present(AuthPageLocators. AUTH_USERNAME_INPUT_ACTIV_EMAIL), "элемент не найден"

    # RT004 метод проверки ссылки на форму восстановления пароля
    def link_to_the_password_recovery_form(self):
        себя. find_element(AuthPageLocators. AUTH_FORGOT_PASSWORD_LINK). щелчок()
        Утверждение "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               в себе. браузер. current_url, "URL не совпадает"
        Самоутвердиться. is_element_present(ChangePassPageLocators. CHANGE_PASS_HEADING), "элемент не найден"

    # RT005 метод проверки ссылки на форму регистрации
    def link_to_the_registration_form(self):
        себя. find_element(AuthPageLocators. AUTH_REGISTER_LINK). щелчок()
        Самоутвердиться. is_element_present(RegPageLocators. REG_HEADING), "элемент не найден"
        Утверждайте "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               в себе. браузер. current_url, "URL не совпадает"

    # RT006 метод проверки ссылки под кнопкой "Войти" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = себя. браузер. current_window_handle
        Assert len(self. браузер. window_handles) == 1
        себя. find_element(AuthPageLocators. AUTH_USER_AGREEMENT_LINK). щелчок()
        для window_handle в себе. браузер. window_handles:
            Если window_handle != original_window:
                себя. браузер. switch_to. окно(window_handle)
            Еще:
                проходить
        Самоутвердиться. is_element_present(UserAgreementPageLocators. USER_AGREEMENT_HEADING), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/sso-static/agreement/agreement.html» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

    # RT007 метод проверки ссылки на страницу авторизации с помощью соцсети "ВКонтакте"
    def link_to_social_vk(self):
        себя. find_element(AuthPageLocators. AUTH_SOCIAL_VK_LINK). щелчок()
        утверждать «https://oauth.vk.com/authorize» в себе. браузер. current_url, "URL-адрес не совпадает"

    # RT008 метод проверки авторизации с незаполненными полями
    def authorization_with_blank_fields(self):
        себя. find_element(AuthPageLocators. AUTH_TAB_PHONE). щелчок()
        себя. find_element(AuthPageLocators. AUTH_ENTER_BUTTON). щелчок()
        Самоутвердиться. is_element_present(AuthPageLocators. AUTH_ERROR_ENTER_PHONE_NUMBER), "элемент не найден"
        утверждать «https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth» в себе. браузер. current_url, \
            «URL-адрес не совпадает»

  
