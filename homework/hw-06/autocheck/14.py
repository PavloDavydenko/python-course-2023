"""
Створіть функціонал для розпакування архіву.

Зробіть import пакету shutil

Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive 
та розпаковуватиме архів archive_path у місце path_to_unpack.

Функція нічого не повертає.
"""


import shutil


def unpack(archive_path, path_to_unpack) -> None:
    shutil.unpack_archive(archive_path, path_to_unpack)


def main():
    archive_path = "D:\\projects\\python-course-2023\\backup_folder.zip"
    path_to_unpack = "D:\\projects\\python-course-2023\\backup"

    unpack(archive_path, path_to_unpack)


if __name__ == "__main__":
    main()