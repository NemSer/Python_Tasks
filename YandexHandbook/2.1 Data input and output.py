# A

# print(f"Привет, Яндекс!")

# B

# username = input()
# print(f'Как Вас зовут?\nПривет, {username}')

# C

# info = input()
# print(info, info, info, sep='\n')

# D

# print(int(int(input()) - 2.5 * 38))

# E

# price = int(input())
# weight = int(input())
# cash = int(input())
# print(cash - price * weight)

# F

# name = input()
# price = int(input())
# weight = int(input())
# cash = int(input())
# total = price * weight
# answer = cash - total
# print(f'Чек\n{name} - {weight}кг - {price}руб/кг\nИтого: {total}руб\nВнесено: {cash}руб\nСдача: {answer}руб')

# G

# N = int(input())
# print('Купи слона!\n' * N)

# H

# N = int(input())
# S = input()
# print(f'Я больше никогда не буду писать "{S}"!\n' * N)

# I

# N, M = int(input()), int(input())
# print(int((M / 2) * N))

# J

# name = input()
# number = int(input())
#
# print(f'Группа №{number // 100}.\n{number % 10}. {name}.\nШкафчик: {number}.\nКроватка: {(number // 10) % 10}.')

# K

# number = int(input())
# print((number // 100) % 10,
#       number // 1000,
#       number % 10,
#       (number // 10) % 10, sep='')

# L

# n1 = int(input())
# n2 = int(input())
# print((n1 // 100 + n2 // 100) % 10,
#       ((n1 // 10) % 10 + (n2 // 10) % 10) % 10,
#       (n1 % 10 + n2 % 10) % 10, sep='')

# M

# n = int(input())
# m = int(input())
# print(m // n, m % n, sep='\n')

# N

# n1, n2, n3 = int(int(input())), int(int(input())), int(int(input()))
# print(n1 + n3 + 1)

# O

# hours = int(input())
# minutes = int(input())
# T = int(input())
# hours_result = (hours * 60 + minutes + T) % 1440 // 60
# minutes_result = (hours * 60 + minutes + T) % 1440 % 60
# print(f'{hours_result // 10}{hours_result % 10}:{minutes_result // 10}{minutes_result % 10}')


# P

# shop_x = int(input())
# stock_x = int(input())
# velocity = int(input())
# print(f'{(stock_x - shop_x) / velocity:.2f}')

# Q


# n = int(input())
# m = int(input(), 2)
# print(n + m)

# R

# price = int(input(), 2)
# cash = int(input())
# print(cash - price)


# S


# name, price, weight, cash = input(), input(), input(), input()
# x = f'{weight}кг * {price}руб/кг'
# y = f'{int(weight) * int(price)}руб'
# z = f'{int(cash) - int(weight) * int(price)}руб'
# a = f'{cash}руб'
# print(f'================Чек================\n'
#       f'Товар:{name.rjust(29)}\n'
#       f'Цена:{x.rjust(30)}\n'
#       f'Итого:{y.rjust(29)}\n'
#       f'Внесено:{a.rjust(27)}\n'
#       f'Сдача:{z.rjust(29)}\n'
#       f'===================================')

# T

# N, M, K1, K2 = int(input()), int(input()), int(input()), int(input())
# print(N * (M - K2) // (K1 - K2), N * (K1 - M) // (K1 - K2))
