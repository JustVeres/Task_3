import pytest
from selenium import webdriver
from api_methods import UserApiMethods
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_page import IngredientPage
from pages.account_profile_page import AccountProfilePage
from pages.order_history_page import OrderHistoryPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

"""Запуск браузера Chrome/Firefox"""
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    yield driver
    driver.quit()

"""Регистрация и логин пользователя"""
@pytest.fixture
def logged_in_user(driver):
    # 1. Создаем пользователя через API
    status, body, payload = UserApiMethods.create_user_api()
    access_token = body["accessToken"]

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.input_email(payload["email"])
    login_page.input_password(payload["password"])
    login_page.click_login_button()

    # 3. Возвращаем данные пользователя для теста
    yield {
        "email": payload["email"],
        "password": payload["password"],
        "access_token": access_token
    }

    # 4. Удаляем пользователя через API
    UserApiMethods().delete_user_api(access_token)

"""Фикстуры для страниц"""
@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)
    return order_feed_page

@pytest.fixture
def ingredient_page(driver):
    ingredient_page = IngredientPage(driver)
    return ingredient_page

@pytest.fixture
def account_profile_page(driver):
    account_profile_page = AccountProfilePage(driver)
    return account_profile_page

@pytest.fixture
def order_history_page(driver):
    order_history_page = OrderHistoryPage(driver)
    return order_history_page

@pytest.fixture
def forgot_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    return forgot_password_page

@pytest.fixture
def reset_password_page(driver):
    reset_password_page = ResetPasswordPage(driver)
    return reset_password_page