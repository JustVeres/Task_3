import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators as BPL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    """Хедеры"""
    @allure.step('Клик по «Личный кабинет» в хедере')
    def click_personal_account_header(self):
        self.wait_visible(BPL.PERSONAL_ACCOUNT_HEADER)
        self.wait_clickable_and_click(BPL.PERSONAL_ACCOUNT_HEADER)

    @allure.step('Клик по «Конструктор» в хедере')
    def click_constructor_header(self):
        self.wait_invisible(BPL.MODAL_OVERLAY)
        self.wait_clickable_and_click(BPL.CONSTRUCTOR_HEADER)

    @allure.step('Клик по «Лента заказов» в хедере')
    def click_order_feed_header(self):
        self.wait_invisible(BPL.MODAL_OVERLAY)
        self.wait_clickable_and_click(BPL.ORDER_FEED_HEADER)

    """Вспомогательные методы"""
    @allure.step('Открыть URL')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ждем элемент и кликаем')
    def wait_clickable_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Ожидаем и возвращаем видимый элемент')
    def wait_visible_return(self, locator): #
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Вводим текст в поле')
    def input_text(self, locator, text):
        element = self.wait_visible_return(locator)
        element.send_keys(text)

    @allure.step('Возвращаем URL')
    def get_url_contains(self, url):
        return self.wait.until(EC.url_contains(url))

    @allure.step('Ожидаем исчезновение элемента')
    def wait_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидаем URL')
    def wait_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step('Клик через JS')
    def js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Находим элемент')
    def find_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Закрываем модальное окно при загрузке страницы')
    def close_modal(self):
        try:
            self.wait.until(EC.visibility_of_element_located(BPL.MODAL_OVERLAY))
            self.wait_clickable_and_click(BPL.CLOSE_MODAL_BUTTON)
            self.wait.until(EC.invisibility_of_element_located(BPL.MODAL_OVERLAY))
        except:
            pass
