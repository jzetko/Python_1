numbers = [8, 9, 10, 11]

# del numbers[1]
# numbers.insert(1, 17)
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
# numbers.remove(numbers[0])
# numbers.extend(numbers)
# numbers.insert(3, 25)
# print(numbers)

numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)