import requests
from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, STATUS_CODE_201, STATUS_CODE_200
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(CREATE_COURIER_URL, data=payload)
    return response


def login_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(LOGIN_COURIER_URL, data=payload)
    return response


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
