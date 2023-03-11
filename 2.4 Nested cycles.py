# A

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=' ')
#     print()

# B

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f'{j} * {i} = {j * i}')

# C

# n = int(input())
# k = 1
# j = 1
# while j <= n:
#     for i in range(k):
#         print(j, end=' ')
#         j += 1
#         if j > n:
#             break
#     print()
#     k += 1

# D

# s = 0
# for i in range(n := int(input())):
#     k = int(input())
#     while k != 0:
#         s += k % 10
#         k //= 10
# print(s)

# E

# flag = 0
# k = 0
# for i in range(int(input())):
#     while (s := input()) != 'ВСЁ':
#         if s == 'зайка':
#             flag = 1
#     k += flag
#     flag = 0
# print(k)

# F

# n = int(input())
# a = int(input())
# b = int(input())
# while a % b != 0:
#     r = a % b
#     a = b
#     b = r
# nod = b
# for i in range(n - 2):
#     c = int(input())
#     if c % nod != 0:
#         a = c
#         b = nod
#         while a % b != 0:
#             r = a % b
#             a = b
#             b = r
#         nod = b
# print(nod)

# H

# k = 0
# for i in range(int(input())):
#     name = input()
#     x = int(input())
#     s = 0
#     while x != 0:
#         s += x % 10
#         x //= 10
#         if s >= k:
#             k = s
#             winner = name
# print(winner)

# I

# answer = ''
# for i in range(int(input())):
#     x = int(input())
#     k = x % 10
#     while x != 0:
#         s = x % 10
#         if s > k:
#             k = s
#         x //= 10
#     answer += str(k)
# print(answer)

# J

# n = int(input())
# print('А Б В')
# for i in range(1, n - 1):
#     for j in range(1, n - i):
#         print(i, j, n - i - j)

# K

# k = 0
# for i in range(int(input())):
#     x = int(input())
#     for j in range(2, int(x**0.5 + 1)):
#         if x % j == 0:
#             break
#     else:
#         if x != 1:
#             k += 1
# print(k)

# L

# n, m = int(input()), int(input())
# i = 1
# while i <= m * n:
#     print(str(i).rjust(len(str(n * m))), end=' ')
#     if i % m == 0:
#         print()
#     i += 1

# M

# n, m = int(input()), int(input())
# for j in range(1, n + 1):
#     k = j
#     for i in range(m):
#         print(str(k).rjust(len(str(m * n))), end=' ')
#         k += n
#     print()

# N

# n, m = int(input()), int(input())
# k = 1
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         for j in range(m):
#             print(str(k).rjust(len(str(m * n))), end=' ')
#             k += 1
#         print()
#         k += m - 1
#     else:
#         for j in range(m):
#             print(str(k).rjust(len(str(m * n))), end=' ')
#             k -= 1
#         print()
#         k += m + 1

# O

# n, m = int(input()), int(input())
# s1 = 2 * n - 1
# s2 = 1
# for j in range(1, n + 1):
#     k = j
#     for i in range(1, m + 1):
#         if i % 2 != 0:
#             print(str(k).rjust(len(str(m * n))), end=' ')
#             k += s1
#         else:
#             print(str(k).rjust(len(str(m * n))), end=' ')
#             k += s2
#     s1 -= 2
#     s2 += 2
#     print()

# P

# n, m = int(input()), int(input())
# for i in range(1, n + 1):
#     s = ''
#     for j in range(1, n + 1):
#         s += str(i * j).center(m) + '|'
#     print(s + '\b')
#     if i != n:
#         print('-'.center(m * n + n - 1, '-'), end='\n')

# Q

# n = int(input())
# answer = 0
# for i in range(n):
#     x = int(input())
#     new = 0
#     copy = x
#     for j in range(len(str(copy))):
#         k = x % 10
#         new += k * 10**(len(str(copy)) - j - 1)
#         x //= 10
#     if new == copy:
#         answer += 1
# print(answer)

# T

# n = int(input())
# answer = 2
# summa = 0
# for b in range(2, 11):
#     k = 0
#     copy = n
#     while copy != 0:
#         k += copy % b
#         copy //= b
#     if k > summa:
#         summa = k
#         answer = b
# print(answer)


