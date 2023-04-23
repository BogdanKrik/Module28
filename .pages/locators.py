из селена. Веб-драйвер. общий. по импорту По

класс BaseLocators:
    ТЕЛО = (По. XPATH, "//body")

класс AuthPageLocators:
    AUTH_HEADING = (По. XPATH, "//h1[contains(text(),'Авторизация')]")
    AUTH_LOGO = (По. XPATH, "//section[@id='page-left']/*/div[@class='what-is-container__logo-container']/*")
    AUTH_SLOGAN = (По. XPATH,
                   "//section[@id='page-left']/*//p[contains(text(),'Персональный помощник в цифровом мире "
                   "Ростелекома')]")
    AUTH_TAB_MENU = (По. XPATH,
                     "//section[@id='page-right']/*//div[@id='t-btn-tab-phone' или @id='t-btn-tab-mail' или "
                     "@id='t-btn-tab-login' или @id='t-btn-tab-ls']")
    AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE = (По. XPATH, "//span[contains(text(),'Мобильный телефон')]")
    AUTH_USERNAME_INPUT = (По. XPATH, "//input[@id='username']")
    AUTH_USERNAME_INPUT_ACTIV_EMAIL = (По. XPATH, "//span[contains(text(),'Электронная почта')]")
    AUTH_FORGOT_PASSWORD_LINK = (По. XPATH, "//a[@id='forgot_password']")
    AUTH_REGISTER_LINK = (По. XPATH, "//a[@id='kc-register']")
    AUTH_USER_AGREEMENT_LINK = (По. XPATH,
                                "//span[contains(text(),'Нажимая кнопку «Войти», вы принимаете "
                                "условия')]/follow-sibling::a")
    AUTH_PRIVACY_POLICY_LINK = (По. XPATH, "//a[@id='rt-footer-agreement-link']")
    AUTH_SOCIAL_VK_LINK = (По. XPATH, "//a[@id='oidc_vk']")
    AUTH_TAB_PHONE = (По. XPATH, "//div[@id='t-btn-tab-phone']")
    AUTH_ENTER_BUTTON = (По. XPATH, "//button[@id='kc-login']")
    AUTH_ERROR_ENTER_PHONE_NUMBER = (По. XPATH, "//span[contains(text(),'Введите номер телефона')]")
    AUTH_PASSWORD_INPUT = (По. XPATH, "//input[@id='password']")
    AUTH_HEADING_BY_CODE = (По. XPATH, "//h1[contains(text(),'Авторизация по коду')]")

класс ChangePassPageLocators:
    CHANGE_PASS_HEADING = (По. XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE = (По. XPATH, "//span[contains(text(),'Мобильный телефон')]")
    CHANGE_PASS_TAB_PHONE = (По. XPATH, "//div[@id='t-btn-tab-phone']")
    CHANGE_PASS_USERNAME_INPUT = (По. XPATH, "//input[@id='username']")
    CHANGE_PASS_USERNAME_INPUT_VALUE = (По. XPATH, "//input[@name='username']")
    CHANGE_PASS_TAB_MAIL = (По. XPATH, "//div[@id='t-btn-tab-mail']")
    CHANGE_PASS_GO_BACK_BUTTON = (По. XPATH, "//button[@id='reset-back']")
    CHANGE_PASS_PRIVACY_POLICY_LINK = (По. XPATH, "//a[@id='rt-footer-agreement-link']")
    CHANGE_PASS_CONTINUE_BUTTON = (По. XPATH, "//button[@id='reset']")
    CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER = (По. XPATH, "//span[contains(text(),'Введите номер телефона')]")
    CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT = (
    Мимо. XPATH, "//span[@id='form-error-message' и contains(text(),'Неверный логин или текст с картинки')]")

класс RegPageLocators:
    REG_HEADING = (По. XPATH, "//h1[contains(text(),'Регистрация')]")
    REG_FIRST_NAME_INPUT_PAGE_RIGHT = (
    Мимо. XPATH, "//section[@id='page-right']//span[contains(text(),'Имя')]/preceding-sibling::input")
    REG_REGISTER_BUTTON_PAGE_RIGHT = (
    Мимо. XPATH, "//section[@id='page-right']//span[contains(text(),'Зарегистрироваться')]")
    REG_USER_AGREEMENT_LINK_PAGE_RIGHT = (По. XPATH,
                                          "//section[@id='page-right']//span[contains(text(),'Нажимая кнопку "
                                          "«Зарегистрироваться», вы принимаете условия')]/follow-sibling::a")
    REG_FIRST_NAME_INPUT = (По. XPATH, "//span[contains(text(),'Имя')]/preceding-sibling::input")
    REG_ERROR_FIRST_NAME_INPUT = (
    Мимо. XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    REG_EMAIL_PHONE_INPUT = (По. XPATH, "//input[@id='address']")
    REG_EMAIL_PHONE_INPUT_VALUE = (По. XPATH, "//input[@type='hidden' и @name='address']")
    REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT = (
    Мимо. XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХХ или +375XXX')]")
    REG_PASSWORD_INPUT = (По. XPATH, "//input[@id='password']")
    REG_ERROR_INVALID_PASSWORD_INPUT = (
    Мимо. XPATH, "//span[contains(text(),'Пароль должен') или contains(text(),'Длина пароля')]")
    REG_LAST_NAME_INPUT = (По. XPATH, "//span[contains(text(),'Фамилия')]/preceding-sibling::input")
    REG_PASSWORD_CONFIRM_INPUT = (По. XPATH, "//input[@id='password-confirm']")
    REG_ENTER_BUTTON = (
    Мимо. XPATH, "//button[@class='rt-btn rt-btn--оранжевый rt-btn--средний rt-btn--округленный регистр-form__reg-btn']")
    REG_USER_AGREEMENT_LINK = (По. XPATH,
                               "//span[contains(text(),'Нажимая кнопку «Зарегистрироваться», "
                               "вы принимаете условия')]/follow-sibling::a")
    REG_PRIVACY_POLICY_LINK = (По. XPATH, "//a[@id='rt-footer-agreement-link']")
    REG_ERROR_PASSWORD_DONT_MATCH = (По. XPATH, "//span[contains(text(),'Пароли не совпадают')]")

класс EmailConfirmPageLocators:
    EMAIL_CONF_HEADING = (По. XPATH, "//p[contains(text(),'Kод подтверждения отправлен')]")

класс UserAgreementPageLocators:
    USER_AGREEMENT_HEADING = (По. XPATH, "//h1[contains(text(),'Пользователь')]")

класс RejectedRequestPageLocators:
    REJECTED_REQUEST_HEADING = (
    Мимо. XPATH, "//h2[contains(text(),'Ваш запрос был отклонен из соображений безопасности.')]")
    REJECTED_REQUEST_INFO = (По. XPATH, "//div[contains(text(),'Код запроса: ')]")
