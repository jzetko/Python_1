# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
# 1−2+3−4+5−6+…+(−1)n+1n.

n = int(input())
n1 = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        i *= -1
    n1 += i

print(n1)