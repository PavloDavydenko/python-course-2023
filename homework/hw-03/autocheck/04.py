"""
Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price. 
Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1. 
Тут і надалі ми під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни. 
І на цей розмір ми знижуємо підсумкову вартість товару. Логіку функції необхідно прописати у внутрішній функції apply_discount, 
використовуючи оголошення зміною price як nonlocal.
"""

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount

    apply_discount()
    return price


def main():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount coefficient (between 0 and 1): "))
    print(f"Price with discount = {discount_price(price, discount)}")


if __name__ == "__main__":
    main()