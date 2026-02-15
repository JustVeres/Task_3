import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import IngredientPageLocators as IPL

class IngredientPage(BasePage):

    @allure.step('Находим заголовок «Детали ингредиента»')
    def find_details_ingredient_title(self):
        return self.find_element_text(IPL.INGREDIENT_DETAILS)

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
