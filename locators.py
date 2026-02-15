from selenium.webdriver.common.by import By

class BasePageLocators:
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[p[normalize-space()='Личный Кабинет']]")
    LOGOUT_LINK = (By.XPATH, "//button[normalize-space()='Выход']")

class OrderHistoryLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[normalize-space()='История заказов']")

class LoginPageLocators: # /login
    RECOVER_THE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, 'Пароль')
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    LOGIN_TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")

class ForgotPasswordLocators: # /forgot-password
    EMAIL_FIELD = (By.XPATH, "//input[contains(@class,'input__textfield') and @name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

class ResetPasswordLocators: # /reset-password
    PASSWORD_RECOVERY = (By.XPATH, "//h2[text()='Восстановление пароля']")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    HIDDEN_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon')]")
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input_status_active")
