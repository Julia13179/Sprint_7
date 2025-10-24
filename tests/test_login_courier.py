import pytest
import requests
import allure
from data import LOGIN_COURIER_URL, STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_404, ERROR_MESSAGES
from api.courier_api import create_courier, delete_courier_by_credentials
from helpers.helpers_on_check_response import check_response_status_code, check_response_has_id, check_response_has_error_message


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_200)
        check_response_has_id(response)

    @allure.title("Авторизация без логина")
    def test_login_courier_missing_login_fails(self, unique_password):
        password = unique_password
        
        payload = {
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    @allure.title("Авторизация без пароля")
    def test_login_courier_missing_password_fails(self, unique_login):
        login = unique_login
        
        payload = {
            "login": login
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    @allure.title("Авторизация с пустым телом запроса")
    def test_login_courier_empty_payload_fails(self):
        payload = {}
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    @allure.title("Авторизация с неправильным логином")
    def test_login_courier_wrong_login_fails(self, nonexistent_user_data):
        login = nonexistent_user_data["login"]
        password = nonexistent_user_data["password"]
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

    @allure.title("Авторизация с неправильным паролем")
    def test_login_courier_wrong_password_fails(self, courier_data, wrong_password):
        payload = {
            "login": courier_data[0],
            "password": wrong_password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_courier_nonexistent_user_fails(self, nonexistent_user_data):
        payload = {
            "login": nonexistent_user_data["login"],
            "password": nonexistent_user_data["password"]
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

