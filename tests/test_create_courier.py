import allure
import pytest

from data import (
    COURIER_CREATED_OK,
    COURIER_LOGIN_ALREADY_USED,
    COURIER_NOT_ENOUGH_DATA,
)
from methods.courier_methods import CourierMethods


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_payload):
        with allure.step("Отправляем запрос на создание курьера"):
            response = CourierMethods.create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == COURIER_CREATED_OK

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, created_courier):
        courier_payload, _ = created_courier

        with allure.step("Повторно создаём того же курьера"):
            response = CourierMethods.create_courier(courier_payload)

        assert response.status_code == 409
        assert response.json()["message"] == COURIER_LOGIN_ALREADY_USED

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self, courier_payload):
        courier_payload.pop("login")

        response = CourierMethods.create_courier(courier_payload)

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_NOT_ENOUGH_DATA

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self, courier_payload):
        courier_payload.pop("password")

        response = CourierMethods.create_courier(courier_payload)

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_NOT_ENOUGH_DATA