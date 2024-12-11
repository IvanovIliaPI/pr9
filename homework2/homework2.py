a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
squares = [x**2 for x in range(min(a, b), max(a, b) + 1)]
print("Список квадратов:", squares)
