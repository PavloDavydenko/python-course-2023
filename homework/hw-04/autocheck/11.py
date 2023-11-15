"""
Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.
"""


def is_valid_password(password):
    
    digit, lower, upper = 0, 0, 0
    for char in password:
        if char.isdigit():
            digit += 1
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
    if len(password) == 8 and digit and lower and upper:
        return True

    return False


def main():
    password = "3j2hsE~l"
    
    print(is_valid_password(password))


if __name__ == "__main__":
    main()