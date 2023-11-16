"""
У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:

['Robert Stivenson,28', 'Alex Denver,30']
Це список рядків із прізвищем та віком співробітника, розділеними комами.

Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.

Функція запису в файл write_employees_to_file(employee_list, path), де:

path – шлях до файлу.
employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
Вимоги:

запишіть вміст employee_list у файл, використовуючи режим "w".
ми поки що не використовуємо менеджер контексту with
кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
"""


def write_employees_to_file(employee_list, path) -> None:

    file = open(path, 'w')
    
    for dept in range(len(employee_list)):
        for employee in range(len(employee_list[dept])):
            file.write(f'{employee_list[dept][employee]}\n')
    
    file.close()


def print_employees_from_file(path) -> None:

    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        print(line, end='')

    fh.close()    


def main():

    employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\02_list.txt'   
    
    write_employees_to_file(employee_list, path)
    print_employees_from_file(path)


if __name__ == "__main__":
    main()