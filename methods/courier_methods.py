import requests

import urls


class CourierMethods:

    @staticmethod
    def create_courier(payload: dict):
        return requests.post(urls.CREATE_COURIER, data=payload, timeout=30)

    @staticmethod
    def login_courier(payload: dict):
        return requests.post(urls.LOGIN_COURIER, data=payload, timeout=5)

    @staticmethod
    def delete_courier(courier_id: int):
        return requests.delete(f"{urls.DELETE_COURIER}/{courier_id}", timeout=10)