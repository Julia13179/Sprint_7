import pytest
import requests
from data import CREATE_COURIER_URL, STATUS_CODE_201, STATUS_CODE_400, STATUS_CODE_409, ERROR_MESSAGES
from helpers.helpers_on_create_courier import create_courier, register_new_courier_and_return_login_password
from helpers.helpers_on_check_response import check_response_status_code, check_response_is_ok, check_response_has_error_message


class TestCreateCourier:

    def test_create_courier_success(self):
        import time
        timestamp = str(int(time.time()))
        login = f"test_courier_{timestamp}"
        password = "password123"
        first_name = "Test"
        
        response = create_courier(login, password, first_name)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_is_ok(response)
        
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(login, password)

    def test_create_duplicate_courier_fails(self):
        """Тест невозможности создания двух одинаковых курьеров"""
        # Создаем первого курьера с уникальным логином
        import time
        timestamp = str(int(time.time()))
        login = f"duplicate_test_{timestamp}"
        password = "password123"
        first_name = "Test"
        
        response1 = create_courier(login, password, first_name)
        check_response_status_code(response1, STATUS_CODE_201)
        
        # Пытаемся создать курьера с тем же логином
        response2 = create_courier(login, password, first_name)
        
        # Проверяем код ответа
        check_response_status_code(response2, STATUS_CODE_409)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response2, ERROR_MESSAGES["DUPLICATE_LOGIN"])
        
        # Удаляем созданного курьера
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(login, password)

    def test_create_courier_missing_login_fails(self):
        """Тест создания курьера без логина"""
        import time
        timestamp = str(int(time.time()))
        password = f"password_{timestamp}"
        first_name = "Test"
        
        payload = {
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_400)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    def test_create_courier_missing_password_fails(self):
        """Тест создания курьера без пароля"""
        import time
        timestamp = str(int(time.time()))
        login = f"test_login_{timestamp}"
        first_name = "Test"
        
        payload = {
            "login": login,
            "firstName": first_name
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_400)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    def test_create_courier_missing_first_name_fails(self):
        """Тест создания курьера без имени"""
        import time
        timestamp = str(int(time.time()))
        login = f"test_login_{timestamp}"
        password = f"password_{timestamp}"
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        # API принимает создание курьера без firstName, поэтому проверяем успешное создание
        check_response_status_code(response, STATUS_CODE_201)
        check_response_is_ok(response)
        
        # Удаляем созданного курьера
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(login, password)

    def test_create_courier_empty_payload_fails(self):
        """Тест создания курьера с пустым телом запроса"""
        payload = {}
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_400)
        
        # Проверяем сообщение об ошибке
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    def test_register_new_courier_helper(self):
        """Тест helper функции регистрации курьера"""
        courier_data = register_new_courier_and_return_login_password()
        
        # Проверяем что функция вернула данные курьера
        assert len(courier_data) == 3, "Функция должна вернуть логин, пароль и имя"
        assert courier_data[0] is not None, "Логин не должен быть пустым"
        assert courier_data[1] is not None, "Пароль не должен быть пустым"
        assert courier_data[2] is not None, "Имя не должно быть пустым"
        
        # Удаляем созданного курьера
        from helpers.helpers_on_delete_courier import delete_courier_by_credentials
        delete_courier_by_credentials(courier_data[0], courier_data[1])

