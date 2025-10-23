import allure


@allure.step("Проверка кода ответа")
def check_response_status_code(response, expected_code):
    assert response.status_code == expected_code, f"Ожидался код {expected_code}, получен {response.status_code}"


@allure.step("Проверка наличия поля в ответе")
def check_response_has_field(response, field_name):
    response_data = response.json()
    assert field_name in response_data, f"Поле '{field_name}' отсутствует в ответе"


@allure.step("Проверка значения поля в ответе")
def check_response_field_value(response, field_name, expected_value):
    response_data = response.json()
    assert response_data[field_name] == expected_value, f"Поле '{field_name}' имеет значение {response_data[field_name]}, ожидалось {expected_value}"


@allure.step("Проверка наличия track в ответе")
def check_response_has_track(response):
    response_data = response.json()
    assert "track" in response_data, "Поле 'track' отсутствует в ответе"
    assert response_data["track"] is not None, "Поле 'track' пустое"


@allure.step("Проверка успешного ответа")
def check_response_is_ok(response):
    response_data = response.json()
    assert response_data["ok"] is True, f"Ожидался ok: true, получен {response_data}"


@allure.step("Проверка сообщения об ошибке")
def check_response_has_error_message(response, expected_message):
    response_data = response.json()
    assert "message" in response_data, "Сообщение об ошибке отсутствует в ответе"
    assert expected_message in response_data["message"], f"Ожидалось сообщение '{expected_message}', получено '{response_data['message']}'"


@allure.step("Проверка наличия id в ответе")
def check_response_has_id(response):
    response_data = response.json()
    assert "id" in response_data, "Поле 'id' отсутствует в ответе"
    assert response_data["id"] is not None, "Поле 'id' пустое"

