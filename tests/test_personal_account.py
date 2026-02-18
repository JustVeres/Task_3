import allure
from data.data_urls import *

class TestPersonalAccount:

    @allure.title('Личный кабинет ')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_open_page_personal_account(self, logged_in_user, main_page, account_profile_page):

        with allure.step('Ожидаем загрузки главной страницы и кликаем по «Личный кабинет»'):
            main_page.wait_url_main_page()
            main_page.click_personal_account_header()

        with allure.step('Ожидаем загрузки страницы account/profile'):
            account_profile_page.wait_url_account_profile()

        with allure.step('ОР: открылась страница account/profile'):
            assert account_profile_page.get_current_url() == ACCOUNT_PROFILE_URL

    @allure.title('Личный кабинет ')
    @allure.description('Переход в раздел «История заказов»')
    def test_open_page_order_history(self, logged_in_user, main_page, order_history_page):

        with allure.step('Ожидаем загрузки главной страницы и кликаем по «Личный кабинет»'):
            main_page.wait_url_main_page()
            main_page.click_personal_account_header()

        with allure.step('Переходим в раздел «История заказов»'):
            order_history_page.click_order_history_link()
            order_history_page.wait_url_order_history()

        with allure.step('ОР: открылась страница account/order-history'):
            assert order_history_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title('Личный кабинет ')
    @allure.description('Выход из аккаунта')
    def test_logout_account_profile(self, logged_in_user, main_page, account_profile_page, login_page):

        with allure.step('Ожидаем загрузки главной страницы и кликаем по «Личный кабинет»'):
            main_page.wait_url_main_page()
            main_page.click_personal_account_header()
            account_profile_page.wait_url_account_profile()

        with allure.step('Выходим из аккаунта'):
            account_profile_page.click_logout_link()


        with allure.step('Ожидаем загрузки со страницей входа'):
            login_page.wait_url_login_page()

        with allure.step('ОР: открылась страница для входа'):
            assert login_page.get_current_url() == LOGIN_URL
            assert login_page.find_login_title() == "Вход"
