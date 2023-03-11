# A

# def print_hello(name):
#     print(f'Hello, {name}!')

# B

# def gcd(a, b):
#     while a % b != 0:
#         copy = a
#         a = b
#         b = copy % b
#     return b

# C

# def number_length(number: int):
#     if number >= 0:
#         return len(str(number))
#     else:
#         return len(str(number)) - 1

# D


# def month(number: int, language: str):
#     month_en = {1: 'January',
#                 2: 'February',
#                 3: 'March',
#                 4: 'April',
#                 5: 'May',
#                 6: 'June',
#                 7: 'July',
#                 8: 'August',
#                 9: 'September',
#                 10: 'October',
#                 11: 'November',
#                 12: 'December'}
#     month_ru = {1: 'Январь',
#                 2: 'Февраль',
#                 3: 'Март',
#                 4: 'Апрель',
#                 5: 'Май',
#                 6: 'Июнь',
#                 7: 'Июль',
#                 8: 'Август',
#                 9: 'Сентябрь',
#                 10: 'Октябрь',
#                 11: 'Ноябрь',
#                 12: 'Декабрь'}
#     if language == 'en':
#         return month_en[number]
#     else:
#         return month_ru[number]

# E

# def split_numbers(data_input: str):
#     data_output = []
#     i = 0
#     while i < len(data_input):
#         element = ''
#         while i < len(data_input) and data_input[i] != ' ':
#             element += data_input[i]
#             i += 1
#         data_output.append(int(element))
#         i += 1
#     return tuple(data_output)

# F

# history = set()
#
#
# def modern_print(data: str):
#     if data not in history:
#         print(data)
#     history.add(data)


# G

# def can_eat(coordinates1: tuple, coordinates2: tuple):
