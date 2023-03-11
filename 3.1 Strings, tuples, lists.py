# A

# answer = 'YES'
# for i in range(int(input())):
#     if not (s := input()).startswith(('а', 'б', 'в')):
#         answer = 'NO'
# else:
#     print(answer)

# B

# for i in (s := input()):
#     print(i)

# С

# k = int(input())
# for i in range(int(input())):
#     if len((s := input())) > k:
#         print(s[:k - 3].ljust(k, '.'))
#     else:
#         print(s)

# D

# while (s := input()) != '':
#     if s.endswith('@@@'):
#         continue
#     elif s.startswith('##'):
#         print(s.lstrip('#'))
#     else:
#         print(s)

# E

# s = input()
# if len(s) % 2 == 0:
#     if s[:len(s) // 2] == s[:len(s) // 2 - 1: -1]:
#         print('YES')
#     else:
#         print('NO')
# else:
#     if s[:len(s) // 2] == s[:len(s) // 2: -1]:
#         print('YES')
#     else:
#         print('NO')

# F

# s = ''
# for i in range(int(input())):
#     s += input() + ' '
# print(s.split().count('зайка'))

# G

# a = input().split()
# print(int(a[0]) + int(a[1]))

# H

# for i in range(int(input())):
#     if 'зайка' in (s := input()):
#         print(s.find('зайка') + 1)
#     else:
#         print('Заек нет =(')

# I

# while (s := input()) != '':
#     if s.startswith('#'):
#         continue
#     elif s.count('#') == 0:
#         print(s)
#     else:
#         i = s.find('#')
#         while '"' in s[i + 1:]:
#             i += s[i + 1:].find('#') + 1
#         print(s[:i])

# J

# a = []
# b = ''
# c = []
# while (s := input()) != 'ФИНИШ':
#     a += s.split()
# for i in ''.join(a).lower():
#     if i not in b:
#         b += i
# for i in b:
#     c += [(''.join(a).lower().count(i), i)]
# c.sort(reverse=True)
# answer = c[0][1]
# j = c[0][0]
# for i in c:
#     if i[0] == j and i[1] < answer:
#         answer = i[1]
# print(answer)

# K

# n = int(input())
# a = []
# for i in range(n + 1):
#     a.append((s := input()))
# for i in range(len(a) - 1):
#     if a[-1].lower() in a[i].lower():
#         print(a[i])

# L

# a = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
# n = int(input())
# for i in range(n // 5):
#     print('\n'.join(a))
# for i in range(n % 5):
#     print(a[i])

# M

# n = int(input())
# a = []
# for i in range(n + 1):
#     a.append(int(input()))
# for i in range(len(a) - 1):
#     print(a[i]**a[-1])

# N

# a, p = input().split(), int(input())
# for i in range(len(a)):
#     print(int(a[i])**p, end=' ')

# O

# a = input().split()
# i = 0
# a1 = int(a[i])
# a2 = int(a[i + 1])
# while a1 % a2 != 0:
#     c = a2
#     a2 = a1 % a2
#     a1 = c
# nod = a2
# i += 1
# while i != len(a) - 1:
#     a1 = nod
#     a2 = int(a[i])
#     while a1 % a2 != 0:
#         c = a2
#         a2 = a1 % a2
#         a1 = c
#     nod = a2
#     i += 1
# print(nod)

# Q

# a = ''.join(input().lower().split())
# if len(a) % 2 != 0 and a[:len(a) // 2] == a[len(a) - 1:len(a) // 2:-1]:
#     print('YES')
# elif a[:len(a) // 2] == a[len(a) - 1:len(a) // 2 - 1:-1]:
#     print("YES")
# else:
#     print('NO')

# R

# s = input()
# answer = ''
# k = s[0]
# j = 0
# for i in range(len(s)):
#     if k != s[i]:
#         answer += str(k) + ' ' + str(j) + '\n'
#         k = s[i]
#         j = 1
#     else:
#         j += 1
# answer += str(k) + ' ' + str(j)
# print(answer)

# S

# s = input().split()
# stack = []
# i = 0
# while i < len(s):
#     if s[i].isdigit():
#         stack.append(s[i])
#     else:
#         if s[i] == '*':
#             stack[-1] = int(stack[-1]) * int(stack[-2])
#             stack.pop(-2)
#         elif s[i] == '+':
#             stack[-1] = int(stack[-1]) + int(stack[-2])
#             stack.pop(-2)
#         else:
#             stack[-1] = int(stack[-2]) - int(stack[-1])
#             stack.pop(-2)
#     i += 1
# print(stack[-1])

# T

# s = input().split()
# stack = []
# for i in s:
#     if i.isdigit():
#         stack.append(int(i))
#     else:
#         if i == '~':
#             stack[-1] = -stack[-1]
#         elif i == '!':
#             i = 1
#             a = 1
#             while i <= stack[-1]:
#                 a *= i
#                 i += 1
#             stack[-1] = a
#         elif i == '#':
#             stack.append(stack[-1])
#         elif i == '@':
#             stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
#         elif i == '+':
#             stack[-1] = stack[-1] + stack[-2]
#             stack.pop(-2)
#         elif i == '-':
#             stack[-1] = stack[-2] - stack[-1]
#             stack.pop(-2)
#         elif i == '*':
#             stack[-1] = stack[-2] * stack[-1]
#             stack.pop(-2)
#         else:
#             stack[-1] = stack[-2] // stack[-1]
#             stack.pop(-2)
# print(stack[-1])


