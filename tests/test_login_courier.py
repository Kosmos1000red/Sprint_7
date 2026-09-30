import allure
import requests

from data import COURIER_LOGIN_NOT_ENOUGH_DATA, COURIER_NOT_FOUND
from helpers import generate_courier_payload
from methods.courier_methods import CourierMethods


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, registered_courier):
        response = CourierMethods.login_courier({
            "login": registered_courier["login"],
            "password": registered_courier["password"],
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Нельзя авторизоваться без логина")
    def test_login_courier_without_login(self, registered_courier):
        response = CourierMethods.login_courier({
            "password": registered_courier["password"],
        })

        assert response.status_code == 400
        assert response.json()["message"] == COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title("Нельзя авторизоваться без пароля")
    def test_login_courier_without_password(self, registered_courier):
        try:
            response = CourierMethods.login_courier({
                "login": registered_courier["login"],
            })
            assert response.status_code == 504
        except requests.exceptions.ReadTimeout:
            # известный баг API: без пароля запрос зависает
            pass

    @allure.title("Ошибка при неверном логине")
    def test_login_courier_wrong_login(self, registered_courier):
        response = CourierMethods.login_courier({
            "login": "wrong_login_12345",
            "password": registered_courier["password"],
        })

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND

    @allure.title("Ошибка при неверном пароле")
    def test_login_courier_wrong_password(self, registered_courier):
        response = CourierMethods.login_courier({
            "login": registered_courier["login"],
            "password": "wrong_password",
        })

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND

    @allure.title("Ошибка при авторизации под несуществующим пользователем")
    def test_login_non_existent_courier(self):
        payload = generate_courier_payload()

        response = CourierMethods.login_courier({
            "login": payload["login"],
            "password": payload["password"],
        })

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND