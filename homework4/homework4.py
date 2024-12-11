# homework4
numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
even_count = len([x for x in numbers if x % 2 == 0])
odd_count = len(numbers) - even_count
print("Количество четных:", even_count)
print("Количество нечетных:", odd_count)
