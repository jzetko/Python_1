# Даны два числа: натуральное число n и вещественное число a. Напишите программу, которая находит площадь указанного
# правильного многоугольника.

from math import *

n, a = int(input()), float(input())

print((n * a * a) / (4 * tan(pi / n)))