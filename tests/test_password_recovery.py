import allure
from data.data_urls import *
from data.data_helpers import ResetPasswordPageData as RPPD
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:

    @allure.title('Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_page_restore_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_recover_password()
        assert driver.current_url == FORGOT_PASSWORD_URL


    @allure.title('Восстановление пароля')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_redirect_to_forgot_password_after_click_recover(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_recover_password()

        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_field_email()
        forgot_password_page.click_button_restore()

        reset_password_page = ResetPasswordPage(driver)

        assert "Восстановление пароля" in reset_password_page.wait_password_recovery_text()
        assert driver.current_url == RESET_PASSWORD_URL

    @allure.title('Восстановление пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_hidden_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_recover_password()

        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.input_field_email()
        forgot_password_page.click_button_restore()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.input_new_password()
        reset_password_page.click_visible_hidden_password_button()

        password_field = reset_password_page.wait_active_password_field()

        assert reset_password_page.is_password_field_focused() == driver.switch_to.active_element
        assert reset_password_page.get_password_value() == RPPD.password
        assert "input_status_active" in password_field.get_attribute("class")
