"""
Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. 
Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та повертає словник.

При виклику функції:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію
Якщо збігів не виявлено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
"""


import re


def find_word(text, word) -> dict:

    result = re.search(word, text)
    
    if result:
        found_data = {
                    'result': True,
                    'first_index': result.span()[0],
                    'last_index': result.span()[1],
                    'search_string': word,
                    'string': text
                    }
    else:
        found_data = {
                    'result': False,
                    'first_index': None,
                    'last_index': None,
                    'search_string': word.lower(),
                    'string': text
                    }

    return found_data


def main():
    text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    word = "Python"

    print(find_word(text, word))


if __name__ == "__main__":
    main()