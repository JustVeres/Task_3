import allure
import pytest
from data.data_urls import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_page import IngredientPage

class TestBasicFunctionality:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Конструктор»')
    def test_open_after_click_on_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()

        main_page = MainPage(driver)
        main_page.close_modal()
        main_page.click_constructor_header()
        main_page.wait_url_main_page()

        assert main_page.find_create_burger_title() == "Соберите бургер"

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_open_after_click_on_order_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_url_login_page()

        main_page = MainPage(driver)
        main_page.close_modal()
        main_page.click_order_feed_header()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_url_login_page()

        assert driver.current_url == ORDER_FEED_URL
        assert order_feed_page.find_create_burger_title() == "Лента заказов"

    @allure.title('Проверка основного функционала')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize("bun_name", [
        "Краторная булка N-200i",
        "Флюоресцентная булка R2-D3"
    ])
    def test_ingredient_details(self, driver, bun_name):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.close_modal()
        main_page.click_ingredient(bun_name)

        ingredient_page = IngredientPage(driver)

        assert ingredient_page.find_details_ingredient_title() == "Детали ингредиента"
        assert ingredient_page.find_ingredient_name(bun_name) == bun_name