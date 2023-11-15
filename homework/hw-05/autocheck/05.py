"""
Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. 
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
"""


def sanitize_phone_number(phone) -> str:
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    return new_phone


def get_phone_numbers_for_countries(list_phones) -> dict:
    new_dict = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
    }

    for phone in list_phones:

        new_phone = sanitize_phone_number(phone)
        
        if new_phone.startswith('81'):
            new_dict["JP"].append(new_phone)
        elif new_phone.startswith('65'):
            new_dict["SG"].append(new_phone)
        elif new_phone.startswith('886'):
            new_dict["TW"].append(new_phone)
        else:
            new_dict["UA"].append(new_phone)
        
    return new_dict
    

def main():
    list_phones = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
    ]
    
    print(get_phone_numbers_for_countries(list_phones))


if __name__ == "__main__":
    main()