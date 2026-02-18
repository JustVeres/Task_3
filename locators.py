from selenium.webdriver.common.by import By

class BasePageLocators:
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay__x2ZCr']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close_modified')]")
    MODAL_OVERLAY_ANIMATION = (By.XPATH, "//img[contains(@alt, 'loading animation')]")
    PERSONAL_ACCOUNT_HEADER = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_HEADER = (By.XPATH, "//p[normalize-space()='Конструктор']")
    ORDER_FEED_HEADER = (By.XPATH, "//a[.//p[normalize-space()='Лента Заказов']]")
    LOGOUT_LINK = (By.XPATH, "//button[normalize-space()='Выход']")

class MainPageLocators:
    CREATE_BURGER_TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    CONSTRUCTOR_BURGER = (By.CSS_SELECTOR, '.constructor-element_pos_bottom > span:nth-child(1) > span:nth-child(2)')
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ID_MODAL = (By.XPATH, "//h2[contains(@class,'Modal_modal__title') and not(text()='')]")
    ORDER_STATUS_MODAL = (By.XPATH, "//p[normalize-space()='Ваш заказ начали готовить']")

class IngredientPageLocators:
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")
    CALORIES_LABEL = (By.XPATH, "//p[normalize-space()='Калории,ккал']")
    PROTEIN_LABEL = (By.XPATH, "//p[normalize-space()='Белки, г']")
    FATS_LABEL = (By.XPATH, "//p[normalize-space()='Жиры, г']")
    CARBOHYDRATES_LABEL = (By.XPATH, "//p[normalize-space()='Углеводы, г']")

class OrderHistoryLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[normalize-space()='История заказов']")
    ORDER_ITEMS = (By.XPATH, "//p[contains(@class,'text text_type_digits-default')]")

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

class OrderFeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    ORDER_ITEMS = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]//p[starts-with(text(),'#')]")
    ORDER_ID_FEED = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]//p[contains(@class,'text_type_digits-default')]")
    ORDER_ID_MODAL = (By.XPATH,"//div[contains(@class,'Modal_modal__contentBox')]//p[contains(@class,'text_type_digits-default')]")
    ORDER_FEED_BLOCK = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")
    ORDER_NUMBER = (By.CSS_SELECTOR, "p.text_type_digits-default")
    COUNTER_FOR_ALL_TIME = (By.XPATH, "//p[normalize-space(text())='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[normalize-space(text())='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_NUMBER_IN_PROGRESS = (By.XPATH, "//p[normalize-space(text())='В работе:']/following-sibling::ul/li")
