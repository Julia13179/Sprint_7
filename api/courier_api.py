import requests
import allure
from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL, STATUS_CODE_201, STATUS_CODE_200
from helpers.helpers_utils import generate_random_string


@allure.step("Создание курьера")
def create_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(CREATE_COURIER_URL, data=payload)
    return response


@allure.step("Авторизация курьера")
def login_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(LOGIN_COURIER_URL, data=payload)
    return response


@allure.step("Удаление курьера")
def delete_courier(courier_id):
    response = requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")
    return response


@allure.step("Регистрация нового курьера")
def register_new_courier_and_return_login_password():
    login_pass = []
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    response = create_courier(login, password, first_name)
    
    if response.status_code == STATUS_CODE_201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    
    return login_pass


@allure.step("Удаление курьера по логину и паролю")
def delete_courier_by_credentials(login, password):
    login_response = login_courier(login, password)
    
    if login_response.status_code == STATUS_CODE_200:
        courier_id = login_response.json()["id"]
        return delete_courier(courier_id)
    else:
        return login_response
