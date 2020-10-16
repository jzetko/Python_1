# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:

# 1
# 121
# 12321
# 1234321
# 123454321

def triangle():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
            if j == i:
                for k in range(i - 1, 0, -1):
                    print(k, end='')
        print()


triangle()
