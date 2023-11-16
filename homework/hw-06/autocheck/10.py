"""
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, 
яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password 
для кожного елемента словника users_info
"""

def save_credentials_users(path, users_info) -> None:
    with open(path, 'wb') as fh:
        lines = []
        for key, value in users_info.items():
            lines.append(f"{key}:{value}\n".encode()) # encode - кодує строку в byte
        
        fh.writelines(lines)


def main():
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\10_output.bin'
    users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
    
    save_credentials_users(path, users_info)


if __name__ == "__main__":
    main()