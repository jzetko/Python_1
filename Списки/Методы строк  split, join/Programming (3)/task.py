# На вход программе подается строка текста, содержащая целые числа. Напишите программу,
# которая по заданным числам строит столбчатую диаграмму.

s = input()

for i in s.split():
    print(int(i) * '+')