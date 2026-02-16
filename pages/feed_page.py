import allure
from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from locators import OrderFeedLocators as OFL
from helpers import order_by_number

class FeedPage(BasePage):

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
