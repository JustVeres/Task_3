import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import IngredientPageLocators as IPL

class IngredientPage(BasePage):

    @allure.step('Клик по крестику')
    def close_modal_ingredient(self):
        self.wait_clickable_and_click(IPL.CLOSE_MODAL_BUTTON)
        self.wait_invisible(IPL.INGREDIENT_DETAILS_TITLE)

    @allure.step('Находим заголовок «Детали ингредиента»')
    def find_details_ingredient_title(self):
        return self.find_element_text(IPL.INGREDIENT_DETAILS_TITLE)

    @allure.step('Находим заголовок названия ингредиента')
    def find_ingredient_name(self, name):
        locator = (By.XPATH, f"//p[normalize-space()='{name}']")
        return self.driver.find_element(*locator).text

    @allure.step('Находим метку «Калории»')
    def find_details_calories_label(self):
        return self.find_element_text(IPL.CALORIES_LABEL)

    @allure.step('Находим метку «Белки»')
    def find_details_protein_label(self):
        return self.find_element_text(IPL.PROTEIN_LABEL)

    @allure.step('Находим метку «Жиры»')
    def find_details_fats_label(self):
        return self.find_element_text(IPL.FATS_LABEL)

    @allure.step('Находим метку «Углеводы»')
    def find_details_carbohydrates_label(self):
        return self.find_element_text(IPL.CARBOHYDRATES_LABEL)
