"""
Необхідно написати функцію, яка буде обчислювати суму за користування послугами таксі. 
Сума складається з базового тарифу 40 грн, та 10 грн за кожен кілометр поїздки. 
Напишіть функцію, яка приймає один параметр — відстань поїздки в кілометрах. 
Функція має повертати підсумкову суму оплати за послуги таксі дійсним числом. 
Також функція повинна змінювати глобальну змінну — лічильник total_trip після кожного виклику та збільшувати її на одиницю.
"""

base_rate = 40
price_per_km = 10
total_trip = 0

def trip_price(path):
    global total_trip
    total_trip += 1
    return base_rate + price_per_km * path


def main():
    path = int(input("Enter number of kilometers: "))
    print(f"Trip price: {trip_price(path)}")
    print(f"Total trip: {total_trip}")


if __name__ == "__main__":
    main()