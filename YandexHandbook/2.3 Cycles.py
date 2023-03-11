# A

# while input() != 'Три!':
#     print('Режим ожидания...')
# print('Ёлочка, гори!')

# B

# i = 0
# while (x := input()) != 'Приехали!':
#     if 'зайка' in x:
#         i += 1
# print(i)

# C

# begin, end = int(input()), int(input())
# for i in range(begin, end + 1):
#     print(i, end=' ')

# D

# begin, end = int(input()), int(input())
# if begin <= end:
#     for i in range(begin, end + 1):
#         print(i, end=' ')
# else:
#     for i in range(begin, end - 1, -1):
#         print(i, end=' ')

# E

# s = 0
# while (price := float(input())) != 0:
#     if price < 500:
#         s += price
#     else:
#         s += 0.9 * price
# print(s)

# F

# a, b = int(input()), int(input())
# if a < b:
#     a, b = b, a
# while (r := a % b) != 0:
#     a = b
#     b = r
# print(b)

# G

# x, y = int(input()), int(input())
# a, b = x, y
# if a < b:
#     a, b = b, a
# while (r := a % b) != 0:
#     a = b
#     b = r
# print(x * y // b)

# H

# s = input()
# n = int(input())
# for i in range(n):
#     print(s)

# I

# s = 1
# n = int(input())
# while n != 1:
#     s *= n
#     n -= 1
# print(s)

# J

# x, y = 0, 0
# while (s := input()) != 'СТОП':
#     step = int(input())
#     if s == 'СЕВЕР':
#         y += step
#     elif s == 'ЮГ':
#         y -= step
#     elif s == 'ВОСТОК':
#         x += step
#     else:
#         x -= step
# print(y, x, sep='\n')

# K

# s = 0
# n = int(input())
# for i in str(n):
#     s += int(i)
# print(s)

# L

# k = 0
# n = int(input())
# for i in str(n):
#     if int(i) > k:
#         k = int(i)
# print(k)

# M

# n = int(input())
# name = input()
# for i in range(n - 1):
#     s = input()
#     if s < name:
#         name = s
# print(name)

# N

# n = int(input())
# s = 'YES'
# if n == 1:
#     s = 'NO'
# for i in range(2, int(n**0.5 + 1)):
#     if n % i == 0:
#         s = 'NO'
# print(s)

# O

# n = int(input())
# k = 0
# for i in range(n):
#     string = input()
#     if 'зайка' in string:
#         k += 1
# print(k)

# P

# n = int(input())
# copy_n = n
# result = 0
# while n != 0:
#     x = n % 10
#     result = result * 10 + x
#     n = n // 10
# if result == copy_n:
#     print('YES')
# else:
#     print('NO')

# Q

# n = int(input())
# result = 0
# while n != 0:
#     if (x := n % 10) % 2 != 0:
#         result = 10 * result + x
#     n //= 10
# result_new = 0
# while result != 0:
#     x = result % 10
#     result_new = result_new * 10 + x
#     result //= 10
# print(result_new)

# R

# n = int(input())
# s = ''
# x = 2
# while n != 1:
#     if n % x == 0:
#         if n // x == 1:
#             s += f'{x}'
#         else:
#             s += f'{x} * '
#         n //= x
#     else:
#         s1 = 'bad'
#         while s1 != 'good':
#             x += 1
#             s1 = 'good'
#             for i in range(2, int(x**0.5 + 1)):
#                 if x % i == 0:
#                     s1 = 'bad'
# print(s)

# S

# left = 0
# right = 1001
# x = (right - left) // 2
# print(x)
# while (s := input()) != 'Угадал!':
#     if s == 'Больше':
#         left = x
#         x = (right - left) // 2 + left
#     else:
#         right = x
#         x = (right - left) // 2 + left
#     print(x)

