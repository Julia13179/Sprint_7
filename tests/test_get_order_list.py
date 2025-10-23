import pytest
import allure
from data import STATUS_CODE_200
from helpers.helpers_on_create_order import get_order_list
from helpers.helpers_on_check_response import check_response_status_code


class TestGetOrderList:

    @allure.title("Успешное получение списка заказов")
    def test_get_order_list_success(self):
        response = get_order_list()
        
        check_response_status_code(response, STATUS_CODE_200)
        
        response_data = response.json()
        assert isinstance(response_data, dict), "Ответ должен быть словарем"
        assert "orders" in response_data, "В ответе должно быть поле 'orders'"
        assert isinstance(response_data["orders"], list), "Поле 'orders' должно быть списком"

    @allure.title("Структура ответа списка заказов")
    def test_get_order_list_response_structure(self):
        response = get_order_list()
        
        check_response_status_code(response, STATUS_CODE_200)
        
        response_data = response.json()
        
        assert "orders" in response_data, "В ответе должно быть поле 'orders'"
        assert isinstance(response_data["orders"], list), "Поле 'orders' должно быть списком"

    @allure.title("Проверка типа данных списка заказов")
    def test_get_order_list_is_list(self):
        response = get_order_list()
        
        check_response_status_code(response, STATUS_CODE_200)
        
        response_data = response.json()
        orders = response_data.get("orders", [])
        assert isinstance(orders, list), "Поле 'orders' должно быть списком"

