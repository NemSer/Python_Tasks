# A

# print([i**2 for i in range(int(input()), int(input()) + 1)])

# B

# n = int(input())
# print([[i * j for i in range(1, n + 1)] for j in range(1, n + 1)])

# C

# sentence = input()
# print([len(i) for i in sentence.split()])

# D

# numbers = [int(i) for i in input().split()]
# print({element for element in numbers if element % 2 != 0})

# E

# numbers = [number for number in range(16, 100, 4)]
# print({element for element in numbers if int(element**0.5) == element**0.5})

# F

# text = '''Ехали медведи
# На велосипеде.
#
# А за ними кот
# Задом наперёд.'''
# print(dict(zip([i for i in ''.join(text.lower().split()) if i.isalpha()],
#                [''.join(text.lower().split()).count(i) for i in ''.join(
#                    text.lower().split()) if i.isalpha()])))

# G

# numbers = {15, 49, 36}
#
#
# print(dict(zip(numbers, [[i for i in range(1, j + 1) if j % i == 0] for j in numbers])))

# H

# string = 'открытое акционерное общество'
#
# print(''.join([i[0].upper() for i in string.split()]))

# I

# numbers = [1, 1000000000]
#
# print(' - '.join(str(x) for x in sorted(set(sorted(numbers)))))

# J

# rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
# print(''.join([i[0] for i in rle for j in range(i[1])]))


