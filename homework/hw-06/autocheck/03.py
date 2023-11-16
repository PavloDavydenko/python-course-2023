"""
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), 
яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.

Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
"""

['Alexandr Popov,28', 'Larisa Host,31', 'Pavel Durov,2']
['Alexandr Popov,28', 'Larisa Host,31', 'Pavel Durov,29']



def read_employees_from_file(path) -> list:
    list = []

    file = open(path, 'r')
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        list.append(line)
    
    file.close()
    
    return list



def main():
  
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\02_list.txt'   
    
    new_list = read_employees_from_file(path)
    print(new_list)


if __name__ == "__main__":
    main()