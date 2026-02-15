import allure
from pages.base_page import BasePage
from data.data_urls import *
from locators import BasePageLocators as BPL

class MainPage(BasePage):

    @allure.step('Открыть сайт StellarBurgers')
    def open_main_page(self):
        self.open(BASE_URL)
        self.wait_invisible(BPL.MODAL)

    @allure.step('Ожидаем url главной страницы')
    def wait_url_main_page(self):
        self.wait_url(BASE_URL)

    @allure.step('Клик по «Личный кабинет»')
    def click_personal_account_button(self):
        self.wait_visible(BPL.PERSONAL_ACCOUNT_BUTTON)
        self.wait_clickable_and_click(BPL.PERSONAL_ACCOUNT_BUTTON)
