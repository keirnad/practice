import requests
import time
from typing import Dict, Any

# Простейший in-memory кэш: город -> {data, expires}
CACHE: Dict[str, Dict[str, Any]] = {}
CACHE_TTL = 60  # секунды

API_KEY = "47fe844faa4abf4096554b42de86ebdd"  # сюда подставьте свой ключ


def get_weather(city: str):
    """Получение погоды с кэшированием и обработкой ошибок."""
    now = time.time()

    # Кэширование
    if city in CACHE and CACHE[city]["expires"] > now:
        return CACHE[city]["data"]

    params = {
        "q": city,
        "appid": API_KEY,
    }

    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=5)
    except requests.RequestException:
        return {"error": "Weather service unavailable"}

    if r.status_code == 404:
        return {"error": "City not found"}

    if r.status_code >= 500:
        return {"error": "External weather server error"}

    data = r.json()

    CACHE[city] = {"data": data, "expires": now + CACHE_TTL}
    return data
