"""
Рядок — це об'єкт, що ітерується, а, значить, ми можемо використовувати його в циклі for. 
Підрахуйте в заданому рядку message кількість входжень символу зі змінної search. Результат помістіть у змінну result.
"""

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    
    if char == search:
        result += 1