import requests
from data import DELETE_COURIER_URL, LOGIN_COURIER_URL, STATUS_CODE_200


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


def delete_courier_by_credentials(login, password):
    login_response = login_courier(login, password)
    
    if login_response.status_code == STATUS_CODE_200:
        courier_id = login_response.json()["id"]
        return delete_courier(courier_id)
    else:
        return login_response
