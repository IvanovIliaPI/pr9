# homework3
numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
odds = [x for x in numbers if x % 2 != 0]
print("Нечетные числа из списка:", odds)
