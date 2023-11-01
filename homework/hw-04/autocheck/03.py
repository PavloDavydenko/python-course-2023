"""
Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar
Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] 
та повертатиме рядок зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.
"""


def format_ingredients(items):
    if len(items) > 1:
        return f'{", ".join(items[0:-1])} and {items[-1]}'
    else:
        return f'{"".join(items)}'   
            

def main():
    ingredients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
    # ingredients = ["2 eggs"]
    print(format_ingredients(ingredients))


if __name__ == "__main__":
    main()