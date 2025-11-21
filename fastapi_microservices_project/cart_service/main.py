from fastapi import FastAPI, HTTPException
import requests

from weather import get_weather

app = FastAPI(title="Cart Service")

PRODUCT_SERVICE_URL = "http://localhost:8001"  # URL сервиса каталога
cart = []  # простая in-memory корзина (для примера)


@app.post("/cart/add/{product_id}")
def add_to_cart(product_id: int):
    """Добавить товар в корзину по ID из сервиса каталога."""
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    except requests.RequestException:
        raise HTTPException(status_code=503, detail="Product service unavailable")

    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Product not found")

    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Error from product service")

    cart.append(r.json())
    return {"message": "Added", "cart": cart}


@app.get("/cart")
def get_cart():
    """Получить текущую корзину."""
    return {"cart": cart}


@app.get("/weather/{city}")
def weather(city: str):
    """Получить погоду для города (через внешний API с кэшированием)."""
    data = get_weather(city)
    if "error" in data:
        # В get_weather уже обработаны ошибки 404/500 и т.д.
        raise HTTPException(status_code=400, detail=data["error"])
    return data
