# Sprint_7

# Тест-сьют для проверки API приложения "Самокат" с помощью Pytest и библиотеки Requests

## Файлы:

* tests/ - папка с файлами тестов:
  * tests/test_create_courier.py - тесты эндпойнта создания курьера
  * tests/test_login_courier.py - тесты эндпойнта авторизации курьера
  * tests/test_create_order.py - тесты эндпойнта создания заказа
  * tests/test_get_order_list.py - тесты эндпойнта получения списка заказов

* helpers/ - папка вспомогательных функций:
  * helpers/helpers_on_create_courier.py - функции для создания и авторизации курьера
  * helpers/helpers_on_delete_courier.py - функции для удаления курьера
  * helpers/helpers_on_create_order.py - функции для создания заказа и получения списка заказов
  * helpers/helpers_on_check_response.py - функции для проверки полученного ответа на запрос к API

* conftest.py - функции для setup и teardown тестов
* data.py - константы, URL-адреса и данные для тестов
* .gitignore - файл для проекта в Git/GitHub
* requirements.txt - файл с внешними зависимостями
* README.md - файл с описанием проекта (этот файл)

