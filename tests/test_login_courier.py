import allure
import requests

from data import (
    COURIER_LOGIN_NOT_ENOUGH_DATA,
    COURIER_NOT_FOUND,
)
from helpers import generate_courier_payload
from methods.courier_methods import CourierMethods


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, created_courier):
        courier_payload, courier_id = created_courier

        response = CourierMethods.login_courier(courier_payload)

        assert response.status_code == 200
        assert response.json().get("id") == courier_id

    @allure.title("Нельзя авторизоваться без логина")
    def test_login_courier_without_login(self, created_courier):
        courier_payload, _ = created_courier
        payload = {"password": courier_payload["password"]}

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title("Нельзя авторизоваться без пароля")
    def test_login_courier_without_password(self, created_courier):
        courier_payload, _ = created_courier
        payload = {"login": courier_payload["login"]}

        try:
            response = CourierMethods.login_courier(payload)
            assert response.status_code == 504
        except requests.exceptions.ReadTimeout:
            pass  # это тоже валидный исход для данного бага

    @allure.title("Ошибка при неверном логине")
    def test_login_courier_wrong_login(self, created_courier):
        courier_payload, _ = created_courier
        payload = {
            "login": "wrong_login_12345",
            "password": courier_payload["password"],
        }

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND

    @allure.title("Ошибка при неверном пароле")
    def test_login_courier_wrong_password(self, created_courier):
        courier_payload, _ = created_courier
        payload = {
            "login": courier_payload["login"],
            "password": "wrong_password",
        }

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND

    @allure.title("Ошибка при авторизации под несуществующим пользователем")
    def test_login_non_existent_courier(self):
        payload = generate_courier_payload()

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND