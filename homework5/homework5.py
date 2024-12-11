# homework5
numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print("Элементы больше предыдущего:", result)
