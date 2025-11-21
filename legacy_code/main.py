def calculate_discount(user_status: str, price: float, special: bool = False) -> float:
    """
    Рассчитывает итоговую цену с учетом скидок.

    Args:
        user_status (str): уровень пользователя ("gold", "silver", "bronze")
        price (float): исходная цена товара
        special (bool): применяется ли спец-скидка

    Returns:
        float: итоговая цена товара
    """

    base_discounts = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.05
    }

    discount = base_discounts.get(user_status, 0)
    final_discount = price * discount

    if special:
        final_discount *= 0.95

    return price - final_discount
