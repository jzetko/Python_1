# На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу,
# которая переворачивает и выводит последовательность символов, заключенную между первым и последним вхождением буквы
# «h».

s = input()
q = s[s.find('h') + 1:s.rfind('h')]

print(s[:s.find('h') + 1] + q[::-1] + s[s.rfind('h'):])

