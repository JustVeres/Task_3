import allure
from pages.base_page import BasePage
from locators import OrderFeedLocators as OFL
from data.data_urls import *

class OrderFeedPage(BasePage):

    @allure.step('Ожидаем URL /stellarburgers/feed')
    def wait_url_login_page(self):
        self.wait_url(ORDER_FEED_URL)

    @allure.step('Находим заголовок «Лента заказов»')
    def find_create_burger_title(self):
        self.wait_visible(OFL.ORDER_FEED_TITLE)
        return self.find_element_text(OFL.ORDER_FEED_TITLE)