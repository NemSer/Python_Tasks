# A

# for i in set((s := input())):
#     print(i, end='')

# B

# s1, s2 = set(input()), set(input())
# print(''.join(s1 & s2))

# C

# s = ''
# for i in range(int(input())):
#     s += input() + ' '
# for i in set(s.split()):
#     print(i)

# D

# n, m = int(input()), int(input())
# a = set()
# b = set()
# for i in range(n):
#     a.add(input())
# for i in range(m):
#     b.add(input())
# if len(a & b):
#     print(len(a & b))
# else:
#     print('Таких нет')

# E

# j = 0
# n, m = int(input()), int(input())
# a = dict()
# for i in range(n + m):
#     s = input()
#     a[s] = a.get(s, 0) + 1
# for key in a:
#     if a[key] == 1:
#         j += 1
# if j:
#     print(j)
# else:
#     print('Таких нет')

# F

# b = []
# n, m = int(input()), int(input())
# a = dict()
# for i in range(n + m):
#     s = input()
#     a[s] = a.get(s, 0) + 1
# for key, values in a.items():
#     if values == 1:
#         b.append(key)
# if len(b):
#     b.sort()
#     for i in b:
#         print(i)
# else:
#     print('Таких нет')

# G

# a = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
#      'E': '.', 'F': '..-.',
#      'G': '--.', 'H': '....', 'I': '..',
#      'J': '.---', 'K': '-.-', 'L': '.-..',
#      'M': '--', 'N': '-.', 'O': '---',
#      'P': '.--.', 'Q': '--.-', 'R': '.-.',
#      'S': '...', 'T': '-', 'U': '..-',
#      'V': '...-', 'W': '.--', 'X': '-..-',
#      'Y': '-.--', 'Z': '--..',
#      '0': '-----', '1': '.----', '2': '..---',
#      '3': '...--', '4': '....-', '5': '.....',
#      '6': '-....', '7': '--...', '8': '---..',
#      '9': '----.'}
# for i in input().upper().split():
#     for j in i:
#         print(a[j], end=' ')
#     print()

# H

# a = dict()
# for i in range(int(input())):
#     s = input()
#     for j in s.split()[1:]:
#         a[j] = a.get(j, []) + [s.split()[0]]
# for i in a:
#     a[i].sort()
# if (s := input()) in a:
#     for i in a[s]:
#         print(i)
# else:
#     print('Таких нет')

# I

# a = dict()
# while (s := input()) != '':
#     for i in s.split():
#         a[i] = a.get(i, 0) + 1
# for key, value in a.items():
#     print(key, value)

# J

# a = {'А': 'A', 'Б': 'В', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#      'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
#      'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
#      'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y',
#      'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}
# s = input().split(' ')
# for i in range(len(s)):
#     if s[i].strip(''''"ъьЪЬ«»''') == '':
#         s[i] = ''
# b = ' '.join(s)
# answer = ''
# for i in b:
#     if i.isupper() and i in a:
#         answer += a[i].capitalize()
#     elif i.islower() and i.upper() in a:
#         answer += a[i.upper()].lower()
#     elif i in 'ьъЪЬ':
#         continue
#     else:
#         answer += i
# print(answer)


# K

# a = dict()
# count = 0
# for i in range(int(input())):
#     s = input()
#     a[s] = a.get(s, 0) + 1
# for i in a:
#     if a[i] > 1:
#         count += a[i]
# print(count)

# L

# a = dict()
# for i in range(int(input())):
#     s = input()
#     a[s] = a.get(s, 0) + 1
# s = []
# for i in a.keys():
#     if a[i] > 1:
#         s.append(i)
# s.sort()
# if len(s):
#     for i in s:
#         print(f'{i} - {a[i]}')
# else:
#     print('Однофамильцев нет')

# M

# a = set()
# b = set()
# for i in range(int(input())):
#     a.add(input())
# for i in range(int(input())):
#     for j in range(int(input())):
#         b.add(input())
# if len(c := list(a - b)):
#     c.sort()
#     for i in c:
#         print(i)
# else:
#     print('Готовить нечего')

# L

# a = set()
# b = dict()
# answer = []
# for i in range(int(input())):
#     a.add(input())
# for i in range(int(input())):
#     s = input()
#     for j in range(int(input())):
#         if s not in b:
#             b[s] = set()
#             b[s].add(input())
#         else:
#             b[s].add(input())
# for i in b:
#     if b[i] <= a:
#         answer.append(i)
# answer.sort()
# if len(answer):
#     for j in answer:
#         print(j)
# else:
#     print('Готовить нечего')

# O

# a = []
# b = []
# for i in input().split():
#     a.append(int(i))
# for i in range(len(a)):
#     b.append({"digits": len(str(bin(a[i]))) - 2, "units": str(bin(a[i]))[2:].count('1'),
#               "zeros": str(bin(a[i]))[2:].count('0')})
# print(b)

# P

# answer = set()
# while (s := input()) != '':
#     c = s.split()
#     for i in range(len(c)):
#         if c[i] == 'зайка' and i == 0 and len(c) != 1:
#             answer.add(c[i + 1])
#         elif c[i] == 'зайка' and i == len(c) - 1 and len(c) != 1:
#             answer.add(c[i - 1])
#         elif c[i] == 'зайка' and len(c) != 1:
#             answer.add(c[i - 1])
#             answer.add(c[i + 1])
# for i in answer:
#     print(i)

# Q

# a = dict()
# b = dict()
# c = []
# while (s := input()) != '':
#     a[s.split()[0]] = a.get(s.split()[0], set()).union({s.split()[1]})
#     a[s.split()[1]] = a.get(s.split()[1], set()).union({s.split()[0]})
# for i in a.keys():
#     c.append(i)
# for i in sorted(c):
#     for j in a[i]:
#         b[i] = b.get(i, set()).union(a[j].difference(a[i])).difference({i})
#     b[i] = sorted(list(b[i]))
# answer = ''
# c.sort()
# for i in range(len(c)):
#     answer += f'{c[i]}: '
#     if len(b[c[i]]) != 0:
#         for j in b[c[i]]:
#             answer += f'{j}, '
#         answer += '\b\b'
#     if i != len(c) - 1:
#         answer += '\n'
# print(answer)

# R

# a = dict()
# c = []
# for i in range(int(input())):
#     s = input().split()
#     a[int(s[0])**2 + int(s[1])**2] = (int(s[0]), int(s[1]))
# for i in a.keys():
#     c.append(i)
# c.sort()
# answer = 1
# i = 0
# k = 1
# for i in range(len(c) - 1):
#     k = i + 1
#     j = 1
#     while k != len(c):
#         b1 = str(a[c[i]][0])
#         b2 = str(a[c[k]][0])
#         b3 = str(a[c[i]][1])
#         b4 = str(a[c[k]][1])
#         if b1[0:len(b1) - 1] == b2[0:len(b2) - 1] and b3[0:len(b3) - 1] == b4[0:len(b4) - 1]:
#             j += 1
#             i = k
#             k += 1
#         elif len(b1) == len(b2) == 1 and b3[0:len(b3) - 1] == b4[0:len(b4) - 1]:
#             j += 1
#             i = k
#             k += 1
#         elif len(b3) == len(b4) == 1 and b1[0:len(b1) - 1] == b2[0:len(b2) - 1]:
#             j += 1
#             i = k
#             k += 1
#         elif len(b1) == len(b2) == 1 and len(b3) == len(b4) == 1:
#             j += 1
#             i = k
#             k += 1
#         else:
#             k += 1
#     if j > answer:
#         answer = j
# print(answer)

# S

# a = dict()
# c = []
# answer = ''
# for i in range(int(input())):
#     s = input().split()
#     for j in s[1:]:
#         a[j.strip(',')] = a.get(j.strip(','), []) + [s[0]]
# for i in a.keys():
#     c.append(i)
# c.sort()
# for i in c:
#     if len(a[i]) == 1:
#         print(i)

# T

# c = dict()
# s = list(set(map(int, input().split('; '))))
# s.sort()
# i = 0
# while i != len(s):
#     k = i + 1
#     while k != len(s):
#         a, b = s[i], s[k]
#         while a % b != 0:
#             b, a = a % b, b
#         if b == 1:
#             c[s[i]] = c.get(s[i], []) + [str(s[k])]
#             c[s[k]] = c.get(s[k], []) + [str(s[i])]
#         k += 1
#     i += 1
# for i in s:
#     if i not in c:
#         continue
#     print(f"{i} - {', '.join(c[i])}")
