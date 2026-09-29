import allure

from methods.order_methods import OrderMethods


@allure.feature("Список заказов")
class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        with allure.step("Отправляем GET-запрос на /api/v1/orders"):
            response = OrderMethods.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)