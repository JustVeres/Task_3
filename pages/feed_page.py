import allure
from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from locators import OrderFeedLocators as OFL
from helpers import order_by_number
from data.data_urls import *

class FeedPage(BasePage):

    @allure.step('Ожидаем URL /stellarburgers/feed')
    def wait_url_feed_page(self):
        self.wait_url(ORDER_FEED_URL)

    @allure.step('Находим заголовок «Лента заказов»')
    def find_create_burger_title(self):
        self.wait_visible(OFL.ORDER_FEED_TITLE)
        return self.find_element_text(OFL.ORDER_FEED_TITLE)

    @allure.step('Кликаем по первому видимому заказу в ленте')
    def click_first_order(self):
        orders = self.find_all_elements(OFL.ORDER_ITEMS)
        for order in orders:
            if order.is_displayed():
                self.scroll_to_element(order)
                order.click()
                return
        raise AssertionError("Нет видимых заказов")

    @allure.step("Получаем номер первого заказа из ленты")
    def get_first_order_number(self):
        element = self.wait_visible_return(OFL.ORDER_ID_FEED)
        return element.text.strip()

    @allure.step("Получаем номер заказа из модального окна")
    def get_order_number_from_modal(self):
        element = self.wait_visible_return(OFL.ORDER_ID_MODAL)
        return element.text.strip()

    @allure.step("Проверяем, что модальное окно заказа открылось")
    def is_order_modal_open(self):
        modal = self.wait_visible_return(OFL.ORDER_MODAL)
        return modal.is_displayed()

    @allure.step("Ищем заказ в ленте по номеру")
    def find_order(self, order_number: str, max_attempts=20):

        container = self.wait_visible_return(OFL.ORDER_FEED_BLOCK)
        attempts = 0

        while attempts < max_attempts:
            try:
                element = container.find_element(*order_by_number(order_number))
                return element.text.strip().lstrip("#").lstrip("0")

            except NoSuchElementException:
                self.scroll_container(container)
                attempts += 1

        raise AssertionError(f"Заказ {order_number} не найден в ленте")

    @allure.step("Получение счетчика 'Выполнено за всё время'")
    def get_total_counter_all_time(self):
        counter = self.wait_visible_return(OFL.COUNTER_FOR_ALL_TIME).text
        return int(counter)

    @allure.step("Получаем значение счетчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        counter = self.wait_visible_return(OFL.COUNTER_TODAY).text
        return int(counter)

    @allure.step("Ожидаем увеличение счетчика заказов за все время")
    def wait_total_orders_updated(self, old_value):
        return self.wait_number_to_increase(OFL.COUNTER_FOR_ALL_TIME, old_value)

    @allure.step("Ожидаем увеличение счетчика заказов за сегодня")
    def wait_total_orders_today(self, old_value):
        return self.wait_number_to_increase(OFL.COUNTER_TODAY, old_value)

    @allure.step("Ждём появления заказа в разделе 'В работе'")
    def wait_order_in_progress(self, order_number):
        self.wait_text_to_be_present(OFL.ORDERS_NUMBER_IN_PROGRESS, order_number)
        return order_number
