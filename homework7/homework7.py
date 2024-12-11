# homework7
numbers = list(map(int, input("Введите числа через пробел: ").split()))
numbers = [numbers[-1]] + numbers[:-1]
print("Список после сдвига:", numbers)
