import pytest
import requests
import allure
from data import CREATE_COURIER_URL, STATUS_CODE_201, STATUS_CODE_400, STATUS_CODE_409, ERROR_MESSAGES
from api.courier_api import create_courier, register_new_courier_and_return_login_password, delete_courier_by_credentials
from helpers.helpers_on_check_response import check_response_status_code, check_response_is_ok, check_response_has_error_message


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data, test_first_name):
        login = f"test_courier_{courier_data[0]}"
        password = "password123"
        first_name = test_first_name
        
        response = create_courier(login, password, first_name)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_is_ok(response)

    @allure.title("Невозможность создания дубликата курьера")
    def test_create_duplicate_courier_fails(self, courier_data, test_first_name):
        login = f"duplicate_test_{courier_data[0]}"
        password = "password123"
        first_name = test_first_name
        
        response1 = create_courier(login, password, first_name)
        check_response_status_code(response1, STATUS_CODE_201)
        
        response2 = create_courier(login, password, first_name)
        
        check_response_status_code(response2, STATUS_CODE_409)
        check_response_has_error_message(response2, ERROR_MESSAGES["DUPLICATE_LOGIN"])
        
        delete_courier_by_credentials(login, password)

    @allure.title("Создание курьера без логина")
    def test_create_courier_missing_login_fails(self, unique_password, test_first_name):
        password = unique_password
        first_name = test_first_name
        
        payload = {
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_400)
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    @allure.title("Создание курьера без пароля")
    def test_create_courier_missing_password_fails(self, unique_login, test_first_name):
        login = unique_login
        first_name = test_first_name
        
        payload = {
            "login": login,
            "firstName": first_name
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_400)
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    @allure.title("Создание курьера без имени")
    def test_create_courier_missing_first_name_fails(self, unique_courier_data):
        login = unique_courier_data["login"]
        password = unique_courier_data["password"]
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_is_ok(response)
        
        delete_courier_by_credentials(login, password)

    @allure.title("Создание курьера с пустым телом запроса")
    def test_create_courier_empty_payload_fails(self):
        payload = {}
        
        response = requests.post(CREATE_COURIER_URL, data=payload)
        
        check_response_status_code(response, STATUS_CODE_400)
        check_response_has_error_message(response, ERROR_MESSAGES["MISSING_FIELD"])

    @allure.title("Тест helper функции регистрации курьера")
    def test_register_new_courier_helper(self):
        courier_data = register_new_courier_and_return_login_password()
        
        assert len(courier_data) == 3, "Функция должна вернуть логин, пароль и имя"
        assert courier_data[0] is not None, "Логин не должен быть пустым"
        assert courier_data[1] is not None, "Пароль не должен быть пустым"
        assert courier_data[2] is not None, "Имя не должно быть пустым"
        
        delete_courier_by_credentials(courier_data[0], courier_data[1])

