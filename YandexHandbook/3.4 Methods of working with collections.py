# A

# for index, value in enumerate(input().split(), 1):
#     print(f'{index}. {value}')

# B

# for i in zip(input().split(', '), input().split(', ')):
#     print(f'{i[0]} - {i[1]}')

# C

# from itertools import count
#
# values = [float(x) for x in input().split()]
# for value in count(values[0], values[2]):
#     if value > values[1]:
#         break
#     print(round(value, 2))

# D

# from itertools import accumulate
#
# data = input().split()
# data_new = []
# for i in data:
#     data_new.append(i)
#     data_new.append(' ')
# i = 0
# for values in accumulate(data_new):
#     if i % 2 == 0:
#         print(values)
#     i += 1
# print(data_new)

# E

# data = []
# for i in range(3):
#     data += input().split(', ')
# for index, value in enumerate(sorted(data), 1):
#     print(f'{index}. {value}')

# F

# from itertools import product
#
# data = input()
# for values in product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
#                       ['пик', 'треф', 'бубен', 'червей']):
#     if values[1] == data:
#         continue
#     else:
#         print(values[0], values[1])

# G

# import itertools as it
#
# data = []
# for i in range(int(input())):
#     data.append(input())
# for i in it.combinations(data, 2):
#     print(f'{i[0]} - {i[1]}')


# H

# from itertools import islice
#
# a = []
# for i in range(int(input())):
#     a.append(input())
# b = int(input())
# for i in range(b // len(a)):
#     for j in list(islice(a, len(a))):
#         print(j)
# for j in islice(a, b % len(a)):
#     print(j)

# I

# from itertools import product
#
# answer = ''
# number = int(input())
# data_list = list(product([x for x in range(1, number + 1)], [x for x in range(1, number + 1)]))
# list_output = [x[0] * x[1] for x in data_list]
# for i in range(len(list_output)):
#     if (i + 1) % number == 0:
#         answer += str(list_output[i]) + '\n'
#     else:
#         answer += str(list_output[i]) + ' '
# print(answer)

# J

# from itertools import product
#
# number = int(input())
# data_output = list(product([x for x in range(1, number - 1)], repeat=2))
# print('А Б В')
# for i in data_output:
#     if number - (i[0] + i[1]) > 0:
#         print(f'{i[0]} {i[1]} {number - (i[0] + i[1])}')

# K

from itertools import product

# answer = ''
# a, b = int(input()), int(input())
# data_output = [str(x) for x in range(1, a * b + 1)]
# for i in range(len(data_output)):
#     if (i + 1) % b == 0:
#         answer += data_output[i].rjust(len(str(a * b))) + '\n'
#     else:
#         answer += data_output[i].rjust(len(str(a * b))) + ' '
# print(answer)


# L

# a = int(input())
# data_input = ''
# for i in range(a):
#     data_input += ' '.join(input().split(', ')) + ' '
# data_output = [i for i in sorted(data_input.split())]
# for index, value in enumerate(data_output, 1):
#     print(f'{index}. {value}')

# M

# from itertools import permutations
#
# data_input = [input() for i in range(int(input()))]
# for i in permutations(sorted(data_input)):
#     print(', '.join(list(i)))

# N

# from itertools import permutations
#
# data_input = [input() for i in range(int(input()))]
# for i in sorted(permutations(data_input, 3)):
#     print(', '.join(list(i)))

# O

# from itertools import permutations
# data_input = []
# for i in range(int(input())):
#     data_input += input().split(', ')
# for i in sorted(permutations(data_input, 3)):
#     print(' '.join(list(i)))

# R

# from itertools import product
#
# data_input = input().split()
# i = 0
# while i != len(data_input):
#     if data_input[i] == 'or':
#         data_input[i] = '+'
#     elif data_input[i] == 'and':
#         data_input[i] = '*'
#     i += 1
# print("a", "b", "c", "f")
# for i in list(product([0, 1], [0, 1], [0, 1])):
#     copy = ' '.join(data_input).split()
#     for j in range(len(copy)):
#         if copy[j] == 'a':
#             copy[j] = str(i[0])
#         elif copy[j] == 'b':
#             copy[j] = str(i[1])
#         elif copy[j] == 'c':
#             copy[j] = str(i[2])
#     j = 0
#     while j != len(copy):
#         if copy[j] == 'not':
#             if copy[j + 1] == '1':
#                 copy[j + 1] = '0'
#             else:
#                 copy[j + 1] = '1'
#             copy.pop(j)
#         j += 1
#     if eval(eval("''.join(copy)")):
#         print(i[0], i[1], i[2], 1)
#     else:
#         print(i[0], i[1], i[2], 0)


