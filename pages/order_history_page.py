import allure
from pages.base_page import BasePage
from data.data_urls import *
from locators import OrderHistoryLocators as OHL

class OrderHistoryPage(BasePage):

    @allure.step('Ожидаем URL /order-history')
    def wait_url_order_history(self):
        self.wait_url(ORDER_HISTORY_URL)

    @allure.step('Клик по «История заказов»')
    def click_order_history_link(self):
        self.wait_clickable_and_click(OHL.ORDER_HISTORY_LINK)
