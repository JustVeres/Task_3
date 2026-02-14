import allure
from pages.base_page import BasePage
from locators import LoginPageLocators as LPL

class LoginPage(BasePage):

    @allure.step('Клик по «Восстановить пароль»')
    def click_recover_password(self):
        self.wait_clickable_and_click(LPL.RECOVER_THE_PASSWORD)
