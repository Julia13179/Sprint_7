import pytest
from data import STATUS_CODE_200
from helpers.helpers_on_create_order import get_order_list
from helpers.helpers_on_check_response import check_response_status_code


class TestGetOrderList:
    """Тесты для эндпоинта получения списка заказов"""

    def test_get_order_list_success(self):
        """Тест успешного получения списка заказов"""
        # Получаем список заказов
        response = get_order_list()
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_200)
        
        # Проверяем что ответ содержит список
        response_data = response.json()
        assert isinstance(response_data, dict), "Ответ должен быть словарем"
        assert "orders" in response_data, "В ответе должно быть поле 'orders'"
        assert isinstance(response_data["orders"], list), "Поле 'orders' должно быть списком"

    def test_get_order_list_response_structure(self):
        """Тест структуры ответа списка заказов"""
        # Получаем список заказов
        response = get_order_list()
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_200)
        
        # Проверяем структуру ответа
        response_data = response.json()
        
        # Проверяем что есть поле orders
        assert "orders" in response_data, "В ответе должно быть поле 'orders'"
        
        # Если есть заказы, проверяем их структуру
        if response_data["orders"]:
            order = response_data["orders"][0]
            # Проверяем основные поля заказа
            expected_fields = ["id", "track"]
            for field in expected_fields:
                assert field in order, f"В заказе должно быть поле '{field}'"

    def test_get_order_list_is_list(self):
        """Тест что ответ содержит список заказов"""
        # Получаем список заказов
        response = get_order_list()
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_200)
        
        # Проверяем что orders - это список
        response_data = response.json()
        orders = response_data.get("orders", [])
        assert isinstance(orders, list), "Поле 'orders' должно быть списком"

