import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.data_urls import *
from data.data_helpers import BadValue
from locators import BasePageLocators as BPL, MainPageLocators as MPL

class MainPage(BasePage):

    @allure.step('Открыть сайт StellarBurgers')
    def open_main_page(self):
        self.open(BASE_URL)
        self.wait_invisible(BPL.MODAL_OVERLAY)

    @allure.step('Ожидаем URL главной страницы')
    def wait_url_main_page(self):
        self.wait_url(BASE_URL)

    @allure.step('Находим заголовок «Соберите бургер»')
    def find_create_burger_title(self):
        return self.find_element_text(MPL.CREATE_BURGER_TITLE)

    @allure.step('Находим конструктор бургера')
    def find_constructor_element(self):
        return self.driver.find_element(*MPL.CONSTRUCTOR_BURGER)

    @allure.step('Клик по кнопке «Оформить заказ»')
    def click_order_button(self):
        self.wait_clickable_and_click(MPL.ORDER_BUTTON)

    """Ингридиенты"""
    @allure.step('Кликаем по ингредиенту')
    def click_ingredient(self, name):
        locator = (By.XPATH, f"//p[normalize-space()='{name}']")
        self.wait_clickable_and_click(locator)

    @allure.step('Находим ингредиент')
    def find_ingredient(self, name):
        return self.driver.find_element(By.XPATH, f"//p[normalize-space()='{name}']")

    @allure.step('Получаем счётчик ингредиента по имени')
    def get_ingredient_counter(self, ingredient_element):
        locator = (By.XPATH, f"//p[text()='{ingredient_element}']/parent::a/div/p")
        return self.find_locator(locator).text

    """Модалка с оформленным заказом"""

    @allure.step('Ждём появления статуса заказа')
    def wait_order_status(self):
        element = self.wait_visible_return(MPL.ORDER_STATUS_MODAL)
        return element.text

    @allure.step('Ждём появления корректного номера заказа')
    def wait_real_order_number(self):
        return self.wait_text_not_equal(MPL.ORDER_ID_MODAL, BadValue.bad_value_order_id)
