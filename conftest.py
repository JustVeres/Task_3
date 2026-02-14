import pytest
from selenium import webdriver

"""Фикстура для запуска браузера"""
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
