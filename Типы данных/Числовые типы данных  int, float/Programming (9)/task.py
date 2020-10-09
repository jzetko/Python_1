# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число
# интересное» иначе «Число неинтересное».

number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10

if max(a, b, c) - min(a, b, c) == a + b + c - max(a, b , c) - min(a, b, c):
    print('Число интересное')
else:
    print('Число неинтересное')
