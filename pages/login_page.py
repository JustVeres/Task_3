import allure
from pages.base_page import BasePage
from locators import LoginPageLocators as LPL, BasePageLocators as BPL
from data.data_urls import *

class LoginPage(BasePage):

    @allure.step('Открыть url stellarburgers/login')
    def open_login_page(self):
        self.open(LOGIN_URL)
        self.wait_url(LOGIN_URL)
        self.wait_invisible(BPL.MODAL)

    @allure.step('Ожидаем url stellarburgers/login')
    def wait_url_login_page(self):
        self.wait_url(LOGIN_URL)

    @allure.step("Находим заголовок «Вход»")
    def find_login_title(self):
        return self.find_element_text(LPL.LOGIN_TITLE)

    @allure.step('Клик по «Восстановить пароль»')
    def click_recover_password(self):
        self.wait_clickable_and_click(LPL.RECOVER_THE_PASSWORD)

    @allure.step('Заполнить поле «Email»')
    def input_email(self, email):
        self.input_text(LPL.EMAIL_FIELD, email)

    @allure.step('Заполнить поле «Пароль»')
    def input_password(self, password):
        self.input_text(LPL.PASSWORD_FIELD, password)

    @allure.step('Клик по кнопке «Войти»')
    def click_login_button(self):
        self.wait_invisible(BPL.MODAL)
        self.js_click(LPL.LOGIN_BUTTON)
