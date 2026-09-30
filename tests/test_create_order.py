import allure

from data import ORDER_PAYLOAD_TEMPLATE
from methods.order_methods import OrderMethods


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с одним цветом — BLACK")
    def test_create_order_with_black_color(self):
        payload = {**ORDER_PAYLOAD_TEMPLATE, "color": ["BLACK"]}

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с одним цветом — GREY")
    def test_create_order_with_grey_color(self):
        payload = {**ORDER_PAYLOAD_TEMPLATE, "color": ["GREY"]}

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с двумя цветами")
    def test_create_order_with_two_colors(self):
        payload = {**ORDER_PAYLOAD_TEMPLATE, "color": ["BLACK", "GREY"]}

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        payload = dict(ORDER_PAYLOAD_TEMPLATE)  # поле color отсутствует

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()