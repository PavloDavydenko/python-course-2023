"""
Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""


import re


def real_len(text) -> int:
    return len(text) - len(re.findall('[\n\f\r\t\v]', text))


def main():
    text = 'Alex\nKdfe23\t\f\v.\r'

    print(real_len(text))


if __name__ == "__main__":
    main()