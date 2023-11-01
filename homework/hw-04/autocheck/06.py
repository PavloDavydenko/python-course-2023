"""
У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити список на дві частини. 
Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. 
У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. 
Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
"""

def split_list(grade):

    first = [] 
    second = []
    # Find mean of numbers
    sum = 0
    for item in grade:
        sum += item
    try:
        mean_of_numbers = sum / len(grade)
    except ZeroDivisionError:
        return (first, second)

    # Form two lists
    for item in grade:
        if item <= mean_of_numbers:
            first.append(item)
        else:
            second.append(item)
    return (first, second)


def main():

    date_set = [5, 2, 7, 1, 9, 8, 3, 6, 4]
    # date_set = []
    print(split_list(date_set))


if __name__ == "__main__":
    main()