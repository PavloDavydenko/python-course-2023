"""
Сучасна система оцінок в університеті має такий вигляд:

Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, get_grade приймає ключ у вигляді оцінки ECTS, 
і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга get_description теж приймає ключ у вигляді оцінки ECTS, 
але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента. 
На відсутній ключ функції повинні повертати значення None .
"""


def get_grade(key):
    
    grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    if key in grade:
        return grade[key]
    


def get_description(key):
    
    description = {"F": "Unsatisfactorily", 
                   "FX": "Unsatisfactorily", 
                   "E": "Enough", 
                   "D": "Satisfactorily", 
                   "C": "Good", 
                   "B": "Very good", 
                   "A": "Perfectly"}
    if key in description:
        return description[key]
    

def main():
    
    input_grade = input("Enter Grade: ").upper()
    print(f"{input_grade} = {get_grade(input_grade)}")
    print(f"{input_grade} = {get_description(input_grade)}")



if __name__ == "__main__":
    main()