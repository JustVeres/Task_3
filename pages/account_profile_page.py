import allure
from pages.base_page import BasePage
from data.data_urls import *
from locators import BasePageLocators as BPL

class AccountProfilePage(BasePage):

    @allure.step('Открываем URL /account/profile')
    def get_open_url_account_profile(self):
        self.open(ACCOUNT_PROFILE_URL)

    @allure.step('Ожидаем URL /account/profile')
    def wait_url_account_profile(self):
        self.wait_url(ACCOUNT_PROFILE_URL)

    @allure.step('Клик по «Выход»')
    def click_logout_link(self):
        self.wait_clickable_and_click(BPL.LOGOUT_LINK)
