# put your python code here
n = int(input())
print(f'Сумма цифр = {n // 100 + n // 10 % 10 + n % 10}')
print(f'Произведение цифр = {(n // 100) * (n // 10 % 10) * (n % 10)}')