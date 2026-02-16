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
        self.click(OHL.ORDER_HISTORY_LINK)

    @allure.step("Получаем номер заказа из истории заказов")
    def get_order_history_id(self):
        #element = self.wait_visible_return(OHL.ORDER_ITEMS)
        #return element.text.lstrip("#")
        element = self.wait_visible_return(OHL.ORDER_ITEMS)
        order_id_str = element.text.lstrip("#")
        return str(int(order_id_str))
