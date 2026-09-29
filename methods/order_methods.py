import requests

import urls


class OrderMethods:

    @staticmethod
    def create_order(payload: dict):
        return requests.post(urls.CREATE_ORDER, json=payload, timeout=15)

    @staticmethod
    def get_orders(params: dict = None):
        return requests.get(urls.GET_ORDERS, params=params, timeout=30)