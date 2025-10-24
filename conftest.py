import pytest
import time
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


@pytest.fixture
def wrong_password():
    return "wrong_password"


@pytest.fixture
def nonexistent_user_data():
    timestamp = str(int(time.time()))
    return {
        "login": f"nonexistent_user_{timestamp}",
        "password": "password123"
    }


@pytest.fixture
def unique_login():
    timestamp = str(int(time.time()))
    return f"test_login_{timestamp}"


@pytest.fixture
def unique_password():
    timestamp = str(int(time.time()))
    return f"password_{timestamp}"


@pytest.fixture
def unique_courier_data():
    timestamp = str(int(time.time()))
    return {
        "login": f"test_courier_{timestamp}",
        "password": f"password_{timestamp}",
        "first_name": "Test"
    }


@pytest.fixture
def test_first_name():
    return "Test"

