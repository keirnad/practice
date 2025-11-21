"""
Product Service — сервис каталога товаров.
Предоставляет API для получения списка товаров и информации о товаре.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Product Service")

products = [
    {"id": 1, "name": "Milk", "price": 50},
    {"id": 2, "name": "Bread", "price": 30},
    {"id": 3, "name": "Cheese", "price": 120},
]


@app.get("/products")
def get_products():
    """
    Возвращает список всех товаров.

    Returns:
        list: Список словарей с товарами, содержащих id, name и price.
    """
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    """
    Возвращает информацию о конкретном товаре по ID.

    Args:
        product_id (int): Идентификатор товара.

    Returns:
        dict: Данные товара, если найден.
        dict: {"error": "..."} — если товар отсутствует.
    """
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")
