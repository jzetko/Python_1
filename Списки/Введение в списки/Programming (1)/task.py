# На вход программе подается одно число n. Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

n = int(input())
s = list()
for i in range(97, n + 97):
    s += chr(i)
print(s)