# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n различных
# последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского
# алфавита, при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму
# количество сообщений от Оди.

n = int(input())
count = 0

for i in range(n):
    n = input()
    if n.count('11') >= 3:
        count += 1

print(count)