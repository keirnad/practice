import requests

PRODUCT_SERVICE_URL = "http://localhost:8001"
CART_SERVICE_URL = "http://localhost:8002"


def test_product_service_alive():
    r = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_add_valid_product_to_cart():
    r = requests.post(f"{CART_SERVICE_URL}/cart/add/1")
    assert r.status_code == 200
    body = r.json()
    assert "cart" in body
    assert len(body["cart"]) >= 1


def test_add_invalid_product_to_cart():
    r = requests.post(f"{CART_SERVICE_URL}/cart/add/9999")
    assert r.status_code == 404


def test_get_cart():
    r = requests.get(f"{CART_SERVICE_URL}/cart")
    assert r.status_code == 200
    assert "cart" in r.json()


def test_weather_endpoint():
    # Этот тест будет работать, если задан корректный API_KEY
    r = requests.get(f"{CART_SERVICE_URL}/weather/London")
    # Может быть 200 или 400 (если неправильный ключ / ошибка)
    assert r.status_code in (200, 400)
