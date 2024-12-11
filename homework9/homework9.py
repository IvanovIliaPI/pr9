# homework9
import re

email = input("Введите email: ")
match = re.match(r'([^@]+)@(.+)', email)
if match:
    username, domain = match.groups()
    print("Имя пользователя:", username)
    print("Доменное имя:", domain)
else:
    print("Некорректный email!")
