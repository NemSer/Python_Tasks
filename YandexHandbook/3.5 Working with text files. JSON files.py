# A

# from sys import stdin
#
# data_output = 0
# for line in stdin:
#     data_output += sum([int(x) for x in line.rstrip('\n').split()])
# print(data_output)

# B

# from sys import stdin
#
# data_output = []
# for line in stdin:
#     data_output.append(int(line.split()[2]) - int(line.split()[1]))
# print(round(sum(data_output) / len(data_output)))

# D

# from sys import stdin
#
# data_input = stdin.readlines()
# for i in range(len(data_input) - 1):
#     if data_input[-1].rstrip('\n').lower() in data_input[i].rstrip('\n').lower():
#         print(data_input[i].rstrip('\n'))

# E

# from sys import stdin
#
# data_output = []
# for line in stdin:
#     for i in line.split():
#         object = i.rstrip('\n').lower()
#         lenght = len(object)
#         if lenght % 2:
#             if object[:lenght // 2] == object[lenght // 2 + 1:][::-1]:
#                 if i.rstrip('\n') not in data_output:
#                     data_output.append(i.rstrip('\n'))
#         else:
#             if object[:lenght // 2] == object[lenght // 2:][::-1]:
#                 if i.rstrip('\n') not in data_output:
#                     data_output.append(i.rstrip('\n'))
# for i in sorted(data_output):
#     print(i)

# G

# data = []
# with open(input(), 'r', encoding='UTF8') as filein:
#     for line in filein:
#         data += [int(x) for x in line.split()]
# total = sum(data)
# count = len(data)
# print(count)
# print(len([x for x in data if x > 0]))
# print(min(data), max(data), total, round(total / count, 2), sep='\n')

# H

# with open(input(), 'r', encoding='UTF-8') as filein_1:
#     data_filein_1 = filein_1.readlines()
# with open(input(), 'r', encoding='UTF-8') as filein_2:
#     data_filein_2 = filein_2.readlines()
# set_filein_1 = set(' '.join(''.join(data_filein_1).split('\n')).split())
# set_filein_2 = set(' '.join(''.join(data_filein_2).split('\n')).split())
# data_output = sorted(list(set_filein_1.symmetric_difference(set_filein_2)))
# data_output = '\n'.join(data_output)
# with open(input(), 'w', encoding='UTF-8') as filein_3:
#     filein_3.write(data_output)

# I

# with open(input(), 'r', encoding='UTF-8') as filein:
#     data_input = filein.readlines()
# data_clear = []
# # print(data_input)
# for element in data_input:
#     new_element = ''
#     if element.startswith('\n'):
#         continue
#     for i in list(element):
#         if i != '\t':
#             new_element += i
#     new_element = ' '.join(new_element.split()) + '\n'
#     data_clear.append(new_element)
# with open(input(), 'w', encoding='UTF-8') as fileout:
#     fileout.writelines(data_clear)

# J

# with open(input(), 'r', encoding='UTF-8') as file_in:
#     data_output = file_in.readlines()
# for line in data_output[len(data_output) - int(input()):]:
#     print(line.rstrip('\n'))

# K

# import json
#
# with open(input(), 'r', encoding='UTF-8') as file_in:
#     data_input = file_in.readlines()
# prepared_data = []
# for line in data_input:
#     prepared_data.append(line.rstrip('\n'))
# count = len(' '.join(prepared_data).split())
# positive_count = len([i for i in ' '.join(prepared_data).split() if int(i) > 0])
# min = min([int(i) for i in ' '.join(prepared_data).split()])
# max = max([int(i) for i in ' '.join(prepared_data).split()])
# sum = sum([int(i) for i in ' '.join(prepared_data).split()])
# average = round(sum / count, 2)
# data_output = {"count": count,
#                "positive_count": positive_count,
#                "min": min,
#                "max": max,
#                "sum": sum,
#                "average": average}
# with open(input(), 'w', encoding='UTF-8') as file_out:
#     json.dump(data_output, file_out, ensure_ascii=False, indent=4)

# L

# with open('input()', 'r', encoding='UTF-8') as file_in:
#     data_input = file_in.readlines()
# prepared_data = [x.split() for x in data_input]
# even_str = ''
# odd_str = ''
# eq_str = ''
# for line in prepared_data:
#     for element in line:
#         even = 0
#         odd = 0
#         for i in element:
#             if int(i) % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#         if even > odd:
#             even_str += element + ' '
#         elif even < odd:
#             odd_str += element + ' '
#         else:
#             eq_str += element + ' '
#     even_str += '\n'
#     odd_str += '\n'
#     eq_str += '\n'
# with open('input()', 'w', encoding='UTF-8') as file_out:
#     file_out.write(even_str)
# with open('input()', 'w', encoding='UTF-8') as file_out:
#     file_out.write(odd_str)
# with open('input()', 'w', encoding='UTF-8') as file_out:
#     file_out.write(eq_str)

# M

# import json
# from sys import stdin
#
# with open((name := input()), 'r', encoding='UTF-8') as file_in:
#     data_input = json.load(file_in)
# for line in stdin:
#     key = line.rstrip('\n').split(' == ')[0]
#     value = line.rstrip('\n').split(' == ')[1]
#     data_input[key] = value
# with open(name, 'w', encoding='UTF-8') as file_out:
#     json.dump(data_input, file_out, ensure_ascii=False, indent=4)

# N

# import json
#
# with open((s := input()), 'r', encoding='UTF-8') as file_in1:
#     data_input = json.load(file_in1)
# with open(input(), 'r', encoding='UTF-8') as file_in2:
#     data_update = json.load(file_in2)
# new_data = dict()
# for element in data_input:
#     new_data[element["name"]] = dict()
#     for key in element.keys():
#         if key != "name":
#             new_data[element["name"]][key] = element[key]
# for element in data_update:
#     for key in element.keys():
#         if key != "name" and new_data[element["name"]].get(key, '') < element[key]:
#             new_data[element["name"]][key] = element[key]
# with open(s, 'w', encoding='UTF-8') as file_out1:
#     json.dump(new_data, file_out1, ensure_ascii=False, indent=4)

# O

# import json
# from sys import stdin
#
# tests_data = stdin.readlines()
#
# with open('scoring.json', 'r', encoding='UTF-8') as file_in:
#     data_input = json.load(file_in)
# answers = dict()
# for distcionaries in data_input:
#     bonus = distcionaries["points"] // len(distcionaries["tests"])
#     for elements in distcionaries["tests"]:
#         answers[bonus] = answers.get(bonus, []) + [elements["pattern"]]
# for line in stdin:
#     tests_data = stdin.readlines()
# result = 0
# i = 0
# while i < len(tests_data):
#     for elements in answers.keys():
#         for values in answers[elements]:
#             if i < len(tests_data) and values == tests_data[i].strip("\n"):
#                 result += elements
#             i += 1
# print(result)

# P

# from sys import stdin
#
# query = input()
# sites = []
# answer = []
# for line in stdin:
#     sites.append(line.rstrip('\n'))
# for element in sites:
#     with open(element, 'r', encoding='UTF-8') as file_in:
#         print(file_in.readlines())
#         data_input = ' '.join(''.join(file_in.readlines()).split())
#     if query.upper() in data_input.upper():
#         answer.append(element)
# if len(answer):
#     print(*answer)
# else:
#     print('404. Not Found')

# Q

# a = []
# with open('secret.txt', 'r', encoding='UTF-8') as file_in:
#     data_input = file_in.read()
# for element in data_input.rstrip('\n'):
#     if ord(element) >= 128:
#         new_ord = int(str(bin(ord(element)))[len(str(bin(ord(element)))) - 8:], 2)
#     else:
#         new_ord = ord(element)
#     a.append(chr(new_ord))
# print(''.join(a))

# S


# shift = int(input())
# with open('public.txt', 'r', encoding='UTF-8') as file_in:
#     data_input = []
#     for element in file_in.read():
#         if 65 <= ord(element) <= 90:
#             if shift >= 0 and ord(element) + (shift % 26) > 90:
#                 data_input.append(chr(64 + (shift % 26) - (90 - ord(element))))
#             elif shift >= 0 and ord(element) + (shift % 26) <= 90:
#                 data_input.append(chr(ord(element) + (shift % 26)))
#             elif shift < 0 and ord(element) - (abs(shift) % 26) < 65:
#                 data_input.append(chr(91 - ((abs(shift) % 26) - (ord(element) - 65))))
#             else:
#                 data_input.append(chr(ord(element) - (abs(shift) % 26)))
#         elif 97 <= ord(element) <= 122:
#             if shift >= 0 and ord(element) + (shift % 26) > 122:
#                 data_input.append(chr(96 + (shift % 26) - (122 - ord(element))))
#             elif shift >= 0 and ord(element) + (shift % 26) <= 122:
#                 data_input.append(chr(ord(element) + (shift % 26)))
#             elif shift < 0 and ord(element) - (abs(shift) % 26) < 97:
#                 data_input.append(chr(123 - ((abs(shift) % 26) - (ord(element) - 97))))
#             else:
#                 data_input.append(chr(ord(element) - (abs(shift) % 26)))
#         else:
#             data_input.append(element)
# with open('private.txt', 'w', encoding='UTF-8') as file_out:
#     file_out.write(''.join(data_input))




