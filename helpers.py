import random
import string

from methods.courier_methods import CourierMethods


def generate_random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_courier_payload() -> dict:
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }


def delete_courier_by_payload(payload: dict) -> None:
    login_response = CourierMethods.login_courier({
        "login": payload["login"],
        "password": payload["password"],
    })
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            CourierMethods.delete_courier(courier_id)