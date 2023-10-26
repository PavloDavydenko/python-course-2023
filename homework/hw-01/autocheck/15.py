"""
При заповненні анкети на сайті нам необхідно через функцію input присвоїти відповідним змінним значення:

name - ваше ім'я, тип рядок
email - ваша електронна пошта, тип рядок
age - ваш вік, тип число int
height - ваш зріст, тип число float
is_active - чи бажаєте ви отримувати повідомлення від сайту, тип булевий
"""

name = input("Your name? ")
email = input("Your e-mail? ")
age = int(input("Your age? "))
height = float(input("Your height? "))
is_active = bool(input("Do you want to recive massagers from site? "))