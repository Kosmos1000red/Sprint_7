import allure
import pytest

from data import ORDER_COLORS, ORDER_PAYLOAD_TEMPLATE


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", ORDER_COLORS)
    def test_create_order_with_colors(self, tracked_order, color):
        payload = dict(ORDER_PAYLOAD_TEMPLATE)
        if color:
            payload["color"] = color

        with allure.step(f"Отправляем заказ с цветом: {color}"):
            response = tracked_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()