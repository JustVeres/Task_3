import allure
from pages.base_page import BasePage
from locators import ForgotPasswordLocators as FPL
from data.data_helpers import ForgotPasswordPageData as FPPD
from data.data_urls import *

class ForgotPasswordPage(BasePage):

    @allure.step('Ввод в поле «Email»')
    def input_field_email(self):
        self.input_text(FPL.EMAIL_FIELD, FPPD.email)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_button_restore(self):
        self.wait_clickable_and_click(FPL.RESTORE_BUTTON)

    @allure.step('Ожидаем URL /forgot-password"')
    def wait_url_forgot_password(self):
        self.wait_url(FORGOT_PASSWORD_URL)
