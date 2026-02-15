from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url): # Открываем url
        self.driver.get(url)

    def wait_clickable_and_click(self, locator): # Ждем элемент и кликаем
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_visible_return(self, locator): # Ожидание видимости элемента
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_visible(self, locator): # Ожидание видимости элемента
        self.wait.until(EC.visibility_of_element_located(locator))

    def input_text(self, locator, text): # Вводим текст в поле
        element = self.wait_visible_return(locator)
        element.send_keys(text)

    def get_url_contains(self, url): # ожидаем url
        return self.wait.until(EC.url_contains(url))

    def wait_invisible(self, locator): # Ожидаем исчезновение элемента
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_url(self, url): # Ожидаем url
        self.wait.until(EC.url_to_be(url))

    def js_click(self, locator): # Клик через JS
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def find_element_text(self, locator): # Находим элемент
        return self.driver.find_element(*locator).text
