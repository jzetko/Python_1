# На вход программе подается три натуральных числа m,p,n:
#
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить
# размер популяции
# в каждый день, начиная с 1 и заканчивая n-м днем.

m, p, n = [int(input()) for _ in range(3)]

for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)

