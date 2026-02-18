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

    @allure.title('Раздел «Лента заказов»')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_total_counter_increases_after_order(self, logged_in_user, main_page, feed_page):

        with allure.step("Открываем ленту заказов"):
            main_page.click_order_feed_header()
            feed_page.wait_url_feed_page()

        with allure.step("Запоминаем текущее значение счетчика за все время"):
            old_total = feed_page.get_total_counter_all_time()

        with allure.step("Переходим в конструктор"):
            feed_page.click_constructor_header()

        with allure.step("Собираем бургер"):
            bun = main_page.find_ingredient(BI.flur_bun)
            area = main_page.find_constructor_element()
            main_page.drag_and_drop_js(bun, area)

        with allure.step("Оформляем заказ"):
            main_page.click_order_button()
            main_page.wait_real_order_number()
            main_page.close_modal()

        with allure.step("Снова открываем ленту заказов"):
            main_page.click_order_feed_header()
            feed_page.wait_url_feed_page()

        with allure.step("Ждём обновления счетчика"):
            new_total = feed_page.wait_total_orders_updated(old_total)

        with allure.step("ОР: счетчик «Выполнено за всё время» увеличился"):
            assert new_total > old_total

    @allure.title('Раздел «Лента заказов»')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_counter_increment_after_order(self, logged_in_user, main_page, feed_page):

        with allure.step("Открываем ленту заказов"):
            main_page.click_order_feed_header()
            feed_page.wait_url_feed_page()

        with allure.step("Запоминаем текущее значение счетчика за сегодня"):
            old_total_today = feed_page.get_today_counter()

        with allure.step("Переходим в конструктор"):
            feed_page.click_constructor_header()

        with allure.step("Собираем бургер"):
            bun = main_page.find_ingredient(BI.flur_bun)
            area = main_page.find_constructor_element()
            main_page.drag_and_drop_js(bun, area)

        with allure.step("Оформляем заказ"):
            main_page.click_order_button()
            main_page.wait_real_order_number()
            main_page.close_modal()

        with allure.step("Снова открываем ленту заказов"):
            main_page.click_order_feed_header()
            feed_page.wait_url_feed_page()

        with allure.step("Ждём обновления счетчика за сегодня"):
            new_total_today = feed_page.wait_total_orders_today(old_total_today)

        with allure.step("ОР: счетчик «Выполнено за сегодня» увеличился"):
            assert new_total_today > old_total_today

    @allure.title('Раздел «Лента заказов»')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_creating_order_id_have_status_in_progress(self, logged_in_user, main_page, feed_page):

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

        with allure.step("Переходим в «Лента заказов» и ожидаем заказ в разделе «В работе»"):
            feed_page.click_order_feed_header()
            order_id_in_progress = feed_page.wait_order_in_progress(order_id_in_modal)

        with allure.step("ОР: созданный заказ отображается в разделе «В работе»"):
            assert order_id_in_modal == order_id_in_progress
