из селена. Веб-драйвер. Поддержка. wait import WebDriverWait
из селена. Веб-драйвер. поддержка импорта expected_conditions как EC
из селена. общий. исключения импортируют  NoSuchElementException, TimeoutException
от . локаторы импортируют AuthPageLocators


# Конструктор класса. Принимает browser — экземпляр webdriver
класс BasePage():
    def __init__(self, browser, url, timeout=5):
        себя.  браузер = браузер
        себя.  url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        себя. браузер. implicitly_wait(тайм-аут)

    # метод find_element ищет один элемент и возвращает его
    def find_element(self, locator, time=10):
        return WebDriverWait(self. браузер, время). до тех пор, пока(EC. presence_of_element_located(локатор),
                                                       message=f"Не удается найти элемент по локатору {locator}")

    # метод open открывает нужную страницу в браузере, используя метод get()
    def open(self):
        себя. браузер. get(self. URL-адрес)

    # метод open_reg_page открывает форму регистрации в браузере, используя метод get()
    def open_reg_page(self):
        себя. браузер. get(self. URL-адрес)
        себя. find_element(AuthPageLocators. AUTH_REGISTER_LINK). щелчок()

    # метод is_element_present перехватывает исключение
    # будет использоваться для проверки присутствия элемента на странице
    def is_element_present(self, what):
        Попробуйте:
            WebDriverWait(self. браузер, 10). до тех пор, пока(EC. presence_of_element_located(( что)))
        кроме (NoSuchElementException):
            return False
        вернуть Правда

    # метод is_not_element_present будет использоваться для проверки отсутствия элемента на странице
    def is_not_element_present(self, what):
        Попробуйте:
            WebDriverWait(self. браузер, 10). до тех пор, пока(EC. presence_of_element_located(( что)))
        кроме (TimeoutException):
            вернуть Правда
        return False
