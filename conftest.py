import pytest

from helpers import delete_courier_by_payload, generate_courier_payload
from methods.courier_methods import CourierMethods


@pytest.fixture
def registered_courier():
    payload = generate_courier_payload()
    CourierMethods.create_courier(payload)
    yield payload
    delete_courier_by_payload(payload)


@pytest.fixture
def courier_cleanup():
    created = []

    def _register_for_cleanup(payload: dict):
        created.append(payload)

    yield _register_for_cleanup

    for payload in created:
        delete_courier_by_payload(payload)