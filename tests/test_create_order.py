import pytest
from data import STATUS_CODE_201, BLACK_COLOR, GREY_COLOR
from helpers.helpers_on_create_order import create_order
from helpers.helpers_on_check_response import check_response_status_code, check_response_has_track


class TestCreateOrder:
    """Тесты для эндпоинта создания заказа"""

    @pytest.mark.parametrize("color", [BLACK_COLOR, GREY_COLOR])
    def test_create_order_with_single_color(self, order_data, color):
        """Тест создания заказа с одним цветом"""
        # Добавляем цвет к данным заказа
        order_data["color"] = [color]
        
        # Создаем заказ
        response = create_order(order_data)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_201)
        
        # Проверяем что в ответе есть track
        check_response_has_track(response)

    def test_create_order_with_both_colors(self, order_data):
        """Тест создания заказа с обоими цветами"""
        # Добавляем оба цвета к данным заказа
        order_data["color"] = [BLACK_COLOR, GREY_COLOR]
        
        # Создаем заказ
        response = create_order(order_data)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_201)
        
        # Проверяем что в ответе есть track
        check_response_has_track(response)

    def test_create_order_without_color(self, order_data):
        """Тест создания заказа без указания цвета"""
        # Не добавляем поле color к данным заказа
        
        # Создаем заказ
        response = create_order(order_data)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_201)
        
        # Проверяем что в ответе есть track
        check_response_has_track(response)

    def test_create_order_with_empty_color_list(self, order_data):
        """Тест создания заказа с пустым списком цветов"""
        # Добавляем пустой список цветов
        order_data["color"] = []
        
        # Создаем заказ
        response = create_order(order_data)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_201)
        
        # Проверяем что в ответе есть track
        check_response_has_track(response)

    def test_create_order_response_contains_track(self, order_data):
        """Тест что ответ создания заказа содержит track"""
        # Создаем заказ
        response = create_order(order_data)
        
        # Проверяем код ответа
        check_response_status_code(response, STATUS_CODE_201)
        
        # Проверяем что в ответе есть track
        check_response_has_track(response)
        
        # Проверяем что track не пустой
        response_data = response.json()
        assert response_data["track"] != "", "Track не должен быть пустой строкой"
        assert isinstance(response_data["track"], (str, int)), "Track должен быть строкой или числом"

