# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.

n = int(input())
summa = 0

for i in range(n):
    summa += int(input())

print(summa)
