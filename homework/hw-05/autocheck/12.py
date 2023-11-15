"""
У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. 
Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), 
перевіряє його на вміст заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, 
підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.
"""


import re


def replace_spam_words(text, spam_words) -> str:
    
    for word in spam_words:
        text = re.sub(word, '*'*len(word), text, flags=re.IGNORECASE)

    return text


def main():
    text = "Hello my friend! Can you tell me what going on?"
    spam_words = ["my", "tell"]

    print(replace_spam_words(text, spam_words))


if __name__ == "__main__":
    main()