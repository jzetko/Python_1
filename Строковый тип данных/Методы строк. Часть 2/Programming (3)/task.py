# На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

s = input()
ans = 0
for char in s:
    if "0" <= char <= "9":
        ans += 1
print(ans)