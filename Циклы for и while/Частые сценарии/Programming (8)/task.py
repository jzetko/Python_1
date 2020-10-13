# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())
max1, max2 = 1, 0

for i in range(n):
    n1 = int(input())
    if n1 > max1:
        max2 = max1
        max1 = n1
    if max1 > n1 > max2:
        max2 = n1

print(max1, max2, sep='\n')
