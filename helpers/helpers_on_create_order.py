import requests
import allure
from data import CREATE_ORDER_URL, GET_ORDER_LIST_URL, STATUS_CODE_201, STATUS_CODE_200


@allure.step("Создание заказа")
def create_order(order_data):
    response = requests.post(CREATE_ORDER_URL, json=order_data)
    return response


@allure.step("Получение списка заказов")
def get_order_list():
    response = requests.get(GET_ORDER_LIST_URL)
    return response


@allure.step("Получение заказа по трек-номеру")
def get_order_by_track(track_number):
    response = requests.get(f"{GET_ORDER_LIST_URL}/track?t={track_number}")
    return response

