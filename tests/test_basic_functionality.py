import allure
import pytest
from data.data_urls import *
from data.data_titles import *
from data.data_helpers import BadValue, BunsIngredient as BI
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_page import IngredientPage

class TestBasicFunctionality:

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Конструктор»')
    def test_open_after_click_on_constructor(self, driver):
        with allure.step("Открываем страницу с логином"):
            login_page = LoginPage(driver)
            login_page.open_login_page()

        main_page = MainPage(driver)
        with allure.step("Кликаем на «Конструктор»"):
            main_page.click_constructor_header()
            main_page.wait_url_main_page()

        with allure.step("ОР: Открылся раздел «Конструктор»"):
            assert main_page.find_create_burger_title() == "Соберите бургер"

    @allure.title('Проверка основного функционала')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_open_after_click_on_order_feed(self, driver):
        with allure.step("Открываем страницу с логином"):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            login_page.wait_url_login_page()

        main_page = MainPage(driver)
        with allure.step("Кликаем по «Лента заказов»"):
            main_page.click_order_feed_header()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_url_feed_page()

        with allure.step("ОР: Открылся раздел «Лента заказов»"):
            assert driver.current_url == ORDER_FEED_URL
            assert order_feed_page.find_create_burger_title() == "Лента заказов"

    @allure.title('Проверка основного функционала')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize("bun_name", [
        f"{BI.crator_bun}",
        f"{BI.flur_bun}"
    ])
    def test_visible_ingredient_details(self, driver, bun_name):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем по ингредиенту"):
            main_page.click_ingredient(bun_name)

        ingredient_page = IngredientPage(driver)

        with allure.step("ОР: Отображается модальное окно с информацией об ингредиенте"):
            assert ingredient_page.find_details_ingredient_title() == details_ingredient_title
            assert ingredient_page.find_ingredient_name(bun_name) == bun_name
            assert ingredient_page.find_details_calories_label() == "Калории,ккал"
            assert ingredient_page.find_details_protein_label() == "Белки, г"
            assert ingredient_page.find_details_fats_label() == "Жиры, г"
            assert ingredient_page.find_details_carbohydrates_label() == "Углеводы, г"

    @allure.title('Проверка основного функционала')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_close_modal_ingredient_details(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step(f"Кликаем по «{BI.crator_bun}»"):
            main_page.click_ingredient(BI.crator_bun)

        ingredient_page = IngredientPage(driver)
        with allure.step("Нажать на крестик модального окна"):
            ingredient_page.close_modal()

        with allure.step("ОР: Модальное окно закрылось"):
            assert ingredient_page.find_details_ingredient_title() != details_ingredient_title

    @allure.title('Проверка основного функционала')
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize("ingredient_name", [
        f"{BI.crator_bun}",
        f"{BI.flur_bun}"
    ])
    def test_add_ingredient_and_counter(self, driver, ingredient_name):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Перетаскиваем ингредиент в конструктор"):
            bun = main_page.find_ingredient(ingredient_name)
            constructor_area = main_page.find_constructor_element()
            main_page.drag_and_drop_js(bun, constructor_area)

        with allure.step("Проверяем, что счётчик увеличился"):
           counter = main_page.get_ingredient_counter(ingredient_name)

        with allure.step("ОР: счетчик булки = 2"):
            assert counter == "2"


    @allure.title('Проверка основного функционала')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_an_order(self, driver, logged_in_user):
        main_page = MainPage(driver)

        with allure.step("Перетаскиваем ингредиент в конструктор"):
            bun = main_page.find_ingredient(BI.flur_bun)
            constructor_area = main_page.find_constructor_element()
            main_page.drag_and_drop_js(bun, constructor_area)

        with allure.step("Клик по кнопке «Оформить заказ»"):
            main_page.click_order_button()

        with allure.step("ОР: в модальном окне есть информация о заказе"):
            assert main_page.wait_real_order_number() is not None
            assert main_page.wait_real_order_number() != BadValue.bad_value_order_id
            assert main_page.wait_order_status() == "Ваш заказ начали готовить"
