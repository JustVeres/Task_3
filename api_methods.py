import requests
import allure
from data.data_urls import *
from helpers import *

class UserApiMethods:

    @staticmethod
    @allure.step("Создать/зарегистрировать пользователя")
    def create_user_api():
        payload = create_user_payload()
        response = requests.post(AUTH_REGISTER_API, json=payload)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        return response.status_code, response.json(), payload

    @allure.step("Удалить пользователя")
    def delete_user_api(self, access_token: str):
        headers = {"Authorization": access_token}
        response = requests.delete(DELETE_USER_API, headers=headers)
        return response.status_code, response.json()
