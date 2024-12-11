# homework8
import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

user_choices = [int(input(f"Выберите число из строки {row}: {row} ")) for row in ticket]
random_choices = [random.choice(row) for row in ticket]

matches = len(set(user_choices) & set(random_choices))
print("Ваши числа:", user_choices)
print("Случайные числа:", random_choices)
print(f"Совпадений: {matches}")
