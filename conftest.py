import pytest
from selenium import webdriver
from api_methods import UserApiMethods
from pages.login_page import LoginPage

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
