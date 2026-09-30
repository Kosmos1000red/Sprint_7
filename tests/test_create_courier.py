import allure

from data import (
    COURIER_CREATED_OK,
    COURIER_LOGIN_ALREADY_USED,
    COURIER_NOT_ENOUGH_DATA,
)
from helpers import generate_courier_payload
from methods.courier_methods import CourierMethods


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_cleanup):
        payload = generate_courier_payload()

        response = CourierMethods.create_courier(payload)
        courier_cleanup(payload)  # фикстура удалит после теста

        assert response.status_code == 201
        assert response.json() == COURIER_CREATED_OK

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, registered_courier):
        # registered_courier уже создан фикстурой, она же удалит после теста
        response = CourierMethods.create_courier(registered_courier)

        assert response.status_code == 409
        assert response.json()["message"] == COURIER_LOGIN_ALREADY_USED

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        payload = generate_courier_payload()
        payload.pop("login")

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_NOT_ENOUGH_DATA

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self):
        payload = generate_courier_payload()
        payload.pop("password")

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_NOT_ENOUGH_DATA