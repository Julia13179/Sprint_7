import pytest
from data import ORDER_DATA
from api.courier_api import register_new_courier_and_return_login_password, login_courier, delete_courier


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
    return ORDER_DATA.copy()

