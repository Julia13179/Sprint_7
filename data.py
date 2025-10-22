BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_URL = f"{BASE_URL}/api/v1/courier"
LOGIN_COURIER_URL = f"{BASE_URL}/api/v1/courier/login"
CREATE_ORDER_URL = f"{BASE_URL}/api/v1/orders"
GET_ORDER_LIST_URL = f"{BASE_URL}/api/v1/orders"
DELETE_COURIER_URL = f"{BASE_URL}/api/v1/courier"
ACCEPT_ORDER_URL = f"{BASE_URL}/api/v1/orders/accept"
GET_ORDER_BY_TRACK_URL = f"{BASE_URL}/api/v1/orders/track"

STATUS_CODE_201 = 201
STATUS_CODE_200 = 200
STATUS_CODE_400 = 400
STATUS_CODE_404 = 404
STATUS_CODE_409 = 409

BLACK_COLOR = "BLACK"
GREY_COLOR = "GREY"

ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, ул. Тверская, 1",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-12-31",
    "comment": "Комментарий к заказу"
}

ERROR_MESSAGES = {
    "MISSING_FIELD": "Недостаточно данных для создания учетной записи",
    "DUPLICATE_LOGIN": "Этот логин уже используется. Попробуйте другой.",
    "INVALID_CREDENTIALS": "Учетная запись не найдена",
    "MISSING_LOGIN_PASSWORD": "Недостаточно данных для входа",
    "INVALID_LOGIN_PASSWORD": "Учетная запись не найдена"
}

