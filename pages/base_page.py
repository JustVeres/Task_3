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

    @allure.step('Находим элемент и возвращаем текст')
    def find_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Найти локатор")
    def find_locator(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Закрываем модальное окно при загрузке страницы')
    def close_modal(self):
        try:
            self.wait.until(EC.visibility_of_element_located(BPL.MODAL_OVERLAY))
            self.wait_clickable_and_click(BPL.CLOSE_MODAL_BUTTON)
            self.wait.until(EC.invisibility_of_element_located(BPL.MODAL_OVERLAY))
        except:
            pass

    @allure.step('Используем скрипт на перетаскивание элемента')
    def drag_and_drop_js(self, source, target):
        self.driver.execute_script("""
        const dataTransfer = new DataTransfer();
        ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(eventType => {
        const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
        (eventType === 'dragstart' || eventType === 'dragend' ? arguments[0] : arguments[1]).dispatchEvent(event);
        });
        """, source, target)


    def wait_text_not_equal(self, locator, bad_value):
        def _condition(driver):
            element = driver.find_element(*locator)
            text = element.text.strip()

            if text and text != bad_value:
                return text  # вернём уже корректный текст

            return False

        return self.wait.until(_condition)
