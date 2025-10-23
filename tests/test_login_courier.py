import pytest
import requests
import allure
from data import LOGIN_COURIER_URL, STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_404, ERROR_MESSAGES
from api.courier_api import create_courier, delete_courier_by_credentials
from helpers.helpers_on_check_response import check_response_status_code, check_response_has_id, check_response_has_error_message


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        login = f"login_test_{courier_data[0]}"
        password = "password123"
        first_name = "Test"
        
        create_response = create_courier(login, password, first_name)
        assert create_response.status_code == 201, "Курьер должен быть создан"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_200)
        check_response_has_id(response)
        
        delete_courier_by_credentials(login, password)

    @allure.title("Авторизация без логина")
    def test_login_courier_missing_login_fails(self):
        import time
        timestamp = str(int(time.time()))
        password = f"password_{timestamp}"
        
        payload = {
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    @allure.title("Авторизация без пароля")
    def test_login_courier_missing_password_fails(self):
        import time
        timestamp = str(int(time.time()))
        login = f"test_login_{timestamp}"
        
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
    def test_login_courier_wrong_login_fails(self):
        import time
        timestamp = str(int(time.time()))
        login = f"nonexistent_user_{timestamp}"
        password = "password123"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

    @allure.title("Авторизация с неправильным паролем")
    def test_login_courier_wrong_password_fails(self):
        import time
        timestamp = str(int(time.time()))
        login = f"wrong_password_test_{timestamp}"
        password = "correct_password"
        first_name = "Test"
        
        create_response = create_courier(login, password, first_name)
        assert create_response.status_code == 201, "Курьер должен быть создан"
        
        wrong_password = "wrong_password"
        payload = {
            "login": login,
            "password": wrong_password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])
        
        delete_courier_by_credentials(login, password)

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_courier_nonexistent_user_fails(self):
        import time
        timestamp = str(int(time.time()))
        login = f"nonexistent_user_{timestamp}"
        password = "password123"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_404)
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

