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
#     x = coordinates1[0]
#     y = coordinates1[1]
#     variants = [(x + 1, y + 2),
#                 (x + 2, y + 1),
#                 (x + 2, y - 1),
#                 (x + 1, y - 2),
#                 (x - 1, y - 2),
#                 (x - 2, y - 1),
#                 (x - 2, y + 1),
#                 (x - 1, y + 2)]
#     if coordinates2 in variants:
#         return True
#     else:
#         return False

# H

# def is_palindrome(object):
#     if isinstance(object, int):
#         if len(str(object)) % 2 != 0:
#             if str(object)[0:len(str(object)) // 2] == str(object)[len(str(object)) // 2 + 1:][::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if str(object)[0:len(str(object)) // 2] == str(object)[len(str(object)) // 2:][::-1]:
#                 return True
#             else:
#                 return False
#     elif isinstance(object, str):
#         if len(object) % 2 != 0:
#             if object[0:len(object) // 2] == object[len(object) // 2 + 1:][::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if object[0:len(object) // 2] == object[len(object) // 2:][::-1]:
#                 return True
#             else:
#                 return False
#     elif isinstance(object, tuple):
#         if len(object) % 2 != 0:
#             if object[0:len(object) // 2] == object[len(object) // 2 + 1:][::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if object[0:len(object) // 2] == object[len(object) // 2:][::-1]:
#                 return True
#             else:
#                 return False
#     elif isinstance(object, list):
#         if len(object) % 2 != 0:
#             if object[0:len(object) // 2] == object[len(object) // 2 + 1:][::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if object[0:len(object) // 2] == object[len(object) // 2:][::-1]:
#                 return True
#             else:
#                 return False

# I

# def is_prime(number: int):
#     if number != 1:
#         for i in range(2, int(number ** (1 / 2)) + 1):
#             if number % i == 0:
#                 return False
#         return True
#     else:
#         return False

# J

# def merge(cortej1: tuple, cortej2: tuple):
#     i, j = 0, 0
#     c = []
#     while i != len(cortej1) and j != len(cortej2):
#         if cortej1[i] > cortej2[j]:
#             c.append(cortej2[j])
#             j += 1
#         elif cortej1[i] < cortej2[j]:
#             c.append(cortej1[i])
#             i += 1
#         else:
#             c.extend([cortej1[i], cortej2[j]])
#             i += 1
#             j += 1
#     if i == len(cortej1):
#         c.extend(cortej2[j::])
#     elif j == len(cortej2):
#         c.extend(cortej1[i::])
#     return tuple(c)

