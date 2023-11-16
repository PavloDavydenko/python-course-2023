"""
Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл 
і повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with
"""


def total_salary(path) -> float:
    file = open(path, 'r', encoding='utf-8')
    total_salary = 0

    while True:
        line = file.readline()
        if not line:
            break
        total_salary += float(line.split(',')[1])

    file.close()

    return total_salary  


def main():
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\01_workers.txt'   
    print(total_salary(path))


if __name__ == "__main__":
    main()