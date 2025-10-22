import pytest
import requests
from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():
    login_pass = []
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(CREATE_COURIER_URL, data=payload)
    
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    
    return login_pass


def login_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(LOGIN_COURIER_URL, data=payload)
    return response


def delete_courier(courier_id):
    response = requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")
    return response


@pytest.fixture
def courier_data():
    courier_info = register_new_courier_and_return_login_password()
    yield courier_info
    if courier_info:
        login_response = login_courier(courier_info[0], courier_info[1])
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)


@pytest.fixture
def order_data():
    from data import ORDER_DATA
    return ORDER_DATA.copy()

