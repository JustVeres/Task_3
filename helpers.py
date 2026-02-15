import random
import string

def random_string(length=8): # Генерируем случайные буквы
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_user_payload():
        return {
            "email": f"{random_string()}@test.com",
            "password": random_string(12),
            "name": random_string(6).capitalize()
        }
