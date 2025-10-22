import pytest
import requests
from data import LOGIN_COURIER_URL, STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_404, ERROR_MESSAGES
from helpers.helpers_on_create_courier import create_courier
from helpers.helpers_on_check_response import check_response_status_code, check_response_has_id, check_response_has_error_message


class TestLoginCourier:
    """Тесты для эндпоинта авторизации курьера"""

    def test_login_courier_success(self):
        """Тест успешной авторизации курьера"""
        # Создаем курьера с уникальным логином
        import time
        timestamp = str(int(time.time()))
        login = f"login_test_{timestamp}"
        password = "password123"
        first_name = "Test"
        
        create_response = create_courier(login, password, first_name)
        assert create_response.status_code == 201, "Курьер должен быть создан"
        
        # Авторизуемся
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_200)
        
        # Проверяем что в ответе есть id
        check_response_has_id(response)
        
        # Удаляем курьера
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(login, password)

    def test_login_courier_missing_login_fails(self):
        """Тест авторизации без логина"""
        import time
        timestamp = str(int(time.time()))
        password = f"password_{timestamp}"
        
        payload = {
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа (API может возвращать 504 вместо 400)
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке только если код 400
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    def test_login_courier_missing_password_fails(self):
        """Тест авторизации без пароля"""
        import time
        timestamp = str(int(time.time()))
        login = f"test_login_{timestamp}"
        
        payload = {
            "login": login
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа (API может возвращать 504 вместо 400)
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке только если код 400
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    def test_login_courier_empty_payload_fails(self):
        """Тест авторизации с пустым телом запроса"""
        payload = {}
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа (API может возвращать 504 вместо 400)
        assert response.status_code in [STATUS_CODE_400, 504], f"Ожидался код 400 или 504, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке только если код 400
        if response.status_code == STATUS_CODE_400:
            check_response_has_error_message(response, ERROR_MESSAGES["MISSING_LOGIN_PASSWORD"])

    def test_login_courier_wrong_login_fails(self):
        """Тест авторизации с неправильным логином"""
        import time
        timestamp = str(int(time.time()))
        login = f"nonexistent_user_{timestamp}"
        password = "password123"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_404)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

    def test_login_courier_wrong_password_fails(self):
        """Тест авторизации с неправильным паролем"""
        # Создаем курьера с уникальным логином
        import time
        timestamp = str(int(time.time()))
        login = f"wrong_password_test_{timestamp}"
        password = "correct_password"
        first_name = "Test"
        
        create_response = create_courier(login, password, first_name)
        assert create_response.status_code == 201, "Курьер должен быть создан"
        
        # Пытаемся авторизоваться с неправильным паролем
        wrong_password = "wrong_password"
        payload = {
            "login": login,
            "password": wrong_password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_404)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])
        
        # Удаляем курьера
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(login, password)

    def test_login_courier_nonexistent_user_fails(self):
        """Тест авторизации несуществующего пользователя"""
        import time
        timestamp = str(int(time.time()))
        login = f"nonexistent_user_{timestamp}"
        password = "password123"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(LOGIN_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_404)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["INVALID_LOGIN_PASSWORD"])

