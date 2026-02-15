import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.data_urls import *
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

    """Ингридиенты"""
    def click_ingredient(self, name):
        locator = (By.XPATH, f"//p[normalize-space()='{name}']")
        self.wait_clickable_and_click(locator)
