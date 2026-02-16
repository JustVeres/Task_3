import random
import string
from selenium.webdriver.common.by import By

def random_string(length=8): # Генерируем случайные буквы
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_user_payload():
        return {
            "email": f"{random_string()}@test.com",
            "password": random_string(12),
            "name": random_string(6).capitalize()
        }

def order_by_number(number: str):
    return By.XPATH, f".//p[contains(text(), '{number}')]"