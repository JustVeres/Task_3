import allure
from data.data_helpers import BunsIngredient as BI

class TestOrderFeedSection:

    @allure.title('Раздел «Лента заказов»')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_visible_details_order_after_click(self, main_page, feed_page):

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликаем по «Лента заказов»"):
            main_page.click_order_feed_header()

        with allure.step("Запоминаем номер заказа в ленте"):
            expected_number = feed_page.get_first_order_number()

        with allure.step("Кликаем по первому заказу"):
            feed_page.click_first_order()

        with allure.step("Получаем номер заказа из модального окна"):
            actual_number = feed_page.get_order_number_from_modal()

        with allure.step("ОР: Открылось модальное окно"):
            assert feed_page.is_order_modal_open()

        with allure.step("ОР: Открылся соответствующий заказ"):
            assert expected_number == actual_number, f"Открыт неправильный заказ: {actual_number}, ожидался {expected_number}"

    @allure.title('Раздел «Лента заказов»')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_visible_order_history_in_order_feed(self, logged_in_user, main_page, feed_page, account_profile_page, order_history_page):

        with allure.step("Перетаскиваем ингредиент в конструктор"):
            bun = main_page.find_ingredient(BI.flur_bun)
            constructor_area = main_page.find_constructor_element()
            main_page.drag_and_drop_js(bun, constructor_area)

        with allure.step("Клик по кнопке «Оформить заказ»"):
            main_page.click_order_button()
            main_page.wait_real_order_number()

        with allure.step("Запоминаем номер заказа в модальном окне"):
            order_id_in_modal = main_page.get_success_order_number_from_modal()
            main_page.close_modal()
            main_page.wait_invisible_animation()

        with allure.step("Переходим в раздел «Личный кабинет»'"):
            main_page.click_personal_account_header()
            account_profile_page.wait_url_account_profile()

        with allure.step("Открываем историю заказов"):
            order_history_page.click_order_history_link()
            order_history_page.wait_url_order_history()

        with allure.step("Запоминаем номер в истории заказов"):
            order_id_in_history = order_history_page.get_order_history_id()

        with allure.step("Переходим в «Лента заказов»"):
            order_history_page.click_order_feed_header()

        order_id_in_feed = feed_page.find_order(order_id_in_history)

        with allure.step("ОР: номер заказа отображается на всех этапах"):
            assert order_id_in_modal == order_id_in_history == order_id_in_feed

    #@allure.title('Раздел «Лента заказов»')
    #@allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    #def test_when_creating_new_order_counter_increases(self):
