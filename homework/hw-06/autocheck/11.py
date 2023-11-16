"""
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. 
Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
"""

def get_credentials_users(path) -> list:
    with open(path, 'rb') as fh:
        lines = []
        while True:
            line = fh.readline()
            if not line:
                break
            lines.append(line.decode().replace("\n", ""))

    return lines



def main():
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\11_source.bin'
    print(get_credentials_users(path))


if __name__ == "__main__":
    main()