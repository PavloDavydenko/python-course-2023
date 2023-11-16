"""
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
"""

def sanitize_file(source, output) -> None:
    with open(source, 'r') as sf:
        lines = sf.readlines()
        
        new_lines = "" 
        for el in range(len(lines)):
            for char in range(len(lines[el])):
                if not lines[el][char].isnumeric():
                    new_lines += lines[el][char]
                    
        with open(output, "w") as of:            
            of.write(new_lines)  
              

def main():
    source = 'D:\\projects\\python-course-2023\\homework\\hw-06\\07_source.txt'
    output = 'D:\\projects\\python-course-2023\\homework\\hw-06\\07_output.txt'

    sanitize_file(source, output)


if __name__ == "__main__":
    main()