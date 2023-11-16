"""
Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
"""

def is_equal_string(utf8_string, utf16_string) -> bool:
    return utf8_string.decode() == utf16_string.decode('utf-16')


def main():
    s_a = "Hello world"
    s_b = "Hello world!"

    utf8_string = s_a.encode()
    utf16_string = s_b.encode('utf-16')

    print(is_equal_string(utf8_string, utf16_string))


if __name__ == "__main__":
    main()