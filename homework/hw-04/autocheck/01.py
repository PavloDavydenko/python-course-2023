"""
У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, 
чи додатними, якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів, 
підсумовує додатні значення та повертає суму платежу наприкінці місяця.
"""

def amount_payment(payment):
    sum = 0
    for item in payment:
        if item >= 0:
            sum += item
    return sum


def main():
    payment_list = [100, 200, 300, -500]
    print(amount_payment(payment_list))


if __name__ == "__main__":
    main()