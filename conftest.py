import pytest
import requests

import urls
from helpers import generate_courier_payload
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_payload():
    return generate_courier_payload()


@pytest.fixture
def created_courier(courier_payload):
    create_response = CourierMethods.create_courier(courier_payload)

    courier_id = None
    login_response = CourierMethods.login_courier(courier_payload)
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")

    yield courier_payload, courier_id

    if courier_id:
        CourierMethods.delete_courier(courier_id)


@pytest.fixture
def tracked_order():
    created_tracks = []

    def _create(payload: dict):
        response = requests.post(urls.CREATE_ORDER, json=payload)
        if response.status_code == 201:
            created_tracks.append(response.json().get("track"))
        return response

    yield _create

    created_tracks.clear()