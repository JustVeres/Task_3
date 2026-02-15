import allure
from data.data_urls import *
from pages.main_page import MainPage
from pages.account_profile_page import AccountProfilePage
from pages.order_history_page import OrderHistoryPage
from pages.login_page import LoginPage

class TestPersonalAccount:

    @allure.title('Личный кабинет ')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_open_page_personal_account(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.wait_url_main_page()
        main_page.click_personal_account_button()

        account_profile_page = AccountProfilePage(driver)
        account_profile_page.wait_url_account_profile()

        assert driver.current_url == ACCOUNT_PROFILE_URL

    @allure.title('Личный кабинет ')
    @allure.description('Переход в раздел «История заказов»')
    def test_open_page_order_history(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.wait_url_main_page()
        main_page.click_personal_account_button()

        order_history_page = OrderHistoryPage(driver)
        order_history_page.click_order_history_link()
        order_history_page.wait_url_order_history()

        assert driver.current_url == ORDER_HISTORY_URL

    @allure.title('Личный кабинет ')
    @allure.description('Выход из аккаунта')
    def test_logout_account_profile(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.wait_url_main_page()
        main_page.click_personal_account_button()

        account_profile_page = AccountProfilePage(driver)
        account_profile_page.wait_url_account_profile()
        account_profile_page.click_logout_link()

        login_page = LoginPage(driver)
        login_page.wait_url_login_page()

        assert driver.current_url == LOGIN_URL
        assert login_page.find_login_title() == "Вход"
