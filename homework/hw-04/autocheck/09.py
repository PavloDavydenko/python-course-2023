"""
Всім відомо, що для доступу до кредитної картки банку потрібний пін-код. Класично склалося, що це поєднання чотири цифри. 
Нам необхідно вирішити наступне програмістське завдання. Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes, 
яка буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр і повертати логічне значення — валідний список чи ні. 
Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, всі вони зберігаються у вигляді рядків, 
їх довжина дорівнює 4 символам і містять вони тільки цифри.

Приклад аргументу для функції is_valid_pin_codes:

['1101', '9034', '0011']
Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True. Якщо хоч одну з умов порушено, повертається значення — False. 
Передбачити перевірку на порожній список в аргументі функції та повернути при цьому значення False.
"""


def is_valid_pin_codes(pin_codes):
    # Check if list is empty
    if not pin_codes:
        return False
    
    # Check for doubles
    pin_set = set(pin_codes)
    if len(pin_codes) != len(pin_set):
        return False
    
    # Check if rows str and have only 4 symbols which are int
    for item in pin_codes:
        try:
            test = int(item)
            if len(item) != 4:
                return False
        except:
            return False
    return True


def main():
    pin_codes = ['1101', '9034', '0011']
    # pin_codes = ['1101', '9034', '1101']

    print(is_valid_pin_codes(pin_codes))


if __name__ == "__main__":
    main()