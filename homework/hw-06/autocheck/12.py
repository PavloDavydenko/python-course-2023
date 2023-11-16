"""
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, 
виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
"""

import base64


def encode_data_to_base64(data) -> list:
    encoded_list = []
    for el in range(len(data)):
        element_bytes = data[el].encode('utf-8')
        base64_bytes = base64.b64encode(element_bytes)
        base64_element = base64_bytes.decode('utf-8')
        encoded_list.append(base64_element)

    return encoded_list


def main():
    data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
    print(encode_data_to_base64(data))


if __name__ == "__main__":
    main()