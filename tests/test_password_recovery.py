import allure
from data.data_urls import *
from data.data_helpers import ResetPasswordPageData as RPPD

class TestPasswordRecovery:

    @allure.title('Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_page_restore_password(self, main_page, login_page, forgot_password_page):

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Переходим в раздел «Личный кабинет»"):
            main_page.click_personal_account_header()

        with allure.step("Кликаем по кнопке «Восстановить пароль»"):
            login_page.click_recover_password()

        with allure.step("Ожидаем загрузки страницы forgot-password"):
            forgot_password_page.wait_url_forgot_password()

        with allure.step('ОР: открылась страница forgot-password'):
            assert forgot_password_page.get_current_url() == FORGOT_PASSWORD_URL


    @allure.title('Восстановление пароля')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_redirect_to_forgot_password_after_click_recover(self, main_page, login_page, forgot_password_page, reset_password_page):

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
            main_page.wait_url_main_page()

        with allure.step("Переходим в раздел «Личный кабинет»"):
            main_page.click_personal_account_header()

        with allure.step("Кликаем по кнопке «Восстановить пароль»"):
            login_page.click_recover_password()

        with allure.step('Заполняем поле «Email»'):
            forgot_password_page.input_field_email()

        with allure.step('Кликаем на кнопку «Восстановить»'):
            forgot_password_page.click_button_restore()

        with allure.step("Ожидаем загрузки страницы reset-password"):
            reset_password_page.wait_url_reset_password()

        with allure.step('ОР: открылась страница reset-password'):
            assert "Восстановление пароля" in reset_password_page.wait_password_recovery_text()
            assert reset_password_page.get_current_url() == RESET_PASSWORD_URL

    @allure.title('Восстановление пароля')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_hidden_password(self, main_page, login_page, forgot_password_page, reset_password_page):

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
            main_page.wait_url_main_page()

        with allure.step("Переходим в раздел «Личный кабинет»"):
            main_page.click_personal_account_header()

        with allure.step("Кликаем по кнопке «Восстановить пароль»"):
            login_page.click_recover_password()

        with allure.step('Заполняем поле «Email»'):
            forgot_password_page.input_field_email()

        with allure.step('Кликаем на кнопку «Восстановить»'):
            forgot_password_page.click_button_restore()

        with allure.step('Заполняем поле «Пароль»'):
            reset_password_page.input_new_password()

        with allure.step('Кликаем на иконку "глаза"'):
            reset_password_page.click_visible_hidden_password_button()

        with allure.step('Ожидаем подсвечивание поля «Пароль»'):
            password_field = reset_password_page.wait_active_password_field()

        with allure.step('ОР: пароль отображается, поле имеет активную подсветку'):
            assert reset_password_page.is_password_field_focused() == reset_password_page.get_active_element()
            assert reset_password_page.get_password_value() == RPPD.password
            assert "input_status_active" in password_field.get_attribute("class")
