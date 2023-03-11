# A

# print(f'Как Вас зовут?')
# name = input()
# print(f'Здравствуйте, {name}!\nКак дела?')
# parametr = input()
# match parametr:
#     case 'хорошо':
#         print('Я за вас рада!')
#     case 'плохо':
#         print('Всё наладится!')

# B

# v1, v2 = int(input()), int(input())
# if v1 > v2:
#     print('Петя')
# else:
#     print('Вася')

# C

# v1, v2, v3 = int(input()), int(input()), int(input())
# v_ = max(v1, v2, v3)
# if v_ == v1:
#     print('Петя')
# elif v_ == v2:
#     print('Вася')
# else:
#     print('Толя')

# D

# v1, v2, v3 = int(input()), int(input()), int(input())
# if v1 < v2 < v3:
#     print('1. Толя\n2. Вася\n3. Петя')
# elif v1 < v3 < v2:
#     print('1. Вася\n2. Толя\n3. Петя')
# elif v2 < v1 < v3:
#     print('1. Толя\n2. Петя\n3. Вася')
# elif v2 < v3 < v1:
#     print('1. Петя\n2. Толя\n3. Вася')
# elif v3 < v1 < v2:
#     print('1. Вася\n2. Петя\n3. Толя')
# else:
#     print('1. Петя\n2. Вася\n3. Толя')

# E

# N, M = int(input()), int(input())
# if 6 + N > 12 + M:
#     print('Петя')
# else:
#     print('Вася')

# F

# year = int(input())
# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print('NO')
#     else:
#         print('YES')
# else:
#     print('NO')

# G

# x = int(input())
# x4 = x % 10
# x3 = x // 10 % 10
# x2 = x // 100 % 10
# x1 = x // 1000
# if x1 == x4 and x2 == x3:
#     print('YES')
# else:
#     print('NO')

# H

# x = input()
# if 'зайка' in x:
#     print('YES')
# else:
#     print('NO')

# I

# name1, name2, name3 = input(), input(), input()
# print(min(name1, name2, name3))

# J

# x = int(input())
# x1 = x % 10
# x2 = x // 10 % 10
# x3 = x // 100
# k1 = x1 + x2
# k2 = x2 + x3
# if k1 > k2:
#     print(k1, k2, sep='')
# else:
#     print(k2, k1, sep='')

# K

# x = int(input())
# x3 = x % 10
# x2 = x // 10 % 10
# x1 = x // 100
# if x1 == max(x1, x2, x3) and x2 == min(x1, x2, x3) or x1 == min(x1, x2, x3) and x2 == max(x1, x2, x3):
#     if x1 + x2 == x3 * 2:
#         print('YES')
#     else:
#         print('NO')
# elif x2 == max(x1, x2, x3) and x3 == min(x1, x2, x3) or x2 == min(x1, x2, x3) and x3 == max(x1, x2, x3):
#     if x2 + x3 == x1 * 2:
#         print('YES')
#     else:
#         print('NO')
# else:
#     if x1 + x3 == x2 * 2:
#         print('YES')
#     else:
#         print('NO')

# L

# a, b, c = int(input()), int(input()), int(input())
# if a >= b + c:
#     print('NO')
# elif b >= a + c:
#     print('NO')
# elif c >= a + b:
#     print('NO')
# else:
#     print('YES')

# M

# x1, x2, x3 = int(input()), int(input()), int(input())
# if x1 % 10 == x2 % 10 == x3 % 10:
#     print(x1 % 10)
# elif x1 // 10 == x2 // 10 == x3 // 10:
#     print(x1 // 10)

# N

# x = int(input())
# x1 = x // 100
# x2 = x // 10 % 10
# x3 = x % 10
# if x2 == 0 and x3 == 0:
#     print(str(x1) + str(x2), str(x1) + str(x2))
# elif x2 == 0:
#     if x1 > x3:
#         print(str(x3) + str(x2), str(x1) + str(x3))
#     else:
#         print(str(x1) + str(x2), str(x3) + str(x1))
# elif x3 == 0:
#     if x1 > x2:
#         print(str(x2) + str(x3), str(x1) + str(x2))
#     else:
#         print(str(x1) + str(x3), str(x2) + str(x1))
# elif x1 == max(x1, x2, x3) and x2 == min(x1, x2, x3):
#     print(str(x2) + str(x3), str(x1) + str(x3))
# elif x1 == min(x1, x2, x3) and x2 == max(x1, x2, x3):
#     print(str(x1) + str(x3), str(x2) + str(x3))
# elif x2 == max(x1, x2, x3) and x3 == min(x1, x2, x3):
#     print(str(x3) + str(x1), str(x2) + str(x1))
# elif x2 == min(x1, x2, x3) and x3 == max(x1, x2, x3):
#     print(str(x2) + str(x1), str(x3) + str(x1))
# elif x1 == max(x1, x2, x3) and x3 == min(x1, x2, x3):
#     print(str(x3) + str(x2), str(x1) + str(x2))
# else:
#     print(str(x1) + str(x2), str(x3) + str(x2))

# O

# a, b = int(input()), int(input())
# x1 = a % 10
# x2 = a // 10
# x3 = b % 10
# x4 = b // 10
# if x1 == max(x1, x2, x3, x4) and x2 == min(x1, x2, x3, x4):
#     if x3 + x4 > 9:
#         print(str(x1) + str((x3 + x4) // 10) + str(x2))
#     else:
#         print(str(x1) + str(x3 + x4) + str(x2))
# elif x1 == min(x1, x2, x3, x4) and x2 == max(x1, x2, x3, x4):
#     if x3 + x4 > 9:
#         print(str(x2) + str((x3 + x4) // 10) + str(x1))
#     else:
#         print(str(x2) + str(x3 + x4) + str(x1))
#
# elif x1 == max(x1, x2, x3, x4) and x3 == min(x1, x2, x3, x4):
#     if x2 + x4 > 9:
#         print(str(x1) + str((x2 + x4) // 10) + str(x3))
#     else:
#         print(str(x1) + str(x2 + x4) + str(x3))
# elif x1 == min(x1, x2, x3, x4) and x3 == max(x1, x2, x3, x4):
#     if x2 + x4 > 9:
#         print(str(x3) + str((x2 + x4) // 10) + str(x1))
#     else:
#         print(str(x3) + str(x2 + x4) + str(x1))
#
# elif x1 == max(x1, x2, x3, x4) and x4 == min(x1, x2, x3, x4):
#     if x2 + x3 > 9:
#         print(str(x1) + str((x2 + x3) // 10) + str(x4))
#     else:
#         print(str(x1) + str(x2 + x3) + str(x4))
# elif x1 == min(x1, x2, x3, x4) and x4 == max(x1, x2, x3, x4):
#     if x2 + x3 > 9:
#         print(str(x4) + str((x2 + x3) // 10) + str(x1))
#     else:
#         print(str(x4) + str(x2 + x3) + str(x1))
#
# elif x2 == max(x1, x2, x3, x4) and x3 == min(x1, x2, x3, x4):
#     if x1 + x4 > 9:
#         print(str(x2) + str((x1 + x4) // 10) + str(x3))
#     else:
#         print(str(x2) + str(x1 + x4) + str(x3))
# elif x2 == min(x1, x2, x3, x4) and x3 == max(x1, x2, x3, x4):
#     if x1 + x4 > 9:
#         print(str(x3) + str((x1 + x4) // 10) + str(x2))
#     else:
#         print(str(x3) + str(x1 + x4) + str(x2))
#
# elif x2 == max(x1, x2, x3, x4) and x4 == min(x1, x2, x3, x4):
#     if x1 + x3 > 9:
#         print(str(x2) + str((x1 + x3) // 10) + str(x4))
#     else:
#         print(str(x2) + str(x1 + x3) + str(x4))
# elif x2 == min(x1, x2, x3, x4) and x4 == max(x1, x2, x3, x4):
#     if x1 + x3 > 9:
#         print(str(x4) + str((x1 + x3) // 10) + str(x2))
#     else:
#         print(str(x4) + str(x1 + x3) + str(x2))
#
# elif x3 == max(x1, x2, x3, x4) and x4 == min(x1, x2, x3, x4):
#     if x1 + x2 > 9:
#         print(str(x3) + str((x1 + x2) // 10) + str(x4))
#     else:
#         print(str(x3) + str(x1 + x2) + str(x4))
# else:
#     if x1 + x2 > 9:
#         print(str(x4) + str((x1 + x2) // 10) + str(x3))
#     else:
#         print(str(x4) + str(x1 + x2) + str(x3))

# P

# Petya, Vacya, Tolya = int(input()), int(input()), int(input())
# if Petya < Vacya < Tolya:
#     k1 = 'Толя'
#     k2 = 'Вася'
#     k3 = 'Петя'
# elif Petya < Tolya < Vacya:
#     k1 = 'Вася'
#     k2 = 'Толя'
#     k3 = 'Петя'
# elif Vacya < Petya < Tolya:
#     k1 = 'Толя'
#     k2 = 'Петя'
#     k3 = 'Вася'
# elif Vacya < Tolya < Petya:
#     k1 = 'Петя'
#     k2 = 'Толя'
#     k3 = 'Вася'
# elif Tolya < Petya < Vacya:
#     k1 = 'Вася'
#     k2 = 'Петя'
#     k3 = 'Толя'
# else:
#     k1 = 'Петя'
#     k2 = 'Вася'
#     k3 = 'Толя'
# I_ = 'I'
# II = 'II'
# III = 'III'
# print(f'{k1.center(24)}\n'
#       f'{k2.center(8)}\n'
#       f'\t\t\t\t{k3.center(8)}\n'
#       f'{II.center(8)}{I_.center(8)}{III.center(8)}')

# Q

# a, b, c = float(input()), float(input()), float(input())
# if a == b == c == 0:
#     print('Infinite solutions')
# elif a == b == 0:
#     print('No solution')
# elif a == c == 0:
#     print(0)
# elif a == 0:
#     print(round(-c / b, 2))
# else:
#     D = b**2 - 4 * a * c
#     if D > 0:
#         x1 = (-b + D**0.5) / (2 * a)
#         x2 = (-b - D**0.5) / (2 * a)
#         if x1 < x2:
#             print(f'{x1:.2f}', f'{x2:.2f}')
#         else:
#             print(f'{x2:.2f}', f'{x1:.2f}')
#     elif D == 0:
#         x = -b / (2 * a)
#         print(f'{x:.2f}')
#     else:
#         print('No solution')

# R

# a, b, c = int(input()), int(input()), int(input())
# if a == max(a, b, c):
#     if b**2 + c**2 == a**2:
#         print('100%')
#     elif b**2 + c**2 < a**2:
#         print('велика')
#     else:
#         print('крайне мала')
# elif b == max(a, b, c):
#     if a**2 + c**2 == b**2:
#         print('100%')
#     elif a**2 + c**2 < b**2:
#         print('велика')
#     else:
#         print('крайне мала')
# else:
#     if a**2 + b**2 == c**2:
#         print('100%')
#     elif a**2 + b**2 < c**2:
#         print('велика')
#     else:
#         print('крайне мала')


# T

# a, b, c = input(), input(), input()
# if 'зайка' in a and 'зайка' not in b and 'зайка' not in c:
#     print(a, len(a))
# elif 'зайка' in b and 'зайка' not in a and 'зайка' not in c:
#     print(b, len(b))
# elif 'зайка' in c and 'зайка' not in a and 'зайка' not in b:
#     print(c, len(c))
# elif 'зайка' in a and 'зайка' in b and 'зайка' not in c:
#     if a >= b:
#         print(b, len(b))
#     else:
#         print(a, len(a))
# elif 'зайка' in a and 'зайка' in c and 'зайка' not in b:
#     if a >= c:
#         print(c, len(c))
#     else:
#         print(a, len(a))
# elif 'зайка' in b and 'зайка' in c and 'зайка' not in a:
#     if b >= c:
#         print(c, len(c))
#     else:
#         print(b, len(b))
# else:
#     if a == min(a, b, c):
#         print(a, len(a))
#     elif b == min(a, b, c):
#         print(b, len(b))
#     else:
#         print(c, len(c))



