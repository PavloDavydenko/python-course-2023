"""
Завдання
У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою ви зможете настроїти цю програму під себе і вона виконуватиме індивідуальний сценарій, 
що відповідає вашим потребам. Для цього наш додаток буде перевіряти розширення файлу (останні символи у імені файлу, як правило, після крапки) і, 
залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент при запуску — це ім'я папки, в якій він буде проводити сортування. Допустимо файл з програмою називається sort.py, 
тоді, щоб відсортувати папку /user/Desktop/Мотлох, треба запустити скрипт командою python sort.py /user/Desktop/Мотлох

Для того щоб успішно впорається з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли по групам:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відео файли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення.
Ви можете розширити та доповнити цей список, якщо хочете.

В результатах роботи повинні бути:

Список файлів в кожній категорії (музика, відео, фото и ін.)
Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
Перелік всіх розширень, які скрипту невідомі.
Після необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

Крім того, всі файли та папки треба перейменувати, видалив із назви всі символи, що призводять до проблем. 
Для цього треба застосувати до імен файлів функцію normalize. Слід розуміти, що перейменувати файли треба так, щоб не змінити розширень файлів.

Функція normalize:

Проводить транслітерацію кирилічного алфавіту на латинський.
Замінює всі символи крім латинських літер, цифр на '_'.
Вимоги до функції normalize:

приймає на вхід рядок та повертає рядок;
проводить транслітерацію кирилічних символів на латиницю;
замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
транслітерація може не відповідати стандарту, але бути читабельною;
великі літери залишаються великими, а маленькі — маленькими після транслітерації.
Умови для обробки:
зображення переносимо до папки images
документи переносимо до папки documents
аудіо файли переносимо до audio
відео файли до video
архіви розпаковуються та їх вміст переноситься до папки archives
Критерії прийому завдання
всі файли та папки перейменовуються за допомогою функції normalize.
розширення файлів не змінюється після перейменування.
порожні папки видаляються
скрипт ігнорує папки archives, video, audio, documents, images;
розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення у кінці;
файли, розширення яких невідомі, залишаються без зміни.
"""

"""
_______РОБОТА СКРИПТУ_______

Скрипт запускається з командного рядка з одним аргументом (шлях до папки, яку потрібно відсортувати)
Потім потрібно ввести шлях до папки, в яку потрібно перенести відсортовані файли. Та погодитись на використання папки, якщо вона вже існує. 
Або ввести новий шлях.

В результаті сортування на екран виведеться:
- список усіх розширень, що відомі;
- список всіх розширень, що не відомі;
- та словник по категоріям оброблених файлів.

Також ця інформація буде продубльована в файлах в відсортованій папці у підпапці "_results".
"""

import sys
import shutil
from pathlib import Path


def normalize(name):

    # Transliteration from Cyrillic to Latin 
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}
        
    for cyr, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cyr)] = latin
        TRANS[ord(cyr.upper())] = latin.upper()    

    name = name.translate(TRANS)

    # Change all symbols to "_" except letters, numbers and "."
    normalized_name = ''
    for char in name:
        if char.isalnum() or char in {"_", "."}:
            normalized_name += char
        else:
            normalized_name += "_"

    return normalized_name


def working_in_directories(unsorted_path, sorted_path):

    # Data to fill
    all_files_extension_list = set()
    known_files_extension_list = set()
    unknown_files_extension_list = set()
    files_by_category_lists = {
        "images": [],
        "documents": [],
        "audio": [],
        "video": [],
        "archives": [],
        "unknown": []
    }        

    # Сreate directories for file types
    file_types = {
        'images': {'jpg', 'jpeg', 'png', 'svg'},
        'documents': {'doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'},
        'audio': {'mp3', 'ogg', 'wav', 'amr'},
        'video': {'avi', 'mp4', 'mov', 'mkv'},
        'archives': {'zip', 'gz', 'tar'},
        'unknown': set()
    }

    # Create sorted dirs in sorted path
    for type in file_types.keys():
        file_type_path = sorted_path / type
        if not file_type_path.exists():
            file_type_path.mkdir(exist_ok=True)

    # Sort through files and folders into an unsorted directory
    for item in unsorted_path.iterdir():
        if item.is_file():
            file_name = item.name
            normalized_file_name = normalize(file_name)
            destination_directory = None

            # Determining the file extension using
            file_extension = item.suffix[1:].lower() if item.suffix else ''

            # Define the file type and folder for the file
            for type, extensions in file_types.items():
                if file_extension in extensions:
                    destination_directory = type
                    known_files_extension_list.add(file_extension)
                    files_by_category_lists[type].append(normalized_file_name)
                    break
                else:
                    destination_directory = "unknown"
                    all_files_extension_list.add(file_extension)

            unknown_files_extension_list = all_files_extension_list - known_files_extension_list
            if file_extension in unknown_files_extension_list:
                files_by_category_lists["unknown"].append(normalized_file_name)
          
            # Creat new_path for archives and other files
            if item.suffix[1:] in file_types["archives"]:

                # new_path for archives files
                new_path = sorted_path / destination_directory / normalized_file_name.rsplit(".", 1)[0]
                shutil.unpack_archive(item, new_path)
            else:
                # New_path for other files
                new_path = sorted_path / destination_directory / normalized_file_name
                
                # check for file duplicates
                while new_path.exists():
                    base = new_path.stem
                    ext = new_path.suffix
                    new_file_name = f"{base} - copy{ext}"
                    new_path = sorted_path / destination_directory / new_file_name
 
                shutil.move(item, new_path)

        # Recursive calling of subdirectiries
        elif item.is_dir():
            working_in_directories(item, sorted_path)

    # Recursive delete unsorted directiries
    shutil.rmtree(unsorted_path)
            
    return known_files_extension_list, unknown_files_extension_list, files_by_category_lists


def arg_path_check() -> Path:

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path")
        exit(1)

    path = Path(sys.argv[1]).absolute()

    if not path.exists():
        print(f"There is no such directory. Enter path to existing directory")
        exit(2)
    elif path.is_file():
        print(f"You have to enter path to directory. Not to file.")
        exit(3)    

    return path


def sorted_directory_path() -> Path:
    # Enter path to sorted directoty. Create it or use existing one.
    while True:
        sorted_path = Path(input("Enter full path to sorted directory: ")).absolute()
        
        if not sorted_path.exists():
            sorted_path.mkdir()
            print(f"Directoty '{sorted_path}' created.")
            break
        else:
            print(f"Directory '{sorted_path}' already exists.")
            existing_directory_select = input("Do you want use it? (y/n): ").lower()
            if existing_directory_select == "y":
                break

    return sorted_path


def write_list(my_list, file_name, path):
    path = path / "_results" / file_name
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")


def write_dict(my_dict, file_name, path):
    path = path / "_results" / file_name
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as file:
        for key, value in my_dict.items():
            file.write(f"{key}:\n")
            
            for item in value:
                file.write(f"{" "*len(key)} {item}\n")    
            file.write(f"\n")


def main():

    unsorted_path = arg_path_check()

    sorted_path = sorted_directory_path()

    known_files_extension_list, unknown_files_extension_list, files_by_category_lists = working_in_directories(unsorted_path, sorted_path)

    write_list(known_files_extension_list, "known_files_extension_list.txt", sorted_path)
    write_list(unknown_files_extension_list, "unknown_files_extension_list.txt", sorted_path)    
    write_dict(files_by_category_lists, "files_by_category_lists.txt", sorted_path)

    print(known_files_extension_list)
    print()
    print(unknown_files_extension_list)
    print()
    print(files_by_category_lists)


if __name__ == "__main__":
    main()