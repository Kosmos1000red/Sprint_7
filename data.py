# Тексты ответов API
COURIER_CREATED_OK = {"ok": True}
COURIER_LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
COURIER_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
COURIER_LOGIN_NOT_ENOUGH_DATA = "Недостаточно данных для входа"
COURIER_NOT_FOUND = "Учетная запись не найдена"


# Шаблоны тестовых данных для заказа
ORDER_PAYLOAD_TEMPLATE = {
    "firstName": "Naruto",
    "lastName": "Uzumaki",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-30",
    "comment": "Saske, come back to Konoha",
}

# Варианты цветов для параметризации
ORDER_COLORS = [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    [],
]