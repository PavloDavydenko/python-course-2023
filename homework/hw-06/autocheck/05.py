"""
Ми маємо таку структуру файлу:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, 
для першого запису початок 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. 
Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3. 
Всі частини запису розділені символом кома ,

Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
Параметри функції:

path - шлях до файлу
Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми використовуємо менеджер контексту with
"""


def get_cats_info(path) -> list:
    result_list = []
    key_list = ["id", "name", "age"]
    with open(path, 'r') as fh:
        while True:
            line = fh.readline().replace("\n", "")
            if not line:
                break
            value_list = line.split(",")

            temp_dict = {key:value for (key, value) in zip(key_list, value_list)}
            result_list.append(temp_dict)
    
    return result_list



def main():
    path = 'D:\\projects\\python-course-2023\\homework\\hw-06\\05_file.txt'    
    print(get_cats_info(path))



if __name__ == "__main__":
    main()