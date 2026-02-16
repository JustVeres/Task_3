import allure
from pages.base_page import BasePage
from locators import ResetPasswordLocators as RPL
from data.data_urls import *
from data.data_helpers import ResetPasswordPageData as RPPD

class ResetPasswordPage(BasePage):

    @allure.step('Ожидание заголовка «Восстановление пароля»')
    def wait_password_recovery_text(self):
        self.get_url_contains(RESET_PASSWORD_URL)
        return self.wait_visible_return(RPL.PASSWORD_RECOVERY).text

    @allure.step('Ввод в поле «Пароль»')
    def input_new_password(self):
        self.input_text(RPL.NEW_PASSWORD_FIELD, RPPD.password)

    @allure.step('Клик по иконке «Глаз»')
    def click_visible_hidden_password_button(self):
        self.wait_visible_return(RPL.HIDDEN_PASSWORD_BUTTON)
        self.click(RPL.HIDDEN_PASSWORD_BUTTON)

    @allure.step('Ждем, что поле «Пароль» заполнено и возвращаем значение')
    def get_password_value(self):
        element = self.wait_visible_return(RPL.NEW_PASSWORD_FIELD)
        return element.get_attribute("value")

    @allure.step('Ожидаем видимость поля «Пароль»')
    def is_password_field_focused(self):
        return self.wait_visible_return(RPL.NEW_PASSWORD_FIELD)

    @allure.step('Ожидаем подсвечивание поля «Пароль»')
    def wait_active_password_field(self):
        return self.wait_visible_return(RPL.PASSWORD_FIELD_ACTIVE)

    @allure.step('Ожидаем URL /reset-password')
    def wait_url_reset_password(self):
        self.wait_url(RESET_PASSWORD_URL)
