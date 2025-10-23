import pytest
import allure
from data import STATUS_CODE_201, BLACK_COLOR, GREY_COLOR
from helpers.helpers_on_create_order import create_order
from helpers.helpers_on_check_response import check_response_status_code, check_response_has_track


class TestCreateOrder:

    @pytest.mark.parametrize("color", [BLACK_COLOR, GREY_COLOR])
    @allure.title("Создание заказа с одним цветом")
    def test_create_order_with_single_color(self, order_data, color):
        order_data["color"] = [color]
        
        response = create_order(order_data)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_has_track(response)

    @allure.title("Создание заказа с обоими цветами")
    def test_create_order_with_both_colors(self, order_data):
        order_data["color"] = [BLACK_COLOR, GREY_COLOR]
        
        response = create_order(order_data)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_has_track(response)

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self, order_data):
        response = create_order(order_data)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_has_track(response)

    @allure.title("Создание заказа с пустым списком цветов")
    def test_create_order_with_empty_color_list(self, order_data):
        order_data["color"] = []
        
        response = create_order(order_data)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_has_track(response)

    @allure.title("Проверка наличия track в ответе")
    def test_create_order_response_contains_track(self, order_data):
        response = create_order(order_data)
        
        check_response_status_code(response, STATUS_CODE_201)
        check_response_has_track(response)
        
        response_data = response.json()
        assert response_data["track"] != "", "Track не должен быть пустой строкой"
        assert isinstance(response_data["track"], (str, int)), "Track должен быть строкой или числом"

